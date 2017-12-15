import pandas as pd
import scipy.stats
import numpy as np


def get_df_with_stat_info(df_raw, content_type=[]):
    """
        Возвращает описательный DataFrame со стат. данными для каждой колонки: количество, среднее,
        минимальное значение, медиана, максимальное значение, мода. Дополнительно переменной content_type можно
        задать тип контента, по которому нужно вывести статистику

    Args:
        df_raw: DataFrame of raw data
        content_type: list of available values ['Photo', 'Status,' 'Link', 'Video']; default=[] (all values)

    Returns:
        DataFrame of statistics
    """
    if content_type:
        df_raw = df_raw[df_raw['Type'].isin(content_type)]
    result_df = df_raw.describe(percentiles=[.5]).rename({'50%': 'median'}).drop('std')
    mode_list = [scipy.stats.mode(df_raw[label]).mode[0] for label in labels]
    return result_df.append(pd.DataFrame([mode_list], columns=labels)).rename({0: 'mode'})[df_raw.columns.tolist()]


def add_CR_and_CTR_to_df(df_raw):
    """
        Добавляет в DataFrame две новые колонки: CR и CTR.
        CR = (Уник.юзеры, кликнувшие в посте / Уник. юзеры, видевшие пост)*100
        CTR = (Клики в посте / Показы поста)*100
    Args:
        df_raw: DataFrame

    Returns:
        DataFrame с двумя новыми колонками 'CR' и 'CTR'
    """
    df_raw['CR'] = (df_raw['Lifetime Engaged Users'] + df_raw['Total Interactions']) / df_raw[
        'Lifetime Post Total Reach'] * 100
    df_raw['CTR'] = df_raw['Lifetime Post Consumptions'] / df_raw['Lifetime Post Total Impressions'] * 100
    return df_raw


if __name__ == "__main__":
    df = pd.read_csv('dataset_Facebook.csv', delimiter=';')
    labels = df.columns
    content_types = ['Photo', 'Status,' 'Link', 'Video']  # ['Photo', 'Status,' 'Link', 'Video'] or [] for use all

    # Statistical description of the array. Optional: content_types.
    stat_df = get_df_with_stat_info(df, content_types)
    print('\nStatistical data for content_types %s:\n%s' % (content_types, stat_df.transpose()))

    df = add_CR_and_CTR_to_df(df)
    popular_post_by_attr = {
        'CR': df.sort_values(by=['CR'], ascending=False).iloc[0],
        'CTR': df.sort_values(by=['CTR'], ascending=False).iloc[0],
        'Total Interactions': df.sort_values(by=['Total Interactions'], ascending=False).iloc[0],
    }

    # Create df from posts with 1) the greatest CR value 2) the greatest CTR value 3) the greatest interactions value
    popular_posts = pd.concat([
        popular_post_by_attr['CR'],
        popular_post_by_attr['CTR'],
        popular_post_by_attr['Total Interactions']
    ], axis=1)

    popular_posts.columns = ['by CR', 'by CTR', 'by Interactions']
    print('\nThe most popular posts:\n%s' % popular_posts)

# test_task
Test task to check python skills

## Описание

Скрипт анализирует приложенный массив данных `dataset_Facebook.csv`, а именно:

1. Вычисляет:

* Среднее значение (mean)
* Максимальное значение (max)
* Минимальноe значение (min)
* Медиану (median)
* Моду (mode)

как для всего массива, так и для отдельных типов постов (колонка 'Type')

2. Выбирает из предложенных данных самый популярный пост. Выбор осуществляется по параметрам:

* CR
* CTR
* Total Interactions

Если считать, что популярность есть показатель интересности контента, то, оценив степень вовлеченности, можно
принять за самый популярный один из двух других постов:

* 'by CR' - пост, по которому кликнуло (один раз) больше всего людей из всех людей, (один раз) видевших пост
(отношение люди/люди).
* 'by CTR' - пост, собравший наибольшее количество кликов при фиксированном количестве показов (отношение клики/показы).

Исходя из того предположения, что гугл на запрос "Most popular post" предлагает "Most liked post", в третьей колонке
результирующего DataFrame выведен объект с максимальной суммой лайков, репостов и комментариев.


## Как использовать

1. При необходимости внутри скрипта изменить переменную `content_types` (стр.46)
2. Запустить скрипт
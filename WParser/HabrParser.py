import re
import requests
import time
from os import listdir
from os.path import isfile, join

WORKING_DIRECTORY_PATH = "D:/Github/WikiSearch/habr/"  # Путь к дирректории для сохранения

list_of_files = [int(re.findall(r'\d+', f)[0]) for f in listdir(WORKING_DIRECTORY_PATH) if isfile(join(WORKING_DIRECTORY_PATH, f))]
list_of_files.sort()
last_file_idx = list_of_files[len(list_of_files) - 1] if len(list_of_files) > 0 else 0

RANGE = 579842                    # Кол-во запросов (при скорости 1 запрос/сек -> 3600 запросов в час)
TOTAL_MAX = 579842              # Максимальное кол-во постов на сайте (Если известно)
START = last_file_idx           # Стартовый индекс
SLEEP_TIME = 0.5                  # 1 запрос в 1 секунду. (если поставить 0.5 -> 2 запроса в 1 секунду)

END = TOTAL_MAX if (START + RANGE) >= TOTAL_MAX else START + RANGE  # Завершающий индекс

for i in range(START, END):
    time.sleep(1)
    response = requests.get(f"https://habr.com/ru/post/{i}/")

    if (i - START) % 15 == 0:
        dir_files = listdir(WORKING_DIRECTORY_PATH)
        print(f"Выполнено: {round(((i - START) / (END - START)), 4)}%   совершено запросов: {i}/{TOTAL_MAX}   файлов на диске: {len(dir_files)}")

    if response.status_code == 200:
        data = response.content.decode('utf-8', 'ignore')
        full_path = WORKING_DIRECTORY_PATH + f"habr_{i}.html"

        with open(full_path, "w+", encoding='utf-8') as file:
            file.write(str(data))
    else:
        if not ((response.status_code == 403) or (response.status_code == 404)):
            print(f"там хуета какая-то случилась... #{response.status_code}")



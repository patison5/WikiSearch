#!/usr/bin/env python
import io
import os
import string
from imp import reload
from os import listdir, path
from os.path import isfile, join
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import re
import json
import codecs

load_dotenv()

DIRTY_DATA_PATH = os.getenv("DIRTY_DATA_PATH")
CLEAN_DATA_PATH = os.getenv("CLEAN_DATA_PATH")

if not path.exists(CLEAN_DATA_PATH):
    os.makedirs(CLEAN_DATA_PATH)

if not path.exists(CLEAN_DATA_PATH + "/txt"):
    os.makedirs(CLEAN_DATA_PATH + "/txt")

if not path.exists(CLEAN_DATA_PATH + "/json"):
    os.makedirs(CLEAN_DATA_PATH + "/json")

list_of_files = [f for f in listdir(DIRTY_DATA_PATH) if isfile(join(DIRTY_DATA_PATH, f))]


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# -*- coding: utf-8 -*-
import sys
import codecs

def setup_console(sys_enc="utf-8"):
    reload(sys)
    try:
        # для win32 вызываем системную библиотечную функцию
        if sys.platform.startswith("win"):
            import ctypes
            enc = "cp%d" % ctypes.windll.kernel32.GetOEMCP() #TODO: проверить на win64/python64
        else:
            # для Linux всё, кажется, есть и так
            enc = (sys.stdout.encoding if sys.stdout.isatty() else
                        sys.stderr.encoding if sys.stderr.isatty() else
                            sys.getfilesystemencoding() or sys_enc)

        # кодировка для sys
        sys.setdefaultencoding(sys_enc)

        # переопределяем стандартные потоки вывода, если они не перенаправлены
        if sys.stdout.isatty() and sys.stdout.encoding != enc:
            sys.stdout = codecs.getwriter(enc)(sys.stdout, 'replace')

        if sys.stderr.isatty() and sys.stderr.encoding != enc:
            sys.stderr = codecs.getwriter(enc)(sys.stderr, 'replace')

    except:
        pass # Ошибка? Всё равно какая - работаем по-старому...

setup_console()

dirty_files = []
clean_files = []

dirty_files_KB = []
clean_files_KB = []

for file_name in list_of_files:
    print("\n<> ------- <> ------- <>")
    full_path = DIRTY_DATA_PATH + "/" + file_name
    clean_file_path = CLEAN_DATA_PATH + "/txt/" + file_name[:-4] + 'txt'
    clean_file_path_json = CLEAN_DATA_PATH + "/json/" + file_name[:-4] + 'json'

    print("full_path : " + full_path)

    HTMLFile = codecs.open(full_path, "r", "utf-8") # на винде работает, на маке строчка ниже
    # HTMLFile = open(full_path, "r")
    index = HTMLFile.read()

    Parse = BeautifulSoup(index, 'lxml')
    # divs = Parse.find_all("div", {"class": "hello"})

    article_full = Parse.find_all("div", {"class": "tm-page-article__body"})
    if len(article_full) != 0:
        article_full = article_full[0]
    else:
        print(Parse)
        continue

    article_h1 = remove_html_tags(str(article_full.h1))

    article_body = article_full.find_all("div", {"id": "post-content-body"})[0]
    # article_body = article_body.get_text(strip=True)
    # article_body = remove_html_tags(str(article_body.encode('utf-8')))
    article_body = remove_html_tags(str(article_body))
    article_body = os.linesep.join([s for s in article_body.splitlines() if s])

    dirty_file_length = len(index)
    clean_files.append(len(article_body))
    dirty_files.append(len(index))
    print("dirty_file_length, {0}".format(dirty_file_length))
    print("clean_file_length, {0}".format(len(article_body)))

    print("clean_file_path : " + clean_file_path)
    print("clean_file_path : " + clean_file_path_json)

    with open("D:/Github/WikiSearch/habr/clean/txt/11.txt", 'w+', encoding='cp866', errors='replace', newline='') as csvfile:
        csvfile.write(article_h1)
        csvfile.write("\n")
        csvfile.write(article_body)

    with open(clean_file_path, 'w+', encoding='cp866', errors='replace') as csvfile:
        csvfile.write(article_h1)
        csvfile.write("\n")
        csvfile.write(article_body)

    with open(clean_file_path_json, 'w+', encoding='utf8', errors='replace') as f:
        data = {
            "id": file_name[5:-5],
            "title": article_h1,
            "body": article_body,
        }
        data_string = json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')).encode("utf8")
        f.write(data_string.decode())

    # with open(clean_file_path_json, 'w+', encoding='cp866', errors='replace') as f:
    #     data = {
    #         "id": file_name[5:-5],
    #         "title": article_h1,
    #         "body": article_body,
    #     }
    #     data_string = json.dumps(data, sort_keys=False, indent=4, ensure_ascii=True, separators=(',', ': ')).encode("utf8")
    #     f.write(data_string.decode())

    dirty_size = os.path.getsize("{0}/{1}".format(DIRTY_DATA_PATH, file_name))
    clean_size = os.path.getsize("{0}/{1}".format(CLEAN_DATA_PATH + "/json/", file_name[:-4] + 'json'))
    # clean_size = os.path.getsize("{0}/{1}".format(CLEAN_DATA_PATH + "/txt/", file_name[:-4] + 'txt'))

    dirty_files_KB.append(round(dirty_size / 1024, 3))
    clean_files_KB.append(round(clean_size / 1024, 3))

    print("dirty size: {0}KB".format(round(dirty_size / 1024, 3)))
    print("clean size: {0}KB".format(round(clean_size / 1024, 3)))


print(clean_files)
print(dirty_files)

print("------")

print(dirty_files_KB)
print(clean_files_KB)
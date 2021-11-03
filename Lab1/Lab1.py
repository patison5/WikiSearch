import os
import string
from os import listdir, path
from os.path import isfile, join
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

DIRTY_DATA_PATH = os.getenv("DIRTY_DATA_PATH")
CLEAN_DATA_PATH = os.getenv("CLEAN_DATA_PATH")

if not path.exists(CLEAN_DATA_PATH):
    os.makedirs(CLEAN_DATA_PATH)

list_of_files = [f for f in listdir(DIRTY_DATA_PATH) if isfile(join(DIRTY_DATA_PATH, f))]


def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


dirty_files = []
clean_files = []

dirty_files_KB = []
clean_files_KB = []

for file_name in list_of_files:
    full_path = DIRTY_DATA_PATH + "/" + file_name
    clean_file_path = CLEAN_DATA_PATH + "/" + file_name

    HTMLFile = open(full_path, "r")
    index = HTMLFile.read()

    Parse = BeautifulSoup(index, 'lxml')
    divs = Parse.find_all("div", {"class": "hello"})

    article_full = Parse.find_all("div", {"class": "tm-page-article__body"})
    if len(article_full) != 0:
        article_full = article_full[0]
    else:
        print(Parse)
        continue

    article_h1 = remove_html_tags(str(article_full.h1))

    article_body = article_full.find_all("div", {"id": "post-content-body"})[0]
    # article_body = article_body.get_text(strip=True)
    article_body = remove_html_tags(str(article_body.encode('utf-8')))
    article_body = os.linesep.join([s for s in article_body.splitlines() if s])

    dirty_file_length = len(index)
    clean_files.append(len(article_body))
    dirty_files.append(len(index))
    print("dirty_file_length, {0}".format(dirty_file_length))
    print("clean_file_length, {0}".format(len(article_body)))

    with open(clean_file_path, 'w+') as cf:
        cf.write(article_h1)
        cf.write("\n")
        cf.write(article_body)

    dirty_size = os.path.getsize("{0}/{1}".format(DIRTY_DATA_PATH, file_name))
    clean_size = os.path.getsize("{0}/{1}".format(CLEAN_DATA_PATH, file_name))

    dirty_files_KB.append(round(dirty_size / 1024, 3))
    clean_files_KB.append(round(clean_size / 1024, 3))

    print("dirty size: {0}KB".format(round(dirty_size / 1024, 3)))
    print("clean size: {0}KB".format(round(clean_size / 1024, 3)))


print(clean_files)
print(dirty_files)

print("------")

print(dirty_files_KB)
print(clean_files_KB)
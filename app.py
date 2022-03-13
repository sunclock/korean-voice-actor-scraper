import wikipediaapi
from mediawikiapi import MediaWikiAPI
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# 시도 1 -> 실패. <li> 태그를 읽어오지 못함

wiki = wikipediaapi.Wikipedia(
    'ko',
    extract_format=wikipediaapi.ExtractFormat.HTML)

keyword = ["한국방송 성우극회", "문화방송 성우극회", "교육방송 성우극회",
           "대원방송 성우극회", "대교방송 성우극회", "투니보이스 성우극회",
           "기독교방송 성우극회", "가톨릭평화방송 성우극회", "대한민국의 남자 성우", "대한민국의 여자 성우"]


def is_wiki_page(keyword):
    page_wiki = wiki.page(keyword)
    print("Page - Exists: %s" % page_wiki.exists())


def is_wiki_content(keyword):
    page_wiki = wiki.page(keyword)
    print("Page Content\n%s" % page_wiki.text)


def store_wiki_content(keyword):
    page_wiki = wiki.page(keyword)
    with open(keyword + ".json", "w") as f:
        json.dump(page_wiki.text, f, indent=2)
    print("New json file is created from" + keyword + ".json file")

# 시도 2 -> 실패. 성우 정보 페이지 자체를 읽어오지 못함.


mediawikiapi = MediaWikiAPI()


def is_mediawiki_page(keyword):
    page_wiki = mediawikiapi.page(keyword)
    print("Page - Exists: %s" % page_wiki.exists())


def is_mediawiki_content(keyword):
    page_wiki = mediawikiapi.page(keyword)
    soup = BeautifulSoup(page_wiki.html(), 'html.parser')
    tables = soup.findAll("div", {"class": "div-col"})
    print("Page Content\n%s" % tables)


def store_mediawiki_content(keyword):
    page_wiki = mediawikiapi.page(keyword)
    with open(keyword + ".json", "w") as f:
        json.dump(page_wiki.text, f, indent=2)
    print("New json file is created from" + keyword + ".json file")


# is_mediawiki_page("성우")
# is_mediawiki_content(keyword[-1])

urls = [
    "https://ko.m.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EC%84%B1%EC%9A%B0",
    "https://ko.m.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EC%84%B1%EC%9A%B0"
]


def get_list_item(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    item = bsObject.select('div.mw-category-generated')
    print(item)
    return item


get_list_item(urls[0])

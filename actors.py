from datetime import datetime
import wikipediaapi
from mediawikiapi import MediaWikiAPI
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from html.parser import HTMLParser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 단계 1: 위키피디아 객체 생성

# 시도 1 -> 실패. <li> 태그를 읽어오지 못함

# wiki = wikipediaapi.Wikipedia(
#     'ko',
#     extract_format=wikipediaapi.ExtractFormat.HTML)

# keyword = ["한국방송 성우극회", "문화방송 성우극회", "교육방송 성우극회",
#            "대원방송 성우극회", "대교방송 성우극회", "투니보이스 성우극회",
#            "기독교방송 성우극회", "가톨릭평화방송 성우극회", "대한민국의 남자 성우", "대한민국의 여자 성우"]


# def is_wiki_page(keyword):
#     page_wiki = wiki.page(keyword)
#     print("Page - Exists: %s" % page_wiki.exists())


# def is_wiki_content(keyword):
#     page_wiki = wiki.page(keyword)
#     print("Page Content\n%s" % page_wiki.text)


# def store_wiki_content(keyword):
#     page_wiki = wiki.page(keyword)
#     with open(keyword + ".json", "w") as f:
#         json.dump(page_wiki.text, f, indent=2)
#     print("New json file is created from" + keyword + ".json file")

# 시도 2 -> 실패. 검색 결과 없음.


# mediawikiapi = MediaWikiAPI()


# def is_mediawiki_page(keyword):
#     page_wiki = mediawikiapi.page(keyword)
#     print("Page - Exists: %s" % page_wiki.exists())


# def is_mediawiki_content(keyword):
#     page_wiki = mediawikiapi.page(keyword)
#     soup = BeautifulSoup(page_wiki.html(), 'html.parser')
#     tables = soup.findAll("div", {"class": "div-col"})
#     print("Page Content\n%s" % tables)


# def store_mediawiki_content(keyword):
#     page_wiki = mediawikiapi.page(keyword)
#     with open(keyword + ".json", "w") as f:
#         json.dump(page_wiki.text, f, indent=2)
#     print("New json file is created from" + keyword + ".json file")

# 시도 3 -> 성공


# domain = "https://ko.m.wikipedia.org"

# urls = [
#     "https://ko.m.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EC%84%B1%EC%9A%B0",
#     "https://ko.m.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EC%84%B1%EC%9A%B0"
# ]


# def get_html(url):
#     html = urlopen(url)
#     bsObject = BeautifulSoup(html, "html.parser")
#     html = bsObject.select('div.mw-category-generated')
#     return html


# html = get_html(urls[0])


# 단계 2: html 태그 분리

# 시도 1 -> html parser 사용 실패. a의 href 가져오지 못함.


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Encountered a start tag:", tag)

#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)

#     def handle_data(self, data):
#         print("Encountered some data  :", data)


# parser = MyHTMLParser()
# parser.feed(str(html))

# 시도 2 -> bs4 find_all 사용. 성공.
domain = "https://ko.m.wikipedia.org"

urls = {
    "male": "https://ko.m.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EC%84%B1%EC%9A%B0",
    "male_2": "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EC%84%B1%EC%9A%B0&pagefrom=%EC%84%9D%EC%8A%B9%ED%9B%88#mw-pages",
    "male_3": "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%82%A8%EC%9E%90_%EC%84%B1%EC%9A%B0&pagefrom=%EC%A0%95%EB%AA%85%EC%98%A5+%28%EC%84%B1%EC%9A%B0%29#mw-pages",
    "female": "https://ko.m.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EC%84%B1%EC%9A%B0",
    "female_2": "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EC%84%B1%EC%9A%B0&pagefrom=%EC%84%A0%EC%9D%80%ED%98%9C#mw-pages",
    "female_3": "https://ko.wikipedia.org/w/index.php?title=%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%97%AC%EC%9E%90_%EC%84%B1%EC%9A%B0&pagefrom=%EC%A0%84%ED%95%B4%EB%A6%AC#mw-pages",
}

count = 0


def get_html(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    html = bsObject.select('div.mw-category-generated')
    return html


def get_actor_list(html):
    soup = BeautifulSoup(html, "html.parser")
    hrefs = soup.find_all('a', href=True)
    return hrefs


male_html = get_html(urls['male'])
male_html_2 = get_html(urls['male_2'])
male_html_3 = get_html(urls['male_3'])
female_html = get_html(urls['female'])
female_html_2 = get_html(urls['female_2'])
female_html_3 = get_html(urls['female_3'])
male_actors = get_actor_list(str(male_html))
male_actors_2 = get_actor_list(str(male_html_2))
male_actors_3 = get_actor_list(str(male_html_3))
female_actors = get_actor_list(str(female_html))
female_actors_2 = get_actor_list(str(female_html_2))
female_actors_3 = get_actor_list(str(female_html_3))

# 단계 3: firebase에 저장. 성공.

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def store_actors(actors, sex):
    for actor in actors:
        global count
        count += 1
        actor_ref = db.collection(u'actors').document(u'%s' % actor.string)
        actor_ref.set({
            u'name': actor.string.strip().replace(
                '\n', '').replace('\t', '').replace('\r', '').split(' ')[0],
            u'url': domain + actor['href'],
            u'sex': sex,
            u'filmography': [],
            u'created_at': datetime.now(),
            u'modified_at': datetime.now(),
        })


print('성우 저장 시작')
store_actors(male_actors, '남성')
store_actors(male_actors_2, '남성')
store_actors(male_actors_3, '남성')
store_actors(female_actors, '여성')
store_actors(female_actors_2, '여성')
store_actors(female_actors_3, '여성')
print('총 %d 건의 성우 저장 완료' % count)

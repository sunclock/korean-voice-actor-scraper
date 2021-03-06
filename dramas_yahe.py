from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

domain = "http://www.yahe-shop.com/"

count = 0


def get_drama_list(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    html = bsObject.find_all('li', 'name')
    dramas = []
    for drama in html:
        r18 = True
        production = '밤바다 야해'
        title = drama.text.lstrip('(예약판)').lstrip('(일반판)').split('( 리뷰 ')[0].replace('\n', '').replace(
            '\t', '').replace('\r', '').strip()
        author = ''
        voice_actor = []
        dramas.append({
            'title': title,
            'url': '',
            'author': author,
            'r18': r18,
            'production': production,
            'cast': voice_actor,
            'created_at': datetime.now(),
            'modified_at': datetime.now(),
        })
    return dramas


dramas = get_drama_list(domain)


cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def store_dramas(dramas):
    for drama in dramas:
        global count
        count += 1
        drama_ref = db.collection(u'dramas').document(u'%s' % drama['title'])
        drama_ref.set(drama)


print('밤바다 야해 드라마 저장 시작')
store_dramas(dramas)
print('총 %d 건의 밤바다 야해 드라마 저장 시작' % count)

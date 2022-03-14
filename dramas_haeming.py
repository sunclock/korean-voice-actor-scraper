from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

domain = "https://audiocomics.kr/"

urls = {
    "bl":  "https://hae-ming.com/sub/bl",
    "drama": "https://hae-ming.com/sub/drama",
    "romance": "https://hae-ming.com/sub/romance",
}


def get_html(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    html = bsObject.find_all('div', 'audiobook')
    return html


def get_drama_list(html):
    bsObject = BeautifulSoup(html, "html.parser")
    html = bsObject.find_all('div', 'audiobook')
    dramas = []
    for drama in html:
        print(drama)
        imgSrc = drama.find(
            'div', 'audiobook-img-wrapper').find('button').find('img').get('src')
        if (imgSrc == "/static/images/no_adult.jpeg"):
            r18 = True
        else:
            r18 = False
        production = '밤바다 야해'
        content = drama.find('div', 'audiobook-content').find_all('p')
        title = content[0].string.replace('\n', '').replace(
            '\t', '').replace('\r', '').strip()
        author = content[1].string.replace('\n', '').replace(
            '\t', '').replace('\r', '').strip()
        voice_actor = content[2].string.strip().replace(
            '\n', '').replace('\t', '').replace('\r', '').split(',')
        print(title)
        print(author)
        print(voice_actor)
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


bl_html = get_html(urls['bl'])
drama_html = get_html(urls['drama'])
romance_html = get_html(urls['romance'])
bl_dramas = get_drama_list(str(bl_html))
drama_dramas = get_drama_list(str(drama_html))
romance_dramas = get_drama_list(str(romance_html))


cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def store_dramas(dramas):
    for drama in dramas:
        print(drama)
        drama_ref = db.collection(u'dramas').document(u'%s' % drama['title'])
        drama_ref.set(drama)


store_dramas(bl_dramas)
store_dramas(drama_dramas)
store_dramas(romance_dramas)

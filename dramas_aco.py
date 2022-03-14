from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

domain = "https://audiocomics.kr/"

urls = {
    "complete": "https://audiocomics.kr/audiodrama/complete?sort=newer",
    "complete_2": "https://audiocomics.kr/audiodrama/complete?sort=newer&per_page=2",
    "complete_3": "https://audiocomics.kr/audiodrama/complete?sort=newer&per_page=3",
    "complete_4": "https://audiocomics.kr/audiodrama/complete?sort=newer&per_page=4",
    "complete_5": "https://audiocomics.kr/audiodrama/complete?sort=newer&per_page=5",
    "serial": "https://audiocomics.kr/audiodrama/serial?cycle=ALL"
}


def get_html(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    html = bsObject.select('div.product-list')
    return html


def get_drama_list(html):
    soup = BeautifulSoup(html, "html.parser")
    html = soup.find_all('div', 'product')
    dramas = []
    for drama in html:
        title = drama.find('h3', 'subjet').find('a').string.strip().replace(
            '\n', '').replace('\t', '').replace('\r', '')
        print('title', title)
        url = drama.find('h3', 'subjet').find('a').get('href').strip().replace(
            '\n', '').replace('\t', '').replace('\r', '')
        r18 = drama.find('span', 'adult')
        if (r18):
            r18 = True
        else:
            r18 = False
        production = drama.find('div', 'production')
        writer = drama.find('div', 'writer').find('a').string.strip().replace(
            '\n', '').replace('\t', '').replace('\r', '')
        if (title == '연애수업/연애사업'):
            title = '연애수업, 연애사업'
        if (production):
            production = production.string.strip().replace(
                '\n', '').replace('\t', '').replace('\r', '')
        else:
            production = '오디오코믹스'
        voice_actor = drama.find(
            'div', 'voice_actor').string.strip().replace('\n', '').replace('\t', '').replace('\r', '').split(',')
        for i in range(len(voice_actor)):
            voice_actor[i] = voice_actor[i].strip().replace('\n', '').replace(
                '\t', '').replace('\r', '')
        dramas.append({
            'title': title,
            'url': url,
            'author': writer,
            'r18': r18,
            'production': production,
            'cast': voice_actor,
            'created_at': datetime.now(),
            'modified_at': datetime.now(),
        })
    return dramas


# complete_html = get_html(urls['complete'])
complete_2_html = get_html(urls['complete_2'])
complete_3_html = get_html(urls['complete_3'])
complete_4_html = get_html(urls['complete_4'])
complete_5_html = get_html(urls['complete_5'])
# serial_html = get_html(urls['serial'])
# complete_dramas = get_drama_list(str(complete_html))
complete_2_dramas = get_drama_list(str(complete_2_html))
complete_3_dramas = get_drama_list(str(complete_3_html))
complete_4_dramas = get_drama_list(str(complete_4_html))
complete_5_dramas = get_drama_list(str(complete_5_html))
# serial_dramas = get_drama_list(str(serial_html))


cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def store_dramas(dramas):
    for drama in dramas:
        print(drama)
        drama_ref = db.collection(u'dramas').document(u'%s' % drama['title'])
        drama_ref.set(drama)


# store_dramas(complete_dramas)
store_dramas(complete_2_dramas)
store_dramas(complete_3_dramas)
store_dramas(complete_4_dramas)
store_dramas(complete_5_dramas)
# store_dramas(serial_dramas)

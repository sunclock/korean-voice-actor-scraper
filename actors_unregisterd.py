
from datetime import datetime
from logging import exception
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

failures = [{'title': 'FOOLS (풀스)', 'cast': '리우'}, {'title': 'Keep Us Together', 'cast': '김신우'}, {'title': 'Love so Sweet', 'cast': '이재국'}, {'title': 'Love so Sweet', 'cast': '양성무'}, {'title': 'Love so Sweet', 'cast': '황진희'}, {'title': 'Love so Sweet', 'cast': '배준호'}, {'title': 'Love so Sweet', 'cast': '최영수'}, {'title': 'Love so Sweet', 'cast': '이 호'}, {'title': 'NEW', 'cast': '김수지'}, {'title': 'PASSION (패션)', 'cast': '박상훈'}, {'title': 'PASSION (패션)', 'cast': '강성우'}, {'title': 'PASSION (패션)', 'cast': '이상운'}, {'title': 'PASSION (패션) : 다이아포닉 심포니아', 'cast': '박상훈'}, {'title': 'PASSION (패션) : 다이아포닉 심포니아', 'cast': '강성우'}, {'title': 'PASSION (패션) : 다이아포닉 심포니아', 'cast': '이상운'}, {'title': 'PAX VOBIS (팍스 보비스)', 'cast': '박상훈'}, {'title': 'PAX VOBIS (팍스 보비스)', 'cast': '이상운'}, {'title': 'PAX VOBIS (팍스 보비스)', 'cast': '이명호'}, {'title': 'PAYBACK part.1', 'cast': '박하진'}, {'title': 'PAYBACK part.1', 'cast': '서정익'}, {'title': 'PAYBACK part.2', 'cast': '박하진'}, {'title': 'PAYBACK part.2', 'cast': '서정익'}, {'title': 'PAYBACK part.3', 'cast': '서정익'}, {'title': '宮(궁) 上편', 'cast': '정명준'}, {'title': '宮(궁) 下편', 'cast': '정명준'}, {'title': '구원', 'cast': '김신우'}, {'title': '달콤한 남자', 'cast': '이상운'}, {'title': '덕후의 여자', 'cast': '이명호'}, {'title': '덕후의 여자', 'cast': '강성우'}, {'title': '러닝타임 (Running Time)', 'cast': '김용석'}, {'title': '러닝타임 (Running Time)', 'cast': '방시우'}, {'title': '미필적 고의에 의한 연애사', 'cast': '서정익'}, {'title': '반칙', 'cast': '김신우'}, {'title': '불가역', 'cast': '박상훈'}, {'title': '불가역', 'cast': '이명호'}, {'title': '불가역', 'cast': '김도희'}, {'title': '불길한 손님 제 1장', 'cast': '이명호'}, {'title': '불길한 손님 제 2장', 'cast': '이명호'}, {'title': '불길한 손님 제 2장', 'cast': '오해성'}, {'title': '살인마 르웰린씨의 낭만적인 정찬 part.1', 'cast': '서정익'}, {'title': '살인마 르웰린씨의 낭만적인 정찬 part.1', 'cast': '이명상'}, {'title': '살인마 르웰린씨의 낭만적인 정찬 part.2', 'cast': '서정익'}, {'title': '살인마 르웰린씨의 낭만적인 정찬 part.3', 'cast': '서정익'}, {'title': '살인마 르웰린씨의 낭만적인 정찬 part.3', 'cast': '이보용'}, {
    'title': '상수리나무 아래 Part.4', 'cast': '박상훈'}, {'title': '소실점', 'cast': '이상운'}, {'title': '아코디온(ACODION)', 'cast': '박상훈'}, {'title': '안녕 엄마', 'cast': '이명호'}, {'title': '안녕 엄마', 'cast': '이한솔'}, {'title': '안녕 엄마', 'cast': '나은혁'}, {'title': '여고생과 편의점', 'cast': '강성우'}, {'title': '여고생과 편의점', 'cast': '이상호'}, {'title': '여고생과 편의점', 'cast': '리우'}, {'title': '연애수업, 연애사업', 'cast': '강성우'}, {'title': '예호', 'cast': '정유수'}, {'title': '예호', 'cast': '조은선'}, {'title': '예호', 'cast': '박기진'}, {'title': '예호', 'cast': '황진희'}, {'title': '예호', 'cast': '최영수'}, {'title': '예호', 'cast': '양성무'}, {'title': '예호', 'cast': '김현명'}, {'title': '온 오어 오프 시즌 1', 'cast': '이한솔'}, {'title': '온 오어 오프 시즌 1', 'cast': '리우'}, {'title': '온 오어 오프 시즌2', 'cast': '이한솔'}, {'title': '온 오어 오프 시즌2', 'cast': '리우'}, {'title': '완전무결하게 사로잡히다', 'cast': '남영택'}, {'title': '유실', 'cast': '나은혁'}, {'title': '유실', 'cast': '이명상'}, {'title': '인스턴트', 'cast': '정형민'}, {'title': '인스턴트', 'cast': '노형태'}, {'title': '인스턴트', 'cast': '디도'}, {'title': '인스턴트', 'cast': '황대연'}, {'title': '인스턴트', 'cast': '김장환'}, {'title': '적해도 제 2편', 'cast': '이한솔'}, {'title': '적해도 제 3편', 'cast': '이한솔'}, {'title': '천추세인 제  1편', 'cast': '박상훈'}, {'title': '천추세인 제 4편', 'cast': '박상훈'}, {'title': '크리미널 리비도', 'cast': '강성우'}, {'title': '키스톤 로맨틱 콤비', 'cast': '김신우'}, {'title': '킹메이커 (KING MAKER)', 'cast': '이명호'}, {'title': "킹스메이커 (King's Maker)", 'cast': '이상호'}, {'title': '테일코트', 'cast': '박상훈'}, {'title': '폐하의 무릎 위', 'cast': '디도'}, {'title': '필로우 토크 TAKE #1', 'cast': '이한솔'}, {'title': '필로우 토크 TAKE #1', 'cast': '김용석'}, {'title': '필로우 토크 TAKE #1', 'cast': '나은혁'}, {'title': '필로우 토크 TAKE #2', 'cast': '이한솔'}, {'title': '필로우 토크 TAKE #2', 'cast': '김용석'}, {'title': '필로우 토크 TAKE #2', 'cast': '나은혁'}, {'title': '필로우 토크 TAKE #3', 'cast': '이한솔'}, {'title': '필로우 토크 TAKE #3', 'cast': '나은혁'}, {'title': '해후', 'cast': '김용석'}, {'title': '황제와 여기사', 'cast': '디도'}, {'title': '황제와 여기사', 'cast': '이상운'}]


def get_actors_list(failures):
    actors_list = []
    for failure in failures:
        actor = failure['cast']
        if (actor in actors_list):
            continue
        else:
            actors_list.append(actor)
    return actors_list


def get_dramas_list(failures):
    dramas_list = []
    for failure in failures:
        drama = failure['title']
        if (drama in dramas_list):
            continue
        else:
            dramas_list.append(drama)
    return dramas_list


actors_list = get_actors_list(failures)
dramas_list = get_dramas_list(failures)

print('actors_list', actors_list)
print('dramas_list', dramas_list)

# 예외 1. 협회 성우, 위키피디아 미등록


def exception_1(failures):
    for actor in ["강성우", "박하진", "서정익", "김용석", "방시우", "김도희",
                  "오해성", "이명상", "이보용", "이한솔", "나은혁", "이상호"]:
        actor_ref = db.collection(u'actors').document(u'%s' % actor)
        sex = '여성'
        if (actor in ["강성우", "서정익", "김용석", "오해성", "이명상", "나은혁", "이상호"]):
            sex = '남성'
        filmography = []
        for drama in failures:
            if drama['cast'] == actor:
                filmography.append(drama['title'])
        actor_ref.set({
            u'name': actor,
            u'url': '',
            u'sex': sex,
            u'filmography': filmography,
            u'created_at': datetime.now(),
            u'modified_at': datetime.now(),
        })


exception_1(failures)


# 예외 2. 비협회 성우. 위키피디아 미등록.
def exception_2(failures):
    for actor in ["이재국", "양성무", "황진희", "배준호",
                                "최영수", "이호", "정유수", "조은선", "박기진", "김현명",
                  "남영택", "정형민", "노형태", "황대연", "김장환"]:
        actor_ref = db.collection(u'actors').document(u'%s' % actor)
        sex = '여성'
        if (actor in ["이재국", "양성무", "배준호", "최영수", "이호", "정유수", "김현명", "남영택", "정형민", "노형태", "황대연", "김장환"]):
            sex = '남성'
        filmography = []
        for drama in failures:
            if drama['cast'] == actor:
                filmography.append(drama['title'])
        actor_ref.set({
            u'name': actor,
            u'url': '',
            u'sex': sex,
            u'filmography': filmography,
            u'created_at': datetime.now(),
            u'modified_at': datetime.now(),
        })
# 예외 3. 협회 성우, 기타 호칭, 가명, 개명 {"캐스팅 표에 등록된 이름": "위키피디아에 등록된 이름"}


exception_2(failures)


def exception_3(failures):
    dict = {"이상운": "이승준", "정명준": "정우석", "리우": "오보미", "김신우": "김현구",
            "박상훈": "박상훈 (1982년)", "이명호": "이명호 (여자 성우)", "디도": "김디도"}
    values = list(dict.values())
    keys = list(dict.keys())
    for i in range(len(values)):
        actors_ref = db.collection(u'actors')
        actor_doc = actors_ref.document(u'%s' % values[i]).get()
        if actor_doc is None:
            print('%s is not in the database' % values[i])
        else:
            actor_ref = db.collection(u'actors').document(u'%s' % keys[i])
            filmography = []
            for drama in failures:
                if drama['cast'] == keys[i]:
                    filmography.append(drama['title'])
            actor_ref.set({
                u'name': keys[i],
                u'url': actor_doc.get('url'),
                u'sex': actor_doc.get('sex'),
                u'filmography': actor_doc.get('filmography'),
                u'created_at': datetime.now(),
                u'modified_at': datetime.now(),
            })
            actors_ref.document(u'%s' % values[i]).delete()


exception_3(failures)

# 예외 4. 모르겠음
# ["김수지", ]

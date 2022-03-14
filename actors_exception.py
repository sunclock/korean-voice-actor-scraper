
# -*- coding: utf-8 -*-
from datetime import datetime
from logging import exception
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

failures = [{'title':'title', 'cast':'cast'},]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'cast': '지병문'}, {'title': '아코디온(ACODION)', 'cast': '박상훈'}, {'title': '안녕 엄마', 'cast': '이명호'}, {'title': '안녕 엄마', 'cast': '이한솔'}, {'title': '안녕 엄마', 'cast': '나은혁'}, {'title': '언노운코드', 'cast': '강성우'}, {'title': '여고생과 편의점', 'cast': '강성우'}, {'title': '여고생과 편의점', 'cast': '이상호'}, {'title': '여고생과 편의점', 'cast': '리우'}, {'title': '연애수업, 연애사업', 'cast': '강성우'}, {'title': '예호', 'cast': '정유수'}, {'title': '예호', 'cast': '조은선'}, {'title': '예호', 'cast': '박기진'}, {'title': '예호', 'cast': '황진희'}, {'title': '예호', 'cast': '최영수'}, {'title': '예호', 'cast': '양성무'}, {'title': '예호', 'cast': '김현명'}, {'title': '온 오어 오프 시즌 1', 'cast': '이한솔'}, {'title': '온 오어 오프 시즌 1', 'cast': '리우'}, {'title': '온 오어 오프 시즌2', 'cast': '이한솔'}, {'title': '온 오어 오프 시즌2', 'cast': '리우'}, {'title': '완전무결하게 사로잡히다', 'cast': '남영택'}, {'title': '욕망이라는 것에 대하여', 'cast': '이상운'}, {'title': '욕망이라는 것에 대하여', 'cast': '이상호'}, {'title': '욕망이라는 것에 대하여', 'cast': '방시우'}, {'title': '우리 강산 푸르게 푸르게 : 열역학 제二법칙', 'cast': '박상훈'}, {'title': '우리 강산 푸르게 푸르게 : 열역학 제二법칙', 'cast': '김도희'}, {'title': '유실', 'cast': '나은혁'}, {'title': '유실', 'cast': '이명상'}, {'title': '유실 AU', 'cast': '나은혁'}, {'title': '인스턴트', 'cast': '정형민'}, {'title': '인스턴트', 'cast': '노형태'}, {'title': '인스턴트', 'cast': '디도'}, {'title': '인스턴트', 'cast': '황대연'}, {'title': '인스턴트', 'cast': '김장환'}, {'title': '적해도 제 2편', 'cast': '이한솔'}, {'title': '적해도 제 3편', 'cast': '이한솔'}, {'title': '천추세인 제  1편', 'cast': '박상훈'}, {'title': '천추세인 제 4편', 'cast': '박상훈'}, {'title': '청사과 낙원', 'cast': '김용석'}, {'title': '청사과 낙원', 'cast': '장지민'}, {'title': '크리미널 리비도', 'cast': '강성우'}, {'title': '키스톤 로맨틱 콤비', 'cast': '김신우'}, {'title': '킹메이커 (KING MAKER)', 'cast': '이명호'}, {'title': "킹스메이커 (King's Maker)", 'cast': '이상호'}, {'title': '탐색전', 'cast': '나은혁'}, {'title': '탐색전', 'cast': '김희승'}, {'title': '테일코트', 'cast': '박상훈'}, {'title': '파트타임 파트너', 'cast': '강성우'}, {'title': '파트타임 파트너', 'cast': '나은혁'}, {'title': '파트타임 파트너', 'cast': '김도희'}, {'title': '폐하의 무릎 위', 'cast': '디도'}, {'title': '푸른 괴물의 껍질', 'cast': '강성우'}, {'title': '푸른 괴물의 껍질', 'cast': '이상준'}, {'title': '푸른 괴물의 껍질', 'cast': '정의택'}, {'title': '필로우 토크 TAKE #1', 'cast': '이한솔'}, {'title': '필로우 토크 TAKE #1', 'cast': '김용석'}, {'title': '필로우 토크 TAKE #1', 'cast': '나은혁'}, {'title': '필로우 토크 TAKE #2', 'cast': '이한솔'}, {'title': '필로우 토크 TAKE #2', 'cast': '김용석'}, {'title': '필로우 토크 TAKE #2', 'cast': '나은혁'}, {'title': '필로우 토크 TAKE #3', 'cast': '이한솔'}, {'title': '필로우 토크 TAKE #3', 'cast': '나은혁'}, {'title': '해후', 'cast': '김용석'}, {'title': '황금펜상 : 각인', 'cast': '박상훈'}, {'title': '황금펜상 : 국선 변호사 - 그해 여름', 'cast': '박상훈'}, {'title': '황금펜상 : 귀양다리', 'cast': '박상훈'}, {'title': '황금펜상 : 소나기', 'cast': '박상훈'}, {'title': '황금펜상 : 유일한 범인', 'cast': '박상훈'}, {'title': '황제와 여기사', 'cast': '디도'}, {'title': '황제와 여기사', 'cast': '이상운'}]


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


print("성우 예외 처리 시작")
print("예외 1. 협회 성우, 위키피디아 미등록 시작")
exception_1(failures)
print("예외 1. 협회 성우, 위키피디아 미등록 끝")

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


print("예외 2. 비협회 성우. 위키피디아 미등록 시작")
exception_2(failures)
print("예외 2. 비협회 성우. 위키피디아 미등록 끝")

# 예외 3. 협회 성우, 기타 호칭, 가명, 개명 {"캐스팅 표에 등록된 이름": "위키피디아에 등록된 이름"}


def exception_3(failures):
    dict = {"이상운": "이승준 (성우)", "정명준": "정우석", "리우": "오보미", "김신우": "김현구 (성우)",
            "박상훈": "박상훈 (1982년)", "이명호": "이명호 (여자 성우)", "디도": "김디도"}
    values = list(dict.values())
    keys = list(dict.keys())
    for i in range(len(values)):
        actor_ref = db.collection(u'actors').document(u'%s' % values[i])
        actor_doc = actor_ref.get()
        if actor_doc is None:
            print('%s is not in the database' % values[i])
        else:
            filmography = []
            for drama in failures:
                if drama['cast'] == keys[i]:
                    filmography.append(drama['title'])
            actor_ref.update({
                u'name': keys[i],
                u'filmography': firestore.ArrayUnion(filmography),
                u'modified_at': datetime.now(),
            })

# 예외 3. 협회 성우, 기타 호칭, 가명, 개명 {'캐스팅 표에 등록된 이름': '위키피디아에 등록된 이름'}


print("예외 3. 협회 성우, 기타 호칭, 가명, 개명 {'캐스팅 표에 등록된 이름': '위키피디아에 등록된 이름'} 시작")
exception_3(failures)
print("예외 3. 협회 성우, 기타 호칭, 가명, 개명 {'캐스팅 표에 등록된 이름': '위키피디아에 등록된 이름'} 끝")
print("성우 예외 처리 완료")
# 예외 4. 모르겠음
# ["김수지", ]

# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


class Actor(object):
    def __init__(self, name, sex, filmography, url, created_at, modified_at):
        self.name = name
        self.sex = sex
        self.filmography = filmography
        self.url = url
        self.created_at = created_at
        self.modified_at = modified_at

    # @staticmethod
    # def from_dict(source):
    #     # ...

    # def to_dict(self):
    #     # ...

    def __repr__(self):
        return(
            f'City(\
                name={self.name}, \
                sex={self.sex}, \
                filmography={self.filmography}, \
                url={self.url}, \
                created_at={self.created_at}, \
                modified_at={self.modified_at} \
            )'
        )


actors_ref = db.collection(u'actors')
dramas_ref = db.collection(u'dramas')
dramas = dramas_ref.stream()

success_count = 0
failure_count = 0
total_count = 0
failure_list = []

print("성우와 드라마 정보 매칭 시작")
for drama in dramas:
    formed_drama = drama.to_dict()
    casts = formed_drama['cast']
    for cast in casts:
        if (cast == ""):
            continue
        total_count += 1
        actor = actors_ref.document(cast)
        if (actor.get().exists):
            actor.update(
                {u'filmography': firestore.ArrayUnion([formed_drama['title']])})
            success_count += 1
            # print('[Success] title %s cast %s' % (formed_drama['title'], cast))
        else:
            actor = actors_ref.document(cast + u' (성우)')
            if (actor.get().exists):
                actor.update(
                    {u'filmography': firestore.ArrayUnion([formed_drama['title']])})
                success_count += 1
                # print('[Success] title %s cast %s' %
                #       (formed_drama['title'], cast))
            else:
                failure_count += 1
                failure_list.append(
                    {'title': formed_drama['title'], 'cast': cast})
                # print('[Failure] title %s cast %s' %
                #       (formed_drama['title'], cast))

print("성우와 드라마 정보 매칭 완료")
print('Total Cast: %d' % total_count)
print('Success Cast: %d / %d' % (success_count, total_count))
print('Failure Cast: %d / %d' % (failure_count, total_count))
print('Success Rate: %.2f%%' % (success_count / total_count * 100))
print('Failure Rate: %.2f%%' % (failure_count / total_count * 100))
print('Failure List: %s' % failure_list)

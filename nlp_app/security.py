import bcrypt
from pymongo import MongoClient
import response_handling as response

client = MongoClient("mongodb://db:27017")
db = client.users_db
users = db["users"]


def user_in_bd(user):
    return users.count({'user': user}) != 0


def register_user(user, password):
    if not user_in_bd(user):
        users.insert({
            'user': user,
            'pw': bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()),
            'tokens': 10
        })
        return response.user_created()
    else:
        return response.existing_user()


def login(user, password_to_check):
    if user_in_bd(user):
        detected_user = users.find({'user': user})[0]
        if bcrypt.checkpw(password_to_check.encode('utf8'),
                         detected_user['pw']):
            return response.success_login(str(detected_user['tokens']))
        else:
            return response.wrong_login_details()
    else:
        return response.unknown_user()


def change_pw(user, old_pw, new_pw):
    if user_in_bd(user):
        detected_user = users.find({'user': user})[0]
        if bcrypt.checkpw(old_pw.encode('utf8'),
                         detected_user['pw']):
            users.update({'user': user}, {"$set": {"pw": bcrypt.hashpw(new_pw.encode('utf8'), bcrypt.gensalt())}})
            return response.pw_change_success()
        else:
            return response.wrong_login_details()
    else:
        return response.unknown_user()
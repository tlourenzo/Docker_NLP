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
        try:
            users.insert({
                'user': user,
                'pw': bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()),
                'tokens': 10
            })
            return response.user_created()
        except Exception as e:
            print(e)
            return response.internal_error('Error registering User!')
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


def internal_login(user, password_to_check):
    if user_in_bd(user):
        detected_user = users.find({'user': user})[0]
        return bcrypt.checkpw(password_to_check.encode('utf8'), detected_user['pw'])
    else:
        return False


def change_pw(user, old_pw, new_pw):
    if user_in_bd(user):
        detected_user = users.find({'user': user})[0]
        if bcrypt.checkpw(old_pw.encode('utf8'),
                         detected_user['pw']):
            try:
                users.update({'user': user}, {"$set": {"pw": bcrypt.hashpw(new_pw.encode('utf8'), bcrypt.gensalt())}})
                return response.pw_change_success()
            except Exception as e:
                print(e)
                return response.internal_error('Password not changed! DB error!')
        else:
            return response.wrong_login_details()
    else:
        return response.unknown_user()

def list_users(user, password):
    if user == 'admin' and bcrypt.checkpw(password.encode('utf8'), users.find({'user': user})[0]['pw']):
        user_list = []
        for u in users.find({}):
            user_data = {
                'user': u['user'],
                'tokens': u['tokens']
            }
            user_list.append(user_data)
        return response.success_list_users(user_list)
    else:
        return response.wrong_login_details()

def delete_user(user, password, user_to_delete):
    if user == 'admin' and bcrypt.checkpw(password.encode('utf8'), users.find({'user': user})[0]['pw']):
        try:
            users.remove({'user': user_to_delete}, 1)
            return response.user_deleted(user_to_delete)
        except Exception as e:
            print(e)
            return response.internal_error('User deletion error')
    else:
        return response.wrong_login_details()

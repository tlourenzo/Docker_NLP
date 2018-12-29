from flask import Flask, jsonify, request, render_template, make_response
from flask_restful import Api, Resource
import os
from security import register_user, login, change_pw, list_users, delete_user, internal_login, internal_delete_user
from nlp import compare_text, compare_urls
from response_handling import request_error

app = Flask(__name__)
api = Api(app)


class Score_Nlp_Strings(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            if internal_login(data['user'], data['password']):
                print('Login success and ready to check words!!!!')
                return compare_text(data['original_text'], data['new_text'])
            else:
                return login(data['user'], data['password'])
        except Exception:
            return request_error()

class Score_Nlp_Text_Urls(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            if internal_login(data['user'], data['password']):
                print('Login success and ready to check both urls!!!!')
                return compare_urls(data['url_1'], data['url_2'])
            else:
                return login(data['user'], data['password'])
        except Exception:
            return request_error()

class Login(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            return login(data['user'], data['password'])
        except Exception:
            return request_error()


class Register(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            return register_user(data['user'], data['password'])
        except Exception:
            return request_error()

class Update_Pw(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            return change_pw(data['user'], data['old_password'], data['new_password'])
        except Exception:
            return request_error()

class All_Users(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            return list_users(data['user'], data['password'])
        except Exception:
            return request_error()

class Delete_User(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            return delete_user(data['user'], data['password'], data['user_to_delete'])
        except Exception:
            return request_error()

class Welcome(Resource):
    def get(self):
        return make_response(render_template('welcome.html'),
                             200,
                             {'Content-Type': 'text/html'})


api.add_resource(Welcome, '/')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Update_Pw, '/update_pw')
api.add_resource(Score_Nlp_Strings, '/score_strings')
api.add_resource(Score_Nlp_Text_Urls, '/score_urls')
api.add_resource(All_Users, '/list_users')
api.add_resource(Delete_User, '/delete')

if __name__ == '__main__':
    try:
        if 'ADMIN_USR' in os.environ:
            if internal_delete_user(os.environ.get('ADMIN_USR')):
                register_user(os.environ.get('ADMIN_USR'), os.environ.get('ADMIN_PW'))
    except Exception as e:
        print(e)
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, jsonify, request, render_template, make_response
from flask_restful import Api, Resource
import os
from security import register_user, login, change_pw, list_users

app = Flask(__name__)
api = Api(app)


class Score_Nlp_Strings(Resource):
    def post(self):
        pass


class Score_Nlp_Text_Urls(Resource):
    def post(self):
        pass


class Login(Resource):
    def post(self):
        data = request.get_json(force=True)
        return login(data['user'], data['password'])


class Register(Resource):
    def post(self):
        data = request.get_json(force=True)
        return register_user(data['user'], data['password'])


class Update_Pw(Resource):
    def post(self):
        data = request.get_json(force=True)
        return change_pw(data['user'], data['old_password'], data['new_password'])

class All_Users(Resource):
    def post(self):
        data = request.get_json(force=True)
        return list_users(data['user'], data['password'])


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

if __name__ == '__main__':
    try:
        if 'ADMIN_USR' in os.environ:
            register_user(os.environ.get('ADMIN_USR'), os.environ.get('ADMIN_PW'))
    except Exception as e:
        print(e)
    app.run(host="0.0.0.0", debug=True)

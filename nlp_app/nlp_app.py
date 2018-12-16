from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
import bcrypt

app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return render_template('welcome.html')


api.add_resource(Welcome, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

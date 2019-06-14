from flask import Flask, abort, jsonify
from flask_restful import Api, Resource, reqparse, fields
from flask_httpauth import HTTPBasicAuth, make_response
import pymysql, urllib.parse, custom_functions

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'user':
        return 'pass'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


class EscapeString(Resource):
  decorators = [auth.login_required]
  
  def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('string')
        self.reqparse.add_argument('type')
        super(EscapeString, self).__init__()


  def post(self):
    args = self.reqparse.parse_args()
    string = args["string"]
    type_ = args["type"]
    if type_ == "mysql":
      response = pymysql.escape_string(string)
    elif type_ == "url":
      response = urllib.parse.quote(string)
    elif type_ == "html":
      response = custom_functions.html_escape(string)
    else:
      response = "invalid type"
    return {'response': response}, 201


class WhiteList(Resource):
  decorators = [auth.login_required]

  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('whitelist', type=str, action='append')
    self.reqparse.add_argument('string', type=str)
    super(WhiteList, self).__init__()


  def post(self):
      args = self.reqparse.parse_args()
      string = args["string"]
      whitelist = args["whitelist"]
      # print(whitelist)
      if string in whitelist:
        return {'response' : True}, 201
      return {'response' : False}, 201


api.add_resource(EscapeString, '/escape', endpoint='escape')
api.add_resource(WhiteList, '/whitelist', endpoint='whitelist')


if __name__ == '__main__':
    app.run(debug=True)
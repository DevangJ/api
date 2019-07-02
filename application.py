from flask import Flask, request, jsonify, render_template, url_for
import pymysql

app = Flask(__name__)


@app.errorhandler(405)
def not_allowed(error=None):
    message = {
            'status': 405,
            'message': 'Method not allowed: ' + request.method,
    }
    resp = jsonify(message)
    resp.status_code = 405

    return resp


@app.errorhandler(400)
def invalid_params(error=None):
    message = {
            'status': 400,
            'message': 'Invalid parameters',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.route('/sql', methods=["POST"])
def sql():
  if request.method == "POST":
    print(request.form["datatype"])
    return sql_response(request.form["datatype"], request.form["input"])
  else:
    return not_allowed()


@app.route('/url', methods=["POST"])
def url():
  if request.method == "POST":
    body = request.json
    return url_response(body["datatype"], body["input"])
  else:
    return not_allowed()


@app.route('/home')
def home():
   return render_template("index.html")


def sql_response(datatype, input):
  if datatype == "integer":
    if isinstance(input, int) or input.isdigit(): 
      message = {
        'output': input
      }
    else:
      message = {
        'output': 'invalid input: contains non integers'
      }
  elif datatype == "string":
    message = {
      'output' : pymysql.escape_string(input)
    }
  else:
    return invalid_params()
  resp = jsonify(message)
  resp.status_code = 200
  return resp






if __name__ == '__main__':
  app.run(host='localhost', port=8000, debug=True)
 
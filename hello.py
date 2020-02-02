from flask import Flask, request
from werkzeug.exceptions import MethodNotAllowed, BadRequest
app = Flask(__name__)


def sum(a, b):
    return a + b


@app.route('/', methods=['GET'])
def hello_world():
    if request.method != 'GET':
        return MethodNotAllowed('Only GET method is allowed')

    if 'a' not in request.args or 'b' not in request.args:
        return BadRequest('Parameters \'a\' and \'b\' are mandatory')
    return sum(request.args['a'], request.args['b'])

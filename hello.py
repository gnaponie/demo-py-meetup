from flask import Flask, request, Blueprint, jsonify
from werkzeug.exceptions import MethodNotAllowed, BadRequest
app = Flask(__name__)
api = (Blueprint('api', __name__))

# run with: env FLASK_APP=hello.py flask run


def _sum(a, b):
    return int(a) + int(b)


@api.route('/', methods=['GET'])
def hello_world():
    if request.method != 'GET':
        raise MethodNotAllowed('Only GET method is allowed')

    if 'a' not in request.args or 'b' not in request.args:
        raise BadRequest('Parameters \'a\' and \'b\' are mandatory')
    if not request.args['a'].isdigit() or not request.args['b'].isdigit():
        raise BadRequest('Parameters \'a\' and \'b\' have to be numbers')
    return jsonify(_sum(request.args['a'], request.args['b']))


app.register_blueprint(api)

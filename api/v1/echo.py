from flask import Blueprint, jsonify, request

echo = Blueprint('v1_echo', __name__, url_prefix='/v1/echo')


@echo.route('/', methods=['GET', 'POST'])
def echo_():
    if request.method == 'GET':
        return jsonify({'result': 'ok'})

    if request.method == 'POST':
        data = request.json
        return_data = {'result': 'post message = ' + data['msg']}
        return jsonify(return_data)

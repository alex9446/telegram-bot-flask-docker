import logging
from http import HTTPStatus
from os import getenv

from flask import Flask, Response, jsonify, request

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


SECRET = getenv('SECRET')
if not SECRET:
    logger.critical('no SECRET env')


@app.post("/")
def root() -> Response:
    request_secret = request.headers.get('X-Telegram-Bot-Api-Secret-Token')
    if not SECRET or request_secret != SECRET:
        return Response(status=HTTPStatus.UNAUTHORIZED)

    request_json = request.get_json()
    try:
        chat_id = request_json['message']['chat']['id']
        name = request_json['message']['from']['first_name']
    except KeyError:
        return Response(status=HTTPStatus.NO_CONTENT)
    logger.debug(request_json)
    return jsonify({
        'method': 'sendMessage',
        'chat_id': chat_id,
        'text': f'hello {name}!'
    })

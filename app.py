from datetime import datetime
from flask import Flask, request, jsonify
from os import environ

app = Flask('HTTP Request Catcher')

last_request = None


@app.route('/__last_request__', methods=['GET'])
def get_last_request():
    return jsonify(last_request), 200


@app.route('/', defaults={'path': ''}, methods=['PUT', 'POST', 'GET', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['PUT', 'POST', 'GET', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS'])
def catch(path):
    global last_request

    last_request = {
        'method': request.method,
        'data': request.data.decode('utf-8'),
        'headers': dict(request.headers),
        'url': request.url,
        'time': datetime.now().isoformat(),
    }

    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

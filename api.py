from flask import Flask, request

from util import decrypt
from event import Event

app = Flask(__name__)


@app.route("/", methods=['POST'])
def events():
    data = decrypt(request)
    return Event(data).result


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")

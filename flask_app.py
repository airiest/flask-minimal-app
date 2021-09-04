from flask import Flask, render_template
from flask_sockets import Sockets

from api.v1 import echo as v1_echo
from api.ws import ws

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)

app.register_blueprint(v1_echo)
sockets.register_blueprint(ws)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

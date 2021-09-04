from flask import Blueprint
import json
import datetime
import time

ws = Blueprint("ws", __name__, url_prefix='/ws')


@ws.route('/clock')
def clock(ws):
    while not ws.closed:
        datetime_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y/%m/%d %H:%M:%S')
        data = {
            'now': datetime_now
        }
        try:
            ws.send(json.dumps(data))
        except Exception:
            break
        time.sleep(1)

from flask import Flask, request
import os
import json
import urllib, urllib2

app = Flask(__name__)
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    execfile(ROOT_DIR + "/logentries-hipchat.cfg")
except IOError:
    print "logentries-hipchat.cfg not found"
    sys.exit(1)

@app.route("/logentries-%s" % LOGENTRIES_URL_SECRET, methods=["POST"])
def logentries():
    try:
        payload = json.loads(request.form["payload"])
        msg = "%s: %s" % (payload["alert"]["name"], payload["event"]["m"])

        data = {
            "from": "Logentries",
            "message": msg.encode("utf-8"),
            "message_format": "text",
            "color": "purple",
            "room_id": HIPCHAT_ROOM_ID,
            "notify": "1"
        }

        data = urllib.urlencode(data)
        req = urllib2.urlopen("https://api.hipchat.com/v1/rooms/message?format=json&auth_token=%s" % HIPCHAT_API_KEY, data)
        req.read()
    except:
        import traceback
        traceback.print_exc()
        raise
    return ""

if __name__ == '__main__':
    app.run()

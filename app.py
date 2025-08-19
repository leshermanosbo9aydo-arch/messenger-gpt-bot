from flask import Flask, request
import os

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")

@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print(data)  # يطبع الرسائل في Logs باش تتأكد من التشغيل
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

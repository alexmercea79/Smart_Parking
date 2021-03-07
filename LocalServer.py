from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    path = '/Users/alexm/Desktop/Licenta Mercea Alex/Licenta Mercea Alex/number.txt'
    file = open(path, 'r')
    file_open = file.read()
    resp = MessagingResponse()
    resp.message("Sunt {} locuri libere de parcare".format(str(file_open)))
    return str(resp)


@app.route("/id", methods=['GET', 'POST'])
def sms_repl():
    path = '/Users/alexm/Desktop/Licenta/values.txt'
    days_file = open(path, 'r')
    days = days_file.read()

    return days


if __name__ == "__main__":
    app.run(debug=True)

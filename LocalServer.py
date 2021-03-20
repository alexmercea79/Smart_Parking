from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    path = 'number.txt'
    file = open(path, 'r')
    file_open = file.read()
    resp = MessagingResponse()
    print(str(file_open))
    if str(file_open) == '1':
        resp.message("Este disponibil un singur loc de parcare! Grabeste-te!")
    elif str(file_open) == '0':
        resp.message("Din pacate toate locurile de parcare sunt ocupate.")
    else:
        resp.message("Sunt {} locuri libere de parcare.".format(str(file_open)))
    return str(resp)


@app.route("/id", methods=['GET', 'POST'])
def sms_repl():
    path = 'values.txt'
    days_file = open(path, 'r')
    days = days_file.read()

    return days


def run_app():

    app.run()





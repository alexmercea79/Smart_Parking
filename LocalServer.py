from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    f = open('free_spaces_cameras/camere.txt')
    lines=f.readlines()

    resp = MessagingResponse()
    resp.message('Din pacate textul introdus nu corespunde. Va rugam introduceti o parcare valida')

    for line in lines:
        line = line.rstrip('\n')
        line = line.split(' = ')
        print(line[0])
        print(body)
        if str(line[0]) == str(body):
            print('adevarat toati')
            print(line[1])

            path = 'free_spaces_cameras/'+ line[1]
            file = open(path, 'r')
            file_open = file.read()
            resp = MessagingResponse()

            print('resp= '+str(resp))
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





import os
from datetime import datetime
import timeago

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    f = open('parking_data/parking_cameras.txt')
    lines = f.readlines()

    resp = MessagingResponse()
    resp.message(
        'Din pacate textul introdus nu corespunde. Va rugam introduceti o parcare valida.\nAceasta este lista parcarilor disponibile:')
    all_parking = ''
    verif = 0
    for line in lines:
        line = line.rstrip('\n')
        line = line.split(' = ')
        print(line[1])
        y = line[1].split("https://www.youtube.com/watch?v=")
        print(y[1])
        file_txt = y[1] + '.txt'
        print(body)

        if str(line[0]).lower() == str(body).lower():
            verif = 3
            print('adevarat')
            print(line[1])

            path = 'free_spaces_cameras/' + file_txt
            time = os.path.getmtime(path)
            modTimesinceEpoc = os.path.getmtime(path)
            modificationTime = datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
            now = datetime.now()

            current_time = datetime.now()
            print('current timeeeee=',current_time)
            now_timeago=timeago.format(modificationTime,current_time,locale='ro').capitalize()
            # print('time este egal cu: '+str(time))
            file = open(path, 'r')
            file_open = file.read()
            resp = MessagingResponse()

            print('resp= ' + str(resp).lower())
            print(str(file_open))
            if str(file_open) == '1':
                resp.message(
                    "Este disponibil un singur loc de parcare! Grabeste-te!\nUltima actualizare: {0}.\n({1})".format(
                        str(now_timeago), str(
                            modificationTime)))
            elif str(file_open) == '0':
                resp.message(
                    "Din pacate toate locurile de parcare sunt ocupate.\nUltima actualizare: {0}.\n({1})".format(
                        str(now_timeago), str(
                            modificationTime)))
            else:
                resp.message(
                    '{0}Ultima actualizare: {1}.\n({2})'.format(
                        "Sunt {} locuri libere de parcare.\n".format(str(file_open)), str(now_timeago), str(
                            modificationTime)))
        elif 'Afisare Parcare' == str(body):
            verif = 1
            resp = MessagingResponse()
            all_parking = all_parking + str(line[0]) + '\n'
            # resp.message(str(line[0]))
            print(all_parking)
        elif verif is not 3:
            verif = 2
            # resp.message('Din pacate textul introdus nu corespunde. Va rugam introduceti o parcare valida')
            all_parking = all_parking + str(line[0]) + '\n'

    if verif == 1:
        resp.message(all_parking)
    elif verif == 2:
        resp.message(all_parking)
    print(str(verif) + 'verif')

    return str(resp)


def run_app():
    app.run()

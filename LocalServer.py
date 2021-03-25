from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# https://www.youtube.com/watch?v=U7HRKjlXK-Y&ab_channel=Supercircuits
# U7HRKjlXK-Y&ab_channel=Supercircuits.txt
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    f = open('parking_data/parking_cameras.txt')
    lines=f.readlines()

    resp = MessagingResponse()
    resp.message('Din pacate textul introdus nu corespunde. Va rugam introduceti o parcare valida.\nAceasta este lista parcarilor disponibile:')
    all_parking=''
    verif=0
    for line in lines:
        line = line.rstrip('\n')
        line = line.split(' = ')
        print(line[1])
        y = line[1].split("https://www.youtube.com/watch?v=")
        # print(y[1])
        file_txt=y[1]+'.txt'
        print(body)

        if str(line[0]) == str(body):
            verif=3
            print('adevarat')
            print(line[1])

            path = 'free_spaces_cameras/'+ file_txt
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
        elif 'Afisare Parcare' == str(body):
            verif=1
            resp = MessagingResponse()
            all_parking= all_parking+str(line[0])+'\n'
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





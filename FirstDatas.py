import os.path

import cv2
import numpy as np
import pafy
import yaml

from twilio.rest import Client

refPt = []


class FirstDatas:
    def __init__(self, url, fn_yaml='', cascade_src='classifiers/classifier_02.xml', global_str="Ultima schimbare: ",
                 nr_locuri_libere="Numar locuri libere: ",
                 twilio_account_sid='ACa6df512b91444e4345d1a14f2e2e1645',
                 twilio_auth_token='816de7cec503bc2ce716789ec02d2cbc',
                 twilio_source_phone_number='+13853044103',

                 ):

        self.fn_yaml = fn_yaml
        self.twilio_source_phone_number = twilio_source_phone_number
        self.twilio_auth_token = twilio_auth_token
        self.twilio_account_sid = twilio_account_sid
        self.nr_locuri_libere = nr_locuri_libere
        self.global_str = global_str
        self.url = url
        self.splitter = url

        self.cascade_src = cascade_src
        # self.car_cascade = cv2.CascadeClassifier(cascade_src)

    def initial_values(self,text_overlay = True,
        parking_overlay = True,
        parking_id_overlay = True,
        parking_detection = True,
        motion_detection = True,
        pedestrian_detection = False,  # putere de procesare marita
        min_area_motion_contour = 500,  # detectare miscare
        park_laplacian_th = 2.8,
        park_sec_to_wait = 4,  # 4 schimbare din rosu in verde si invers
        start_frame = 0,  # inceputul videoclipului
        show_ids = True,  # numarul locului de parcare
        classifier_used = True,
        save_video = False):
        text_overlay

    def get_data(self):
        self.splitter = self.url.split("https://www.youtube.com/watch?v=")
        self.fn_yaml = self.splitter[1] + ".yml"
        print(self.fn_yaml)
        print(f'{self.url}')
        video = pafy.new(self.url)
        best = video.getbest(preftype="mp4")
        # print(f'{self.cascade_src}')
        # print(f'{self.global_str}')
        print(f'{self.splitter[1]}')
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        sms_sent = False
        car_cascade = cv2.CascadeClassifier(self.cascade_src)
        self.capture_frame(best.url)

        if os.path.exists("ymls/" + self.fn_yaml):
            pass
        else:
            file = open("ymls/" + self.fn_yaml, 'w')
            file.close()

    def capture_frame(self, videofile):
        vidcap = cv2.VideoCapture(videofile)
        success, image = vidcap.read()
        if success:
            cv2.imwrite("images/" + self.splitter[1] + ".jpg", image)

    def draw(self):
        cropping = False
        data = []
        file_path = "ymls/" + self.fn_yaml
        img = cv2.imread('images/' + self.splitter[1] + ".jpg")

        file = open(file_path, "r+")
        file.truncate(0)
        file.close()

        def yaml_loader(file_path):
            with open(file_path, "r") as file_descr:
                data = yaml.load(file_descr, Loader=yaml.FullLoader)

                return data

        def yaml_dump(file_path, data):
            with open(file_path, "a") as file_descr:
                yaml.dump(data, file_descr)

        def yaml_dump_write(file_path, data):
            with open(file_path, "w") as file_descr:
                yaml.dump(data, file_descr)

        def click_and_crop(event, x, y, flags, param):
            current_pt = {'id': 0, 'points': []}
            global refPt, cropping
            if event == cv2.EVENT_LBUTTONDBLCLK:
                refPt.append((x, y))
                cropping = False
            if len(refPt) == 4:
                if not data:
                    if yaml_loader(file_path) is not None:
                        data_already = len(yaml_loader(file_path))
                    else:
                        data_already = 0
                else:
                    if yaml_loader(file_path) is not None:
                        data_already = len(data) + len(yaml_loader(file_path))
                    else:
                        data_already = len(data)

                cv2.line(image, refPt[0], refPt[1], (0, 255, 0), 1)
                cv2.line(image, refPt[1], refPt[2], (0, 255, 0), 1)
                cv2.line(image, refPt[2], refPt[3], (0, 255, 0), 1)
                cv2.line(image, refPt[3], refPt[0], (0, 255, 0), 1)

                temp_lst1 = list(refPt[2])
                temp_lst2 = list(refPt[3])
                temp_lst3 = list(refPt[0])
                temp_lst4 = list(refPt[1])

                current_pt['points'] = [temp_lst1, temp_lst2, temp_lst3, temp_lst4]
                current_pt['id'] = data_already
                data.append(current_pt)
                # data_already+=1
                refPt = []

        image = cv2.resize(img, None, fx=0.6, fy=0.6)
        clone = image.copy()
        cv2.namedWindow("Dublu click pentru a marca punctul si ESC pentru a iesi")
        cv2.imshow("Dublu click pentru a marca punctul si ESC pentru a iesi", image)
        cv2.setMouseCallback("Dublu click pentru a marca punctul si ESC pentru a iesi", click_and_crop)

        # loop pana apasare tasta q
        while True:
            # display the image and wait for a keypress
            cv2.imshow("Dublu click pentru a marca punctul si ESC pentru a iesi", image)
            key = cv2.waitKey(1) & 0xFF
            if cv2.waitKey(33) == 27:
                break

        # date in yaml
        if data != []:
            yaml_dump(file_path, data)
        cv2.destroyAllWindows()  # important pentru a nu da crash

# # x = FirstDatas('dasdasda')
# y = Options()
#
# # x.get_data()
# y.get_data()

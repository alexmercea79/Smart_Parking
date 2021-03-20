from datetime import time
import re

refPt = []


def draw():
    import cv2
    import yaml
    cropping = False
    data = []
    file_path = "ymls/" + fn_yaml
    img = cv2.imread('images/' + splitter[1] + ".jpg")

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
    if data:
        yaml_dump(file_path, data)
    cv2.destroyAllWindows()  # important pentru a nu da crash


def detections_working(url):
    global car_cascade, splitter, fn_yaml, parking_status
    # Mercea Alex-Ovidiu
    import os.path
    import cv2
    import numpy as np
    import pafy
    import yaml
    from twilio.rest import Client
    fn = "videos/testvideo_03.mp4"  # 3
    # fn = " "
    # fn = " "
    # fn_yaml = "yml_youtube.yml"
    fn_out = "outputvideo_01.avi"
    cascade_src = 'classifiers/classifier_02.xml'
    car_cascade = cv2.CascadeClassifier(cascade_src)
    global_str = "Ultima schimbare: "
    change_pos = 0.00
    nr_locuri_libere = "Numar locuri libere: "
    number = 0
    dict = {
        'text_overlay': True,
        'parking_overlay': True,
        'parking_id_overlay': True,
        'parking_detection': True,
        'motion_detection': True,
        'pedestrian_detection': False,  # putere de procesare marita
        'min_area_motion_contour': 500,  # detectare miscare
        'park_laplacian_th': 2.8,
        'park_sec_to_wait': 4,  # 4 schimbare din rosu in verde si invers
        'start_frame': 0,  # inceputul videoclipului
        'show_ids': True,  # numarul locului de parcare
        'classifier_used': True,
        'save_video': False
    }
    # Twilio
    twilio_account_sid = 'ACa6df512b91444e4345d1a14f2e2e1645'
    twilio_auth_token = '816de7cec503bc2ce716789ec02d2cbc'
    twilio_source_phone_number = '+13853044103'
    # client Twilio
    client = Client(twilio_account_sid, twilio_auth_token)
    sms_sent = False

    if_draw = 'n'
    print(url)
    splitter = url.split("https://www.youtube.com/watch?v=")
    y = re.search('t=[1-9]+[a-z]*&', splitter[1])
    print(splitter[1])
    print('y= '+str(y))
    if y is not None:
        y = re.findall('t=[1-9]+[a-z]*&', splitter[1])
        splitter[1] = splitter[1].replace(str(y[0]), '')
    video = pafy.new(url)
    fn_yaml = splitter[1] + ".yml"
    print(fn_yaml)
    best = video.getbest(preftype="mp4")
    # refPt = []

    def capture_frame(videofile):
        vidcap = cv2.VideoCapture(videofile)
        success, image = vidcap.read()
        if success:
            cv2.imwrite("images/" + splitter[1] + ".jpg", image)

    capture_frame(best.url)

    if not os.path.exists("ymls"):
        os.mkdir('ymls')
    if not os.path.exists("images"):
        os.mkdir('images')

    if os.path.exists("ymls/" + fn_yaml):
        pass
    else:
        file = open("ymls/" + fn_yaml, 'w')
        file.close()
    if if_draw == 'n':
        pass
    else:
        draw()
    # proprietatile videoclipului
    cap = cv2.VideoCapture(best.url)
    video_info = {'fps': cap.get(cv2.CAP_PROP_FPS),
                  'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.6),
                  'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.6),
                  'fourcc': cap.get(cv2.CAP_PROP_FOURCC),
                  'num_of_frames': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    cap.set(cv2.CAP_PROP_POS_FRAMES, dict['start_frame'])  # start numarul de frameuri

    def run_classifier(img, id):
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(img, 1.1, 1)
        if cars is ():
            return False
        else:
            parking_status[id] = False
            # print(parking_status[id])
            return True

    # codec si VideoWriter
    if dict['save_video']:
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I',
                                        'D')  # optiuni: ('P','I','M','1'), ('D','I','V','X'), ('M','J','P','G'), ('X',
        # 'V','I','D')
        out = cv2.VideoWriter(fn_out, -1, 25.0, (video_info['width'], video_info['height']))
    # detector de persoane
    if dict['pedestrian_detection']:
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        # background substractor
    if dict['motion_detection']:
        fgbg = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=16, detectShadows=True)
    # citeste yaml
    with open("ymls/" + fn_yaml, 'r') as stream:
        parking_data = yaml.load(stream, Loader=yaml.FullLoader)
        if parking_data is None:
            print("Niciun loc de parcare inregistrat. Va rugam marcati fiecare loc de parcare!")

            draw()
            parking_data = yaml.load(stream, Loader=yaml.FullLoader)
    parking_contours = []
    parking_bounding_rects = []
    parking_mask = []
    parking_data_motion = []
    if parking_data is not None:
        for park in parking_data:
            points = np.array(park['points'])
            rect = cv2.boundingRect(points)
            points_shifted = points.copy()
            points_shifted[:, 0] = points[:, 0] - rect[0]
            points_shifted[:, 1] = points[:, 1] - rect[1]
            parking_contours.append(points)
            parking_bounding_rects.append(rect)
            mask = cv2.drawContours(np.zeros((rect[3], rect[2]), dtype=np.uint8), [points_shifted], contourIdx=-1,
                                    color=255, thickness=-1, lineType=cv2.LINE_8)
            mask = mask == 255
            parking_mask.append(mask)
    kernel_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # morphological kernel
    kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 19))
    if parking_data is not None:
        parking_status = [False] * len(parking_data)
        parking_buffer = [None] * len(parking_data)

    # bw = ()
    def print_parkIDs(park, coor_points, frame_rev):
        moments = cv2.moments(coor_points)
        centroid = (int(moments['m10'] / moments['m00']) - 3, int(moments['m01'] / moments['m00']) + 3)
        # numar id pe portiunea marcata
        cv2.putText(frame_rev, str(park['id']), (centroid[0] + 1, centroid[1] + 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame_rev, str(park['id']), (centroid[0] - 1, centroid[1] - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame_rev, str(park['id']), (centroid[0] + 1, centroid[1] - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame_rev, str(park['id']), (centroid[0] - 1, centroid[1] + 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame_rev, str(park['id']), centroid, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    while cap.isOpened():

        video_cur_pos = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0  # pozitia curenta pe secunde
        video_cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)  # index frame
        ret, frame_initial = cap.read()
        # cv2.imwrite("frame_03.jpg",frame_initial)
        if ret:
            frame = cv2.resize(frame_initial, None, fx=0.6, fy=0.6)
        if not ret:
            print("Sfarsit Video")
            break

        # fundal substraction
        frame_blur = cv2.GaussianBlur(frame.copy(), (5, 5), 3)
        # frame_blur = frame_blur[150:1000, 100:1800]
        frame_gray = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2GRAY)
        frame_out = frame.copy()

        # colt stanga overlay
        if dict['text_overlay']:
            str_on_frame = "%d/%d" % (video_cur_frame, video_info['num_of_frames'])
            cv2.putText(frame_out, str_on_frame, (5, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame_out, global_str + str(round(change_pos, 2)) + ' sec', (5, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame_out, nr_locuri_libere + str(number), (5, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0),
                        2,
                        cv2.LINE_AA)

        # detectare miscare obiecte
        if dict['motion_detection']:
            # frame_blur = frame_blur[380:420, 240:470]
            # cv2.imshow('dss', frame_blur)
            fgmask = fgbg.apply(frame_blur)
            bw = np.uint8(fgmask == 255) * 255
            bw = cv2.erode(bw, kernel_erode, iterations=1)
            bw = cv2.dilate(bw, kernel_dilate, iterations=1)
            # cv2.imshow('dss',bw)
            # cv2.imwrite("frame%d.jpg" % co, bw)
            (cnts, _) = cv2.findContours(bw.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # loop over the contours
            for c in cnts:
                # print(cv2.contourArea(c))
                # ignor contur mic
                if cv2.contourArea(c) < dict['min_area_motion_contour']:
                    continue
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame_out, (x, y), (x + w, y + h), (255, 0, 0), 1)

        # locuri libere si masini
        if dict['parking_detection']:
            for ind, park in enumerate(parking_data):
                points = np.array(park['points'])

                rect = parking_bounding_rects[ind]
                roi_gray = frame_gray[rect[1]:(rect[1] + rect[3]), rect[0]:(rect[0] + rect[2])]

                laplacian = cv2.Laplacian(roi_gray, cv2.CV_64F)
                # cv2.imshow('oir', laplacian)
                points[:, 0] = points[:, 0] - rect[0]  # roi
                points[:, 1] = points[:, 1] - rect[1]
                delta = np.mean(np.abs(laplacian * parking_mask[ind]))
                # if(delta<2.5):
                # print("ind, del", ind, delta)
                status = delta < dict['park_laplacian_th']
                # schimbare video, apare colt stanga sus, timpul ultimei schimbari
                if status != parking_status[ind] and parking_buffer[ind] is None:
                    parking_buffer[ind] = video_cur_pos
                    change_pos = video_cur_pos
                    # print("state ", ind,delta)
                    # classifier in caz de schimbare
                    # if dict['classifier_used']:
                    #     classifier_result = run_classifier(roi_gray)
                    #     if classifier_result:
                    #         print(classifier_result)
                elif status != parking_status[ind] and parking_buffer[ind] != None:
                    if video_cur_pos - parking_buffer[ind] > dict['park_sec_to_wait']:
                        parking_status[ind] = status
                        parking_buffer[ind] = None
                elif status == parking_status[ind] and parking_buffer[ind] != None:
                    parking_buffer[ind] = None

        # schimbare culoare
        if dict['parking_overlay']:
            number = 0
            # print(str(park['id']))

            # id_bool = [0] * 200
            # id_values = [0] * 200

            for ind, park in enumerate(parking_data):
                points = np.array(park['points'])
                # nr = park['id']
                # print(nr)
                # for i in range(nr):
                # id_values[i] = i

                if parking_status[ind]:
                    color = (0, 255, 0)
                    # print(park['id'])
                    # id_bool[park['id']] = 1
                    # print(id_bool)
                    number = number + 1
                    number_sms = number
                    rect = parking_bounding_rects[ind]
                    roi_gray_ov = frame_gray[rect[1]:(rect[1] + rect[3]),
                                  rect[0]:(rect[0] + rect[2])]  # crop roi pt calculare rapida

                    res = run_classifier(roi_gray_ov, ind)
                    if res:
                        parking_data_motion.append(parking_data[ind])
                        # del parking_data[ind]
                        color = (0, 0, 255)
                        # id_bool[park['id']] = 0
                else:
                    color = (0, 0, 255)
                    # id_bool[park['id']] = 0

                cv2.drawContours(frame_out, [points], contourIdx=-1,
                                 color=color, thickness=2, lineType=cv2.LINE_8)
                if dict['show_ids']:
                    print_parkIDs(park, points, frame_out)
                # print(id_values[0], ' ', id_bool[0])
            # f = open("values.txt", "w")
            # for i in range(nr):
            # f.write(str(id_values[i])+' '+str(id_bool[i])+ '\n')
            # f.close()
        if parking_data_motion:

            for index, park_coord in enumerate(parking_data_motion):

                points = np.array(park_coord['points'])
                color = (0, 0, 255)
                recta = parking_bounding_rects[ind]
                roi_gray1 = frame_gray[recta[1]:(recta[1] + recta[3]),
                            recta[0]:(recta[0] + recta[2])]  # crop roi pt calc rapida
                # laplacian = cv2.Laplacian(roi_gray, cv2.CV_64F)
                # delta2 = np.mean(np.abs(laplacian * parking_mask[ind]))
                # state = delta2<1
                # classifier_result = run_classifier(roi_gray1, index)
                # cv2.imshow('dsd', roi_gray1)
                fgbg1 = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=16, detectShadows=True)
                roi_gray1_blur = cv2.GaussianBlur(roi_gray1.copy(), (5, 5), 3)
                # cv2.imshow('sd', roi_gray1_blur)
                fgmask1 = fgbg1.apply(roi_gray1_blur)
                bw1 = np.uint8(fgmask1 == 255) * 255
                bw1 = cv2.erode(bw1, kernel_erode, iterations=1)
                bw1 = cv2.dilate(bw1, kernel_dilate, iterations=1)
                # cv2.imshow('sd', bw1)
                # cv2.imwrite("frame%d.jpg" % co, bw)
                (cnts1, _) = cv2.findContours(bw1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # loop over the contours
                for c in cnts1:
                    # print(cv2.contourArea(c))
                    # if the contour is too small, we ignore it
                    if cv2.contourArea(c) < 4:
                        continue
                    (x, y, w, h) = cv2.boundingRect(c)
                    classifier_result1 = run_classifier(roi_gray1, index)
                    if classifier_result1:
                        # print(classifier_result1)
                        color = (0, 0, 255)  # rosu daca e masina
                    else:
                        color = (0, 255, 0)

                classifier_result1 = run_classifier(roi_gray1, index)

                if classifier_result1:
                    # print(classifier_result1)
                    color = (0, 0, 255)  # rosu daca e masina
                else:
                    color = (0, 255, 0)

                cv2.drawContours(frame_out, [points], contourIdx=-1,
                                 color=color, thickness=2, lineType=cv2.LINE_8)

        if dict['pedestrian_detection']:
            # oameni, viteza cpu mare
            (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
            # boxes
            for (x, y, w, h) in rects:
                cv2.rectangle(frame_out, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # output frame
        if dict['save_video']:
            #         if video_cur_frame % 35 == 0: # take every 30 frames
            out.write(frame_out)

        f = open("number.txt", "w")
        f.write(str(number))
        f.close()
        # video
        cv2.imshow('frame', frame_out)
        # cv2.imshow('background mask', bw)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('c'):
            cv2.imwrite('frame_3.jpg', frame_initial)
        elif k == ord('j'):
            cap.set(cv2.CAP_PROP_POS_FRAMES, video_cur_frame + 1000)  # jump 1000 frames
        elif k == ord('u'):
            cap.set(cv2.CAP_PROP_POS_FRAMES, video_cur_frame + 50)  # jump 500 frames
        elif k == ord('s'):
            if not sms_sent:
                print("SE TRIMITE SMS!!!")
                message = client.messages.create(
                    body="Sunt " + str(number) + " locuri libere de parcare",
                    from_=twilio_source_phone_number,
                    to="+40741213687"
                )
                sms_sent = True
        if cv2.waitKey(33) == 27:
            break
    cv2.waitKey(0)
    cap.release()
    if dict['save_video']: out.release()
    cv2.destroyAllWindows()


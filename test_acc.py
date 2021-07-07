import cv2
import msvcrt as m
import numpy as np
from imutils.object_detection import non_max_suppression


def wait():
    m.getch()


def get_acc(cascade_src):
    total = [30, 30, 30, 30, 30]
    car_cascade = cv2.CascadeClassifier(cascade_src)
    counter = 1
    index = 0
    list_of_indexes = []
    while True:
        if counter < 6:
            img_init = cv2.imread('images_test/frame_0%d.png' % counter)
            img = cv2.resize(img_init, None, fx=0.6, fy=0.6)
        else:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in cars])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
            index += 1
        counter += 1
        k = cv2.waitKey(0)
        saved = index
        print("%d autovehicule detectate." % saved)
        list_of_indexes.append(saved / total[counter - 2])
        index = 0
        # input("press ")
        if k == 32:
            continue
        # press escape key to exit
        if cv2.waitKey(33) == 27:
            break
        # os.system("pause")
    suma = 0
    for i in list_of_indexes:
        suma = suma + i

    percentage = (suma / len(list_of_indexes)) * 100
    print("Acuratețe vehicule: ", percentage)
    cv2.destroyAllWindows()
    return percentage


# import system module
import sys
import os
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import time
import datetime

# import Opencv module
import cv2
import numpy as np
import recognizer
import pyrebase
import firebase

# from ui_main_window import *
from screen import *
from update_ui import *
import update_model

# Load Haar Cascade Face Detection
font = cv2.FONT_HERSHEY_SIMPLEX
faceCascade = cv2.CascadeClassifier('API/haarcascade_frontalface_default.xml')



def face_detection(img):
    while True:
        # img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            return True, (x, y, w, h)

        return False, (0 ,0 ,0 ,0)

class ImportWindow(QWidget):

    # class constructor
    def __init__(self):

        self.total = 0
        # call QWidget constructor
        super().__init__()

        self.ui = Ui_Form_update()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        self.controlTimer()

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCamImport)
        self.ui.import_bt.clicked.connect(self.recognition)
        self.ui.exit_bt.clicked.connect(self.exit)



    # view camera
    def viewCamImport(self):

        # read image in BGR format
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert image to RGB format
        height, width, channel = image.shape
        step = channel * width

        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)

        # show image in img_label
        self.ui.label.setPixmap(QPixmap.fromImage(qImg))
    
    def recognition(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        bool_face, rect = face_detection(image)
        if bool_face:
            self.flag = 1
        else:
            self.flag = 0


        #check flag is on or off
        if self.flag == 1:
            self.ui.line_status.repaint()
            self.ui.line_status.setText("Detected Face. Please wait....")
            id = recognizer.face_recognition(self.cap)  # receive ID

            if id >0:
                self.ui.line_status.setText("Face already in database")
            else:
                lineID = self.ui.lineID.text()
                lineName = self.ui.line_Name.text()
                f_maSV_current = open("student_list.txt")
                f_maSVs_list_current = f_maSV_current.read().splitlines()

                f_nameSV_current = open("student_list_name.txt")
                f_nameSVs_list_current = f_nameSV_current.read().splitlines()
                num_id = len(f_nameSVs_list_current)
                f_maSV_current.close()
                f_nameSV_current.close()

                if lineID != "0" and lineName != "0":

                    if (lineID in f_maSVs_list_current):
                        self.ui.line_status.setText("ID is already in database")
                        return

                    count = 0
                    id = num_id
                    print("[SYSTEM] adding new student with ID:"+ str(id))

                    try:
                        os.mkdir("dataset_update/" + "new")
                    except:
                        print("[SYSTEM] data folder is already created")

                    while (True):
                        self.ui.line_status.setText("Getting Face")
                        ret, img = self.cap.read()
                        height, width, channel = img.shape
                        step = channel * width

                        # create QImage from image
                        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)

                        # show image in img_label
                        self.ui.label.setPixmap(QPixmap.fromImage(qImg))
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
                        print("get face")
                        count += 1
                        cv2.imwrite("dataset_update/" + "new" + "/"  + str(count) + ".jpg", img)
                        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
                        self.ui.line_status.setText("Please stand in front of Camera")

                        if k == 27:
                            break
                        elif count >= 10:  
                            break

                    f_maSV = open("student_list.txt", "a")
                    f_nameSV = open("student_list_name.txt", "a")
                    f_maSV.write(self.ui.lineID.text())
                    f_maSV.write("\n")
                    f_nameSV.write(self.ui.line_Name.text())
                    f_nameSV.write("\n")

                    self.ui.line_status.setText("Getting Face Done")
                    f_maSV.close()
                    f_nameSV.close()
                    
                    self.ui.line_status.setText("Updating Model.... Please wait")
                    update_model.update_mol("dataset_update", id)

                    self.ui.line_status.setText("Model has been updated")
                    self.controlTimer()
                    self.close()
                else:
                    self.ui.line_status.setText("Invalid ID and Name")


    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():

            self.cap = cv2.VideoCapture(0)

            # create video capture
            self.init_time = time.time()

            # start timer
            self.timer.start(1)

        else:

            self.cap.release()
            self.timer.stop()

            # release video capture
            self.ui.lineID.setText("0")
            self.ui.line_Name.setText("0")

    def exit(self):
        self.controlTimer()
        self.close()


def import_window():

    app = QApplication(sys.argv)
    init_time = time.time()

    # create and show mainWindow
    main = ImportWindow()
    main.show()

    # close file
    print("Close Windows")

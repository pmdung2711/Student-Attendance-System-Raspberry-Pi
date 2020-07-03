# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import time module 
import time
import datetime

# import Opencv and ML module
import cv2
import numpy as np
import recognizer
import imutils

#import firebase module 
import pyrebase # pyrebase library
import firebase # firebase configuration file 

#from ui_main_window import *
from screen import *
from import_window import *
from list import *
from info import *

#Load Haar Cascade Face Detection
font = cv2.FONT_HERSHEY_SIMPLEX
faceCascade = cv2.CascadeClassifier('API/haarcascade_frontalface_default.xml')

# Create list to save data
list_id = []
list_id_time = []
list_id_status = []

# flag for element
flag = 0

# Create Date in History
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")


# Face Detection function 
def face_detection(img):
    while True:
        
        #convert image to gray image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #detect face in image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )
        #getting face location in image
        for (x, y, w, h) in faces:
            return True, (x, y, w, h)
        
        #return False if there's no face 
        return False, (0,0,0,0)


"""
===================Main Program========================
Class: MainWindow 
UI file: screen.py 
=======================================================
"""

class MainWindow(QWidget):

    # class constructor
    def __init__(self):
        self.total = 0
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.flag = 0
        self.time_flag = 0
        self.start = time.time()
        self.init_time = time.time()
        self.idle = True
        self.wait_flag = 0
        self.wait_time = time.time()

        self.if_new_id = False
        self.if_delete = False
        #list
        self.list = []

        # create a timer for displaying video
        self.timer = QTimer()
        self.ui.exit_bt.setText("Send Data and Exit")

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)

        # set button clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)

        self.ui.result_bt.clicked.connect(self.showListDialog)
        self.ui.class_bt.clicked.connect(self.showInfoDialog)
        self.ui.exit_bt.clicked.connect(self.exitWindow)
        self.ui.import_bt.clicked.connect(self.importWindow)
        self.ui.result_bt_2.clicked.connect(self.delete_recent_id)


    # view camera
    def viewCam(self):

        # read image in BGR format
        ret, image = self.cap.read()
        bool_face = True
        rect = []

        # convert image to RGB format
        flag = 0
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Check if any face is detected
        if self.wait_flag == 0:
            bool_face, rect = face_detection(image)
            x, y, w, h = rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #set flag
        if bool_face:
            self.flag = 1
        else:
            self.flag = 0

        # get image infos
        if self.wait_flag == 0:
            self.recognition()
        else:
            if time.time() - self.wait_time < 5:
                if self.if_delete:
                    self.ui.label.setText("Deleted ID. Saving result after " + str(5 - int(time.time() - self.wait_time)) + " seconds")
                else:
                    self.ui.label.setText("Saving result after " + str(5 - int(time.time() - self.wait_time)) + " seconds")

            else:
                self.wait_flag = 0
                self.if_new_id = False
                self.if_delete = False


        self.check_time()
        image = imutils.resize(image, width=640, height = 480)

        height, width, channel = image.shape
        step = channel * width

        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)

        # show image in screen
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))


    # start/stop timer
    def recognition(self):


        #check flag is on or off
        if self.flag == 1:
            self.ui.label.repaint()

            #check countdown
            if self.time_flag == 0:
                self.start = time.time()
                self.time_flag = 1

            #end countdown
            if  self.time_flag == 1 and time.time() - self.start > 1:
                print("Start Recognizing")
                id = recognizer.face_recognition(self.cap) #receive ID
                print("ID = " + str(id))

                self.time_flag = 0 #reset countdown

                #Read current file
                f_maSV = open("student_list.txt")
                f_maSVs = f_maSV.read().splitlines()
                f_nameSV = open("student_list_name.txt")
                f_nameSVs = f_nameSV.read().splitlines()
                f_maSV.close()
                f_nameSV.close()

                if id != -1:  # face is detected!
                    # Set Time
                    now = datetime.datetime.now()
                    ctime = time.time() - self.init_time

                    # Save Result
                    if id != 0 and f_maSVs[id] not in list_id:
                        list_id_time.append(now.strftime("%H:%M:%S"))
                        list_id.append(f_maSVs[id])
                        list_id_status.append("")
                        self.total+=1
                        self.if_new_id = True

                    # Display result
                    self.ui.label_4.setText(f_nameSVs[id]) #show name
                    self.ui.label_5.setText(f_maSVs[id]) #show ID
                    self.ui.image = QtGui.QImage("temporary.jpg") #Show recent image
                    self.ui.pixmap = QtGui.QPixmap.fromImage(self.ui.image)
                    self.ui.label_6.setPixmap(self.ui.pixmap)
                    self.ui.label_6.setScaledContents(True)
                    self.wait_flag = 1
                    self.wait_time = time.time()
            else:
                self.ui.label.setText("Detected Face. Please wait after " + str(1 - int(time.time() - self.start)) + " seconds")



        else:
            self.ui.label.repaint()
            self.start = time.time()
            self.ui.label.setText("Please stand in front of camera")



    def exitWindow(self):
        self.ui.label.repaint()


        #Save 
        f = open("History/" + date + ".txt", "w+")
        for item, item_time, item_status in zip(list_id, list_id_time, list_id_status):
            f.write(str(item) + " " + str(item_time) + " " + str(item_status) + "\n")
        f.close()

        self.ui.label.setText("Sending data to Firebase")

        #Push data to firebase
        firebase.push_data()
        self.close()


    def check_time(self):

        etime = time.time() - self.init_time

        if etime < 720 and self.timer.isActive():
            minutes = int( (720 - etime) / 60 )
            seconds = int( (720 - etime) % 60 )
            self.ui.labelx.setText(str(minutes) + ":" + str(seconds))
        else:
            self.ui.labelx.setText("Ket thuc")
            self.controlTimer()

    def controlTimer(self):

        # if timer is stopped
        if not self.timer.isActive():
            print("[SYSTEM] Capturing....")
            self.cap = cv2.VideoCapture(0)
            self.cap.set(3,320)
            self.cap.set(4,240)

            # create video capture
            self.init_time = time.time()

            # start timer
            self.timer.start(1)
            self.flag = 0
            self.time_flag = 0
            self.start = time.time()
            self.init_time = time.time()
            self.idle = False
            self.wait_flag = 0
            self.wait_time = time.time()

            self.if_new_id = False
            self.if_delete = False

            # update control_bt text
            self.ui.control_bt.setText("Stop Recognition")
        else:
            self.timer.stop()
            # release video captures
            print("[SYSTEM] Release Cap")
            self.cap.release()
            self.idle = True
            # update control_bt text
            self.ui.control_bt.setText("Start Recognition")
            self.ui.label.setText("Press Start to Recognize")
            # update file


    def importWindow(self):
        print("[SYSTEM] Open Import Windows...")

        # create and show mainWindow
        if self.idle:
            self.update_main = ImportWindow()
            self.update_main.show()

    def showListDialog(self):
        self.list_dialog = QtWidgets.QDialog()
        self.list_ui = Ui_Dialog_list()
        self.list_ui.setupUi(self.list_dialog, list_id, list_id_time, list_id_status)
        self.list_dialog.show()

    def showInfoDialog(self):
        self.info_dialog = QtWidgets.QDialog()
        self.list_info = Ui_Dialog_info()
        self.list_info.setupUi(self.info_dialog)
        self.info_dialog.show()

    def delete_recent_id(self):
        if self.wait_flag == 1 and self.if_new_id == True:
            global list_id, list_id_time, list_id_status
            list_id = list_id[:-1]
            list_id_time = list_id_time[:-1]
            list_id_status = list_id_status[:-1]
            self.if_new_id = False
            self.ui.label.setText("Deleted recent ID")
            self.if_delete = True

        else:
            self.ui.label.setText("Can not remove recent ID. Out of time!!")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    init_time = time.time()

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    # close file
    print("Close Windows")

    sys.exit(app.exec_())
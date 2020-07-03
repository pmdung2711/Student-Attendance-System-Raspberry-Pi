# import the necessary packages
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import time
import datetime
import embedding
import dlib

# Setup argument
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--recognizer", default = "Models/recognizer.pickle")
ap.add_argument("-l", "--le", default = "Models/label.pickle")
ap.add_argument("-ru", "--recognizer_update", default = "Models/recognizer_update.pickle",)
ap.add_argument("-lu", "--le_update", default = "Models/label_update.pickle")
args = vars(ap.parse_args())

#Load Haar Cascade Face Detection
faceCascade = cv2.CascadeClassifier('API/haarcascade_frontalface_default.xml')

#Set threshold
threshold = 0.7
num = open("Models/number.txt")
num_len = len(num.read().splitlines()) - 1
threshold_update = 0
if num_len < 5:
	threshold_update = 0.98
else:
	if num_len < 15:
		threshold_update = 0.9
	else:
		if num_len < 25:
			threshold_update = 0.85
		else:
			if num_len < 35:
				threshold_update = 0.8
			else:
				if num_len < 45:
					threshold_update = 0.75
				else:
					threshold_update = 0.7
num.close()


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


def face_recognition(cam):

	# load the face recognition model along with the label encoder
	recognizer = pickle.loads(open(args["recognizer"], "rb").read())
	le = pickle.loads(open(args["le"], "rb").read())
	detect_update = False
	try:
		recognizer_update = pickle.loads(open(args["recognizer_update"], "rb").read())
		le_update = pickle.loads(open(args["le_update"], "rb").read())
		detect_update = True 
	except: 
		print("[SYSTEM] No updated model")

    #Process image
	ret, image = cam.read()
	(h, w) = image.shape[:2]
	bool_face, rect = face_detection(image)
	if not bool_face:
		return -1
	x, y, w, h = rect
	cv2.rectangle(image, (x, y), (x+w, y+h),
				  (0, 0, 255), 2)

	# Get current time
	current_time = datetime.datetime.now()
	ctime = current_time.strftime("%H:%M:%S")

	# Save progess
	cv2.imwrite("temporary.jpg", image)

	# Prepare Input for Neural Network
	rect = dlib.rectangle(x, y, x+w, y+h)

	# Get embeddings
	grab, vec = embedding.compute_embeddings(image, rect)

	# Predict person
	if grab == 1:

		# perform classification to recognize the face
		preds = recognizer.predict_proba(np.reshape(vec, (-1, 128)))[0]
		j = np.argmax(preds)
		proba = preds[j]
		name = le.classes_[j]
		print("[System] Predict ID:"+ name + " proba:"+ str(int(proba*100)))

		if proba < threshold:

			if detect_update:
				print("[System] Try on updated model...")
				preds = recognizer_update.predict_proba(np.reshape(vec, (-1, 128)))[0]
				j = np.argmax(preds)
				proba = preds[j]
				name = le_update.classes_[j]
				print("New threshold = : " + str(ths))
				print("[System] Predict ID:" + name + " proba:"+ str(int(proba*100)))

				if proba < threshold_update:
					return 0
				else:
					return int(name)

			return 0

		else:
			return int(name)

	return -1





# import the necessary packages
import sys
import os
import dlib
import numpy as np

#Load shape predictor model 
sp = dlib.shape_predictor("API/shape_predictor_68_face_landmarks.dat")

#Load Face Embeddings Model 
facerec = dlib.face_recognition_model_v1("API/dlib_face_recognition_resnet_model_v1.dat")

def compute_embeddings(img, rect):
	#Facial Landmark
    shape = sp(img, rect)

    # align face
    face_chip = dlib.get_face_chip(img, shape)

    #get embeddings
    face_descriptor_from_prealigned_image = facerec.compute_face_descriptor(face_chip, 1)

    return 1, np.array(face_descriptor_from_prealigned_image)

    return -1, -1

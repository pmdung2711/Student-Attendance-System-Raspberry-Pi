# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle
import time
import datetime

#start time counter
start = time.time()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--embeddings", default = "Models/embeddings.pickle")
ap.add_argument("-r", "--recognizer", default = "Models/recognizer.pickle")
ap.add_argument("-l", "--le", default = "Models/label.pickle")
args = vars(ap.parse_args())


# load the face embeddings
print("[SYSTEM] loading face embeddings...")
data = pickle.loads(open(args["embeddings"], "rb").read())

# encode the labels
print("[SYSTEM] encoding labels...")
le = LabelEncoder()
labels = le.fit_transform(data["names"])


# train the model used to accept the 128-d embeddings of the face and
# then produce the face recognition model
print("[SYSTEM] training model...")
recognizer = SVC(C=1.0, kernel="linear", probability=True)

recognizer.fit(data["embeddings"], labels)


# write the actual face recognition model to disk
f = open(args["recognizer"], "wb")
f.write(pickle.dumps(recognizer))
f.close()

# write the label encoder to disk
f = open(args["le"], "wb")
f.write(pickle.dumps(le))
f.close()

start = time.time() - start
minutes = int( start / 60 )
seconds = int( start % 60 )
print("Finish after: " + str(minutes) + ":" + str(seconds))

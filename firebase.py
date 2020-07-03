
import pyrebase
import time
import datetime

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

def push_data():

    #setup API
    config = {
        "apiKey": "AIzaSyCNKnnz2QJjr8TERzUvCZsEbU53gV1lPUQ",
        "authDomain": "case-study-70877.firebaseapp.com/",
        "databaseURL": "https://case-study-70877.firebaseio.com",
        "storageBucket": "case-study-70877.appspot.com",
    }

    #get time and open history file
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    fdb = open("History/" + date + ".txt", "r")
    f1 = fdb.readlines()
    print("Date: " + date)

    #connect to firebase
    print("Sending data to FIREBASE...")
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child(date).remove()
    for x in f1:
        print("Generating data....")
        temp = x.split()
        data = {
            "maSV": temp[0],
            "status": "",
            "time": temp[1]
        }
        print("Pushed data.")
        try:
            db.child(date).push(data)
        except:
            print("Data not pushed!!")
    print("SENDING DATA SUCESSFULLY")
    fdb.close()


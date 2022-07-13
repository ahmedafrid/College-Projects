import numpy as np
import cv2
import pickle

import pyttsx3
tts = pyttsx3.init()

#############################################

frameWidth = 640  # CAMERA RESOLUTION
frameHeight = 480
brightness = 180
threshold = 0.95  # PROBABLITY THRESHOLD
font = cv2.FONT_HERSHEY_SIMPLEX
##############################################

# SETUP THE VIDEO CAMERA
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)

# IMPORT THE TRANNIED MODEL
pickle_in = open("model_trained.p", "rb")  ## rb = READ BYTE
model = pickle.load(pickle_in)

# SETUP THE VIDEO CAMERA FOR PHONE
# cap = cv2.VideoCapture(0)
# address="http://192.168.43.1:8080//video"
# cap.open(address)


def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def equalize(img):
    img = cv2.equalizeHist(img)
    return img


def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img


def getCalssName(classNo):
    if classNo == 0:
        tts.say("Speed Limit 20 km")
        voice = tts.runAndWait()
        return 'Speed Limit 20 km/h', voice

    elif classNo == 1:
        tts.say("Speed Limit 30 km")
        voice = tts.runAndWait()
        return 'Speed Limit 30 km/h', voice

    elif classNo == 2:
        tts.say("Speed Limit 50 km")
        voice = tts.runAndWait()
        return 'Speed Limit 50 km/h', voice
    elif classNo == 3:
        tts.say("Speed Limit 60 km")
        voice = tts.runAndWait()
        return 'Speed Limit 60 km/h', voice
    elif classNo == 4:
        tts.say("Speed Limit 70 km")
        voice = tts.runAndWait()
        return 'Speed Limit 70 km/h', voice
    elif classNo == 5:
        tts.say("Speed Limit 80 km")
        voice = tts.runAndWait()
        return 'Speed Limit 80 km/h', voice
    elif classNo == 6:
        tts.say("End of Speed Limit 80 km")
        voice = tts.runAndWait()
        return 'End of Speed Limit 80 km/h', voice
    elif classNo == 7:
        tts.say("Speed Limit 100 km")
        voice = tts.runAndWait()
        return 'Speed Limit 100 km/h', voice
    elif classNo == 8:
        tts.say("Speed Limit 120 km")
        voice = tts.runAndWait()
        return 'Speed Limit 120 km/h', voice
    elif classNo == 9:
        tts.say("No passing")
        voice = tts.runAndWait()
        return 'No passing', voice
    elif classNo == 10:
        tts.say("No passing for vechiles over 3.5 metric tons")
        voice = tts.runAndWait()
        return 'No passing for vechiles over 3.5 metric tons', voice
    elif classNo == 11:
        tts.say("Right-of-way at the next intersection")
        voice = tts.runAndWait()
        return 'Right-of-way at the next intersection', voice
    elif classNo == 12:
        tts.say("Priority road")
        voice = tts.runAndWait()
        return 'Priority road', voice
    # elif classNo == 13:
    #     tts.say("Yield")
    #     voice = tts.runAndWait()
    #     return 'Yield', voice
    elif classNo == 14:
        tts.say("Stop")
        voice = tts.runAndWait()
        return 'Stop', voice
    elif classNo == 15:
        tts.say("No vechiles")
        voice = tts.runAndWait()
        return 'No vechiles', voice
    elif classNo == 16:
        tts.say("Vechiles over 3.5 metric tons prohibited")
        voice = tts.runAndWait()
        return 'Vechiles over 3.5 metric tons prohibited', voice
    elif classNo == 17:
        tts.say("No entry")
        voice = tts.runAndWait()
        return 'No entry', voice
    elif classNo == 18:
        tts.say("General caution")
        voice = tts.runAndWait()
        return 'General caution', voice
    elif classNo == 19:
        tts.say("Dangerous curve to the left")
        voice = tts.runAndWait()
        return 'Dangerous curve to the left', voice
    elif classNo == 20:
        tts.say("Dangerous curve to the right")
        voice = tts.runAndWait()
        return 'Dangerous curve to the right', voice
    elif classNo == 21:
        tts.say("Double curve")
        voice = tts.runAndWait()
        return 'Double curve', voice
    elif classNo == 22:
        tts.say("Bumpy road")
        voice = tts.runAndWait()
        return 'Bumpy road', voice
    elif classNo == 23:
        tts.say("Slippery road")
        voice = tts.runAndWait()
        return 'Slippery road', voice
    elif classNo == 24:
        tts.say("Road narrows on the right")
        voice = tts.runAndWait()
        return 'Road narrows on the right', voice
    elif classNo == 25:
        tts.say("Road work")
        voice = tts.runAndWait()
        return 'Road work', voice
    elif classNo == 26:
        tts.say("Traffic signals")
        voice = tts.runAndWait()
        return 'Traffic signals', voice
    elif classNo == 27:
        tts.say("Pedestrians")
        voice = tts.runAndWait()
        return 'Pedestrians', voice
    elif classNo == 28:
        tts.say("Children crossing")
        voice = tts.runAndWait()
        return 'Children crossing', voice
    elif classNo == 29:
        tts.say("Bicycles crossing")
        voice = tts.runAndWait()
        return 'Bicycles crossing', voice
    elif classNo == 30:
        tts.say("Beware of ice/snow")
        voice = tts.runAndWait()
        return 'Beware of ice/snow', voice
    elif classNo == 31:
        tts.say("Wild animals crossing")
        voice = tts.runAndWait()
        return 'Wild animals crossing', voice
    elif classNo == 32:
        tts.say("End of all speed and passing limits")
        voice = tts.runAndWait()
        return 'End of all speed and passing limits', voice
    elif classNo == 33:
        tts.say("Turn right ahead")
        voice = tts.runAndWait()
        return 'Turn right ahead', voice
    elif classNo == 34:
        tts.say("Turn left ahead")
        voice = tts.runAndWait()
        return 'Turn left ahead', voice
    elif classNo == 35:
        tts.say("Ahead only")
        voice = tts.runAndWait()
        return 'Ahead only', voice
    elif classNo == 36:
        tts.say("Go straight or right")
        voice = tts.runAndWait()
        return 'Go straight or right', voice
    elif classNo == 37:
        tts.say("Go straight or left")
        voice = tts.runAndWait()
        return 'Go straight or left', voice
    elif classNo == 38:
        tts.say("Keep right")
        voice = tts.runAndWait()
        return 'Keep right', voice
    elif classNo == 39:
        tts.say("Keep left")
        voice = tts.runAndWait()
        return 'Keep left', voice
    elif classNo == 40:
        tts.say("Roundabout mandatory")
        voice = tts.runAndWait()
        return 'Roundabout mandatory', voice
    elif classNo == 41:
        tts.say("End of no passing")
        voice = tts.runAndWait()
        return 'End of no passing', voice
    elif classNo == 42:
        tts.say("End of no passing by vechiles over 3.5 metric tons")
        voice = tts.runAndWait()
        return 'End of no passing by vechiles over 3.5 metric tons', voice
    else:
        tts.say("No Traffic Sign Detected")
        voice = tts.runAndWait()
        return 'No Traffic Sign Detected', voice

while True:

    # READ IMAGE
    success, imgOrignal = cap.read()

    # PROCESS IMAGE
    # READ IMAGE
    success, imgOrignal = cap.read()

    # PROCESS IMAGE
    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 32, 32, 1)
    cv2.putText(imgOrignal, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    # PREDICT IMAGE
    predictions = model.predict(img)
    classIndex = model.predict_classes(img)
    probabilityValue = np.amax(predictions)
    if probabilityValue > threshold:
    # print(getCalssName(classIndex))
        cv2.putText(imgOrignal, str(classIndex) + " " + str(getCalssName(classIndex)), (120, 35), font, 0.75, (0, 0, 255), 2,
                    cv2.LINE_AA)
        cv2.putText(imgOrignal, str(round(probabilityValue * 100, 2)) + "%", (180, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("Result", imgOrignal)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
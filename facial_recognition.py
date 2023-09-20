import cv2
import numpy as np
import face_recognition
import os
import time
from send import sendpicture

cap = cv2.VideoCapture(0)  # Change the value based upon your camera
path = 'images'  # Path to the input images
images = []
classNames = []

# Extracting the encodings
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Completed')

if not os.path.exists('detectedimages'):
    os.mkdir('detectedimages')

# Face recognition part
def fcr(img):
    time_stamp = str(time.time())
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    print(len(facesCurFrame))
    print(f'Number of People Detected: {len(facesCurFrame)}')  # Count the number of people present

    for faceLoc in facesCurFrame:
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        img = cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        img = cv2.putText(img, 'Person', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    return img

if __name__ == '__main__':
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture frame")
            break

        img = fcr(img)
        cv2.imshow('Webcam', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

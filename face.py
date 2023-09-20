import cv2
import numpy as np
import face_recognition
import os
import time


cap = cv2.VideoCapture(0)  # change the value based upon your camara
path = 'images'  # path to the input images 
images = []
classNames = []
flag = 0

# Extracting the encodings #####

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


if not os.path.exists('detectedimgaes'):
    os.mkdir('detectedimgaes')

# Face recognition part


def fcr(img):
    time_stamp = str(time.time())
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    print(len(facesCurFrame))
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)
        # print(matches[matchIndex])
        if matches[matchIndex]:
            global flag
            flag = flag + 1
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            img = cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            img = cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            if flag == 8:
                print(f'Found !!!{name}')
                cv2.imwrite(f'detectedimgaes/{time_stamp}_{name}.png',img)
                data = f'Accused Found!!\n\n-------------------------------\nName: {name}\nFound at: code for india foundation \nLocation: https://www.google.com/maps/@17.3703168,78.4072704,13z \n-------------------------------'
                # sendpicture(data,f'detectedimgaes/{time_stamp}_{name}.png')
                flag = 0



if __name__ == '__main__':
    while True:
        time_stamp = str(time.time())
        success, img = cap.read()
        fcr(img)
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

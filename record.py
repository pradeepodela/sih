import sys
import datetime
import cv2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QImage, QGuiApplication, QPixmap
from PyQt5.uic import loadUi


class bindu(QDialog):
    def __init__(self):
        super(bindu, self).__init__()
        loadUi('videocv.ui', self)
        self.logic = 0

        self.START.clicked.connect(self.STARTClicked)

        self.TEXT.setText('kindly press "start button" button to record video')

        self.STOP.clicked.connect(self.STOPClicked)

    @pyqtSlot()
    def STARTClicked(self):
        self.logic = 1
        cap = cv2.VideoCapture(0)
        date = datetime.datetime.now()
        out = cv2.VideoWriter('C:/Users/TARUN/Downloads/video/video_%s%s%sT%s%s%s.mp4' % (date.year, date.month, date.day, date.hour, date.minute, date.second), -1, 20.0, (640, 480))

        while (cap.isOpened()):

            ret, frame = cap.read()
            if ret == True:

                self.displayImage(frame, 1)
                cv2.waitKey(1)


                if (self.logic == 1):
                    out.write(frame)

                    self.TEXT.setText('Start button')

                if (self.logic == 0):
                    self.TEXT.setText('Stop button')

                    break

            else:
                print('return not found')

        cap.release()
        cv2.destroyAllWindows()

    def STOPClicked(self):
        self.logic = 0

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:

            if(img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888

            else:
                qformat = QImage.Format_RGB888

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()

        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        # print('i am here')
        # self.imhLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    def fcr(self,img):
        pass


app = QApplication(sys.argv)
window = bindu()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')
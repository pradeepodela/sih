from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(928, 779)
        self.START = QtWidgets.QPushButton(Dialog)
        self.START.setGeometry(QtCore.QRect(80, 70, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.START.setFont(font)
        self.START.setObjectName("START")
        self.STOP = QtWidgets.QPushButton(Dialog)
        self.STOP.setGeometry(QtCore.QRect(420, 70, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.STOP.setFont(font)
        self.STOP.setObjectName("STOP")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(120, 210, 591, 451))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imgLabel.setMidLineWidth(0)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.TEXT = QtWidgets.QTextBrowser(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(40, 670, 741, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TEXT.setFont(font)
        self.TEXT.setObjectName("TEXT")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(119, 210, 591, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(9)
        self.frame.setObjectName("frame")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.START.setText(_translate("Dialog", "Start button"))
        self.STOP.setText(_translate("Dialog", "Stop button"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

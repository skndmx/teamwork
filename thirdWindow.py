# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CGU\OneDrive - Claremont Graduate University\IST303_Spring2019\teamwork\thirdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import newWindow

class Ui_thirdWindow(object):
    def setupUi(self, thirdWindow):
        thirdWindow.setObjectName("thirdWindow")
        thirdWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(thirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 110, 771, 81))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(50, 20, 50, 20))
        self.radioButton_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_1.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 20, 50, 20))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 20, 50, 20))
        self.radioButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(230, 20, 50, 20))
        self.radioButton_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(350, 20, 50, 20))
        self.radioButton_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(410, 20, 50, 20))
        self.radioButton_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setGeometry(QtCore.QRect(470, 20, 50, 20))
        self.radioButton_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setGeometry(QtCore.QRect(530, 20, 50, 20))
        self.radioButton_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_10.setGeometry(QtCore.QRect(590, 20, 50, 20))
        self.radioButton_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(290, 20, 50, 20))
        self.radioButton_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 70, 381, 16))
        self.label.setObjectName("label")
        thirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(thirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        thirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(thirdWindow)
        self.statusbar.setObjectName("statusbar")
        thirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(thirdWindow)
        QtCore.QMetaObject.connectSlotsByName(thirdWindow)


        buttonname = "0"
        if self.radioButton_1.isChecked():
            buttonname = "1"
        elif self.radioButton_2.isChecked():
            buttonname = "2"
        elif self.radioButton_3.isChecked():
            buttonname = "3"
        elif self.radioButton_4.isChecked():
            buttonname = "4"
        else: #self.radioButton_5.isChecked():
            buttonname = "5"
        #self.pushButton.clicked.connect(lambda: self.btn_clk())
        self.pushButton.clicked.connect(lambda: self.btn_clk(self.centralwidget.findChildren(QtWidgets.QRadioButton))
)


    def retranslateUi(self, thirdWindow):
        _translate = QtCore.QCoreApplication.translate
        thirdWindow.setWindowTitle(_translate("thirdWindow", "thirdWindow"))
        self.pushButton.setText(_translate("thirdWindow", "Submit"))
        self.radioButton_1.setText(_translate("thirdWindow", "1"))
        self.radioButton_2.setText(_translate("thirdWindow", "2"))
        self.radioButton_3.setText(_translate("thirdWindow", "3"))
        self.radioButton_4.setText(_translate("thirdWindow", "4"))
        self.radioButton_5.setText(_translate("thirdWindow", "5"))
        self.radioButton_6.setText(_translate("thirdWindow", "6"))
        self.radioButton_7.setText(_translate("thirdWindow", "7"))
        self.radioButton_8.setText(_translate("thirdWindow", "8"))
        self.radioButton_9.setText(_translate("thirdWindow", "9"))
        self.radioButton_10.setText(_translate("thirdWindow", "10"))
        self.label.setText(_translate("thirdWindow", "Q8. "))

    def btn_clk(self,chk):

        for items in chk:
            if items.isChecked():
                checked_radiobutton = items.text()
                #score = int(checked_radiobutton)
                print("Foo:",foo)
                print(newWindow.score)
                self.label.setText(checked_radiobutton)



'''

    def btn_clk(self, chk):
        score1 = 0
        global score
        global i
        i[0] = i[0]+1
        if chk:
            self.label2.setText("yes")
            score1 += 10
        else:
            self.label2.setText("No")
            score1 += 5
        self.label.setText("2. Did your server greet you?")
        if i[0] == 1:
            score[0] = score1
            print("Q1", score1, i[0],score[0])
        self.pushButton.clicked.connect(lambda: self.btn_clk1(self.radioButton.isChecked()))
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thirdWindow = QtWidgets.QMainWindow()
    ui = Ui_thirdWindow()
    ui.setupUi(thirdWindow)
    thirdWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dev\teamwork\newWindow_new.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newWindow(object):
    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(newWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 621, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 180, 411, 251))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setToolTip("")
        self.groupBox.setStatusTip("")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(140, 30, 100, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.radioButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radioButton.setFont(font)
        self.radioButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setIconSize(QtCore.QSize(20, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 120, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        newWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        newWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(newWindow)
        self.statusbar.setObjectName("statusbar")
        newWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newWindow)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

    def retranslateUi(self, newWindow):
        _translate = QtCore.QCoreApplication.translate
        newWindow.setWindowTitle(_translate("newWindow", "MainWindow"))
        self.label.setText(_translate("newWindow", "Have you been sat?"))
        self.radioButton.setText(_translate("newWindow", "Yes"))
        self.radioButton.setShortcut(_translate("newWindow", "Return"))
        self.radioButton_2.setText(_translate("newWindow", "No"))
        self.pushButton.setText(_translate("newWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newWindow = QtWidgets.QMainWindow()
    ui = Ui_newWindow()
    ui.setupUi(newWindow)
    newWindow.show()
    sys.exit(app.exec_())


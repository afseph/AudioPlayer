# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #161517;")
        self.centralwidget.setObjectName("centralwidget")
        self.PlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlayButton.setGeometry(QtCore.QRect(120, 470, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.PlayButton.setFont(font)
        self.PlayButton.setStyleSheet("QPushButton{\n"
"    backgound-color: #6d6d6d;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #2d2d2d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #454545;\n"
"}")
        self.PlayButton.setObjectName("PlayButton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(580, 470, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("QPushButton{\n"
"    backgound-color: #6d6d6d;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #2d2d2d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #454545;\n"
"}")
        self.StopButton.setObjectName("StopButton")
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(40, 170, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.LoadButton.setFont(font)
        self.LoadButton.setStyleSheet("QPushButton{\n"
"    backgound-color: #6d6d6d;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #2d2d2d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #454545;\n"
"}")
        self.LoadButton.setObjectName("LoadButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 170, 471, 251))
        self.listWidget.setStyleSheet("color:#fff;")
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 471, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff")
        self.label.setObjectName("label")
        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setGeometry(QtCore.QRect(350, 470, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.PauseButton.setFont(font)
        self.PauseButton.setStyleSheet("QPushButton{\n"
"    backgound-color: #6d6d6d;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #2d2d2d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #454545;\n"
"}")
        self.PauseButton.setObjectName("PauseButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(320, 430, 471, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.LoadButton.setText(_translate("MainWindow", "Load"))
        self.label.setText(_translate("MainWindow", "MP3 Player"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))

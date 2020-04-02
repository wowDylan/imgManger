# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgManger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_imgManger(object):
    def setupUi(self, imgManger):
        imgManger.setObjectName("imgManger")
        imgManger.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(imgManger)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 320, 231, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(270, 50, 511, 491))
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 50, 231, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        imgManger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(imgManger)
        self.statusbar.setObjectName("statusbar")
        imgManger.setStatusBar(self.statusbar)

        self.retranslateUi(imgManger)
        QtCore.QMetaObject.connectSlotsByName(imgManger)

    def retranslateUi(self, imgManger):
        _translate = QtCore.QCoreApplication.translate
        imgManger.setWindowTitle(_translate("imgManger", "MainWindow"))
        self.pushButton_3.setText(_translate("imgManger", "Write"))
        self.pushButton_5.setText(_translate("imgManger", "Prev img"))
        self.pushButton_6.setText(_translate("imgManger", "Next img"))
        self.pushButton.setText(_translate("imgManger", "Open img"))
        self.pushButton_7.setText(_translate("imgManger", "Auto callout"))
        self.pushButton_8.setText(_translate("imgManger", "+ +"))
        self.pushButton_9.setText(_translate("imgManger", "- -"))
        self.pushButton_2.setText(_translate("imgManger", "Open file"))
        self.pushButton_4.setText(_translate("imgManger", "Copy"))

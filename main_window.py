# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(325, 367)
        MainWindow.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 223, 255, 69), stop:0.375 rgba(0, 212, 255, 69), stop:0.423533 rgba(0, 255, 190, 145), stop:0.45 rgba(0, 180, 255, 208), stop:0.477581 rgba(71, 146, 255, 130), stop:0.518717 rgba(71, 146, 255, 130), stop:0.55 rgba(0, 104, 255, 255), stop:0.57754 rgba(0, 104, 255, 130), stop:0.625 rgba(0, 104, 255, 69), stop:1 rgba(0, 255, 180, 69));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_ne_task = QLineEdit(self.centralwidget)
        self.tb_ne_task.setObjectName(u"tb_ne_task")

        self.horizontalLayout.addWidget(self.tb_ne_task)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        font = QFont()
        font.setFamily(u"MRT_Nil 3")
        font.setPointSize(10)
        self.btn_new_task.setFont(font)

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tb_n_t_d = QTextEdit(self.centralwidget)
        self.tb_n_t_d.setObjectName(u"tb_n_t_d")

        self.verticalLayout.addWidget(self.tb_n_t_d)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setFamily(u"MRT_Nil 3")
        self.pushButton_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")

        self.horizontalLayout_2.addWidget(self.date)

        self.time = QLineEdit(self.centralwidget)
        self.time.setObjectName(u"time")

        self.horizontalLayout_2.addWidget(self.time)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.i_o_n = QLineEdit(self.centralwidget)
        self.i_o_n.setObjectName(u"i_o_n")

        self.verticalLayout.addWidget(self.i_o_n)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 325, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"insert date", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"insert time", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Important              or               Normal", None))
    # retranslateUi


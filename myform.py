# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 480)
        Form.setStyleSheet(u"QWidget {\n"
"	background: #eeeeee;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: #dedede;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #aaffff;\n"
"}\n"
"")
        self.table = QTableWidget(Form)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 10, 455, 455))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(500, 40, 131, 31))
        font = QFont()
        font.setFamily(u"Hack")
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.editNum = QLineEdit(Form)
        self.editNum.setObjectName(u"editNum")
        self.editNum.setGeometry(QRect(650, 40, 113, 32))
        self.editNum.setFont(font)
        self.editNum.setLayoutDirection(Qt.RightToLeft)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(500, 110, 281, 171))
        font1 = QFont()
        font1.setFamily(u"Hack")
        self.groupBox.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnStop = QPushButton(self.groupBox)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setFont(font)

        self.gridLayout.addWidget(self.btnStop, 0, 0, 1, 1)

        self.btnStart = QPushButton(self.groupBox)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setFont(font)

        self.gridLayout.addWidget(self.btnStart, 0, 1, 1, 1)

        self.btnReset = QPushButton(self.groupBox)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setFont(font)

        self.gridLayout.addWidget(self.btnReset, 1, 0, 1, 1)

        self.btnConfirm = QPushButton(self.groupBox)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setFont(font)

        self.gridLayout.addWidget(self.btnConfirm, 1, 1, 1, 1)

        self.slider = QSlider(Form)
        self.slider.setObjectName(u"slider")
        self.slider.setGeometry(QRect(500, 360, 281, 20))
        self.slider.setMaximum(1800)
        self.slider.setSingleStep(200)
        self.slider.setPageStep(200)
        self.slider.setValue(1000)
        self.slider.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 310, 51, 31))
        font2 = QFont()
        font2.setFamily(u"Hack")
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.btnExit = QPushButton(Form)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(660, 410, 129, 35))
        self.btnExit.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Queen Number:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Options", None))
        self.btnStop.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.btnStart.setText(QCoreApplication.translate("Form", u"Start", None))
        self.btnReset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Speed", None))
        self.btnExit.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi


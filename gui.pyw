from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(717, 487)
        Dialog.setStyleSheet(u"background-color: #90EE90;")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 70, 701, 361))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"background-color: #66CDAA;\n"
"font: 75 12pt \"Courier New\";\n"
"border 5px solid gray; \n"
"margin-left: 0px;\n"
"margin-right:0px;\n"
"width:100%;\n"
"}")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 440, 101, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Comic Sans MS\";\n"
"border: none;\n"
"background-color: #00BFFF;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid gray;\n"
"background-color: #FF6347;\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 4px solid gray;\n"
"background-color: #FF8C00;\n"
"color: black;\n"
"}")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 440, 211, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Comic Sans MS\";\n"
"border: none;\n"
"background-color: #00BFFF;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid gray;\n"
"background-color: #FF6347;\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 4px solid gray;\n"
"background-color: #FF8C00;\n"
"color: black;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, -10, 171, 71))
        self.label.setStyleSheet(u"QLabel{\n"
"font: 75 34pt \"Comic Sans MS\";\n"
"color: #FF7F50;\n"
"text-shadow: -10px 10px 0px #00e6e6,\n"
"-20px 20px 0px #01cccc,\n"
"-30px 30px 0px #00bdbd;\n"
"}\n"
"QLabel:hover{\n"
"font: 75 34pt \"Comic Sans MS\";\n"
"color: #FFA07A;\n"
"border 1px solid gray;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0440\u043b\u0438\u043d", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u0441\u0438\u0441\u0442\u0435\u043d\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0440\u043b\u0438\u043d", None))
    # retranslateUi


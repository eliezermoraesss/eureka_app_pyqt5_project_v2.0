# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\token_verification_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TokenVerificationWindow(object):
    def setupUi(self, TokenVerificationWindow):
        TokenVerificationWindow.setObjectName("TokenVerificationWindow")
        TokenVerificationWindow.resize(480, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TokenVerificationWindow.sizePolicy().hasHeightForWidth())
        TokenVerificationWindow.setSizePolicy(sizePolicy)
        TokenVerificationWindow.setStyleSheet("* {\n"
"    background-color: #ffffff;\n"
"    font-style: \"Segoe UI\";\n"
"     color: #0B090A;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #0B090A;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #DFE0E2;\n"
"    padding-left: 15px;\n"
"    border-radius: 18px;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #fbba72;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #399918;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #6703c5;\n"
"    color: #EEEEEE;\n"
"}\n"
"")
        self.token_field = QtWidgets.QLineEdit(TokenVerificationWindow)
        self.token_field.setGeometry(QtCore.QRect(160, 150, 161, 41))
        self.token_field.setMinimumSize(QtCore.QSize(150, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.token_field.setFont(font)
        self.token_field.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.token_field.setInputMask("")
        self.token_field.setText("")
        self.token_field.setMaxLength(6)
        self.token_field.setClearButtonEnabled(True)
        self.token_field.setObjectName("token_field")
        self.btn_verify_token = QtWidgets.QPushButton(TokenVerificationWindow)
        self.btn_verify_token.setGeometry(QtCore.QRect(120, 300, 111, 41))
        self.btn_verify_token.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.btn_verify_token.setFont(font)
        self.btn_verify_token.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/carraca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_verify_token.setIcon(icon)
        self.btn_verify_token.setIconSize(QtCore.QSize(24, 24))
        self.btn_verify_token.setObjectName("btn_verify_token")
        self.btn_close = QtWidgets.QPushButton(TokenVerificationWindow)
        self.btn_close.setGeometry(QtCore.QRect(250, 300, 111, 41))
        self.btn_close.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton:hover {\n"
"    background-color: #d60000;\n"
"    color: #EEEEEE\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/excluir (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(24, 24))
        self.btn_close.setObjectName("btn_close")
        self.window_title_bar = QtWidgets.QWidget(TokenVerificationWindow)
        self.window_title_bar.setGeometry(QtCore.QRect(0, 0, 481, 51))
        self.window_title_bar.setStyleSheet("* {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 7, 8, 255), stop:1 rgba(102, 7, 8, 255));\n"
"}")
        self.window_title_bar.setObjectName("window_title_bar")
        self.label_2 = QtWidgets.QLabel(self.window_title_bar)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"    font-size: 22px;\n"
"    font-weight: regular;\n"
"    font-style: \"Segoe UI\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.btn_new_token = QtWidgets.QPushButton(TokenVerificationWindow)
        self.btn_new_token.setGeometry(QtCore.QRect(160, 240, 161, 41))
        self.btn_new_token.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.btn_new_token.setFont(font)
        self.btn_new_token.setStyleSheet("QPushButton:hover {\n"
"    background-color: #00b4d8;\n"
"    color: #EEEEEE\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/codigo-binario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new_token.setIcon(icon2)
        self.btn_new_token.setIconSize(QtCore.QSize(24, 24))
        self.btn_new_token.setObjectName("btn_new_token")
        self.label = QtWidgets.QLabel(TokenVerificationWindow)
        self.label.setGeometry(QtCore.QRect(130, 120, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #0B090A;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    font-style: \"Segoe UI\";\n"
"}")
        self.label.setObjectName("label")

        self.retranslateUi(TokenVerificationWindow)
        QtCore.QMetaObject.connectSlotsByName(TokenVerificationWindow)

    def retranslateUi(self, TokenVerificationWindow):
        _translate = QtCore.QCoreApplication.translate
        TokenVerificationWindow.setWindowTitle(_translate("TokenVerificationWindow", "Eureka®"))
        self.btn_verify_token.setText(_translate("TokenVerificationWindow", "Verificar"))
        self.btn_close.setText(_translate("TokenVerificationWindow", " Cancelar"))
        self.label_2.setText(_translate("TokenVerificationWindow", "Verificação de token"))
        self.btn_new_token.setText(_translate("TokenVerificationWindow", "Gerar novo Token"))
        self.label.setText(_translate("TokenVerificationWindow", "Digite o token enviado para o seu e-mail:"))
import resource_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\new_product_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProductWindow(object):
    def setupUi(self, NewProductWindow):
        NewProductWindow.setObjectName("NewProductWindow")
        NewProductWindow.resize(640, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewProductWindow.sizePolicy().hasHeightForWidth())
        NewProductWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        NewProductWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/LOGO.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewProductWindow.setWindowIcon(icon)
        NewProductWindow.setStyleSheet("* {\n"
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
        self.window_title_bar = QtWidgets.QWidget(NewProductWindow)
        self.window_title_bar.setGeometry(QtCore.QRect(0, 0, 641, 51))
        self.window_title_bar.setStyleSheet("* {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(186, 24, 27, 255), stop:1 rgba(102, 7, 8, 255));\n"
"}")
        self.window_title_bar.setObjectName("window_title_bar")
        self.type_label = QtWidgets.QLabel(self.window_title_bar)
        self.type_label.setGeometry(QtCore.QRect(60, 0, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.type_label.setFont(font)
        self.type_label.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"    font-size: 22px;\n"
"    font-weight: regular;\n"
"    font-style: \"Segoe UI\";\n"
"}")
        self.type_label.setObjectName("type_label")
        self.enaplic_logo = QtWidgets.QLabel(self.window_title_bar)
        self.enaplic_logo.setGeometry(QtCore.QRect(590, 4, 41, 41))
        self.enaplic_logo.setText("")
        self.enaplic_logo.setPixmap(QtGui.QPixmap(":/image/image/LOGO.jpeg"))
        self.enaplic_logo.setScaledContents(True)
        self.enaplic_logo.setObjectName("enaplic_logo")
        self.main_area = QtWidgets.QWidget(NewProductWindow)
        self.main_area.setGeometry(QtCore.QRect(0, 50, 641, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_area.sizePolicy().hasHeightForWidth())
        self.main_area.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.main_area.setFont(font)
        self.main_area.setToolTipDuration(-4)
        self.main_area.setStyleSheet("* {\n"
"    background-color: #ffffff;\n"
"    font-style: \'Segoe UI\';\n"
"}\n"
"\n"
"QLabel, QCheckBox {\n"
"    color: #0B090A;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#logo-enaplic {\n"
"    margin: 5px 0;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #DFE0E2;\n"
"    padding-left: 11px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit, QComboBox {\n"
"    background-color: #DFE0E2;\n"
"    padding-left: 11px;\n"
"    border-radius: 18px;\n"
"    height: 20px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QComboBox::down-arrow {\n"
"    image: url(../static/icon/arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 1px solid #000000;\n"
"    background-color: #686D76;\n"
"    padding-left: 10px;\n"
"    margin-bottom: 15px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #262626;\n"
"    color: #A7A6A6;\n"
"    padding: 5px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section:horizontal {\n"
"    border-top: 1px solid #333;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #363636;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    padding-right: 8px;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #000000;\n"
"    color: #EEEEEE;\n"
"    font-weight: bold;\n"
"}")
        self.main_area.setObjectName("main_area")

        self.codigo_field = QtWidgets.QLineEdit(self.main_area)
        self.descricao_field = QtWidgets.QLineEdit(self.main_area)
        self.desc_comp_field = QtWidgets.QLineEdit(self.main_area)
        self.tipo_field = QtWidgets.QLineEdit(self.main_area)
        self.btn_search_tipo = QtWidgets.QPushButton(self.main_area)
        self.um_field = QtWidgets.QLineEdit(self.main_area)
        self.btn_search_um = QtWidgets.QPushButton(self.main_area)
        self.armazem_field = QtWidgets.QLineEdit(self.main_area)
        self.btn_search_arm = QtWidgets.QPushButton(self.main_area)
        self.cc_field = QtWidgets.QLineEdit(self.main_area)
        self.btn_search_cc = QtWidgets.QPushButton(self.main_area)
        self.bloquear_combobox = QtWidgets.QComboBox(self.main_area)
        self.endereco_field = QtWidgets.QLineEdit(self.main_area)
        self.grupo_field = QtWidgets.QLineEdit(self.main_area)
        self.btn_search_grupo = QtWidgets.QPushButton(self.main_area)
        self.desc_grupo_field = QtWidgets.QLineEdit(self.main_area)

        self.desc_comp_field.setGeometry(QtCore.QRect(50, 180, 551, 41))
        self.desc_comp_field.setMinimumSize(QtCore.QSize(301, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.desc_comp_field.setFont(font)
        self.desc_comp_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.desc_comp_field.setInputMask("")
        self.desc_comp_field.setText("")
        self.desc_comp_field.setMaxLength(60)
        self.desc_comp_field.setClearButtonEnabled(True)
        self.desc_comp_field.setObjectName("desc_comp_field")
        self.tipo_field.setGeometry(QtCore.QRect(50, 250, 91, 41))
        self.tipo_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.tipo_field.setFont(font)
        self.tipo_field.setTabletTracking(False)
        self.tipo_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tipo_field.setInputMask("")
        self.tipo_field.setText("")
        self.tipo_field.setMaxLength(2)
        self.tipo_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tipo_field.setClearButtonEnabled(True)
        self.tipo_field.setObjectName("tipo_field")
        self.desc_comp_label = QtWidgets.QLabel(self.main_area)
        self.desc_comp_label.setGeometry(QtCore.QRect(60, 160, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.desc_comp_label.setFont(font)
        self.desc_comp_label.setObjectName("desc_comp_label")
        self.tipo_label = QtWidgets.QLabel(self.main_area)
        self.tipo_label.setGeometry(QtCore.QRect(60, 230, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.tipo_label.setFont(font)
        self.tipo_label.setObjectName("tipo_label")
        self.btn_close = QtWidgets.QPushButton(self.main_area)
        self.btn_close.setGeometry(QtCore.QRect(490, 480, 111, 41))
        self.btn_close.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.btn_close.setFont(font)
        self.btn_close.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_close.setStyleSheet("QPushButton {\n"
"    background-color: #fbba72;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d60000;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #6703c5;\n"
"    color: #EEEEEE;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/excluir (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(16, 16))
        self.btn_close.setObjectName("btn_close")
        self.descricao_label = QtWidgets.QLabel(self.main_area)
        self.descricao_label.setGeometry(QtCore.QRect(60, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.descricao_label.setFont(font)
        self.descricao_label.setObjectName("descricao_label")
        self.descricao_field.setGeometry(QtCore.QRect(50, 110, 551, 41))
        self.descricao_field.setMinimumSize(QtCore.QSize(301, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.descricao_field.setFont(font)
        self.descricao_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.descricao_field.setAccessibleDescription("")
        self.descricao_field.setInputMask("")
        self.descricao_field.setText("")
        self.descricao_field.setMaxLength(100)
        self.descricao_field.setClearButtonEnabled(True)
        self.descricao_field.setObjectName("descricao_field")
        self.um_field.setGeometry(QtCore.QRect(220, 250, 91, 41))
        self.um_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.um_field.setFont(font)
        self.um_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.um_field.setInputMask("")
        self.um_field.setText("")
        self.um_field.setMaxLength(2)
        self.um_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.um_field.setClearButtonEnabled(True)
        self.um_field.setObjectName("um_field")
        self.um_label = QtWidgets.QLabel(self.main_area)
        self.um_label.setGeometry(QtCore.QRect(230, 230, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.um_label.setFont(font)
        self.um_label.setObjectName("um_label")
        self.armazem_label = QtWidgets.QLabel(self.main_area)
        self.armazem_label.setGeometry(QtCore.QRect(390, 230, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.armazem_label.setFont(font)
        self.armazem_label.setObjectName("armazem_label")
        self.btn_save = QtWidgets.QPushButton(self.main_area)
        self.btn_save.setGeometry(QtCore.QRect(360, 480, 111, 41))
        self.btn_save.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.btn_save.setFont(font)
        self.btn_save.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_save.setStyleSheet("QPushButton {\n"
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
"QPushButton:pressed {\n"
"    background-color: #6703c5;\n"
"    color: #EEEEEE;\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/icons8-salvar-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon2)
        self.btn_save.setIconSize(QtCore.QSize(16, 16))
        self.btn_save.setObjectName("btn_save")
        self.grupo_field.setGeometry(QtCore.QRect(50, 410, 91, 41))
        self.grupo_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.grupo_field.setFont(font)
        self.grupo_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.grupo_field.setInputMask("")
        self.grupo_field.setText("")
        self.grupo_field.setMaxLength(4)
        self.grupo_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.grupo_field.setClearButtonEnabled(True)
        self.grupo_field.setObjectName("grupo_field")
        self.grupo_label = QtWidgets.QLabel(self.main_area)
        self.grupo_label.setGeometry(QtCore.QRect(60, 390, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_label.setFont(font)
        self.grupo_label.setObjectName("grupo_label")
        self.desc_grupo_field.setGeometry(QtCore.QRect(210, 410, 391, 41))
        self.desc_grupo_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.desc_grupo_field.setFont(font)
        self.desc_grupo_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.desc_grupo_field.setInputMask("")
        self.desc_grupo_field.setText("")
        self.desc_grupo_field.setMaxLength(30)
        self.desc_grupo_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.desc_grupo_field.setReadOnly(True)
        self.desc_grupo_field.setClearButtonEnabled(False)
        self.desc_grupo_field.setObjectName("desc_grupo_field")
        self.desc_grupo_label = QtWidgets.QLabel(self.main_area)
        self.desc_grupo_label.setGeometry(QtCore.QRect(210, 390, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.desc_grupo_label.setFont(font)
        self.desc_grupo_label.setObjectName("desc_grupo_label")
        self.cc_label = QtWidgets.QLabel(self.main_area)
        self.cc_label.setGeometry(QtCore.QRect(60, 310, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.cc_label.setFont(font)
        self.cc_label.setObjectName("cc_label")
        self.bloquear_combobox.setGeometry(QtCore.QRect(240, 330, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bloquear_combobox.sizePolicy().hasHeightForWidth())
        self.bloquear_combobox.setSizePolicy(sizePolicy)
        self.bloquear_combobox.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.bloquear_combobox.setFont(font)
        self.bloquear_combobox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bloquear_combobox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bloquear_combobox.setMaxCount(10)
        self.bloquear_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.bloquear_combobox.setIconSize(QtCore.QSize(32, 32))
        self.bloquear_combobox.setObjectName("bloquear_combobox")
        self.bloquear_combobox.addItem("")
        self.bloquear_combobox.addItem("")
        self.bloquear_label = QtWidgets.QLabel(self.main_area)
        self.bloquear_label.setGeometry(QtCore.QRect(250, 310, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.bloquear_label.setFont(font)
        self.bloquear_label.setObjectName("bloquear_label")
        self.endereco_field.setGeometry(QtCore.QRect(380, 330, 221, 41))
        self.endereco_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.endereco_field.setFont(font)
        self.endereco_field.setTabletTracking(False)
        self.endereco_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.endereco_field.setInputMask("")
        self.endereco_field.setText("")
        self.endereco_field.setMaxLength(6)
        self.endereco_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.endereco_field.setClearButtonEnabled(True)
        self.endereco_field.setObjectName("endereco_field")
        self.endereco_label = QtWidgets.QLabel(self.main_area)
        self.endereco_label.setGeometry(QtCore.QRect(390, 310, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.endereco_label.setFont(font)
        self.endereco_label.setObjectName("endereco_label")
        self.armazem_field.setGeometry(QtCore.QRect(380, 250, 91, 41))
        self.armazem_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.armazem_field.setFont(font)
        self.armazem_field.setTabletTracking(False)
        self.armazem_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.armazem_field.setInputMask("")
        self.armazem_field.setText("")
        self.armazem_field.setMaxLength(6)
        self.armazem_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.armazem_field.setClearButtonEnabled(True)
        self.armazem_field.setObjectName("armazem_field")
        self.cc_field.setGeometry(QtCore.QRect(50, 330, 121, 41))
        self.cc_field.setMinimumSize(QtCore.QSize(10, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.cc_field.setFont(font)
        self.cc_field.setTabletTracking(False)
        self.cc_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cc_field.setInputMask("")
        self.cc_field.setText("")
        self.cc_field.setMaxLength(9)
        self.cc_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cc_field.setClearButtonEnabled(True)
        self.cc_field.setObjectName("cc_field")
        self.btn_search_tipo.setGeometry(QtCore.QRect(145, 250, 41, 41))
        self.btn_search_tipo.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btn_search_tipo.setFont(font)
        self.btn_search_tipo.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_search_tipo.setStyleSheet("QPushButton {\n"
"    background-color: #fff;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"}")
        self.btn_search_tipo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/lupa (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search_tipo.setIcon(icon3)
        self.btn_search_tipo.setIconSize(QtCore.QSize(32, 32))
        self.btn_search_tipo.setObjectName("btn_search_tipo")
        self.btn_search_um.setGeometry(QtCore.QRect(315, 250, 41, 41))
        self.btn_search_um.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btn_search_um.setFont(font)
        self.btn_search_um.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_search_um.setStyleSheet("QPushButton {\n"
"    background-color: #fff;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"}")
        self.btn_search_um.setText("")
        self.btn_search_um.setIcon(icon3)
        self.btn_search_um.setIconSize(QtCore.QSize(32, 32))
        self.btn_search_um.setObjectName("btn_search_um")
        self.btn_search_arm.setGeometry(QtCore.QRect(475, 250, 41, 41))
        self.btn_search_arm.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btn_search_arm.setFont(font)
        self.btn_search_arm.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_search_arm.setStyleSheet("QPushButton {\n"
"    background-color: #fff;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"}")
        self.btn_search_arm.setText("")
        self.btn_search_arm.setIcon(icon3)
        self.btn_search_arm.setIconSize(QtCore.QSize(32, 32))
        self.btn_search_arm.setObjectName("btn_search_arm")
        self.btn_search_cc.setGeometry(QtCore.QRect(175, 330, 41, 41))
        self.btn_search_cc.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btn_search_cc.setFont(font)
        self.btn_search_cc.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_search_cc.setStyleSheet("QPushButton {\n"
"    background-color: #fff;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"}")
        self.btn_search_cc.setText("")
        self.btn_search_cc.setIcon(icon3)
        self.btn_search_cc.setIconSize(QtCore.QSize(32, 32))
        self.btn_search_cc.setObjectName("btn_search_cc")
        self.btn_search_grupo.setGeometry(QtCore.QRect(145, 410, 41, 41))
        self.btn_search_grupo.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btn_search_grupo.setFont(font)
        self.btn_search_grupo.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_search_grupo.setStyleSheet("QPushButton {\n"
"    background-color: #fff;\n"
"    border: 2px;\n"
"    border-radius: 18px;\n"
"    font-size: 14px;\n"
"    font-weight: regular;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    color: #EEEEEE;\n"
"}")
        self.btn_search_grupo.setText("")
        self.btn_search_grupo.setIcon(icon3)
        self.btn_search_grupo.setIconSize(QtCore.QSize(32, 32))
        self.btn_search_grupo.setObjectName("btn_search_grupo")
        self.logo_enaplic_50 = QtWidgets.QLabel(self.main_area)
        self.logo_enaplic_50.setGeometry(QtCore.QRect(50, 450, 121, 101))
        self.logo_enaplic_50.setText("")
        self.logo_enaplic_50.setPixmap(QtGui.QPixmap(":/image/image/logo_enaplic_50_anos.png"))
        self.logo_enaplic_50.setScaledContents(True)
        self.logo_enaplic_50.setObjectName("logo_enaplic_50")
        self.codigo_field.setGeometry(QtCore.QRect(50, 40, 220, 41))
        self.codigo_field.setMinimumSize(QtCore.QSize(220, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        self.codigo_field.setFont(font)
        self.codigo_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.codigo_field.setAccessibleDescription("")
        self.codigo_field.setInputMask("")
        self.codigo_field.setText("")
        self.codigo_field.setMaxLength(15)
        self.codigo_field.setClearButtonEnabled(True)
        self.codigo_field.setObjectName("codigo_field")
        self.codigo_label = QtWidgets.QLabel(self.main_area)
        self.codigo_label.setGeometry(QtCore.QRect(60, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.codigo_label.setFont(font)
        self.codigo_label.setObjectName("codigo_label")

        self.retranslateUi(NewProductWindow)
        QtCore.QMetaObject.connectSlotsByName(NewProductWindow)

    def retranslateUi(self, NewProductWindow):
        _translate = QtCore.QCoreApplication.translate
        NewProductWindow.setWindowTitle(_translate("NewProductWindow", "Eureka® Engenharia"))
        self.type_label.setText(_translate("NewProductWindow", "Cadastro de novo produto"))
        self.desc_comp_label.setText(_translate("NewProductWindow", "Desc. Complementar"))
        self.tipo_label.setText(_translate("NewProductWindow", "Tipo"))
        self.btn_close.setText(_translate("NewProductWindow", " Cancelar"))
        self.descricao_label.setText(_translate("NewProductWindow", "Descrição"))
        self.um_label.setText(_translate("NewProductWindow", "Unid. Medida"))
        self.armazem_label.setText(_translate("NewProductWindow", "Armazém"))
        self.btn_save.setText(_translate("NewProductWindow", " Salvar"))
        self.grupo_label.setText(_translate("NewProductWindow", "Grupo"))
        self.desc_grupo_label.setText(_translate("NewProductWindow", "Descrição Grupo"))
        self.cc_label.setText(_translate("NewProductWindow", "Centro de Custo"))
        self.bloquear_combobox.setItemText(0, _translate("NewProductWindow", "Não"))
        self.bloquear_combobox.setItemText(1, _translate("NewProductWindow", "Sim"))
        self.bloquear_label.setText(_translate("NewProductWindow", "Bloquear?"))
        self.endereco_label.setText(_translate("NewProductWindow", "Endereço estoque"))
        self.codigo_label.setText(_translate("NewProductWindow", "Código"))
from src.qt.ui import resource_rc

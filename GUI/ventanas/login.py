
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from recursos import login_rc


class Ui_MainWindow(object):

    #
    # STYLES
    #
    styleLineEditOk = (
        "QLineEdit {\n"
        "    border: 2px solid #e4acd0; /* Borde */\n"
        "    border-radius: 5px;\n"
        "    padding: 5px;\n"
        "    background-color: #f5eef2; /* Fondo */\n"
        "    color: #dc84bc; /* Color del texto */\n"
        "    font-family: Arial, sans-serif;\n"
        "    font-size: 14px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    border: 2px solid rgb(255, 255, 255);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid #dc84bc; /* Borde al enfocar */\n"
        "}"
    )

    styleLineEditError = (
        "QLineEdit {\n"
        "    border: 2px solid rgb(255, 85, 127);\n"
        "    border-radius: 5px;\n"
        "    padding: 15px;\n"
        "    background-color: #f5eef2;    \n"
        "    color: rgb(100, 100, 100);\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    border: 2px solid rgb(255, 255, 255);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid #dc84bc;   \n"
        "    color: rgb(200, 200, 200);\n"
        "}"
    )

    stylePopupError = "background-color: rgb(255, 85, 127); border-radius: 5px;"
    stylePopupOk = "background-color: rgb(255, 0, 0); border-radius: 5px;"

    #
    # FUNCTIONS
    #
    def checkFields(self):
        textUser = self.lineEdit_user.text()
        textPassword = self.lineEdit_password.text()

        def showMessage(message):
            self.frame_error.show()
            self.label_error.setText(message)

        # CHECK USER
        if not self.lineEdit_user.text():
            textUser = " Usuario Vacio. "
            self.lineEdit_user.setStyleSheet(self.styleLineEditError)
        else:
            textUser = ""
            self.lineEdit_user.setStyleSheet(self.styleLineEditOk)

        # CHECK PASSWORD
        if not self.lineEdit_password.text():
            textPassword = " Contraseña Vacia. "
            self.lineEdit_password.setStyleSheet(self.styleLineEditError)
        else:
            textPassword = ""
            self.lineEdit_password.setStyleSheet(self.styleLineEditOk)

        # CHECK FIELDS
        if textUser + textPassword != "":
            text = textUser + textPassword
            showMessage(text)
            self.frame_error.setStyleSheet(self.stylePopupError)
        else:
            text = " Usuario o contraseña incorrecta. "
            showMessage(text)
            self.frame_error.setStyleSheet(self.stylePopupOk)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet(self.stylePopupError)
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.pushButton_close_pupup = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close_pupup.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close_pupup.setStyleSheet(
            "QPushButton {\n"
            "    border-radius: 5px;    \n"
            "    background-image: url(:/Salir/images/cil-x.png);\n"
            "    background-position: center;    \n"
            "    background-color: rgb(60, 60, 60);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(50, 50, 50);    \n"
            "    color: rgb(200, 200, 200);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(35, 35, 35);    \n"
            "    color: rgb(200, 200, 200);\n"
            "}"
        )
        self.pushButton_close_pupup.setText("")
        self.pushButton_close_pupup.setObjectName("pushButton_close_pupup")
        self.horizontalLayout_3.addWidget(self.pushButton_close_pupup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet(
            "background-image: url(:/Fondo/images/fondo.jpg);\n"
            "background-repeat: no-repeat;\n"
            "background-position: center;\n"
            ""
        )
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setGeometry(QtCore.QRect(170, 0, 441, 541))
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet(
            "background: transparent;\n" "border-radius: 10px;"
        )
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(40, 0, 361, 311))
        self.logo.setStyleSheet(
            "background-image: url(:/Logo/images/logo.png);\n"
            "background-repeat: no-repeat;\n"
            "background-position: center;"
        )
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 327, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(10)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet(self.styleLineEditOk)
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 390, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet(self.styleLineEditOk)
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(85, 480, 280, 50))
        self.pushButton_login.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; /* Fondo */\n"
            "    color: #ffffff; /* Color del texto */\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; /* Fondo al pasar el cursor */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; /* Fondo al presionar */\n"
            "}"
        )
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        #
        # FUNCTIONS
        #

        # BT CLOSE POPUP
        self.pushButton_close_pupup.clicked.connect(lambda: self.frame_error.hide())

        # HIDE ERROR
        self.frame_error.hide()

        # BT LOGIN
        self.pushButton_login.clicked.connect(self.checkFields)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        MainWindow.setFixedSize(800, 600)
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USUARIO"))
        self.lineEdit_password.setPlaceholderText(
            _translate("MainWindow", "CONTRASEÑA")
        )
        self.pushButton_login.setText(_translate("MainWindow", "INGRESAR"))

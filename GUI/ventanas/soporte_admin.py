from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ventanas.login import Ui_MainWindow


class Ui_soporte_admin(object):
    def setupUi(self, soporte_admin):
        soporte_admin.setObjectName("soporte_admin")
        soporte_admin.resize(800, 600)
        soporte_admin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(soporte_admin)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 241, 61))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 260, 241, 61))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 140, 280, 61))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 260, 280, 61))
        self.pushButton_4.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 201, 61))
        self.pushButton_6.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 380, 241, 61))
        self.pushButton_7.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 380, 241, 61))
        self.pushButton_8.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #dc84bc; \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #d484b4; \n"
            "}"
        )
        self.pushButton_8.setObjectName("pushButton_8")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 201, 71))
        self.label.setStyleSheet('font: 16pt "Arial";')
        self.label.setObjectName("label")

        soporte_admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(soporte_admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        soporte_admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(soporte_admin)
        self.statusbar.setObjectName("statusbar")
        soporte_admin.setStatusBar(self.statusbar)

        self.retranslateUi(soporte_admin)
        QtCore.QMetaObject.connectSlotsByName(soporte_admin)
        self.pushButton_6.clicked.connect(soporte_admin.close)

    def retranslateUi(self, soporte_admin):
        _translate = QtCore.QCoreApplication.translate
        soporte_admin.setWindowTitle(_translate("soporte_admin", "Soporte"))
        self.pushButton.setText(_translate("soporte_admin", "Ventas"))
        self.pushButton_2.setText(_translate("soporte_admin", "Gestión clientes"))
        self.pushButton_3.setText(
            _translate("soporte_admin", "Reportes personalizados")
        )
        self.pushButton_4.setText(
            _translate("soporte_admin", "Reporte diario inventario")
        )
        self.pushButton_6.setText(_translate("soporte_admin", "Cerrar Programa"))
        self.pushButton_7.setText(_translate("soporte_admin", "Catálogo de servicios"))
        self.pushButton_8.setText(
            _translate("soporte_admin", "Inventario de productos")
        )
        self.label.setText(_translate("soporte_admin", "Administrador"))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_Caja(object):  # terminada (falta reporte diario)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Añade esta línea para evitar que la ventana sea maximizable
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC.setGeometry(QtCore.QRect(110, 350, 190, 120))
        self.pushButtonC.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButtonC.setObjectName("pushButton")
        self.pushButtonC_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC_3.setGeometry(QtCore.QRect(520, 350, 190, 120))
        self.pushButtonC_3.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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

        self.pushButtonC_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC_2.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButtonC_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButtonC_2.setObjectName("pushButton_2")
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

        self.pushButtonC_2.clicked.connect(MainWindow.close)
        self.pushButtonC_3.clicked.connect(MainWindow.close)
        self.pushButtonC_3.clicked.connect(self.nextWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CAJA"))
        self.pushButtonC.setText(_translate("MainWindow", "Reporte diario"))
        self.pushButtonC_3.setText(_translate("MainWindow", "Productos/Servicios"))
        self.pushButtonC_2.setText(_translate("MainWindow", "Salir"))

    def nextWindow(self):
        self.sele = QMainWindow()
        self.ui_backC = Sele_Compra()
        self.ui_backC.setupUi(self.sele)
        self.sele.show()


class Sele_Compra(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SeleWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC.setGeometry(QtCore.QRect(50, 380, 700, 150))
        self.pushButtonC.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButtonC.setObjectName("pushButton")
        self.pushButtonC_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC_2.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButtonC_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButtonC_2.setObjectName("pushButton_2")
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
        self.pushButtonC_2.clicked.connect(MainWindow.close)
        self.pushButtonC_2.clicked.connect(self.cancel)
        self.pushButtonC.clicked.connect(MainWindow.close)
        self.pushButtonC.clicked.connect(self.GoClientWindow)

    def cancel(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_Caja()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()

    def GoClientWindow(self):
        self.Cli = QMainWindow()
        self.uiCl = Sele_Cliente()
        self.uiCl.setupUi(self.Cli)
        self.Cli.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SeleCompra"))
        self.label.setText(_translate("MainWindow", "SELECCION DE COMPRA"))
        self.pushButtonC.setText(
            _translate("MainWindow", "Comprar Producto y Servicios")
        )
        self.pushButtonC_2.setText(_translate("MainWindow", "Cancelar"))


class Sele_Cliente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 250, 661, 111))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 380, 661, 111))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.backSele)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.CLcurrwindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.CLNewwindow)

    def CLNewwindow(self):
        self.Clinew = QMainWindow()
        self.cline = Cli_New()
        self.cline.setupUi(self.Clinew)
        self.Clinew.show()

    def CLcurrwindow(self):
        self.Clicur = QMainWindow()
        self.Clicr = Cli_Curr()
        self.Clicr.setupUi(self.Clicur)
        self.Clicur.show()

    def backSele(self):
        self.backsele = QMainWindow()
        self.ui_backC = Sele_Compra()
        self.ui_backC.setupUi(self.backsele)
        self.backsele.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SELECCION CLIENTE"))
        self.label.setText(_translate("MainWindow", "SELECCION CLIENTE"))
        self.pushButton.setText(_translate("MainWindow", "Cliente Nuevo"))
        self.pushButton_3.setText(_translate("MainWindow", "Seleccionar Cliente"))
        self.pushButton_2.setText(_translate("MainWindow", "Atras"))


class Cli_Curr(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 450, 125, 50))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_3.setGeometry(QtCore.QRect(450, 450, 125, 50))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 761, 51))
        self.label_2.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 290, 761, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(21, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.backSeleCli)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.curnextwin)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def curnextwin(self):
        self.next = QMainWindow()
        self.nexte = Compra_Pro()
        self.nexte.setupUi(self.next)
        self.next.show()

    def backSeleCli(self):
        self.back = QMainWindow()
        self.backCli = Sele_Cliente()
        self.backCli.setupUi(self.back)
        self.back.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BUSQUEDA CLIENTE"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_3.setText(_translate("MainWindow", "Aceptar"))
        self.label_2.setText(
            _translate("MainWindow", "Seleccionar Cliente (Buscar por su cedula)")
        )
        self.comboBox.setItemText(0, _translate("MainWindow", "a"))
        self.comboBox.setItemText(1, _translate("MainWindow", "b"))
        self.comboBox.setItemText(2, _translate("MainWindow", "c"))
        self.comboBox.setItemText(3, _translate("MainWindow", "d"))
        self.comboBox.setItemText(4, _translate("MainWindow", "e"))
        self.comboBox.setItemText(5, _translate("MainWindow", "f"))
        self.comboBox.setItemText(6, _translate("MainWindow", "g"))
        self.comboBox.setItemText(7, _translate("MainWindow", "hi"))
        self.comboBox.setItemText(8, _translate("MainWindow", "j"))
        self.comboBox.setItemText(9, _translate("MainWindow", "k"))
        self.comboBox.setItemText(10, _translate("MainWindow", "l"))
        self.comboBox.setItemText(11, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(12, _translate("MainWindow", "m"))
        self.comboBox.setItemText(13, _translate("MainWindow", "n"))
        self.comboBox.setItemText(14, _translate("MainWindow", "o"))
        self.comboBox.setItemText(15, _translate("MainWindow", "pq"))
        self.comboBox.setItemText(16, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(17, _translate("MainWindow", "r"))
        self.comboBox.setItemText(18, _translate("MainWindow", "t"))
        self.comboBox.setItemText(19, _translate("MainWindow", "y"))
        self.comboBox.setItemText(20, _translate("MainWindow", "u"))


class Cli_New(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 480, 111, 41))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 480, 111, 41))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 321, 51))
        self.label_3.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 321, 51))
        self.label_4.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 390, 321, 51))
        self.label_5.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 250, 361, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 320, 361, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 390, 361, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 200, 131, 31))
        self.label_6.setStyleSheet(
            "\n"
            "    border: 1px solid;\n"
            "    border-radius: 2px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: rgb(0, 255, 0);\n"
            "    color: rgb(0, 0, 0);\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 200, 131, 31))
        self.label_7.setStyleSheet(
            "\n"
            "    border: 1px solid;\n"
            "    border-radius: 2px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: rgb(255, 0, 0);\n"
            "    \n"
            "    color: rgb(255, 255, 255);\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.backSeleCli)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.curnextwin)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def curnextwin(self):
        self.next = QMainWindow()
        self.nexte = Compra_Pro()
        self.nexte.setupUi(self.next)
        self.next.show()

    def backSeleCli(self):
        self.back = QMainWindow()
        self.backCli = Sele_Cliente()
        self.backCli.setupUi(self.back)
        self.back.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CLIENTE NUEVO"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        self.label_3.setText(_translate("MainWindow", "Cédula"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Número"))
        self.label_6.setText(_translate("MainWindow", "Cedula valida"))
        self.label_7.setText(_translate("MainWindow", "Cedula valida"))


class Compra_Pro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 691, 111))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 340, 691, 111))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #e4acd0;\n"
            "    border-radius: 2px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.backSeleCli)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.Buy)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.dates)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dates(self):
        self.d = QMainWindow()
        self.date = Cita()
        self.date.setupUi(self.d)
        self.d.show()

    def backSeleCli(self):
        self.back = QMainWindow()
        self.backCli = Sele_Cliente()
        self.backCli.setupUi(self.back)
        self.back.show()

    def Buy(self):
        self.buy = QMainWindow()
        self.buyPro = Carrito()
        self.buyPro.setupUi(self.buy)
        self.buy.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "COMPRA PRODUCTOS"))
        self.pushButton.setText(_translate("MainWindow", "Reservar Cita"))
        self.pushButton_3.setText(
            _translate("MainWindow", "Comprar Productos/Servicios")
        )
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))


class Cita(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);\n" "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #e4acd0;\n"
            "    border-radius: 2px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(370, 320, 312, 183))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(370, 220, 301, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 271, 71))
        self.label_2.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 320, 271, 71))
        self.label_3.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.backBuy)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def backBuy(self):
        self.co = QMainWindow()
        self.com = Compra_Pro()
        self.com.setupUi(self.co)
        self.co.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CITAS"))
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
        self.comboBox.setItemText(0, _translate("MainWindow", "a"))
        self.comboBox.setItemText(1, _translate("MainWindow", "b"))
        self.comboBox.setItemText(2, _translate("MainWindow", "c"))
        self.comboBox.setItemText(3, _translate("MainWindow", "d"))
        self.label_2.setText(_translate("MainWindow", "Seleccionar Servicio"))
        self.label_3.setText(_translate("MainWindow", "Seleccionar Fecha"))


class Carrito(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(120, 350, 161, 111))
        self.cancelButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.cancelButton.setObjectName("pushButton")
        self.serviciosButton = QtWidgets.QPushButton(self.centralwidget)
        self.serviciosButton.setGeometry(QtCore.QRect(630, 210, 161, 41))
        self.serviciosButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.serviciosButton.setObjectName("serviciosButton")
        self.productosButton = QtWidgets.QPushButton(self.centralwidget)
        self.productosButton.setGeometry(QtCore.QRect(10, 210, 161, 41))
        self.productosButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.productosButton.setObjectName("productosButoton")
        self.ContinueButton = QtWidgets.QPushButton(self.centralwidget)
        self.ContinueButton.setGeometry(QtCore.QRect(510, 350, 161, 111))
        self.ContinueButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.ContinueButton.setObjectName("ContinueButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.cancelButton.clicked.connect(MainWindow.close)
        self.cancelButton.clicked.connect(self.cancel)
        self.serviciosButton.clicked.connect(self.open_servicios_window)
        self.productosButton.clicked.connect(self.open_productos_window)

        self.ContinueButton.clicked.connect(MainWindow.close)
        self.ContinueButton.clicked.connect(self.Continue)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CARRITO DE COMPRAS"))
        self.cancelButton.setText(_translate("MainWindow", "Cancelar"))
        self.serviciosButton.setText(_translate("MainWindow", "Servicios"))
        self.productosButton.setText(_translate("MainWindow", "Productos"))
        self.ContinueButton.setText(_translate("MainWindow", "Continuar"))

    def open_servicios_window(self):
        self.selserv = QMainWindow()
        self.Serv = Servicios()
        self.Serv.setupUi(self.selserv)
        self.selserv.show()

    def open_productos_window(self):
        self.selrpro = QMainWindow()
        self.PROD = Productos()
        self.PROD.setupUi(self.selrpro)
        self.selrpro.show()

    def cancel(self):
        self.backCli = QMainWindow()
        self.Bcli = Compra_Pro()
        self.Bcli.setupUi(self.backCli)
        self.backCli.show()

    def Continue(self):
        self.fac = QMainWindow()
        self.fact = Factura()
        self.fact.setupUi(self.fac)
        self.fac.show()


class Productos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 441, 41))
        self.label_2.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 441, 41))
        self.label_3.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 260, 271, 41))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 330, 271, 41))
        self.lineEdit.setObjectName("lineEdit")
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
        self.label.setText(_translate("MainWindow", "Productos"))
        self.label_2.setText(_translate("MainWindow", "Seleccionar Producto"))
        self.label_3.setText(_translate("MainWindow", "Seleccionar Cantidad"))


class Servicios(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 441, 41))
        self.label_2.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 441, 41))
        self.label_3.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 260, 271, 41))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 330, 271, 41))
        self.lineEdit.setObjectName("lineEdit")
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
        self.label.setText(_translate("MainWindow", "Servicios"))
        self.label_2.setText(_translate("MainWindow", "Seleccionar Servicio"))
        self.label_3.setText(_translate("MainWindow", "Seleccionar Cantidad"))


class Factura(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        )
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n" "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 761, 111))
        self.label.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 370, 301, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 271, 71))
        self.label_2.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 350, 271, 71))
        self.label_3.setStyleSheet(
            "\n"
            "    border: 2px solid #e4acd0;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4;\n"
            "    color: #ffffff;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
            ""
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 180, 301, 161))
        self.label_5.setStyleSheet(
            "\n"
            "    padding: 8px 16px;\n"
            "    background-color: rgb(255, 250, 89);\n"
            "    color: #000000;\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 10px;    \n"
            "    border-color: rgb(0, 0, 0);\n"
            "    border-size: 2px\n"
            ""
        )
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 500, 131, 41))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #e4acd0;\n"
            "    border-radius: 2px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_4.setGeometry(QtCore.QRect(440, 500, 131, 41))
        self.pushButton_4.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid #e4acd0;\n"
            "    border-radius: 2px;\n"
            "    padding: 8px 16px;\n"
            "    background-color: #dc95c4; \n"
            "    color: #ffffff; \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 16px;\n"
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
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.cancel)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.ended)

    def cancel(self):
        self.bp = QMainWindow()
        self.backpro = Carrito()
        self.backpro.setupUi(self.bp)
        self.bp.show()

    def ended(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_Caja()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FACTURA"))
        self.comboBox.setItemText(0, _translate("MainWindow", "a"))
        self.comboBox.setItemText(1, _translate("MainWindow", "b"))
        self.comboBox.setItemText(2, _translate("MainWindow", "c"))
        self.comboBox.setItemText(3, _translate("MainWindow", "d"))
        self.label_2.setText(_translate("MainWindow", "Total"))
        self.label_3.setText(_translate("MainWindow", "Seleccionar Metodo de Pago"))
        self.label_5.setText(_translate("MainWindow", "Mostrar Total"))
        self.pushButton_3.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_4.setText(_translate("MainWindow", "Terminar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Caja()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

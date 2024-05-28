from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_Caja(object):  # terminada (falta reporte diario)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # Añade esta línea para evitar que la ventana sea maximizable
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        
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
        self.pushButtonC_3.setObjectName("pushButton_3")
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

    def exit(self):
        self.close()


class Sele_Compra(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SeleWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
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

    def cancel(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_Caja()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SeleCompra"))
        self.label.setText(_translate("MainWindow", "SELECCION DE COMPRA"))
        self.pushButtonC.setText(
            _translate("MainWindow", "Comprar Producto y Servicios")
        )
        self.pushButtonC_2.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Caja()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

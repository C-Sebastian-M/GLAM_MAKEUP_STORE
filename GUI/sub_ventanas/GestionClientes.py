from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
#from ventanas.soporte_admin import Ui_soporte_admin

class Ui_GestionClientes(object):
    def setupUi(self, GestionClientes):
        GestionClientes.setObjectName("GestionClientes")
        GestionClientes.setWindowModality(QtCore.Qt.NonModal)
        GestionClientes.resize(800, 600)
        GestionClientes.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Icono/images/icono.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        GestionClientes.setWindowIcon(icon)
        GestionClientes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(GestionClientes)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 111, 51))
        self.frame.setStyleSheet(
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.BotonAtras = QtWidgets.QPushButton(self.frame)
        self.BotonAtras.setGeometry(QtCore.QRect(0, 0, 111, 51))
        self.BotonAtras.setObjectName("BotonAtras")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 20, 400, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet(
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
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BotonVerClientes = QtWidgets.QPushButton(self.frame_3)
        self.BotonVerClientes.setObjectName("BotonVerClientes")
        self.verticalLayout_2.addWidget(self.BotonVerClientes)
        self.BotonAddCliente = QtWidgets.QPushButton(self.frame_3)
        self.BotonAddCliente.setObjectName("BotonAddCliente")
        self.verticalLayout_2.addWidget(self.BotonAddCliente)
        self.BotonModificarCliente = QtWidgets.QPushButton(self.frame_3)
        self.BotonModificarCliente.setObjectName("BotonModificarCliente")
        self.verticalLayout_2.addWidget(self.BotonModificarCliente)
        self.BotonEliminarInfoCliente = QtWidgets.QPushButton(self.frame_3)
        self.BotonEliminarInfoCliente.setObjectName("BotonEliminarInfoCliente")
        self.verticalLayout_2.addWidget(self.BotonEliminarInfoCliente)
        self.verticalLayout.addWidget(self.frame_3)
        GestionClientes.setCentralWidget(self.centralwidget)

        self.retranslateUi(GestionClientes)
        QtCore.QMetaObject.connectSlotsByName(GestionClientes)
        self.BotonAddCliente.clicked.connect(GestionClientes.close)
        self.BotonAddCliente.clicked.connect(self.abrirCrearCliente)
        self.BotonModificarCliente.clicked.connect(GestionClientes.close)
        self.BotonModificarCliente.clicked.connect(self.abrirModificarCliente)
        #self.BotonAtras.clicked.connect(GestionClientes.close)
        #self.BotonAtras.clicked.connect(self.volverAdmin)

    def abrirCrearCliente(self):
        self.sele = QMainWindow()
        self.ui_backC = Ui_CrearCliente()
        self.ui_backC.setupUi(self.sele)
        self.sele.show()

    def abrirModificarCliente(self):
        self.sele = QMainWindow()
        self.ui_backC = Ui_ModificarCliente()
        self.ui_backC.setupUi(self.sele)
        self.sele.show()
        
    """def volverAdmin(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_soporte_admin()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()"""

    def retranslateUi(self, GestionClientes):
        _translate = QtCore.QCoreApplication.translate
        GestionClientes.setWindowTitle(
            _translate("GestionClientes", "Gestión Clientes")
        )
        self.BotonAtras.setText(_translate("GestionClientes", "Atras"))
        self.BotonVerClientes.setText(_translate("GestionClientes", "Ver Clientes"))
        self.BotonAddCliente.setText(_translate("GestionClientes", "Añadir Cliente"))
        self.BotonModificarCliente.setText(
            _translate("GestionClientes", "Modificar Cliente")
        )
        self.BotonEliminarInfoCliente.setText(
            _translate("GestionClientes", "Eliminar Información de Cliente")
        )


class Ui_CrearCliente(object):
    def setupUi(self, CrearCliente):
        CrearCliente.setObjectName("CrearCliente")
        CrearCliente.resize(800, 600)
        CrearCliente.setMinimumSize(QtCore.QSize(800, 600))
        CrearCliente.setMaximumSize(QtCore.QSize(800, 600))
        CrearCliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(CrearCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FrameFormulario = QtWidgets.QFrame(self.centralwidget)
        self.FrameFormulario.setMaximumSize(QtCore.QSize(400, 551))
        self.FrameFormulario.setStyleSheet(
            "QLineEdit {\n"
            "    border: 2px solid #e4acd0; /* Borde */\n"
            "    border-radius: 5px;\n"
            "    padding: 5px;\n"
            "    background-color: #f5eef2; /* Fondo */ \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 14px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(255, 255, 255);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid #dc84bc; /* Borde al enfocar */\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    background-color: transparent; /* Fondo transparente */\n"
            "    color: #333333; /* Color del texto */\n"
            "    font-family: Arial, sans-serif; /* Fuente del texto */\n"
            "    font-size: 16px; /* Tamaño de la letra */\n"
            "}"
        )
        self.FrameFormulario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameFormulario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameFormulario.setObjectName("FrameFormulario")
        self.IngresoCedula = QtWidgets.QLineEdit(self.FrameFormulario)
        self.IngresoCedula.setGeometry(QtCore.QRect(10, 80, 380, 32))
        self.IngresoCedula.setObjectName("IngresoCedula")
        self.IngresoNombre = QtWidgets.QLineEdit(self.FrameFormulario)
        self.IngresoNombre.setGeometry(QtCore.QRect(10, 240, 380, 32))
        self.IngresoNombre.setObjectName("IngresoNombre")
        self.IngresoTelefono = QtWidgets.QLineEdit(self.FrameFormulario)
        self.IngresoTelefono.setGeometry(QtCore.QRect(10, 400, 380, 32))
        self.IngresoTelefono.setObjectName("IngresoTelefono")
        self.label = QtWidgets.QLabel(self.FrameFormulario)
        self.label.setGeometry(QtCore.QRect(10, 50, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.FrameFormulario)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.FrameFormulario)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 131, 21))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.FrameFormulario)
        self.FrameBotones = QtWidgets.QFrame(self.centralwidget)
        self.FrameBotones.setMaximumSize(QtCore.QSize(113, 115))
        self.FrameBotones.setStyleSheet(
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
        self.FrameBotones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameBotones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameBotones.setObjectName("FrameBotones")
        self.BotonAtras = QtWidgets.QPushButton(self.FrameBotones)
        self.BotonAtras.setGeometry(QtCore.QRect(0, 0, 111, 51))
        self.BotonAtras.setMaximumSize(QtCore.QSize(111, 51))
        self.BotonAtras.setObjectName("BotonAtras")
        self.BotonGuardar = QtWidgets.QPushButton(self.FrameBotones)
        self.BotonGuardar.setGeometry(QtCore.QRect(0, 62, 111, 51))
        self.BotonGuardar.setMaximumSize(QtCore.QSize(111, 51))
        self.BotonGuardar.setObjectName("BotonGuardar")
        self.horizontalLayout.addWidget(self.FrameBotones)
        CrearCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(CrearCliente)
        QtCore.QMetaObject.connectSlotsByName(CrearCliente)
        self.BotonAtras.clicked.connect(CrearCliente.close)
        self.BotonAtras.clicked.connect(self.cancel)

    def cancel(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_GestionClientes()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()

    def retranslateUi(self, CrearCliente):
        _translate = QtCore.QCoreApplication.translate
        CrearCliente.setWindowTitle(_translate("CrearCliente", "Crear Cliente"))
        self.IngresoCedula.setPlaceholderText(_translate("CrearCliente", "Cedula"))
        self.IngresoNombre.setPlaceholderText(_translate("CrearCliente", "Nombre"))
        self.IngresoTelefono.setPlaceholderText(_translate("CrearCliente", "Teléfono"))
        self.label.setText(_translate("CrearCliente", "Ingresar Cedula"))
        self.label_2.setText(_translate("CrearCliente", "Ingresar Nombre"))
        self.label_3.setText(_translate("CrearCliente", "Ingresar Teléfono"))
        self.BotonAtras.setText(_translate("CrearCliente", "Atras"))
        self.BotonGuardar.setText(_translate("CrearCliente", "Guardar"))


class Ui_ModificarCliente(object):
    def setupUi(self, ModificarCliente):
        ModificarCliente.setObjectName("ModificarCliente")
        ModificarCliente.resize(800, 600)
        ModificarCliente.setMinimumSize(QtCore.QSize(800, 600))
        ModificarCliente.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(ModificarCliente)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(112, 52))
        self.frame.setStyleSheet(
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.BotonAtrasMC = QtWidgets.QPushButton(self.frame)
        self.BotonAtrasMC.setGeometry(QtCore.QRect(0, 0, 111, 51))
        self.BotonAtrasMC.setObjectName("BotonAtrasMC")
        self.verticalLayout.addWidget(self.frame)
        self.FrameComBox = QtWidgets.QFrame(self.centralwidget)
        self.FrameComBox.setMaximumSize(QtCore.QSize(800, 50))
        self.FrameComBox.setStyleSheet(
            "QComboBox {\n"
            "    background-color: #f5eef2; /* Fondo del combo box */\n"
            "    border: 2px solid #e4acd0; /* Borde */\n"
            "    border-radius: 5px;\n"
            "    padding: 5px;\n"
            "    color: #000000; /* Color del texto */\n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 14px;\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "    border: 2px solid #dc84bc; /* Borde al pasar el cursor */\n"
            "}\n"
            "\n"
            "QComboBox:focus {\n"
            "    border: 2px solid #ebbcdc; /* Borde al enfocar */\n"
            "    background-color: #e4c4d4; /* Fondo al enfocar */\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 30px;\n"
            "    border-left-width: 1px;\n"
            "    border-left-color: #e4acd0;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 5px;\n"
            "    border-bottom-right-radius: 5px;\n"
            "    background-color: #dc95c4;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url(:/path/to/down_arrow.png); /* Reemplaza con la ruta de tu icono de flecha */\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: #f5eef2; /* Fondo de la lista desplegable */\n"
            "    border: 2px solid #e4acd0; /* Borde de la lista desplegable */\n"
            "    color: #000000; /* Color del texto de los elementos */\n"
            "    selection-background-color: #e49cc6; /* Fondo del elemento seleccionado */\n"
            "    selection-color: #000000; /* Color del texto del elemento seleccionado */\n"
            "}\n"
            "\n"
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
        self.FrameComBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameComBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameComBox.setObjectName("FrameComBox")
        self.comboBoxClientes = QtWidgets.QComboBox(self.FrameComBox)
        self.comboBoxClientes.setGeometry(QtCore.QRect(140, 10, 441, 31))
        self.comboBoxClientes.setObjectName("comboBoxClientes")
        self.comboBoxClientes.addItem("")
        self.comboBoxClientes.addItem("")
        self.comboBoxClientes.addItem("")
        self.comboBoxClientes.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.FrameComBox)
        self.pushButton.setGeometry(QtCore.QRect(620, 5, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.FrameComBox)
        self.FormularioWidget = QtWidgets.QWidget(self.centralwidget)
        self.FormularioWidget.setStyleSheet(
            "QLineEdit {\n"
            "    border: 2px solid #e4acd0; /* Borde */\n"
            "    border-radius: 5px;\n"
            "    padding: 5px;\n"
            "    background-color: #f5eef2; /* Fondo */ \n"
            "    font-family: Arial, sans-serif;\n"
            "    font-size: 14px;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(255, 255, 255);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid #dc84bc; /* Borde al enfocar */\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    background-color: transparent; /* Fondo transparente */\n"
            "    color: #333333; /* Color del texto */\n"
            "    font-family: Arial, sans-serif; /* Fuente del texto */\n"
            "    font-size: 16px; /* Tamaño de la letra */\n"
            "}\n"
            "\n"
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
        self.FormularioWidget.setObjectName("FormularioWidget")
        self.label = QtWidgets.QLabel(self.FormularioWidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.FormularioWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 61, 21))
        self.label_2.setObjectName("label_2")
        self.nombreLineEdit = QtWidgets.QLineEdit(self.FormularioWidget)
        self.nombreLineEdit.setGeometry(QtCore.QRect(40, 120, 341, 31))
        self.nombreLineEdit.setObjectName("nombreLineEdit")
        self.telefonoLineEdit = QtWidgets.QLineEdit(self.FormularioWidget)
        self.telefonoLineEdit.setGeometry(QtCore.QRect(40, 330, 341, 31))
        self.telefonoLineEdit.setObjectName("telefonoLineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.FormularioWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 220, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.FormularioWidget)
        ModificarCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(ModificarCliente)
        QtCore.QMetaObject.connectSlotsByName(ModificarCliente)
        
        self.BotonAtrasMC.clicked.connect(ModificarCliente.close)
        self.BotonAtrasMC.clicked.connect(self.cancel)

    def cancel(self):
        self.backC = QMainWindow()
        self.ui_backC = Ui_GestionClientes()
        self.ui_backC.setupUi(self.backC)
        self.backC.show()

    def retranslateUi(self, ModificarCliente):
        _translate = QtCore.QCoreApplication.translate
        ModificarCliente.setWindowTitle(
            _translate("ModificarCliente", "Modificar Cliente")
        )
        self.BotonAtrasMC.setText(_translate("ModificarCliente", "Atras"))
        self.comboBoxClientes.setItemText(
            0, _translate("ModificarCliente", "Seleccionar Cliente")
        )
        self.comboBoxClientes.setItemText(
            1, _translate("ModificarCliente", "Cristian Rolando")
        )
        self.comboBoxClientes.setItemText(
            2, _translate("ModificarCliente", "Luis Messa")
        )
        self.comboBoxClientes.setItemText(
            3, _translate("ModificarCliente", "Hector Haland")
        )
        self.pushButton.setText(_translate("ModificarCliente", "Seleccionar"))
        self.label.setText(_translate("ModificarCliente", "Nombre"))
        self.label_2.setText(_translate("ModificarCliente", "Teléfono"))
        self.nombreLineEdit.setPlaceholderText(_translate("ModificarCliente", "Nombre"))
        self.telefonoLineEdit.setPlaceholderText(
            _translate("ModificarCliente", "Teléfono")
        )
        self.pushButton_2.setText(_translate("ModificarCliente", "Guardar"))

        self.pushButton.clicked.connect(self.mostrarFormulario)
        self.pushButton_2.clicked.connect(self.guardarInformacion)
        self.FormularioWidget.hide()

    def mostrarFormulario(self):
        usuario = self.comboBoxClientes.currentText()
        if usuario == "Seleccionar Cliente":
            return
        usuario_letras = usuario.split()
        if len(usuario_letras) >= 2:
            self.nombreLineEdit.setText(" ".join(usuario_letras[:2]))
            self.telefonoLineEdit.setText("")
        self.FormularioWidget.show()

    def guardarInformacion(self):
        nombre = self.nombreLineEdit.text()
        telefono = self.telefonoLineEdit.text()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GestionClientes()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

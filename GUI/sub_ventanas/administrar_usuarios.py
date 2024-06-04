from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QCompleter,
    QMessageBox,
)
from PyQt5.QtCore import QPropertyAnimation, Qt, QStringListModel
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor
class CBackground:
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        brocha1 = QBrush(QColor(212, 132, 180), Qt.SolidPattern)
        brocha2 = QBrush(QColor(228, 156, 198), Qt.SolidPattern)
        brocha3 = QBrush(QColor(235, 188, 220), Qt.SolidPattern)

        # Dibujando circulos abajo
        painter.setBrush(brocha3)
        painter.drawEllipse(140, 530, 200, 200)

        painter.setBrush(brocha2)
        painter.drawEllipse(40, 480, 200, 200)

        painter.setBrush(brocha1)
        painter.drawEllipse(-70, 440, 200, 200)

        # Dibujando circulos arriba
        painter.setBrush(brocha3)
        painter.drawEllipse(440, -140, 200, 200)

        painter.setBrush(brocha2)
        painter.drawEllipse(550, -100, 200, 200)

        painter.setBrush(brocha1)
        painter.drawEllipse(700, -70, 200, 200)

        painter.end()

class AdministrarUsuarios(QMainWindow, CBackground):
    def __init__(self):
        super(AdministrarUsuarios, self).__init__()
        loadUi(
            r"GUI\sub_ventanas\ui\AdministrarUsuarios.ui",
            self,
        )
        
        self.menu_boton.clicked.connect(self.mover_menu)
        
        # Conexión botones barra lateral con páginas
        self.ver_usuarios_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ver_usuarios_pagina)
        )
        self.ver_usuarios_boton.clicked.connect(self.limpiar_campos)
        self.add_usuario_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.add_usuario_pagina)
        )
        self.add_usuario_boton.clicked.connect(self.limpiar_campos)
        self.modificar_usuario_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.modificar_usuario_pagina)
        )
        self.modificar_usuario_boton.clicked.connect(self.limpiar_campos)
        self.eliminar_usuario_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.eliminar_usuario_pagina)
        )
        self.eliminar_usuario_boton.clicked.connect(self.limpiar_campos)
        
        
    # Método para limpiar los campos cada que se cambiar de página
    def limpiar_campos(self):
        self.add_id_usuario_lineEdit.clear()
        self.add_nombre_usuario_lineEdit.clear()
        self.add_password_lineEdit.clear()
        self.modify_buscar_usuario_lineEdit.clear()
        self.modify_nombre_usuario_lineEdit.clear()
        self.modify_password_lineEdit.clear()
        self.del_buscar_usuario_lineEdit.clear()

    # Método que permite mover la barra de menú
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 270
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart
            )  # InQuad, InOutQuad, InCubic, InOutExpo
            self.animacion.start()


 
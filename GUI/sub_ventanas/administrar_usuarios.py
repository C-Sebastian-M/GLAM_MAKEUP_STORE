from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QMainWindow,
    QHeaderView,
    QTableWidgetItem,
    QCompleter,
    QMessageBox,
)
import pandas as pd
from API.DATA import GestionDatos
from PyQt5.QtCore import QPropertyAnimation, Qt, QStringListModel
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor
from API.Validaciones import *
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
        self.gestion_datos = GestionDatos()
        # Conexión botones barra lateral con páginas
        self.ver_usuarios_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ver_usuarios_pagina)
        )
        self.ver_usuarios_boton.clicked.connect(self.mostrar_datos)
        self.ver_actualizar_boton.clicked.connect(self.mostrar_datos)
        self.ver_usuarios_boton.clicked.connect(self.limpiar_campos)
        
        self.add_usuario_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.add_usuario_pagina)
        )
        self.add_add_usuario_boton.clicked.connect(self.anadir_usuario)
        self.add_add_usuario_boton.clicked.connect(self.limpiar_campos)
        self.modificar_usuario_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.modificar_usuario_pagina)
        )
        self.modify_guardar_boton.clicked.connect(self.modificar_usuario)
        self.modify_guardar_boton.clicked.connect(self.limpiar_campos)
        self.eliminar_usuario_boton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.eliminar_usuario_pagina)
        )
        self.del_guardar_boton.clicked.connect(self.eliminar_usuario)
        self.del_guardar_boton.clicked.connect(self.limpiar_campos)
        self.modify_actualizar_boton.clicked.connect(self.mostrar_modificar)
        self.del_actualizar_boton.clicked.connect(self.mostrar_eliminar)
        # Ancho columna adaptable
        self.tabla_ver_usuarios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.modify_tabla_usuarios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.del_tabla_usuarios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        
        # Llamada de método de validación en los LineEdit
        self.setupValidatorsIdUsuario()
        self.setupValidatorsPassword()
        #ComboBox del rol
        self.add_rol_combobox.currentIndex()
    # Método para limpiar los campos cada que se cambiar de página
    def limpiar_campos(self):
        self.add_id_usuario_lineEdit.clear()
        self.add_nombre_usuario_lineEdit.clear()
        self.add_password_lineEdit.clear()
        self.modify_buscar_usuario_lineEdit.clear()
        self.modify_nombre_usuario_lineEdit.clear()
        self.modify_password_lineEdit.clear()
        self.del_buscar_usuario_lineEdit.clear()

    # Método para validar la longitud del código de barras
    def setupValidatorsIdUsuario(self):
        validacion = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"\d{1,10}")
        )
        self.add_id_usuario_lineEdit.setValidator(validacion)
        self.modify_buscar_usuario_lineEdit.setValidator(validacion)
        self.del_buscar_usuario_lineEdit.setValidator(validacion)
    
    def setupValidatorsPassword(self):
        password_validacion = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"[A-Za-z0-9]{8,64}")
        )
        self.add_password_lineEdit.setValidator(password_validacion)
        self.modify_password_lineEdit.setValidator(password_validacion)

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


    def anadir_usuario(self):
        usuario = self.add_nombre_usuario_lineEdit.text()
        contraseña = self.add_password_lineEdit.text()
        rol = self.add_rol_combobox.currentIndex()
        id_usuario = int(self.add_id_usuario_lineEdit.text())

        if usuario  != "" and contraseña  != "" and id_usuario != "":
            if usuario in self.gestion_datos.usuarios['usuario'].values:
                return False
            else:
                if usuario not in self.gestion_datos.usuarios['usuario'].values:
                    nueva_fila = pd.DataFrame([[id_usuario, usuario, contraseña, rol]], columns=['ID usuario', 'usuario', 'contraseña', 'Rol ID'])
                    self.gestion_datos.usuarios = pd.concat([self.gestion_datos.usuarios, nueva_fila], ignore_index=True)
                self.gestion_datos.guardar_dataframes()
                return True

    def modificar_usuario(self):
        usuario=self.modify_buscar_usuario_lineEdit.text()
        nuevo_usuario=self.add_nombre_usuario_lineEdit.text()
        nueva_contraseña=self.add_password_lineEdit.text()
        nuevo_rol= self.add_rol_combobox.currentIndex()
        if nuevo_usuario != "" and nueva_contraseña !="" and nuevo_rol != "":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.guardar_dataframes()
                return True
            return False
        elif nueva_contraseña !="" and nuevo_usuario == "" and nuevo_rol =="":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.guardar_dataframes()
                return True
        
        elif nueva_contraseña =="" and nuevo_usuario != "" and nuevo_rol =="":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.guardar_dataframes()
                return True
        
        elif nuevo_rol !="" and nuevo_usuario  == "" and nueva_contraseña == "":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.guardar_dataframes()
                return True
            return False
        
        elif nueva_contraseña !="" and nuevo_rol !="" and nuevo_usuario == "":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.guardar_dataframes()
                return True
            return False 
        
        elif nueva_contraseña !="" and nuevo_usuario !="" and nuevo_rol == "":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'contraseña'] = nueva_contraseña
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.guardar_dataframes()
                return True
            return False

        elif nueva_contraseña =="" and nuevo_rol !="" and nuevo_usuario != "":
            if usuario in self.gestion_datos.usuarios['ID usuario'].values:
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.guardar_dataframes()
                return True
            elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
                usuario = int(usuario)
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'Rol ID'] = nuevo_rol
                self.gestion_datos.usuarios.loc[self.gestion_datos.usuarios['usuario'] == usuario, 'usuario'] = nuevo_usuario
                self.gestion_datos.guardar_dataframes()
                return True
            return False
        else:
            return False 
        
    def eliminar_usuario(self):
        usuario=self.del_buscar_usuario_lineEdit.text()
        if usuario in self.gestion_datos.usuarios['ID usuario'].values:
            self.gestion_datos.usuarios = self.gestion_datos.usuarios[self.gestion_datos.usuarios['ID usuario'] != usuario]
            self.gestion_datos.guardar_dataframes()
            return True
        elif int(usuario) in self.gestion_datos.usuarios['ID usuario'].values:
            usuario = int(usuario)
            self.gestion_datos.usuarios = self.gestion_datos.usuarios[self.gestion_datos.usuarios['ID usuario'] != usuario]
            self.gestion_datos.guardar_dataframes()
            return True  
        else:
            return False  
    
    def mostrar_datos(self):
        self.tabla_ver_usuarios.setRowCount(0)
        for i, row in self.gestion_datos.usuarios.iterrows():
            self.tabla_ver_usuarios.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.tabla_ver_usuarios.setItem(i, j, QTableWidgetItem(str(value)))
    
    def mostrar_modificar(self):
        self.modify_tabla_usuarios.setRowCount(0)
        for i, row in self.gestion_datos.usuarios.iterrows():
            self.modify_tabla_usuarios.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.modify_tabla_usuarios.setItem(i, j, QTableWidgetItem(str(value)))
    
    def mostrar_eliminar(self):
        self.del_tabla_usuarios.setRowCount(0)
        for i, row in self.gestion_datos.usuarios.iterrows():
            self.del_tabla_usuarios.insertRow(i)
            for j, (colname, value) in enumerate(row.items()):
                self.del_tabla_usuarios.setItem(i, j, QTableWidgetItem(str(value)))

    
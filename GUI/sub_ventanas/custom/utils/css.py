from PyQt5.QtWidgets import QGroupBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPainter, QBrush,
    QColor,
)

class CustomGroupBox(QGroupBox):
    def __init__(self, parent, parentQGroupBox=None):
        super().__init__(parentQGroupBox)
        self.parent = parent
        self.label: QLabel = None

        self.setMouseTracking(True)
        self.default_style = """
            QGroupBox {
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                margin-top: 10px;
            }
            QLabel {
                background-color: #f0f0f0;
            }
        """
        self.hover_style = """
            QGroupBox {
                background-color: #d0d0d0;
                border: 2px solid #aaa;
                margin-top: 10px;
            }
            QLabel {
                background-color: #d0d0d0;
            }
        """
        self.setStyleSheet(self.default_style)

    def mousePressEvent(self, event):
        if hasattr(self.parent.cajaFiltro, 'rangoDeFechasLabel'):
            self.parent.cajaFiltro.rangoDeFechasLabel.deleteLater()
            delattr(self.parent, 'rangoDeFechasLabel')
        self.setText()
        super().mousePressEvent(event)

    def setText(self):
        self.parent.consultandoPor.setText(self.label.text())

    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_style)
        super().leaveEvent(event)

class CBackground:
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        brocha1 = QBrush(QColor(212, 132, 180), Qt.SolidPattern)
        brocha2 = QBrush(QColor(228, 156, 198), Qt.SolidPattern)
        brocha3 = QBrush(QColor(235, 188, 220), Qt.SolidPattern)

        # Obtén el tamaño actual de la ventana
        width = self.width()
        height = self.height()

        # Calcula las posiciones y tamaños en función del tamaño de la ventana
        diameter = width // 4
        offset_x = width // 8
        offset_y = height // 5

        # Dibujando círculos abajo
        painter.setBrush(brocha3)
        painter.drawEllipse(int(width // 4 - diameter // 2), int(height - offset_y * .7), int(diameter), int(diameter))

        painter.setBrush(brocha2)
        painter.drawEllipse(int(width // 8 - diameter // 2), int(height - offset_y * 1), int(diameter), int(diameter))

        painter.setBrush(brocha1)
        painter.drawEllipse(int(width // 100_000 - diameter // 2), int(height - offset_y * 1.3), int(diameter), int(diameter))

        # Dibujando círculos arriba
        painter.setBrush(brocha3)
        painter.drawEllipse(int(width // 2 +  offset_x * .8), int(-offset_y), int(diameter), int(diameter))

        painter.setBrush(brocha2)
        painter.drawEllipse(int(width // 2 + offset_x * 2), int(-offset_y // 2), int(diameter), int(diameter))

        painter.setBrush(brocha1)
        painter.drawEllipse(int(width // 2 + offset_x * 3), int(-offset_y // 5), int(diameter), int(diameter))

        painter.end()

from PyQt5.QtWidgets import QGroupBox, QLabel

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

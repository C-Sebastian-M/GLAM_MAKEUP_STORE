from PyQt5.QtWidgets import QGroupBox

class HoverGroupBox(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.default_style = """
            QGroupBox {
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                margin-top: 10px;
            }
            QLabel {
                background-color: #f0f0f0;
                font-size: 13px;
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
                font-size: 14px;
            }
        """
        self.setStyleSheet(self.default_style)

    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_style)
        super().leaveEvent(event)

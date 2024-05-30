from PyQt5.QtWidgets import QStackedWidget

class WindowStack:
    def __init__(self) -> None:
        self.stack = []
        self.widgets_stack = QStackedWidget(self)

    def anterior(self):
        anterior = None

        if self.stack:
            anterior = self.stack.pop()
        self.widgets_stack.setCurrentWidget(anterior)

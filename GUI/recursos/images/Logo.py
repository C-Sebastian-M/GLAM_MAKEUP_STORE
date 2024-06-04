import json
from PyQt5.QtGui import QPixmap
import os
import json


class ManejarLogo:
    _instacia = None

    def __new__(cls):
        if cls._instacia == None:
            cls._instacia = super(ManejarLogo, cls).__new__(cls)
            cls._instacia.ruta_logo = cls._instacia.load_logo_path()
            cls._instacia.observers = []
        return cls._instacia

    @staticmethod
    def load_logo_path():
        if os.path.exists("config.json"):
            with open("config.json", "r") as file:
                config = json.load(file)
                return config.get("logo_path", r"GUI\recursos\images\logo.png")
        return r"GUI\recursos\images\logo.png"

    @staticmethod
    def save_logo_path(path):
        with open("config.json", "w") as file:
            json.dump({"logo_path": path}, file)

    def set_logo(self, path):
        self.logo_path = path
        self.save_logo_path(path)
        self.notify_observers()

    def get_logo(self):
        return self.logo_path

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_logo(self.logo_path)

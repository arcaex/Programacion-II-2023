from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana.ui", self)

class MiVentana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana2.ui", self)
    
app = QApplication([])

win = MiVentana()
win.show()

app.exec_()


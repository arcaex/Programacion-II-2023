from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_1.ui", self)
        self.ventana2 = MiVentana2()
        self.boton.clicked.connect(self.open_window)
    
    def open_window(self):
        self.ventana2.show()


class MiVentana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_2.ui",self)
    
app = QApplication([])
win = MiVentana()
win.show()
# win2 = MiVentana2()
# win2.show()
app.exec()
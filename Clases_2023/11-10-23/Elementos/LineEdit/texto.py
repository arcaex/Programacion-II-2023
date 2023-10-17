from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("texto.ui", self)
        self.boton.clicked.connect(self.mostrar_texto)
        
    def mostrar_texto(self):
        self.etiqueta.setText(self.texto.text())
        print(self.texto.text())

app = QApplication([])
win = MiVentana()
win.show()
app.exec()
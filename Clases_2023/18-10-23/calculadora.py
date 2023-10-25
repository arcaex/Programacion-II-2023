from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        self.boton_calcular.clicked.connect(self.calcular)
    
    def calcular(self):
        numero1 = int(self.numero1.text())
        numero2 = int(self.numero2.text())
        suma = numero1 + numero2
        self.etiqueta_resultado.setText(str(suma))

app = QApplication([])
win = MiVentana()
win.show()
app.exec()
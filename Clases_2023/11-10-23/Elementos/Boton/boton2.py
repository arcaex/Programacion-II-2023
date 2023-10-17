from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("boton.ui", self)
        self.boton.clicked.connect(self.cambiar_label)
    
    def cambiar_label(self):
        if self.etiqueta.text() == "Hola Mundo!":
            self.etiqueta.setText("Chau Mundo!")
        elif self.etiqueta.text() == "Chau Mundo!":
            self.etiqueta.setText("Hola Mundo!")
    


app = QApplication([])
win = MiVentana()
# print(win.boton.text())
# win.boton.setText("No")
win.show()
app.exec()
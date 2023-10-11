from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("boton.ui", self)
        self.boton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        if self.etiqueta.text() == "Chau mundo!":
            self.etiqueta.setText("Hola mundo!")
        elif self.etiqueta.text() == "Hola mundo!":
            self.etiqueta.setText("Chau mundo!")

app = QApplication([])
win = MiVentana()

win.show()
app.exec()

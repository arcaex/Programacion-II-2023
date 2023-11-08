from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentanaPadre(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana1.ui", self)
        self.ventana_hija = MiVentana2(self)
        # self.ventana_hija.show()
        # self.ventana_hija_2 = MiVentana2(self)
        self.boton_padre.clicked.connect(self.mostrar_ventana_hija)
        self.boton_padre.clicked.connect(self.cambiar_texto_hija)

    def cambiar_texto_hija(self):
        texto = self.texto_padre.text()
        self.ventana_hija.label.setText(texto)
        #self.hide()

    def mostrar_ventana_hija(self):
        self.ventana_hija.show()

class MiVentana2(QMainWindow):
    def __init__(self, ventana_padre):
        super().__init__()
        uic.loadUi("ventana2.ui",self)
        self.ventana_padre = ventana_padre
        self.boton_hijo.clicked.connect(self.cambiar_texto_padre)

    def cambiar_texto_padre(self):
        texto = self.texto_hijo.text()
        self.ventana_padre.label.setText(texto)
        self.ventana_padre.show()
        self.hide()

    def closeEvent(self,event):
        self.ventana_padre.show()

app = QApplication([])
win = MiVentanaPadre()
win.show()
app.exec()
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_1.ui", self)
        # Se pasa el Padre como parámetro al constructor de la Ventana Hijo
        self.ventana2 = MiVentana2(self)
        self.boton.clicked.connect(self.open_window)
        self.boton.clicked.connect(self.edit_label_ventana_2)
    
    def open_window(self):
        self.ventana2.show()

    #Comunicación con Ventana Hijo
    def edit_label_ventana_2(self):
        self.ventana2.nombre_label.setText(self.nombre.text())

class MiVentana2(QMainWindow):
    def __init__(self,padre):
        super().__init__()
        uic.loadUi("ventana_2.ui",self)
        self.boton_hijo.clicked.connect(self.click_boton)
        #Se agrega un atributo que guarda todo la Ventana Padre
        self.padre = padre

    #Comunicación con Ventana Padre
    def click_boton(self):
        self.padre.nombre.setText("Hola Mundo!")
        
    
app = QApplication([])
win = MiVentana()
win.show()
# win2 = MiVentana2()
# win2.show()
app.exec()
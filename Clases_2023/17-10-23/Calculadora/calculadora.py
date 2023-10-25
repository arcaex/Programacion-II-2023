from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        self.boton_calcular.clicked.connect(self.calcular)
        self.tipo_operacion.currentTextChanged.connect(self.calcular)
        self.numero1.textChanged.connect(self.calcular)
        self.numero2.textChanged.connect(self.calcular)
        
    def calcular(self):

        operacion = self.tipo_operacion.currentText()

        n1 = self.numero1.text()
        n2 = self.numero2.text()

        # n1_ultimo = 0
        # n2_ultimo = 0
        # if len(n1)-1 <0 :
        #     n1_ultimo = 0
        # else:
        #     n1_ultimo = len(n1)-1
        # if len(n2)-1 <0 :
        #     n2_ultimo = 0
        # else:
        #     n2_ultimo = len(n2)-1
        # if not n1[n1_ultimo].isdigit():
        #     self.numero1.setText("")
        # if not n2[n2_ultimo].isdigit():
        #     self.numero2.setText("")

        if n1.isdigit() and n2.isdigit():
            n1 = int(n1)
            n2 = int(n2)
            if operacion == "Suma":
                resultado = n1 + n2
            elif operacion == "Resta":
                resultado = n1 - n2
            elif operacion == "Multiplicación":
                resultado = n1 * n2 
            else:
                resultado = n1/n2
            self.etiqueta_resultado.setText(str(resultado))

app = QApplication([])
win = MiVentana()
win.show()
app.exec()
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("message_box.ui", self)
        self.mensaje.clicked.connect(self.on_mensaje)

    def on_mensaje(self):
        
        msg = QMessageBox()
        msg.setWindowTitle('Titulo de mensaje')
        msg.setText('Este es un mensaje')
        # msg.setIcon(QMessageBox.Icon.Critical)
        # msg.setIcon(QMessageBox.Icon.Warning)
        # msg.setIcon(QMessageBox.Icon.Information)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)

        respuesta = msg.exec()

        # if respuesta == QMessageBox.Yes:
        #     print('Se eligio si')
        # elif respuesta == QMessageBox.No:
        #     print('Se eligio no')
        # else:
        #     print('Se eligio cancelar')


app = QApplication([])

win = MiVentana()
win.show()

app.exec()

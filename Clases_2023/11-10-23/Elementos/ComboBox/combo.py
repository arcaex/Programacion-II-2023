from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("combo.ui", self)
        self.comboBox.currentTextChanged.connect(self.onChange)
        self.removeBtn.clicked.connect(self.onRemove)
        self.addBtn.clicked.connect(self.onAdd)
    
    def onChange(self):
        print(self.comboBox.currentText())
        print(self.comboBox.currentIndex())
    
    def onRemove(self):
        msg = QMessageBox()
        msg.setWindowTitle("Advertencia")
        msg.setText("¿Está seguro que desea eliminar ese elemento?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        respuesta = msg.exec()

        if respuesta == QMessageBox.StandardButton.Yes:
            index = self.comboBox.currentIndex()
            self.comboBox.removeItem(index)
        
        if self.comboBox.count() == 0 :
            self.removeBtn.setEnabled(False)

    def onAdd(self):
        text = self.addText.text()
        self.comboBox.addItem(text)
        self.removeBtn.setEnabled(True)

    
app = QApplication([])
win = MiVentana()
win.show()
app.exec()

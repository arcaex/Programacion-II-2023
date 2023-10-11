from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("combo.ui", self)
        #self.comboBox.currentIndexChanged.connect(self.onChange)
        self.comboBox.currentTextChanged.connect(self.onChange)
        self.removeBtn.clicked.connect(self.onRemove)
        self.addBtn.clicked.connect(self.onAdd)
    
    def onChange(self):
        print(self.comboBox.currentText())
        print(self.comboBox.currentIndex())
    
    def onRemove(self):
        index = self.comboBox.currentIndex()
        self.comboBox.removeItem(index)

    def onAdd(self):
        text = self.addText.text()
        count = self.comboBox.count()
        flag = 0
        if count < 6:
            for i in range(0,count-1):
                textElement = self.comboBox.itemText(i)
                if text == textElement:
                    flag = 1
            if flag == 0:            
                self.comboBox.addItem(text)
                self.addText.setText("")
            else:
                self.addText.setText("No se puede Agregar")
    
app = QApplication([])
win = MiVentana()
win.show()
app.exec_()

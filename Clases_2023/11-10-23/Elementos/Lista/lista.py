from PyQt6.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt6 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lista.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        self.editar.clicked.connect(self.on_editar)
        self.lista.itemDoubleClicked.connect(self.on_editar)
        self.quitar.clicked.connect(self.on_quitar)
        self.filtrar.textChanged.connect(self.filtrare)
        self.quitar_todos.clicked.connect(self.limpiarLista)
        self.nombre.returnPressed.connect(self.on_agregar)
        self.lista_real = []

    def on_agregar(self):
        #.addItem(Texto) - Agregar un Item
        self.lista.addItem(self.nombre.text())
        self.lista_real.append(self.nombre.text())
        self.nombre.setText('')
    
    def filtrare(self):
        self.lista.clear()
        for item in self.lista_real:
            if self.filtrar.text() in item:
                self.lista.addItem(item)

    def limpiarLista(self):
        self.lista.clear()
            
    def on_editar(self):
        #.currentItem().text() -> Traigo el texto del item seleccionado
        #.currentItem().setText() -> Cambio el texto del item seleccionado
        texto_item = self.lista.currentItem().text()
        nuevo_texto, ok = QInputDialog.getText(self, 'Editar', 'Ingrese nuevo nombre', text=texto_item)
        if ok:
            self.lista.currentItem().setText(nuevo_texto)

    def on_quitar(self):
        # .currentRow() -> Fila actual seleccionada
        # .takeItem(fila) -> Borra una fila
        self.lista.takeItem(self.lista.currentRow())


app = QApplication([])

win = MiVentana()
win.show()

app.exec()

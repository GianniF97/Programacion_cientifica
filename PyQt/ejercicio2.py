import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import random
textos = ['Python','Java','JavaScript','PHP','C++','C#']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "ejercicio2.ui")
        loadUi(ui_path, self)
        

        # Evento: clic en el botón
        self.pushButton_mensaje.clicked.connect(self.tamanio)
        self.pushButton_limpiar.clicked.connect(self.limpiar)
        self.pushButton_salir.clicked.connect(self.salir)

    def limpiar(self):
        self.label_texto.clear()

    def salir(self):
        self.close()

    def tamanio(self):
        texto = random.choice(textos) 
        self.label_texto.setText(f'{texto}')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

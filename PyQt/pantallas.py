from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from PyQt5.uic import loadUi
import sys, os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear el contenedor de pantallas
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Cargar pantallas desde los .ui
        path = os.path.dirname(__file__)
        self.pantalla1 = QWidget()
        self.pantalla2 = QWidget()

        loadUi(os.path.join(path, "pantalla1.ui"), self.pantalla1)
        loadUi(os.path.join(path, "pantalla2.ui"), self.pantalla2)

        # Agregar al stack
        self.stack.addWidget(self.pantalla1)
        self.stack.addWidget(self.pantalla2)

        # Botón para pasar de una a otra
        self.pantalla1.boton_siguiente.clicked.connect(lambda: self.stack.setCurrentWidget(self.pantalla2))
        self.pantalla2.boton_volver.clicked.connect(lambda: self.stack.setCurrentWidget(self.pantalla1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())

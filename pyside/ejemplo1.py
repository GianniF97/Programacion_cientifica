# Importar las clases de PySide6
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *


# Crear una aplicacion Qt
app = QApplication(sys.argv)

# Crear una ventana
ventana = QMainWindow()
ventana.setWindowTitle('Hola Mundo!')

# Crear una etiqueta y mostrar todo junto
etiqueta = QLabel(ventana, alignment=Qt.AlignCenter)
etiqueta.setText('Hola Mundo!')
ventana.setCentralWidget(etiqueta)

ventana.resize(300, 200)
ventana.show()

# Correr la aplicación Qt
sys.exit(app.exec())
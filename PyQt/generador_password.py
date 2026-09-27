import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
#comando pyrcc5 imagenes.qrc -o imagenes_rc.py

from imagenes import imagenes_rc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "generador_password.ui")
        loadUi(ui_path, self)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets
from ejercicio1b import Ui_MainWindow

app = QtWidgets.QApplication([])
ventana = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(ventana)
ventana.show()
app.exec_()
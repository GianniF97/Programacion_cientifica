import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox

#guia https://es.python-3.com/?p=243
# estilos CSS https://jquery-manual.blogspot.com/2015/06/5-python-pyqt-interfaz-grafica-disenar.html
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "ejercicio3.ui")
        loadUi(ui_path, self)
        #bandera para el campo de entrada
        self.bandera = False
        #self.boton_validar.clicked.connect(self.validar)
        #no mostrar las siguientes lineas
        self.boton_validar.accepted.connect(self.validar)
        self.boton_validar.rejected.connect(self.limpiar)

        #llamar a la funcion validar
        #self.boton_validar.clicked.connect(self.validar)
        # Evento: clic en el botón
        self.boton_subir.clicked.connect(self.subir)
    #validar
    def validar(self):
        texto  = self.mensaje_entrada.text()
        if texto == "":
            self.bandera = False
            self.mostrar_error("El campo no puede estar vacío.")
        else:
            self.mostrar_info(f"Texto Correcto")
            self.bandera = True
    #tienen que agregar esto
    def limpiar(self):
        self.mensaje_salida.setText("Limpio")
    #subir
    def subir(self):
        if self.bandera == True:
            texto = self.mensaje_entrada.text()
            self.mensaje_salida.setText(texto)
        else:
            self.mostrar_error("Se debe validar primero")
    #metodo para el error
    #https://stackoverflow.com/questions/40227047/python-pyqt5-how-to-show-an-error-message-with-pyqt5    
    def mostrar_error(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText(mensaje)
        msg.exec_()
    #metodo para la info correcta
    def mostrar_info(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Info")
        msg.setText(mensaje)
        msg.exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStyle
from PyQt5.QtGui import QIcon

#Iconos predeterminados
#https://www.pythonguis.com/faq/built-in-qicons-pyqt/
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')

        # Ícono estándar del sistema (botón de ayuda)
        icon = self.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        self.setWindowIcon(icon)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

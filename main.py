# archibos necesaris
from GUI.ui_VentanaPrin2 import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import MSFluentWindow
# librerias
import sys


# clase principal
class windowPrin(MSFluentWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = windowPrin()
    window.show()
    sys.exit(app.exec())

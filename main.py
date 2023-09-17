# archibos necesaris
from GUI.ui_VentanaPrin2 import Ui_Form
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from qframelesswindow import FramelessWindow
from qfluentwidgets import *
# librerias
import sys

# clase principal
class windowPrin(FramelessWindow, Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = windowPrin()
    window.show()
    sys.exit(app.exec())

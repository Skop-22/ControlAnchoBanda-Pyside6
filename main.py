# archibos necesaris
from GUI.ui_VentanaPrincipal import *
# librerias
import sys


# clase principal
class windowPrin(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.anchoBanda = Ui_MainWindow()
    pass


# objeto
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = windowPrin()
    window.show()
    sys.exit(app.exec())
    pass

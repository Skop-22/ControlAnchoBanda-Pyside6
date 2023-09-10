# archibos necesaris
from GUI.ui_VentanaPrincipal import *
# librerias
import sys


# clase principal
class windowPrin(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ventanaAnchoDeBanda = Ui_MainWindow()
        self.ventanaAnchoDeBanda.setupUi(self)
        self.grupoDeBotones()

    def stilosDelaAplicacion(self,typeStile):
        if(typeStile == "darck"):
            with open("CSS/styles.css","r") as f:
                self.setStyleSheet(f.read())
        elif(typeStile == "ligt"):
            pass
        
    def grupoDeBotones(self):
        pass



# objeto
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = windowPrin()
    window.show()
    sys.exit(app.exec())

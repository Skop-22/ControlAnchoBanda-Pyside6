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
        self.stilosDelaAplicacion("darck")
        self.grupoDeBotones()

    def stilosDelaAplicacion(self,typeStile):
        if(typeStile == "darck"):
            with open("CSS/stylesDarck.css","r") as negro:
                self.setStyleSheet(negro.read())
        elif(typeStile == "with"):
            with open("CSS/stylesWith.css","r") as blaco:
                self.setStyleSheet(blaco.read())
        
    def grupoDeBotones(self):
        pass



# objeto
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = windowPrin()
    window.show()
    sys.exit(app.exec())

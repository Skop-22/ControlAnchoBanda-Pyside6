from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale
# archibos necesaris
from qfluentwidgets import FluentIcon, SplitTitleBar, setThemeColor, FluentTranslator, SplitFluentWindow 
from  FunWin.VentanaCasa import windowHome
# librerias
import sys

# clase principal
class VentanaPrincipal(SplitFluentWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        #titulo de la ventana
        self.Titulo()
        #menu de opciones a agregar
        self.menuDelaAplicacion()

    def menuDelaAplicacion(self):
        self.windowHome = windowHome()
        self.addSubInterface(self.windowHome,FluentIcon.HOME,"Home")


    def Titulo(self):
        # change title bar
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()
        self.setWindowTitle('Control De Ancho De Banda')
        self.windowEffect.setMicaEffect(self.winId())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.installTranslator(FluentTranslator(QLocale()))
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())

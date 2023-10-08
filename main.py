from Rutas.ruta import *

# clase principal
class VentanaPrincipal(SplitFluentWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        #titulo de la ventana
        self.tituloVentana()
        self.stilos()
        self.menuDelaAplicacion()

    def menuDelaAplicacion(self):
        self.windowHome = windowHome(self)
        self.informacion = Info(self)
        self.addSubInterface(self.windowHome,FluentIcon.WIFI,"Wifi")
        self.addSubInterface(self.informacion,FluentIcon.INFO,"Información")


    def tituloVentana(self):
        # change title bar
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()
        self.setWindowTitle('Control De Ancho De Banda')
        self.windowEffect.setMicaEffect(self.winId())

    def stilos(self):
        self.resize(1060, 680)
        with open("CSS/styles.css") as style:
            self.setStyleSheet(style.read())


if __name__ == "__main__":
    setTheme(Theme.DARK)#tema 
    app = QApplication(sys.argv)
    app.installTranslator(FluentTranslator(QLocale()))
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())

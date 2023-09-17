# archibos necesaris
from GUI.ui_VentanaPrin2 import *
from qframelesswindow import AcrylicWindow
from qfluentwidgets import setThemeColor
from qfluentwidgets import FluentTranslator, SplitTitleBar
# librerias
import sys

# clase principal
class windowPrin(AcrylicWindow,Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # change theme color
        setThemeColor('#28afe9')

        # change title bar
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.setWindowTitle('Control De Ancho De Banda')
        self.windowEffect.setMicaEffect(self.winId())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.installTranslator(FluentTranslator(QLocale()))
    window = windowPrin()
    window.show()
    sys.exit(app.exec())

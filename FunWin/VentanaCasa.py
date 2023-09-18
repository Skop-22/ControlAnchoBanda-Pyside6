# archibos necesaris
from GUI.ui_VentanaPrin2 import *
# librerias
import sys

# clase principal
class windowHome(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

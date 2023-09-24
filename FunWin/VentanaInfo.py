from GUI.ui_Info import *

class Info(Ui_Informacion,QWidget):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
    
    def mapaDeDispositivos(self):
        pass

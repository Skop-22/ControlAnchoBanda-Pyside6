# archibos necesaris
from GUI.ui_VentanaPrin2 import *
# librerias
import sys

# clase principal
class windowHome(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.tablaDeDireccionesIP()

    def escanerDeRed(self):
        pass

    def tablaDeDireccionesIP(self):
        self.tableWidget.setWordWrap(False)
        self.tableWidget.verticalHeader().hide()
        devices= [['1','alcatel',"192.168.1.1",'00:1A:2B:3C:4D:5E','Conectado']
                    ,['2','nokia',"192.168.1.2",'D1:22:33:44:55:67','Desconectado']
                    ,['4','nokia',"192.168.1.4",'D1:22:33:44:55:69','Conectado']]
        self.tableWidget.setRowCount(len(devices))#tamaño en columnas
        self.tableWidget.setColumnCount(len(devices[0]))
        self.escanerDeRed()

        for contador, devices in enumerate(devices):
            for j in range(len(devices)):
                #print(f"i = {contador} \n j={j} \n device = {devices[j]}")
                self.tableWidget.setItem(contador,j,QTableWidgetItem(devices[j]))

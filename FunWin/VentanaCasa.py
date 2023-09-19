# archibos necesaris
from socket import timeout
from GUI.ui_VentanaPrin2 import *
from scapy.all import ARP, Ether, packet, srp
# librerias
import sys

# clase principal
class windowHome(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.tablaDeDireccionesIP()

    def escanerDeRed(self,ip_range):
        arp = ARP(pdst=ip_range)
        eternet = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = eternet / arp

        result = srp(packet, timeout=3, verboso=0)[0]

        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        return devices

    def tablaDeDireccionesIP(self):
        self.tableWidget.setWordWrap(False)
        self.tableWidget.verticalHeader().hide()
        #target_ip_range = "192.168.1.0/24"  # Cambia la dirección IP según tu red
        #devices = self.escanerDeRed(target_ip_range)
        devices= [['1','alcatel',"192.168.1.1",'00:1A:2B:3C:4D:5E','Conectado']
                    ,['2','nokia',"192.168.1.2",'D1:22:33:44:55:67','Desconectado']
                    ,['4','nokia',"192.168.1.4",'D1:22:33:44:55:69','Conectado']]
        self.tableWidget.setRowCount(len(devices))#tamaño en columnas
        self.tableWidget.setColumnCount(len(devices[0]))

        for contador, devices in enumerate(devices):
            for j in range(len(devices)):
                #print(f"i = {contador} \n j={j} \n device = {devices[j]}")
                self.tableWidget.setItem(contador,j,QTableWidgetItem(devices[j]))



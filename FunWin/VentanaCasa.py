from Rutas.ruta import *
# clase principal
class windowHome(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.label.setText("Dispositivos")
        self.label_2.setText("Grafica De Dispositivos")
        self.label_3.setText("Grafica Detalles")
        self.progressBar = IndeterminateProgressBar()
        self.Progeso.addWidget(self.progressBar)
        self.progressBar.stop()
        self.Actualizar.clicked.connect(lambda: self.tablaDeDireccionesIP())

        self.definicionDeGraficos()

    def definicionDeGraficos(self):
        arregloDisositivos = [[1,2],[2,4],[5,2],[6,0],[7,1]]
        arregloDetalles =[[1,500],[2,400],[3,50],[4,300]]
        self.Grafico_De_Los_Dispositivos.addWidget(self.graficoTipoLineal(arregloDisositivos,'Dias','Dispositivos'))
        self.Grafico_De_los_Detalles.addWidget(self.graficoTipoLineal(arregloDetalles,'Dias','Conexion'))

    def graficoTipoLineal(self,arreglo,tituloX,tituloY):
        chart = QtCharts.QChart()
        chart.setBackgroundBrush(Qt.transparent)

        series = QLineSeries()
        for i,detalles in enumerate(arreglo):
            series.append(QPointF(detalles[0],detalles[1]))
        # Agregar etiquetas a puntos específicos
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().hide()
        axis_x = chart.axisX()
        axis_y = chart.axisY()
        axis_x.setGridLineVisible(False)
        axis_y.setGridLineVisible(False)
        axis_x.setTitleText(tituloX)
        axis_y.setTitleText(tituloY)
        axis_x.setTitleBrush(QtGui.QColor("white"))
        axis_y.setTitleBrush(QtGui.QColor("white"))
        axis_x.setLabelsColor(QtGui.QColor("white"))
        axis_y.setLabelsColor(QtGui.QColor("white"))

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)#para que los bordes sean mas suaves

        chart_view.setStyleSheet("background-color: transparent;color: rgb(255,255,255);")
        return chart_view

    def tablaDeDireccionesIP(self):
        self.Actualizar.setEnabled(False)
        self.escanerDevice = Escaneo()
        self.escanerDevice.start()
        self.progressBar.start()
        self.createInfoInfoBar("Actualización de los Dispositivos", 'Los dispositivos se estan actualizando porfavor espere')
        self.dataIP = Escaneo()
        self.dataIP.signal.connect(self.actuali)
        self.dataIP.start()

    def createInfoInfoBar(self,Titulo,Contenido):
        content = Contenido 
        w = InfoBar(
            icon=FluentIcon.SPEED_OFF,
            title=Titulo,
            content=content,
            orient=Qt.Vertical,    # vertical layout
            isClosable=False,
            position=InfoBarPosition.TOP_RIGHT,
            duration=2000,
            parent=self
        )
        w.show()

    def actuali(self,devices):
        self.Actualizar.setEnabled(True)
        self.progressBar.stop()
        self.tableWidget.setWordWrap(False)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(len(devices))#tamaño en columnas
        self.tableWidget.setColumnCount(len(devices[0]))

        for contadorEnX, devices in enumerate(devices):
            for contadorEnY in range(len(devices)):
                self.tableWidget.setItem(contadorEnX,contadorEnY,QTableWidgetItem(str(devices[contadorEnY])))

class Escaneo(QObject,threading.Thread):
    signal = Signal(list)
    def __init__(self):
        threading.Thread.__init__(self)  # Llamar a __init__ de threading.Thread
        QObject.__init__(self)  # Llamar a __init__ de QObject
        self.lista = []

    def run(self):
        contador =0
        nm = nmap.PortScanner()
        nm.scan(hosts="192.168.1.0/24", arguments='-T4 -F')
        for hosts in nm.all_hosts():
            if hosts != '192.168.1.254':
                self.lista.insert(contador,[contador+1,nm[hosts].hostname(),hosts,nm[hosts].state()])
            contador +=1
        self.signal.emit(self.lista)

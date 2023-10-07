from Rutas.ruta import *
# clase principal
class windowHome(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.tablaDeDireccionesIP()
        self.label.setText("Dispositivos")
        self.label_2.setText("Grafica De Dispositivos")
        self.label_3.setText("Grafica Detalles")
        self.definicionDeGraficos()

    def definicionDeGraficos(self):
        arregloDisositivos = [[1,2],[2,4],[5,2],[6,0],[7,1]]
        arregloDetalles =[[1,500],[2,400],[3,50],[4,300]]
        self.Grafico_De_Los_Dispositivos.addWidget(self.graficoTipoLineal(arregloDisositivos,'Dias','Dispositivos'))
        self.Grafico_De_los_Detalles.addWidget(self.graficoTipoLineal(arregloDetalles,'Dias','Conexion'))
        pass

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
        self.tableWidget.setWordWrap(False)
        self.tableWidget.verticalHeader().hide()
        devices= [['1','alcatel',"192.168.1.1",'00:1A:2B:3C:4D:5E','Conectado']
                    ,['2','nokia',"192.168.1.2",'D1:22:33:44:55:67','Desconectado']
                    ,['4','nokia',"192.168.1.4",'D1:22:33:44:55:69','Conectado']]
        self.tableWidget.setRowCount(len(devices))#tamaño en columnas
        self.tableWidget.setColumnCount(len(devices[0]))

        for contador, devices in enumerate(devices):
            for j in range(len(devices)):
                #print(f"i = {contador} \n j={j} \n device = {devices[j]}")
                self.tableWidget.setItem(contador,j,QTableWidgetItem(devices[j]))

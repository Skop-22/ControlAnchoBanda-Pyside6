from Rutas.ruta import *

class Info(Ui_Informacion,QWidget):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.mapaDeDispositivos()

    
    def mapaDeDispositivos(self):
        self.donuts = []
        self.chart_view = QChartView(self.frame)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setStyleSheet("background-color: transparent;")
        self.chart = self.chart_view.chart()
        self.chart.setBackgroundBrush(Qt.transparent)
        self.chart.legend().setVisible(False)
        self.chart.setTitle("Estado De la Red")
        self.chart.setAnimationOptions(QChart.AllAnimations)

        self.min_size = 0.1
        self.max_size = 0.9
        self.donut_count = 5

        self.setup_donuts()

        # create main layout
        self.main_layout = QGridLayout(self.frame)
        self.main_layout.addWidget(self.chart_view, 1, 1)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(1250)

    def setup_donuts(self):
        for i in range(self.donut_count):
            donut = QPieSeries()
            slccount = randrange(3, 6)
            for j in range(slccount):
                value = randrange(100, 200)

                slc = QPieSlice(str(value), value)
                slc.setLabelVisible(True)
                slc.setLabelColor(Qt.white)
                slc.setLabelPosition(QPieSlice.LabelInsideTangential)

                # Connection using an extra parameter for the slot
                slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))

                donut.append(slc)
                size = (self.max_size - self.min_size) / self.donut_count
                donut.setHoleSize(self.min_size + i * size)
                donut.setPieSize(self.min_size + (i + 1) * size)

            self.donuts.append(donut)
            self.chart_view.chart().addSeries(donut)

    @Slot()
    def update_rotation(self):
        for donut in self.donuts:
            phase_shift = randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)

    def explode_slice(self, exploded, slc):
        if exploded:
            self.update_timer.stop()
            slice_startangle = slc.startAngle()
            slice_endangle = slc.startAngle() + slc.angleSpan()

            donut = slc.series()
            idx = self.donuts.index(donut)
            for i in range(idx + 1, len(self.donuts)):
                self.donuts[i].setPieStartAngle(slice_endangle)
                self.donuts[i].setPieEndAngle(360 + slice_startangle)
        else:
            for donut in self.donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)

            self.update_timer.start()

        slc.setExploded(exploded)

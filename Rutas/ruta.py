#proyectos de Pyside6
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (
                            QApplication,
                            QStyle, 
                            QWidget, 
                            QGraphicsDropShadowEffect, 
                            QGridLayout, 
                            QWidget)

from PySide6.QtCharts import (
                            QChart, 
                            QChartView, 
                            QLineSeries, 
                            QAreaSeries, 
                            QPieSlice,
                            QPieSeries)

from PySide6.QtCore import (
                            QLocale, 
                            QPointF, 
                            Qt, 
                            QTimer, 
                            Slot)

from PySide6 import QtCharts,QtGui

#archibos necesaris de qfluentwidgets para la nueva version

from qfluentwidgets import (FluentIcon, SplitTitleBar, FluentTranslator, SplitFluentWindow,
                            setTheme, Theme, HorizontalFlipView)
from random import randrange
from functools import partial
import sys

#archivos para la venta 
from GUI.ui_Info import *
from GUI.ui_VentanaPrin2 import *

#funcionalidad de las ventanas 
from FunWin.VentanaCasa import windowHome
from FunWin.VentanaInfo import Info


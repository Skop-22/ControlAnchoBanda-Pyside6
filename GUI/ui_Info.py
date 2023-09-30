# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoKgOeta.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

from qfluentwidgets import CardWidget

class Ui_Informacion(object):
    def setupUi(self, Informacion):
        if not Informacion.objectName():
            Informacion.setObjectName(u"Informacion")
        Informacion.resize(879, 601)
        self.label = QLabel(Informacion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 161, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.frame = CardWidget(Informacion)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 80, 531, 441))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Informacion)

        QMetaObject.connectSlotsByName(Informacion)
    # setupUi

    def retranslateUi(self, Informacion):
        Informacion.setWindowTitle(QCoreApplication.translate("Informacion", u"Informacion", None))
        self.label.setText(QCoreApplication.translate("Informacion", u"Informaci\u00f3n", None))
    # retranslateUi


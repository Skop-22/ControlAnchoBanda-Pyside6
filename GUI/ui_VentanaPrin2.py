# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrin2qstqIg.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)

from qfluentwidgets import PushButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(909, 607)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 40, -1, -1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = PushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1, Qt.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(20)
        self.pushButton_4 = PushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.pushButton_2 = PushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_3 = PushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_5 = PushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_3.addWidget(self.pushButton_5, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi


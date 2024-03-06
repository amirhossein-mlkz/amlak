# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buildingList_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(347, 618)
        window.setStyleSheet(u"*[styleClass=\"label\"]{\n"
"	\n"
"	color:rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color:#404040;\n"
"}\n"
"\n"
"#window{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"#mainFrame{\n"
"	background-color:white;\n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainFrame = QFrame(window)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setMinimumSize(QSize(0, 600))
        self.mainFrame.setBaseSize(QSize(0, 0))
        self.mainFrame.setStyleSheet(u"")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.mainFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 37))
        self.label.setStyleSheet(u"QLabel[buildingState]{\n"
"font-size:18px;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel[buildingState=\"0\"]{\n"
"	background-color:rgb(58, 209, 154);\n"
"}\n"
"\n"
"QLabel[buildingState=\"1\"]{\n"
"	background-color: rgb(255, 191, 0);\n"
"}\n"
"\n"
"QLabel[buildingState=\"2\"]{\n"
"	background-color:rgb(197, 63, 59);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setProperty("buildingState", 2)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.mainFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.mainFrame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4, 0, Qt.AlignRight)

        self.label_3 = QLabel(self.mainFrame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.mainFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 18, 20, 15)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_9 = QFrame(self.mainFrame)
        self.horizontalFrame_9.setObjectName(u"horizontalFrame_9")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.label_23 = QLabel(self.horizontalFrame_9)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.label_23)

        self.label_21 = QLabel(self.horizontalFrame_9)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_21)

        self.label_24 = QLabel(self.horizontalFrame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(22, 22))
        self.label_24.setMaximumSize(QSize(22, 22))
        self.label_24.setSizeIncrement(QSize(30, 30))
        self.label_24.setPixmap(QPixmap(u":/icons/icons/location-20.png"))

        self.horizontalLayout_10.addWidget(self.label_24)


        self.verticalLayout_4.addWidget(self.horizontalFrame_9)

        self.horizontalFrame_14 = QFrame(self.mainFrame)
        self.horizontalFrame_14.setObjectName(u"horizontalFrame_14")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_40 = QLabel(self.horizontalFrame_14)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.label_40)

        self.label_41 = QLabel(self.horizontalFrame_14)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.label_41)

        self.label_42 = QLabel(self.horizontalFrame_14)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(22, 22))
        self.label_42.setMaximumSize(QSize(22, 22))
        self.label_42.setSizeIncrement(QSize(30, 30))
        self.label_42.setPixmap(QPixmap(u":/icons/icons/price-20.png"))

        self.horizontalLayout_16.addWidget(self.label_42)


        self.verticalLayout_4.addWidget(self.horizontalFrame_14)

        self.horizontalFrame_13 = QFrame(self.mainFrame)
        self.horizontalFrame_13.setObjectName(u"horizontalFrame_13")
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalFrame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_37 = QLabel(self.horizontalFrame_13)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)

        self.horizontalLayout_15.addWidget(self.label_37)

        self.label_38 = QLabel(self.horizontalFrame_13)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.label_38)

        self.label_39 = QLabel(self.horizontalFrame_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(22, 22))
        self.label_39.setMaximumSize(QSize(22, 22))
        self.label_39.setSizeIncrement(QSize(30, 30))
        self.label_39.setPixmap(QPixmap(u":/icons/icons/price-20.png"))

        self.horizontalLayout_15.addWidget(self.label_39)


        self.verticalLayout_4.addWidget(self.horizontalFrame_13)

        self.horizontalFrame_11 = QFrame(self.mainFrame)
        self.horizontalFrame_11.setObjectName(u"horizontalFrame_11")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalFrame_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_31 = QLabel(self.horizontalFrame_11)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.label_31)

        self.label_32 = QLabel(self.horizontalFrame_11)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.label_32)

        self.label_33 = QLabel(self.horizontalFrame_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(22, 22))
        self.label_33.setMaximumSize(QSize(22, 22))
        self.label_33.setSizeIncrement(QSize(30, 30))
        self.label_33.setPixmap(QPixmap(u":/icons/icons/price-20.png"))

        self.horizontalLayout_13.addWidget(self.label_33)


        self.verticalLayout_4.addWidget(self.horizontalFrame_11)

        self.horizontalFrame_12 = QFrame(self.mainFrame)
        self.horizontalFrame_12.setObjectName(u"horizontalFrame_12")
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalFrame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_34 = QLabel(self.horizontalFrame_12)
        self.label_34.setObjectName(u"label_34")
        sizePolicy1.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.label_34)

        self.label_35 = QLabel(self.horizontalFrame_12)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_35)

        self.label_36 = QLabel(self.horizontalFrame_12)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(22, 22))
        self.label_36.setMaximumSize(QSize(22, 22))
        self.label_36.setSizeIncrement(QSize(30, 30))
        self.label_36.setPixmap(QPixmap(u":/icons/icons/price-20.png"))

        self.horizontalLayout_14.addWidget(self.label_36)


        self.verticalLayout_4.addWidget(self.horizontalFrame_12)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.line_3 = QFrame(self.mainFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(13, -1, -1, 0)
        self.horizontalFrame_7 = QFrame(self.mainFrame)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        self.horizontalFrame_7.setMinimumSize(QSize(0, 25))
        self.horizontalFrame_7.setSizeIncrement(QSize(1, 1))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_17 = QLabel(self.horizontalFrame_7)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label_17, 0, Qt.AlignRight)

        self.label_18 = QLabel(self.horizontalFrame_7)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_18)


        self.gridLayout_2.addWidget(self.horizontalFrame_7, 2, 0, 1, 1)

        self.horizontalWidget_6 = QWidget(self.mainFrame)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalWidget_6.setMinimumSize(QSize(0, 25))
        self.horizontalWidget_6.setSizeIncrement(QSize(1, 1))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_15 = QLabel(self.horizontalWidget_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_15, 0, Qt.AlignRight)

        self.label_16 = QLabel(self.horizontalWidget_6)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_16)


        self.gridLayout_2.addWidget(self.horizontalWidget_6, 2, 1, 1, 1)

        self.horizontalFrame_4 = QFrame(self.mainFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setMinimumSize(QSize(0, 25))
        self.horizontalFrame_4.setSizeIncrement(QSize(1, 1))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.horizontalFrame_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_11, 0, Qt.AlignRight)

        self.label_12 = QLabel(self.horizontalFrame_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_12)


        self.gridLayout_2.addWidget(self.horizontalFrame_4, 1, 1, 1, 1)

        self.horizontalFrame_5 = QFrame(self.mainFrame)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setMinimumSize(QSize(0, 25))
        self.horizontalFrame_5.setSizeIncrement(QSize(1, 1))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.horizontalFrame_5)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_13, 0, Qt.AlignRight)

        self.label_14 = QLabel(self.horizontalFrame_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_14)


        self.gridLayout_2.addWidget(self.horizontalFrame_5, 1, 0, 1, 1)

        self.horizontalFrame_2 = QFrame(self.mainFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(0, 25))
        self.horizontalFrame_2.setSizeIncrement(QSize(1, 1))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.horizontalFrame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_6, 0, Qt.AlignRight)

        self.label_5 = QLabel(self.horizontalFrame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.gridLayout_2.addWidget(self.horizontalFrame_2, 0, 1, 1, 1)

        self.horizontalFrame_3 = QFrame(self.mainFrame)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setMinimumSize(QSize(0, 24))
        self.horizontalFrame_3.setSizeIncrement(QSize(1, 1))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.horizontalFrame_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_9, 0, Qt.AlignRight)

        self.label_10 = QLabel(self.horizontalFrame_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_10)


        self.gridLayout_2.addWidget(self.horizontalFrame_3, 0, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnMinimumWidth(0, 1)
        self.gridLayout_2.setColumnMinimumWidth(1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.line_4 = QFrame(self.mainFrame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, -1)
        self.label_25 = QLabel(self.mainFrame)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_9.addWidget(self.label_25)

        self.label_22 = QLabel(self.mainFrame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/icons/icons/phone-gray-20.png"))

        self.horizontalLayout_9.addWidget(self.label_22)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.label_20 = QLabel(self.mainFrame)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_9.addWidget(self.label_20)

        self.label_19 = QLabel(self.mainFrame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/icons/icons/user-gray-20.png"))

        self.horizontalLayout_9.addWidget(self.label_19)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_5 = QFrame(self.mainFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 19, -1, -1)
        self.label_27 = QLabel(self.mainFrame)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.label_27, 0, Qt.AlignRight)

        self.label_26 = QLabel(self.mainFrame)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_26)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.mainFrame)


        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Form", None))
        self.label.setText(QCoreApplication.translate("window", u"\u0641\u0639\u0627\u0644", None))
        self.label_2.setText(QCoreApplication.translate("window", u"\u062a\u0635\u0648\u06cc\u0631", None))
        self.label_4.setText(QCoreApplication.translate("window", u"582", None))
        self.label_3.setText(QCoreApplication.translate("window", u"\u06a9\u062f \u0645\u0644\u06a9:", None))
        self.label_23.setText(QCoreApplication.translate("window", u"\u0645\u0644\u06a9\u0634\u0647\u0631", None))
        self.label_23.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_21.setText(QCoreApplication.translate("window", u"\u0645\u062d\u062f\u0648\u062f\u0647:", None))
        self.label_21.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_24.setText("")
        self.label_40.setText(QCoreApplication.translate("window", u"\u0645\u0644\u06a9\u0634\u0647\u0631", None))
        self.label_40.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_41.setText(QCoreApplication.translate("window", u"\u0642\u06cc\u0645\u062a \u06a9\u0644:", None))
        self.label_41.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_42.setText("")
        self.label_37.setText(QCoreApplication.translate("window", u"\u0645\u0644\u06a9\u0634\u0647\u0631", None))
        self.label_37.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_38.setText(QCoreApplication.translate("window", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u062a\u0631:", None))
        self.label_38.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_39.setText("")
        self.label_31.setText(QCoreApplication.translate("window", u"\u0645\u0644\u06a9\u0634\u0647\u0631", None))
        self.label_31.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_32.setText(QCoreApplication.translate("window", u"\u0631\u0647\u0646", None))
        self.label_32.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_33.setText("")
        self.label_34.setText(QCoreApplication.translate("window", u"\u0645\u0644\u06a9\u0634\u0647\u0631", None))
        self.label_34.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_35.setText(QCoreApplication.translate("window", u"\u0627\u062c\u0627\u0631\u0647:", None))
        self.label_35.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_36.setText("")
        self.label_17.setText(QCoreApplication.translate("window", u"250", None))
        self.label_17.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_18.setText(QCoreApplication.translate("window", u"\u062a\u0639\u062f\u0627\u062f \u0648\u0627\u062d\u062f \u062f\u0631 \u0637\u0628\u0642\u0647:", None))
        self.label_18.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_15.setText(QCoreApplication.translate("window", u"250", None))
        self.label_15.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_16.setText(QCoreApplication.translate("window", u"\u062a\u0639\u062f\u0627\u062f \u0637\u0628\u0642\u0627\u062a:", None))
        self.label_16.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_11.setText(QCoreApplication.translate("window", u"250", None))
        self.label_11.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_12.setText(QCoreApplication.translate("window", u"\u0645\u062a\u0631\u0627\u0698:", None))
        self.label_12.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_13.setText(QCoreApplication.translate("window", u"\u06f4", None))
        self.label_13.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_14.setText(QCoreApplication.translate("window", u"\u0637\u0628\u0642\u0647:", None))
        self.label_14.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_6.setText(QCoreApplication.translate("window", u"1376", None))
        self.label_6.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_5.setText(QCoreApplication.translate("window", u"\u0633\u0627\u0644 \u0633\u0627\u062e\u062a:", None))
        self.label_5.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_9.setText(QCoreApplication.translate("window", u"1376", None))
        self.label_9.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_10.setText(QCoreApplication.translate("window", u"\u0646\u0648\u0631\u06af\u06cc\u0631\u06cc", None))
        self.label_10.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
        self.label_25.setText(QCoreApplication.translate("window", u"09135668314", None))
        self.label_22.setText("")
        self.label_20.setText(QCoreApplication.translate("window", u"\u0639\u0628\u0627\u0633\u06cc", None))
        self.label_19.setText("")
        self.label_27.setText(QCoreApplication.translate("window", u"amir", None))
        self.label_27.setProperty("styleClass", QCoreApplication.translate("window", u"value", None))
        self.label_26.setText(QCoreApplication.translate("window", u"\u062b\u0628\u062a \u0634\u062f\u0647 \u062a\u0648\u0633\u0637:", None))
        self.label_26.setProperty("styleClass", QCoreApplication.translate("window", u"label", None))
    # retranslateUi


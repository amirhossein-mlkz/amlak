# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(886, 682)
        MainWindow.setStyleSheet(u"/**************************Global Font***************************/\n"
"#MainWindow,\n"
"#centralwidget{\n"
"	padding:0px;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"	/*font: auto \"Roboto\";*/\n"
"	font: auto \"IRANSansWebFaNum Medium\";\n"
"}\n"
"\n"
"/**************************QLabel***************************/\n"
"\n"
"QLabel{\n"
"	color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/**************************QScrollBar***************************/\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #D7D7D9;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    b"
                        "ackground: #F7F8FA;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #D7D7D9;\n"
"    min-width: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontro"
                        "l-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/**************************QCheckBox***************************/\n"
"\n"
"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #7892DF;\n"
"    background-color: #7892DF;\n"
"    image: url(:/icons/icons/tick.png) \n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid rgba(194, 197, 204, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"/*******"
                        "*******************QGraphicsView***************************/\n"
"\n"
"QGraphicsView{\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/**************************QLineEdit***************************/\n"
"\n"
"QLineEdit {\n"
"  	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	padding-left: 15px;\n"
"	min-height: 35px;\n"
"	min-width: 70px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/***********QSpinBox, QDoubleSpinBox, QDateEdit*************/\n"
"\n"
"QSpinBox, QDoubleSpinBox, QDateEdit\n"
"{\n"
"/*	background-color: transparent;*/\n"
"	background-color: #F7F8FA;\n"
"	border-bottom: 2px solid #D7D7D9;\n"
"	border-radius: 5px;\n"
"	font-size: 18px;\n"
"	min-height: 30px;\n"
"	min-width: 70px;\n"
"	qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled,\n"
"QDateEdit:disabled\n"
"{\n"
"	border-bottom: 2px solid #F0F0F2;\n"
"	color: rgb(120, 120, 1"
                        "20);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, \n"
"QDoubleSpinBox::up-arrow,\n"
"QDateEdit::up-arrow\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,  \n"
"QDoubleSpinBox::down-arrow,\n"
"QDateEdit::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, \n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QDateEdit::up-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled ,  \n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QDateEdit::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDateEdit::up-button\n"
"{\n"
"	border:none;\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin"
                        ";\n"
"    subcontrol-position: right;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::down-button\n"
"{\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button ,\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
"QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled,\n"
"QDateEdit::up-button:disabled,\n"
"QDateEdit::down-button:disabled\n"
"{\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus, QDateEdit:focus{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/**************************QTabWidget*************************"
                        "**/\n"
"\n"
"QTabWidget {\n"
"    background-color: #F7F8FA;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #BDBDBF;\n"
"    color: rgb(20, 20, 20);\n"
"	min-width: 100px;\n"
"    padding: 8px 16px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #D7D7D9;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #E0E4EC;\n"
"    border-top: none;\n"
"    background-color: #E0E4EC;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #E0E4EC;\n"
"    border-bottom: 2px solid #7892DF; \n"
"}\n"
"\n"
"/**************************QTableWidget***************************/\n"
"\n"
"QTableWidget {\n"
"    background-color: #F7F8FA;\n"
"	gridline-color: #D7D7D9;\n"
"	color: rgb(20, 20, 20);\n"
"	border: 2px solid #F7F8FA;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F7F8FA;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 0px;\n"
"	"
                        "border-bottom: 2px solid #BDBDBF;\n"
"	border-right: 1px solid #D7D7D9;\n"
"	font-weight: bold;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"   border-top-left-radius: 4px;\n"
"	border-left: None;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"   border-top-right-radius: 4px;\n"
"	border-right: None;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #E0E4EC;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #D7D7D9;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	\n"
"	image: url(:/icons/icons/table_sort_icon.png);\n"
"}\n"
"\n"
"/**************************QComboBox***************************/\n"
"\n"
"QComboBox\n"
"{\n"
"	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	padding-left: 15px;\n"
"	min-height: 35px;\n"
"	min-width: 70px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QComboBox:enabled{\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"	border: 2px so"
                        "lid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/down_icon_gray.png);\n"
"	width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/down_icon_black.png);\n"
"	width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: bottom right;\n"
"    width: 30px; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px; \n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    border-left: 5px solid #7892DF;\n"
"	background-color: #D7D7D9;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*********************LshowStepsFrameStyle**********************/\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]\n"
"{\n"
"	border: None;\n"
"}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QFrame\n"
"{\n"
"	border: 2px solid #7E84A2;\n"
"	min-height: 0px;\n"
"	max-height: 0px;\n"
"}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QPushButton\n"
"{\n"
"	background-color: transparent;\n"
"	border:5px solid #7E84A2;\n"
"	border-radius: 32px;\n"
"	min-width: 55px;\n"
"	max-width: 55px;\n"
"	min-height: 55px;\n"
"	max-height: 55px;\n"
"	font-size: 24px;\n"
"	color: rgb(20, 20, 20);\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"LshowStepsFrameStyle\"]  .QPushButton:hover\n"
"{\n"
"	border:5px solid #BDBDBF;\n"
"}\n"
"\n"
"/*********************sidebar menu**********************/\n"
"\n"
"*[styleClass=\"sideMenu\"]\n"
"{\n"
"	background-color: #17203A;\n"
"	min-width:150px;\n"
"}\n"
"\n"
"*[styleClass=\"sideMenu\"]  .QPushButton{\n"
"	border: 0px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	min-he"
                        "ight:40px;\n"
"	font-size:16px;\n"
"}\n"
"\n"
"*[styleClass=\"sideMenu\"]  .QPushButton:hover{\n"
"	border-right: 7px solid rgb(101, 142, 255);\n"
"}\n"
"\n"
"\n"
"/*********************DashboardMenu**********************/\n"
"\n"
"*[styleSheet=\"dashboardMenuItem\"]{\n"
"		background-color:#ffffff;\n"
"	padding:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"*[styleClass=\"dashboardMenu\"] *[styleClass=\"dashboardMenuItem\"] {\n"
"	background-color:#ffffff;\n"
"	padding:10px;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"*[styleClass=\"dashboardMenu\"]  *[styleClass=\"dashboardItemTitle\"]  {\n"
"	font-size:18px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*********************top information of building**********************/\n"
"\n"
"*[styleClass=\"buildingTopInfo\"]  .QLabel[styleClass=\"label\"]{\n"
"	font-size:12px;\n"
"	color:rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"*[styleClass=\"buildingTopInfo\"]  .QLabel[styleClass=\"value\"]{\n"
"	font-size:14px;\n"
"}\n"
"\n"
"\n"
"*[styleClass=\"buildingTopInfo\"]  .QLabel[styleClas"
                        "s=\"buildingType\"]{\n"
"	font-size:20px;\n"
"	color:rgb(12, 80, 139);\n"
"}\n"
"\n"
"/*********************top information of building**********************/\n"
"\n"
"*[styleClass=\"buildingPriceInfo\"]  .QLabel[styleClass=\"label\"]{\n"
"	font-size:12px;\n"
"	color:rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"*[styleClass=\"buildingPriceInfo\"] {\n"
"	border: 2px solid rgb(148, 148, 148);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"*[styleClass=\"buildingPriceInfo\"]  .QLabel[styleClass=\"value\"]{\n"
"	font-size:18px;\n"
"	padding-bottom:20px;\n"
"}\n"
"\n"
"/*********************building information body**********************/\n"
"QFrame[styleClass=\"buildingInfo\"]{\n"
"	background-color:white;\n"
"	border-radius: 30px;\n"
"	margin:50px;\n"
"	min-width:700px;\n"
"}\n"
"\n"
"*[styleClass=\"buildingInfo\"]  .QLabel[styleClass=\"header\"]{\n"
"	font-size:24px;\n"
"	color:rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"*[styleClass=\"buildingInfo\"]  .QLabel[styleClass=\"value\"]{\n"
"	font-size:18px;\n"
"	padding-left:5px;\n"
""
                        "}\n"
"\n"
"\n"
"*[styleClass=\"buildingInfo\"]  .QLabel[styleClass=\"label\"]{\n"
"	font-size:14px;\n"
"	color:rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"*[styleClass=\"buildingInfo\"]  QFrame[styleClass=\"sectionBody\"]{\n"
"	padding-right:30px;\n"
"}\n"
"\n"
"*[styleClass=\"buildingInfo\"]  QFrame[styleClass=\"section\"]{\n"
"	padding-bottom:80px;\n"
"}\n"
"\n"
"*[styleClass=\"buildingInfo\"] QFrame[crossCheckIcon=\"false\"]{\n"
" min-width:24px;\n"
" max-width:24px;\n"
" min-height:24px;\n"
" max-height:24px;\n"
" background:url(:/icons/icons/cross-red-24.png)  no-repeat center center;\n"
" background-size: cover;\n"
"}\n"
"\n"
"\n"
"*[styleClass=\"buildingInfo\"] QFrame[crossCheckIcon=\"true\"]{\n"
" min-width:24px;\n"
" max-width:24px;\n"
" min-height:24px;\n"
" max-height:24px;\n"
" background:url(:/icons/icons/check-green-24.png) no-repeat center center;\n"
" background-size: cover;\n"
"}\n"
"\n"
"*[styleClass=\"buildingInfo\"] QFrame[styleClass=\"section\"] QFrame[styleClass=\"seperator\"]{\n"
" min-heigh"
                        "t:1px;\n"
" max-height:1px;\n"
"background-color:rgba(0, 0, 0,20);\n"
"}\n"
"\n"
"*[styleClass=\"buildingPageTopSection\"]{\n"
" background-color:white;\n"
" border-radius:30px;\n"
"}\n"
"\n"
"\n"
"/******************* form style************************/\n"
"\n"
"\n"
"QLabel[styleClass=\"form-label\"]{\n"
" font: auto \"IRANSansWebFaNum Light\";\n"
" font-size:18px;\n"
" padding-top:40px;\n"
"}\n"
"\n"
"QPushButton[styleClass=\"form-btn\"]{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 25px;\n"
"	min-width: 120;\n"
"	max-width: 120;\n"
"	min-height: 50;\n"
"	max-height: 50;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton[styleClass=\"form-btn\"]:disable{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(189, 189, 191, 255), stop:1 rgba(189, 189, 191, 255));\n"
"	color: rgba(120, 120, 120"
                        ", 255);\n"
"}\n"
"\n"
"QPushButton[styleClass=\"form-btn\"]:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.verticalLayout_2 = QVBoxLayout(self.page_dashboard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dashboardFrame = QFrame(self.page_dashboard)
        self.dashboardFrame.setObjectName(u"dashboardFrame")
        self.dashboardFrame.setStyleSheet(u"")
        self.dashboardFrame.setFrameShape(QFrame.StyledPanel)
        self.dashboardFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.dashboardFrame)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.register_rent_building = QFrame(self.dashboardFrame)
        self.register_rent_building.setObjectName(u"register_rent_building")
        self.register_rent_building.setStyleSheet(u"dashboardMenuItem")
        self.register_rent_building.setFrameShape(QFrame.StyledPanel)
        self.register_rent_building.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.register_rent_building)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.register_rent_building)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(100, 100))
        self.label_14.setPixmap(QPixmap(u":/icons/icons/add_rent.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.register_rent_building)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.register_rent_building, 0, 0, 1, 1)

        self.all_rent_building = QFrame(self.dashboardFrame)
        self.all_rent_building.setObjectName(u"all_rent_building")
        self.all_rent_building.setFrameShape(QFrame.StyledPanel)
        self.all_rent_building.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.all_rent_building)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.all_rent_building)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 100))
        self.label_10.setPixmap(QPixmap(u":/icons/icons/all-rents.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.all_rent_building)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.all_rent_building, 1, 1, 1, 1)

        self.users = QFrame(self.dashboardFrame)
        self.users.setObjectName(u"users")
        self.users.setFrameShape(QFrame.StyledPanel)
        self.users.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.users)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.users)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(100, 100))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/all-user.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.users)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_10.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.users, 1, 0, 1, 1)

        self.register_sale_building = QFrame(self.dashboardFrame)
        self.register_sale_building.setObjectName(u"register_sale_building")
        self.register_sale_building.setStyleSheet(u"")
        self.register_sale_building.setFrameShape(QFrame.StyledPanel)
        self.register_sale_building.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.register_sale_building)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.register_sale_building)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/icons/icons/add_home.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.register_sale_building)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.register_sale_building, 0, 1, 1, 1)

        self.all_sale_building = QFrame(self.dashboardFrame)
        self.all_sale_building.setObjectName(u"all_sale_building")
        self.all_sale_building.setFrameShape(QFrame.StyledPanel)
        self.all_sale_building.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.all_sale_building)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.all_sale_building)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(100, 100))
        self.label_8.setPixmap(QPixmap(u":/icons/icons/all-sell.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.all_sale_building)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.all_sale_building, 1, 2, 1, 1)

        self.profile = QFrame(self.dashboardFrame)
        self.profile.setObjectName(u"profile")
        self.profile.setFrameShape(QFrame.StyledPanel)
        self.profile.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.profile)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_224 = QLabel(self.profile)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setMaximumSize(QSize(100, 100))
        self.label_224.setPixmap(QPixmap(u":/icons/icons/user-profiles.png"))
        self.label_224.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_224, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.profile)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.profile, 0, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 1)

        self.verticalLayout_2.addWidget(self.dashboardFrame)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_24)

        self.pages.addWidget(self.page_dashboard)
        self.page_register_property = QWidget()
        self.page_register_property.setObjectName(u"page_register_property")
        self.verticalLayout_5 = QVBoxLayout(self.page_register_property)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.page_register_property)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.page_register_property)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"LshowStepsFrameStyle")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 1, -1, -1)
        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout.addWidget(self.pushButton_19)

        self.frame_31 = QFrame(self.frame)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_31)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.frame_30 = QFrame(self.frame)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_30)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout.addWidget(self.pushButton_11)

        self.frame_29 = QFrame(self.frame)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_29)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_28)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.frame_27 = QFrame(self.frame)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_27)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.frame_26 = QFrame(self.frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_26)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.step1Line = QFrame(self.frame)
        self.step1Line.setObjectName(u"step1Line")
        self.step1Line.setFrameShape(QFrame.StyledPanel)
        self.step1Line.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.step1Line)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout_5.addWidget(self.frame)

        self.form_stackwidget = QStackedWidget(self.page_register_property)
        self.form_stackwidget.setObjectName(u"form_stackwidget")
        self.form_step1 = QWidget()
        self.form_step1.setObjectName(u"form_step1")
        self.verticalLayout_8 = QVBoxLayout(self.form_step1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 11, -1, -1)
        self.label_6 = QLabel(self.form_step1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(20)
        self.widget_6 = QWidget(self.form_step1)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout_2.addWidget(self.widget_6, 0, 1, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_22, 3, 2, 1, 1)

        self.melkCategoryInpt = QComboBox(self.form_step1)
        self.melkCategoryInpt.setObjectName(u"melkCategoryInpt")
        self.melkCategoryInpt.setMinimumSize(QSize(87, 37))

        self.gridLayout_2.addWidget(self.melkCategoryInpt, 2, 2, 1, 1)

        self.widget_5 = QWidget(self.form_step1)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)

        self.melkCategoryLbl = QLabel(self.form_step1)
        self.melkCategoryLbl.setObjectName(u"melkCategoryLbl")

        self.gridLayout_2.addWidget(self.melkCategoryLbl, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout_8.addLayout(self.gridLayout_2)

        self.form_stackwidget.addWidget(self.form_step1)
        self.form_step2 = QWidget()
        self.form_step2.setObjectName(u"form_step2")
        self.verticalLayout_11 = QVBoxLayout(self.form_step2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_34 = QLabel(self.form_step2)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_11.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(50)
        self.gridLayout_10.setVerticalSpacing(20)
        self.gridLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.regionFormLbl = QLabel(self.form_step2)
        self.regionFormLbl.setObjectName(u"regionFormLbl")

        self.gridLayout_10.addWidget(self.regionFormLbl, 0, 1, 1, 1)

        self.cityFormLbl = QLabel(self.form_step2)
        self.cityFormLbl.setObjectName(u"cityFormLbl")

        self.gridLayout_10.addWidget(self.cityFormLbl, 0, 2, 1, 1)

        self.streetFormLbl = QLabel(self.form_step2)
        self.streetFormLbl.setObjectName(u"streetFormLbl")

        self.gridLayout_10.addWidget(self.streetFormLbl, 0, 0, 1, 1)

        self.cityFormInpt = QComboBox(self.form_step2)
        self.cityFormInpt.setObjectName(u"cityFormInpt")

        self.gridLayout_10.addWidget(self.cityFormInpt, 1, 2, 1, 1)

        self.regionFormInpt = QSpinBox(self.form_step2)
        self.regionFormInpt.setObjectName(u"regionFormInpt")

        self.gridLayout_10.addWidget(self.regionFormInpt, 1, 1, 1, 1)

        self.streetFormInpt = QLineEdit(self.form_step2)
        self.streetFormInpt.setObjectName(u"streetFormInpt")

        self.gridLayout_10.addWidget(self.streetFormInpt, 1, 0, 1, 1)

        self.gridLayout_10.setColumnStretch(0, 1)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_10.setColumnStretch(2, 1)

        self.verticalLayout_11.addLayout(self.gridLayout_10)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 17, -1, -1)
        self.addressFormLbl = QLabel(self.form_step2)
        self.addressFormLbl.setObjectName(u"addressFormLbl")

        self.gridLayout_11.addWidget(self.addressFormLbl, 0, 0, 1, 1)

        self.addressFormInpt = QTextEdit(self.form_step2)
        self.addressFormInpt.setObjectName(u"addressFormInpt")

        self.gridLayout_11.addWidget(self.addressFormInpt, 1, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_11)

        self.form_stackwidget.addWidget(self.form_step2)
        self.form_step3 = QWidget()
        self.form_step3.setObjectName(u"form_step3")
        self.verticalLayout_19 = QVBoxLayout(self.form_step3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea_3 = QScrollArea(self.form_step3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 610, 948))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_49 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_20.addWidget(self.label_49, 0, Qt.AlignHCenter)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(100)
        self.gridLayout_6.setVerticalSpacing(20)
        self.owner2MobileNumberFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.owner2MobileNumberFormInpt.setObjectName(u"owner2MobileNumberFormInpt")

        self.gridLayout_6.addWidget(self.owner2MobileNumberFormInpt, 4, 1, 1, 1)

        self.owner1PhoneNumberFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.owner1PhoneNumberFormLbl.setObjectName(u"owner1PhoneNumberFormLbl")

        self.gridLayout_6.addWidget(self.owner1PhoneNumberFormLbl, 0, 0, 1, 1)

        self.guardPhoneNumberFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.guardPhoneNumberFormLbl.setObjectName(u"guardPhoneNumberFormLbl")

        self.gridLayout_6.addWidget(self.guardPhoneNumberFormLbl, 9, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_11, 2, 2, 1, 1)

        self.ownerName1FormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.ownerName1FormLbl.setObjectName(u"ownerName1FormLbl")

        self.gridLayout_6.addWidget(self.ownerName1FormLbl, 0, 2, 1, 1)

        self.tenantNameFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.tenantNameFormInpt.setObjectName(u"tenantNameFormInpt")

        self.gridLayout_6.addWidget(self.tenantNameFormInpt, 7, 2, 1, 1)

        self.ownerName1FormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ownerName1FormInpt.setObjectName(u"ownerName1FormInpt")

        self.gridLayout_6.addWidget(self.ownerName1FormInpt, 1, 2, 1, 1)

        self.guardPhoneNumberFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.guardPhoneNumberFormInpt.setObjectName(u"guardPhoneNumberFormInpt")

        self.gridLayout_6.addWidget(self.guardPhoneNumberFormInpt, 10, 1, 1, 1)

        self.guardNameFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.guardNameFormLbl.setObjectName(u"guardNameFormLbl")

        self.gridLayout_6.addWidget(self.guardNameFormLbl, 9, 2, 1, 1)

        self.ownerName2FormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.ownerName2FormLbl.setObjectName(u"ownerName2FormLbl")

        self.gridLayout_6.addWidget(self.ownerName2FormLbl, 3, 2, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_15, 5, 2, 1, 1)

        self.owner2MobileNumberFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.owner2MobileNumberFormLbl.setObjectName(u"owner2MobileNumberFormLbl")

        self.gridLayout_6.addWidget(self.owner2MobileNumberFormLbl, 3, 1, 1, 1)

        self.owner1MobileNumberFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.owner1MobileNumberFormInpt.setObjectName(u"owner1MobileNumberFormInpt")

        self.gridLayout_6.addWidget(self.owner1MobileNumberFormInpt, 1, 1, 1, 1)

        self.guardNameFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.guardNameFormInpt.setObjectName(u"guardNameFormInpt")

        self.gridLayout_6.addWidget(self.guardNameFormInpt, 10, 2, 1, 1)

        self.tenantPhoneNumberFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.tenantPhoneNumberFormInpt.setObjectName(u"tenantPhoneNumberFormInpt")

        self.gridLayout_6.addWidget(self.tenantPhoneNumberFormInpt, 7, 1, 1, 1)

        self.owner1PhoneNumberFormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.owner1PhoneNumberFormInpt.setObjectName(u"owner1PhoneNumberFormInpt")

        self.gridLayout_6.addWidget(self.owner1PhoneNumberFormInpt, 1, 0, 1, 1)

        self.ownerName2FormInpt = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ownerName2FormInpt.setObjectName(u"ownerName2FormInpt")

        self.gridLayout_6.addWidget(self.ownerName2FormInpt, 4, 2, 1, 1)

        self.tenantNameFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.tenantNameFormLbl.setObjectName(u"tenantNameFormLbl")

        self.gridLayout_6.addWidget(self.tenantNameFormLbl, 6, 2, 1, 1)

        self.owner1MobileNumberFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.owner1MobileNumberFormLbl.setObjectName(u"owner1MobileNumberFormLbl")

        self.gridLayout_6.addWidget(self.owner1MobileNumberFormLbl, 0, 1, 1, 1)

        self.tenantPhoneNumberFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.tenantPhoneNumberFormLbl.setObjectName(u"tenantPhoneNumberFormLbl")

        self.gridLayout_6.addWidget(self.tenantPhoneNumberFormLbl, 6, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_16, 8, 2, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 1)

        self.verticalLayout_20.addLayout(self.gridLayout_6)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 25, -1, -1)
        self.ownerDescriptionFormLbl = QLabel(self.scrollAreaWidgetContents_3)
        self.ownerDescriptionFormLbl.setObjectName(u"ownerDescriptionFormLbl")

        self.verticalLayout_21.addWidget(self.ownerDescriptionFormLbl)

        self.ownerDescriptionFormInpt = QTextEdit(self.scrollAreaWidgetContents_3)
        self.ownerDescriptionFormInpt.setObjectName(u"ownerDescriptionFormInpt")

        self.verticalLayout_21.addWidget(self.ownerDescriptionFormInpt)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_19.addWidget(self.scrollArea_3)

        self.form_stackwidget.addWidget(self.form_step3)
        self.form_step4 = QWidget()
        self.form_step4.setObjectName(u"form_step4")
        self.verticalLayout_12 = QVBoxLayout(self.form_step4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.form_step4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 662, 1597))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_14.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(100)
        self.gridLayout_8.setVerticalSpacing(20)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"label")

        self.gridLayout_8.addWidget(self.label_21, 0, 2, 1, 1)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_8.addWidget(self.widget_2, 0, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_8.addWidget(self.spinBox_3, 1, 2, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnStretch(2, 1)

        self.verticalLayout_14.addLayout(self.gridLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.price_for_sell_frame = QFrame(self.scrollAreaWidgetContents)
        self.price_for_sell_frame.setObjectName(u"price_for_sell_frame")
        self.gridLayout_5 = QGridLayout(self.price_for_sell_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(100)
        self.gridLayout_5.setVerticalSpacing(20)
        self.label_23 = QLabel(self.price_for_sell_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"label")

        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_20 = QLabel(self.price_for_sell_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"label")

        self.gridLayout_5.addWidget(self.label_20, 0, 2, 1, 1)

        self.label_22 = QLabel(self.price_for_sell_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"label")

        self.gridLayout_5.addWidget(self.label_22, 0, 1, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, 20, -1)
        self.radioButton_2 = QRadioButton(self.price_for_sell_frame)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_15.addWidget(self.radioButton_2, 0, Qt.AlignLeft)

        self.radioButton = QRadioButton(self.price_for_sell_frame)
        self.buttonGroup_2.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_15.addWidget(self.radioButton, 0, Qt.AlignLeft)


        self.gridLayout_5.addLayout(self.verticalLayout_15, 1, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.price_for_sell_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.price_for_sell_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)

        self.verticalLayout_13.addWidget(self.price_for_sell_frame)

        self.price_for_rent_frame = QFrame(self.scrollAreaWidgetContents)
        self.price_for_rent_frame.setObjectName(u"price_for_rent_frame")
        self.gridLayout_9 = QGridLayout(self.price_for_rent_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(100)
        self.gridLayout_9.setVerticalSpacing(20)
        self.gridLayout_9.setContentsMargins(-1, 1, -1, -1)
        self.label_24 = QLabel(self.price_for_rent_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"label")

        self.gridLayout_9.addWidget(self.label_24, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.price_for_rent_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_9.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        self.label_25 = QLabel(self.price_for_rent_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"label")

        self.gridLayout_9.addWidget(self.label_25, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.price_for_rent_frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_9.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.widget = QWidget(self.price_for_rent_frame)
        self.widget.setObjectName(u"widget")

        self.gridLayout_9.addWidget(self.widget, 1, 0, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 1)

        self.verticalLayout_13.addWidget(self.price_for_rent_frame)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_7.setHorizontalSpacing(100)
        self.gridLayout_7.setVerticalSpacing(20)
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 20, -1)
        self.radioButton_5 = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_16.addWidget(self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_16.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_16.addWidget(self.radioButton_3)


        self.gridLayout_7.addLayout(self.verticalLayout_16, 10, 2, 1, 1)

        self.spinBox_7 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.gridLayout_7.addWidget(self.spinBox_7, 7, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.gridLayout_7.addWidget(self.textEdit_4, 13, 1, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_28, 0, 0, 1, 1, Qt.AlignRight)

        self.label_31 = QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_31, 6, 1, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_32, 6, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_30, 6, 2, 1, 1)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_42, 13, 2, 1, 1)

        self.spinBox_4 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_7.addWidget(self.spinBox_4, 4, 2, 1, 1)

        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_33, 9, 2, 1, 1)

        self.spinBox_5 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_7.addWidget(self.spinBox_5, 7, 2, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_27, 0, 1, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_26, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 8, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_7.addWidget(self.comboBox_4, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.spinBox_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_7.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.spinBox_6 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_7.addWidget(self.spinBox_6, 7, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_7.addWidget(self.comboBox_3, 1, 2, 1, 1)

        self.label_134 = QLabel(self.scrollAreaWidgetContents)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_134, 12, 2, 1, 1)

        self.label_181 = QLabel(self.scrollAreaWidgetContents)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_181, 12, 1, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"label")

        self.gridLayout_7.addWidget(self.label_29, 3, 2, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_25, 11, 2, 1, 1)

        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.gridLayout_7.setColumnStretch(2, 1)

        self.verticalLayout_14.addLayout(self.gridLayout_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.form_stackwidget.addWidget(self.form_step4)
        self.form_step5 = QWidget()
        self.form_step5.setObjectName(u"form_step5")
        self.verticalLayout_17 = QVBoxLayout(self.form_step5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea_2 = QScrollArea(self.form_step5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 636, 1393))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))
        self.label_35.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_18.addWidget(self.label_35, 0, Qt.AlignHCenter)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(100)
        self.gridLayout_3.setVerticalSpacing(20)
        self.spinBox_9 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.gridLayout_3.addWidget(self.spinBox_9, 4, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 11, 2, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_6, 13, 2, 1, 1)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_3.addWidget(self.comboBox_5, 1, 0, 1, 1)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_3.addWidget(self.label_37, 0, 0, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_3.addWidget(self.label_48, 18, 2, 1, 1)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_3.addWidget(self.label_43, 9, 2, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_3.addWidget(self.label_41, 6, 1, 1, 1)

        self.label_50 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_3.addWidget(self.label_50, 18, 1, 1, 1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_3, 1, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 17, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_9, 5, 2, 1, 1)

        self.spinBox_12 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_12.setObjectName(u"spinBox_12")

        self.gridLayout_3.addWidget(self.spinBox_12, 13, 1, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 3, 2, 1, 1)

        self.spinBox_11 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_11.setObjectName(u"spinBox_11")

        self.gridLayout_3.addWidget(self.spinBox_11, 10, 1, 1, 1)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_3.addWidget(self.label_44, 9, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 2, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_10, 8, 2, 1, 1)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_3.addWidget(self.label_38, 0, 2, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_3.addWidget(self.label_36, 0, 1, 1, 1)

        self.label_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_3.addWidget(self.label_47, 15, 2, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_3.addWidget(self.label_45, 12, 2, 1, 1)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 3, 1, 1, 1)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_8, 19, 2, 1, 1)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_7, 16, 2, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_4, 7, 2, 1, 1)

        self.spinBox_10 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.gridLayout_3.addWidget(self.spinBox_10, 7, 1, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_2, 4, 2, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_3.addWidget(self.label_42, 6, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_12, 14, 2, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_5, 10, 2, 1, 1)

        self.spinBox_8 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.gridLayout_3.addWidget(self.spinBox_8, 1, 1, 1, 1)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_3.addWidget(self.label_46, 12, 1, 1, 1)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_9, 19, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.verticalLayout_18.addLayout(self.gridLayout_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_17.addWidget(self.scrollArea_2)

        self.form_stackwidget.addWidget(self.form_step5)
        self.form_step6 = QWidget()
        self.form_step6.setObjectName(u"form_step6")
        self.verticalLayout_22 = QVBoxLayout(self.form_step6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.scrollArea_4 = QScrollArea(self.form_step6)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 586, 1345))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_51 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_23.addWidget(self.label_51)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(100)
        self.gridLayout_12.setVerticalSpacing(20)
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_17, 5, 1, 1, 1)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_12, 1, 0, 1, 1)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_12.addWidget(self.label_71, 12, 1, 1, 1)

        self.lineEdit_22 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_12.addWidget(self.lineEdit_22, 6, 0, 1, 1)

        self.label_66 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_12.addWidget(self.label_66, 8, 2, 1, 1)

        self.lineEdit_25 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_12.addWidget(self.lineEdit_25, 15, 2, 1, 1)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_12.addWidget(self.lineEdit_15, 2, 2, 1, 1)

        self.lineEdit_23 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_12.addWidget(self.lineEdit_23, 10, 2, 1, 1)

        self.label_64 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_12.addWidget(self.label_64, 0, 1, 1, 1)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 50))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_22, 13, 1, 1, 1)

        self.frame_19 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_19, 9, 2, 1, 1)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_11, 1, 1, 1, 1)

        self.lineEdit_28 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.gridLayout_12.addWidget(self.lineEdit_28, 18, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_17, 7, 2, 1, 1)

        self.label_72 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_12.addWidget(self.label_72, 12, 2, 1, 1)

        self.lineEdit_27 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_12.addWidget(self.lineEdit_27, 18, 2, 1, 1)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_10, 1, 2, 1, 1)

        self.lineEdit_26 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_12.addWidget(self.lineEdit_26, 15, 1, 1, 1)

        self.label_65 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_12.addWidget(self.label_65, 8, 1, 1, 1)

        self.label_74 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_12.addWidget(self.label_74, 16, 2, 1, 1)

        self.label_73 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_12.addWidget(self.label_73, 16, 1, 1, 1)

        self.label_62 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_12.addWidget(self.label_62, 0, 2, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_18, 11, 2, 1, 1)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_20, 9, 1, 1, 1)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_18, 5, 0, 1, 1)

        self.label_68 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_12.addWidget(self.label_68, 4, 1, 1, 1)

        self.label_63 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_12.addWidget(self.label_63, 0, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_14, 3, 2, 1, 1)

        self.frame_23 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 50))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_23, 17, 2, 1, 1)

        self.lineEdit_24 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_12.addWidget(self.lineEdit_24, 10, 1, 1, 1)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_16, 5, 2, 1, 1)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_12.addWidget(self.lineEdit_19, 2, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_12.addWidget(self.lineEdit_20, 6, 2, 1, 1)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_24, 17, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_12.addWidget(self.lineEdit_16, 2, 1, 1, 1)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 50))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_21, 13, 2, 1, 1)

        self.lineEdit_21 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_12.addWidget(self.lineEdit_21, 6, 1, 1, 1)

        self.label_69 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_12.addWidget(self.label_69, 4, 2, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_19, 14, 2, 1, 1)

        self.gridLayout_12.setColumnStretch(0, 1)
        self.gridLayout_12.setColumnStretch(1, 1)
        self.gridLayout_12.setColumnStretch(2, 1)
        self.gridLayout_12.setColumnMinimumWidth(0, 100)
        self.gridLayout_12.setColumnMinimumWidth(1, 100)
        self.gridLayout_12.setColumnMinimumWidth(2, 100)

        self.verticalLayout_23.addLayout(self.gridLayout_12)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_22.addWidget(self.scrollArea_4)

        self.form_stackwidget.addWidget(self.form_step6)
        self.form_step7 = QWidget()
        self.form_step7.setObjectName(u"form_step7")
        self.verticalLayout_24 = QVBoxLayout(self.form_step7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_67 = QLabel(self.form_step7)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_24.addWidget(self.label_67, 0, Qt.AlignHCenter)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(100)
        self.gridLayout_14.setVerticalSpacing(20)
        self.widget_3 = QWidget(self.form_step7)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout_14.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.form_step7)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout_14.addWidget(self.widget_4, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.form_step7)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_14.addWidget(self.pushButton_4, 4, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.form_step7)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_14.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.label_88 = QLabel(self.form_step7)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_14.addWidget(self.label_88, 0, 2, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_20, 5, 2, 1, 1)

        self.label_89 = QLabel(self.form_step7)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_14.addWidget(self.label_89, 3, 2, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_21, 2, 2, 1, 1)

        self.gridLayout_14.setColumnStretch(0, 1)
        self.gridLayout_14.setColumnStretch(1, 1)
        self.gridLayout_14.setColumnStretch(2, 1)

        self.verticalLayout_24.addLayout(self.gridLayout_14)

        self.form_stackwidget.addWidget(self.form_step7)
        self.form_step8 = QWidget()
        self.form_step8.setObjectName(u"form_step8")
        self.verticalLayout_25 = QVBoxLayout(self.form_step8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_70 = QLabel(self.form_step8)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_25.addWidget(self.label_70, 0, Qt.AlignHCenter)

        self.label_90 = QLabel(self.form_step8)
        self.label_90.setObjectName(u"label_90")

        self.verticalLayout_25.addWidget(self.label_90)

        self.textEdit_3 = QTextEdit(self.form_step8)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout_25.addWidget(self.textEdit_3)

        self.form_stackwidget.addWidget(self.form_step8)

        self.verticalLayout_5.addWidget(self.form_stackwidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 16, -1, -1)
        self.pushButton_2 = QPushButton(self.page_register_property)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_2.addItem(self.verticalSpacer_6)

        self.pushButton = QPushButton(self.page_register_property)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.pages.addWidget(self.page_register_property)
        self.page_estate = QWidget()
        self.page_estate.setObjectName(u"page_estate")
        self.verticalLayout_26 = QVBoxLayout(self.page_estate)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_5 = QScrollArea(self.page_estate)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 818, 3178))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_93 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"font-size:24px;\n"
"font-weight:bold;")

        self.verticalLayout_27.addWidget(self.label_93)

        self.label_92 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"QLabel[buildingState]{\n"
"font-size:18px;\n"
"}\n"
"\n"
"QLabel[buildingState=\"0\"]{\n"
"	color:rgb(58, 209, 154);\n"
"}\n"
"\n"
"QLabel[buildingState=\"1\"]{\n"
"	color: rgb(255, 191, 0);\n"
"}\n"
"\n"
"QLabel[buildingState=\"2\"]{\n"
"	color:rgb(197, 63, 59);\n"
"}")
        self.label_92.setProperty("buildingState", 2)

        self.verticalLayout_27.addWidget(self.label_92)

        self.horizontalFrame = QFrame(self.scrollAreaWidgetContents_5)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.BuildingInfoTop = QHBoxLayout(self.horizontalFrame)
        self.BuildingInfoTop.setObjectName(u"BuildingInfoTop")
        self.BuildingInfoTop.setContentsMargins(26, -1, -1, -1)
        self.priceBoxFrame = QFrame(self.horizontalFrame)
        self.priceBoxFrame.setObjectName(u"priceBoxFrame")
        self.priceBoxFrame.setMinimumSize(QSize(0, 0))
        self.priceBoxFrame.setMaximumSize(QSize(250, 16777215))
        self.priceBoxFrame.setStyleSheet(u"")
        self.priceBoxFrame.setFrameShape(QFrame.StyledPanel)
        self.priceBoxFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.priceBoxFrame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_135 = QLabel(self.priceBoxFrame)
        self.label_135.setObjectName(u"label_135")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy)
        self.label_135.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_135, 0, Qt.AlignHCenter)

        self.label_136 = QLabel(self.priceBoxFrame)
        self.label_136.setObjectName(u"label_136")
        sizePolicy.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy)
        self.label_136.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_136, 0, Qt.AlignHCenter)

        self.label_137 = QLabel(self.priceBoxFrame)
        self.label_137.setObjectName(u"label_137")
        sizePolicy.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy)
        self.label_137.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_137, 0, Qt.AlignHCenter)

        self.label_138 = QLabel(self.priceBoxFrame)
        self.label_138.setObjectName(u"label_138")
        sizePolicy.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy)
        self.label_138.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_138, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_140 = QLabel(self.priceBoxFrame)
        self.label_140.setObjectName(u"label_140")
        sizePolicy.setHeightForWidth(self.label_140.sizePolicy().hasHeightForWidth())
        self.label_140.setSizePolicy(sizePolicy)
        self.label_140.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_140, 0, Qt.AlignHCenter)

        self.label_139 = QLabel(self.priceBoxFrame)
        self.label_139.setObjectName(u"label_139")
        sizePolicy.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy)
        self.label_139.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_139, 0, Qt.AlignHCenter)

        self.label_142 = QLabel(self.priceBoxFrame)
        self.label_142.setObjectName(u"label_142")
        sizePolicy.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy)
        self.label_142.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_142, 0, Qt.AlignHCenter)

        self.label_141 = QLabel(self.priceBoxFrame)
        self.label_141.setObjectName(u"label_141")
        sizePolicy.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy)
        self.label_141.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_141, 0, Qt.AlignHCenter)


        self.BuildingInfoTop.addWidget(self.priceBoxFrame)

        self.frame_40 = QFrame(self.horizontalFrame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_40)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_94 = QLabel(self.frame_40)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.label_94)

        self.line = QFrame(self.frame_40)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.label_96 = QLabel(self.frame_40)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_96, 0, Qt.AlignRight)

        self.label_95 = QLabel(self.frame_40)
        self.label_95.setObjectName(u"label_95")
        sizePolicy.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy)
        self.label_95.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_95)


        self.verticalLayout_28.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, 0, 0)
        self.label_105 = QLabel(self.frame_40)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_40)
        self.label_106.setObjectName(u"label_106")
        sizePolicy.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy)
        self.label_106.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_106)


        self.verticalLayout_28.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.label_133 = QLabel(self.frame_40)
        self.label_133.setObjectName(u"label_133")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy1)
        self.label_133.setStyleSheet(u"title")

        self.horizontalLayout_14.addWidget(self.label_133)

        self.label_107 = QLabel(self.frame_40)
        self.label_107.setObjectName(u"label_107")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy2)
        self.label_107.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_40)
        self.label_108.setObjectName(u"label_108")
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)
        self.label_108.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_108)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, 0, 0)
        self.label_109 = QLabel(self.frame_40)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_109, 0, Qt.AlignRight)

        self.label_110 = QLabel(self.frame_40)
        self.label_110.setObjectName(u"label_110")
        sizePolicy.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy)
        self.label_110.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_110)


        self.verticalLayout_28.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, 0, 0)
        self.label_129 = QLabel(self.frame_40)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.label_129)

        self.label_130 = QLabel(self.frame_40)
        self.label_130.setObjectName(u"label_130")
        sizePolicy.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy)
        self.label_130.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.label_130)


        self.verticalLayout_28.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, 0, 0)
        self.label_131 = QLabel(self.frame_40)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.label_131)

        self.label_132 = QLabel(self.frame_40)
        self.label_132.setObjectName(u"label_132")
        sizePolicy.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy)
        self.label_132.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.label_132)


        self.verticalLayout_28.addLayout(self.horizontalLayout_25)


        self.BuildingInfoTop.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.horizontalFrame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.BuildingInfoTop.addWidget(self.frame_39)

        self.BuildingInfoTop.setStretch(0, 1)
        self.BuildingInfoTop.setStretch(1, 1)
        self.BuildingInfoTop.setStretch(2, 1)

        self.verticalLayout_27.addWidget(self.horizontalFrame)

        self.buildingInfoFrame = QFrame(self.scrollAreaWidgetContents_5)
        self.buildingInfoFrame.setObjectName(u"buildingInfoFrame")
        self.buildingInfoFrame.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.buildingInfoFrame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.ownerInfoFrame_2 = QFrame(self.buildingInfoFrame)
        self.ownerInfoFrame_2.setObjectName(u"ownerInfoFrame_2")
        self.ownerInfoFrame_2.setStyleSheet(u"")
        self.ownerInfoFrame_2.setFrameShape(QFrame.StyledPanel)
        self.ownerInfoFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.ownerInfoFrame_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.ownerInfoFrame = QFrame(self.ownerInfoFrame_2)
        self.ownerInfoFrame.setObjectName(u"ownerInfoFrame")
        self.ownerInfoFrame.setStyleSheet(u"")
        self.ownerInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.ownerInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.ownerInfoFrame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.ownerInfoTitle = QLabel(self.ownerInfoFrame)
        self.ownerInfoTitle.setObjectName(u"ownerInfoTitle")
        self.ownerInfoTitle.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.ownerInfoTitle)

        self.ownerInfoBodyFrame = QFrame(self.ownerInfoFrame)
        self.ownerInfoBodyFrame.setObjectName(u"ownerInfoBodyFrame")
        self.ownerInfoBodyFrame.setStyleSheet(u"")
        self.ownerInfoBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.ownerInfoBodyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.ownerInfoBodyFrame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(50)
        self.gridLayout_15.setVerticalSpacing(20)
        self.gridLayout_15.setContentsMargins(24, -1, -1, 25)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_151 = QLabel(self.ownerInfoBodyFrame)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.label_151)

        self.label_152 = QLabel(self.ownerInfoBodyFrame)
        self.label_152.setObjectName(u"label_152")
        sizePolicy2.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy2)
        self.label_152.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.label_152)


        self.gridLayout_15.addLayout(self.horizontalLayout_31, 1, 2, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_146 = QLabel(self.ownerInfoBodyFrame)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.label_146)

        self.label_145 = QLabel(self.ownerInfoBodyFrame)
        self.label_145.setObjectName(u"label_145")
        sizePolicy2.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy2)
        self.label_145.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.label_145)


        self.gridLayout_15.addLayout(self.horizontalLayout_27, 0, 2, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_155 = QLabel(self.ownerInfoBodyFrame)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setStyleSheet(u"")

        self.horizontalLayout_33.addWidget(self.label_155)

        self.label_156 = QLabel(self.ownerInfoBodyFrame)
        self.label_156.setObjectName(u"label_156")
        sizePolicy2.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy2)
        self.label_156.setStyleSheet(u"")

        self.horizontalLayout_33.addWidget(self.label_156)


        self.gridLayout_15.addLayout(self.horizontalLayout_33, 2, 2, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_159 = QLabel(self.ownerInfoBodyFrame)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setStyleSheet(u"")

        self.horizontalLayout_35.addWidget(self.label_159)

        self.label_160 = QLabel(self.ownerInfoBodyFrame)
        self.label_160.setObjectName(u"label_160")
        sizePolicy2.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy2)
        self.label_160.setStyleSheet(u"")

        self.horizontalLayout_35.addWidget(self.label_160)


        self.gridLayout_15.addLayout(self.horizontalLayout_35, 3, 2, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_148 = QLabel(self.ownerInfoBodyFrame)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.label_148, 0, Qt.AlignRight)

        self.label_147 = QLabel(self.ownerInfoBodyFrame)
        self.label_147.setObjectName(u"label_147")
        sizePolicy2.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy2)
        self.label_147.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.label_147)


        self.gridLayout_15.addLayout(self.horizontalLayout_29, 0, 1, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_153 = QLabel(self.ownerInfoBodyFrame)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setStyleSheet(u"")

        self.horizontalLayout_32.addWidget(self.label_153, 0, Qt.AlignRight)

        self.label_154 = QLabel(self.ownerInfoBodyFrame)
        self.label_154.setObjectName(u"label_154")
        sizePolicy2.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy2)
        self.label_154.setStyleSheet(u"")

        self.horizontalLayout_32.addWidget(self.label_154)


        self.gridLayout_15.addLayout(self.horizontalLayout_32, 1, 1, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_161 = QLabel(self.ownerInfoBodyFrame)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.label_161, 0, Qt.AlignRight)

        self.label_162 = QLabel(self.ownerInfoBodyFrame)
        self.label_162.setObjectName(u"label_162")
        sizePolicy2.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy2)
        self.label_162.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.label_162)


        self.gridLayout_15.addLayout(self.horizontalLayout_36, 3, 1, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_157 = QLabel(self.ownerInfoBodyFrame)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.label_157, 0, Qt.AlignRight)

        self.label_158 = QLabel(self.ownerInfoBodyFrame)
        self.label_158.setObjectName(u"label_158")
        sizePolicy2.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy2)
        self.label_158.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.label_158)


        self.gridLayout_15.addLayout(self.horizontalLayout_34, 2, 1, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_163 = QLabel(self.ownerInfoBodyFrame)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.label_163, 0, Qt.AlignRight)

        self.label_164 = QLabel(self.ownerInfoBodyFrame)
        self.label_164.setObjectName(u"label_164")
        sizePolicy2.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy2)
        self.label_164.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.label_164)


        self.gridLayout_15.addLayout(self.horizontalLayout_37, 0, 0, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_15)

        self.label_143 = QLabel(self.ownerInfoBodyFrame)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"label")

        self.verticalLayout_34.addWidget(self.label_143)

        self.label_144 = QLabel(self.ownerInfoBodyFrame)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setStyleSheet(u"")
        self.label_144.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.label_144)


        self.verticalLayout_33.addWidget(self.ownerInfoBodyFrame)


        self.verticalLayout_35.addWidget(self.ownerInfoFrame)


        self.verticalLayout_32.addWidget(self.ownerInfoFrame_2)

        self.FurtherInfoFrame = QFrame(self.buildingInfoFrame)
        self.FurtherInfoFrame.setObjectName(u"FurtherInfoFrame")
        self.FurtherInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.FurtherInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.FurtherInfoFrame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.FurtherInfoTitle = QLabel(self.FurtherInfoFrame)
        self.FurtherInfoTitle.setObjectName(u"FurtherInfoTitle")
        self.FurtherInfoTitle.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.FurtherInfoTitle)

        self.FurtherInfoBodyFrame = QFrame(self.FurtherInfoFrame)
        self.FurtherInfoBodyFrame.setObjectName(u"FurtherInfoBodyFrame")
        self.FurtherInfoBodyFrame.setStyleSheet(u"")
        self.FurtherInfoBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.FurtherInfoBodyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.FurtherInfoBodyFrame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(50)
        self.gridLayout_16.setVerticalSpacing(20)
        self.gridLayout_16.setContentsMargins(24, -1, -1, 25)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_165 = QLabel(self.FurtherInfoBodyFrame)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.label_165, 0, Qt.AlignRight)

        self.label_166 = QLabel(self.FurtherInfoBodyFrame)
        self.label_166.setObjectName(u"label_166")
        sizePolicy2.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy2)
        self.label_166.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.label_166)


        self.gridLayout_16.addLayout(self.horizontalLayout_38, 1, 2, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_167 = QLabel(self.FurtherInfoBodyFrame)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setStyleSheet(u"value")

        self.horizontalLayout_39.addWidget(self.label_167, 0, Qt.AlignRight)

        self.label_168 = QLabel(self.FurtherInfoBodyFrame)
        self.label_168.setObjectName(u"label_168")
        sizePolicy2.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy2)
        self.label_168.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.label_168)


        self.gridLayout_16.addLayout(self.horizontalLayout_39, 0, 2, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_169 = QLabel(self.FurtherInfoBodyFrame)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setStyleSheet(u"")

        self.horizontalLayout_40.addWidget(self.label_169)

        self.label_170 = QLabel(self.FurtherInfoBodyFrame)
        self.label_170.setObjectName(u"label_170")
        sizePolicy2.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy2)
        self.label_170.setStyleSheet(u"")

        self.horizontalLayout_40.addWidget(self.label_170)


        self.gridLayout_16.addLayout(self.horizontalLayout_40, 2, 2, 1, 1)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_171 = QLabel(self.FurtherInfoBodyFrame)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.label_171)

        self.label_172 = QLabel(self.FurtherInfoBodyFrame)
        self.label_172.setObjectName(u"label_172")
        sizePolicy2.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy2)
        self.label_172.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.label_172)


        self.gridLayout_16.addLayout(self.horizontalLayout_41, 3, 2, 1, 1)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_173 = QLabel(self.FurtherInfoBodyFrame)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.label_173, 0, Qt.AlignRight)

        self.label_174 = QLabel(self.FurtherInfoBodyFrame)
        self.label_174.setObjectName(u"label_174")
        sizePolicy2.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy2)
        self.label_174.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.label_174)


        self.gridLayout_16.addLayout(self.horizontalLayout_42, 0, 1, 1, 1)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_175 = QLabel(self.FurtherInfoBodyFrame)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setStyleSheet(u"")

        self.horizontalLayout_43.addWidget(self.label_175, 0, Qt.AlignRight)

        self.label_176 = QLabel(self.FurtherInfoBodyFrame)
        self.label_176.setObjectName(u"label_176")
        sizePolicy2.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy2)
        self.label_176.setStyleSheet(u"")

        self.horizontalLayout_43.addWidget(self.label_176)


        self.gridLayout_16.addLayout(self.horizontalLayout_43, 1, 1, 1, 1)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")

        self.gridLayout_16.addLayout(self.horizontalLayout_46, 0, 0, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_16)

        self.label_183 = QLabel(self.FurtherInfoBodyFrame)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setStyleSheet(u"label")

        self.verticalLayout_36.addWidget(self.label_183)

        self.label_184 = QLabel(self.FurtherInfoBodyFrame)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setStyleSheet(u"")
        self.label_184.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_184)


        self.verticalLayout_41.addWidget(self.FurtherInfoBodyFrame)


        self.verticalLayout_32.addWidget(self.FurtherInfoFrame)

        self.facilitiesInfoFrame = QFrame(self.buildingInfoFrame)
        self.facilitiesInfoFrame.setObjectName(u"facilitiesInfoFrame")
        self.facilitiesInfoFrame.setStyleSheet(u"")
        self.facilitiesInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.facilitiesInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.facilitiesInfoFrame)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.ownerInfoTitle_4 = QLabel(self.facilitiesInfoFrame)
        self.ownerInfoTitle_4.setObjectName(u"ownerInfoTitle_4")
        self.ownerInfoTitle_4.setStyleSheet(u"")

        self.verticalLayout_39.addWidget(self.ownerInfoTitle_4)

        self.facilitiesInfoBodyFrame = QFrame(self.facilitiesInfoFrame)
        self.facilitiesInfoBodyFrame.setObjectName(u"facilitiesInfoBodyFrame")
        self.facilitiesInfoBodyFrame.setStyleSheet(u"")
        self.facilitiesInfoBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.facilitiesInfoBodyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.facilitiesInfoBodyFrame)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(50)
        self.gridLayout_18.setVerticalSpacing(20)
        self.gridLayout_18.setContentsMargins(24, -1, -1, 25)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_180 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setStyleSheet(u"value")

        self.horizontalLayout_61.addWidget(self.label_180, 0, Qt.AlignRight)

        self.frame_44 = QFrame(self.facilitiesInfoBodyFrame)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(26, 26))
        self.frame_44.setMaximumSize(QSize(26, 26))
        self.frame_44.setStyleSheet(u"/*iconState*/\n"
"\n"
"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.frame_44.setProperty("crossCheckIcon", False)

        self.horizontalLayout_61.addWidget(self.frame_44)


        self.gridLayout_18.addLayout(self.horizontalLayout_61, 1, 2, 1, 1)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_208 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setStyleSheet(u"")

        self.horizontalLayout_58.addWidget(self.label_208, 0, Qt.AlignRight)

        self.label_209 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_209.setObjectName(u"label_209")
        sizePolicy2.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy2)
        self.label_209.setStyleSheet(u"")

        self.horizontalLayout_58.addWidget(self.label_209)


        self.gridLayout_18.addLayout(self.horizontalLayout_58, 0, 1, 1, 1)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_214 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setStyleSheet(u"value")

        self.horizontalLayout_66.addWidget(self.label_214, 0, Qt.AlignRight)

        self.frame_49 = QFrame(self.facilitiesInfoBodyFrame)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(26, 26))
        self.frame_49.setMaximumSize(QSize(26, 26))
        self.frame_49.setStyleSheet(u"/*iconState*/\n"
"\n"
"")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.frame_49.setProperty("crossCheckIcon", False)

        self.horizontalLayout_66.addWidget(self.frame_49)


        self.gridLayout_18.addLayout(self.horizontalLayout_66, 3, 2, 1, 1)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_182 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setStyleSheet(u"value")

        self.horizontalLayout_62.addWidget(self.label_182, 0, Qt.AlignRight)

        self.frame_45 = QFrame(self.facilitiesInfoBodyFrame)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(26, 26))
        self.frame_45.setMaximumSize(QSize(26, 26))
        self.frame_45.setStyleSheet(u"/*iconState*/\n"
"\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.frame_45.setProperty("crossCheckIcon", False)

        self.horizontalLayout_62.addWidget(self.frame_45)


        self.gridLayout_18.addLayout(self.horizontalLayout_62, 2, 2, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_179 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setStyleSheet(u"value")

        self.horizontalLayout_45.addWidget(self.label_179, 0, Qt.AlignRight)

        self.frame_43 = QFrame(self.facilitiesInfoBodyFrame)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(26, 26))
        self.frame_43.setMaximumSize(QSize(26, 26))
        self.frame_43.setStyleSheet(u"/*iconState*/\n"
"\n"
"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.frame_43.setProperty("crossCheckIcon", True)

        self.horizontalLayout_45.addWidget(self.frame_43)


        self.gridLayout_18.addLayout(self.horizontalLayout_45, 0, 2, 1, 1)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_210 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setStyleSheet(u"")

        self.horizontalLayout_59.addWidget(self.label_210, 0, Qt.AlignRight)

        self.label_211 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_211.setObjectName(u"label_211")
        sizePolicy2.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy2)
        self.label_211.setStyleSheet(u"")

        self.horizontalLayout_59.addWidget(self.label_211)


        self.gridLayout_18.addLayout(self.horizontalLayout_59, 1, 1, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_216 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setStyleSheet(u"")

        self.horizontalLayout_68.addWidget(self.label_216, 0, Qt.AlignRight)

        self.label_217 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_217.setObjectName(u"label_217")
        sizePolicy2.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy2)
        self.label_217.setStyleSheet(u"")

        self.horizontalLayout_68.addWidget(self.label_217)


        self.horizontalLayout_60.addLayout(self.horizontalLayout_68)


        self.gridLayout_18.addLayout(self.horizontalLayout_60, 0, 0, 1, 1)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_215 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setStyleSheet(u"value")

        self.horizontalLayout_67.addWidget(self.label_215, 0, Qt.AlignRight)

        self.frame_50 = QFrame(self.facilitiesInfoBodyFrame)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(26, 26))
        self.frame_50.setMaximumSize(QSize(26, 26))
        self.frame_50.setStyleSheet(u"/*iconState*/\n"
"\n"
"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.frame_50.setProperty("crossCheckIcon", False)

        self.horizontalLayout_67.addWidget(self.frame_50)


        self.gridLayout_18.addLayout(self.horizontalLayout_67, 4, 2, 1, 1)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_218 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setStyleSheet(u"")

        self.horizontalLayout_69.addWidget(self.label_218, 0, Qt.AlignRight)

        self.label_219 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_219.setObjectName(u"label_219")
        sizePolicy2.setHeightForWidth(self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy2)
        self.label_219.setStyleSheet(u"")

        self.horizontalLayout_69.addWidget(self.label_219)


        self.gridLayout_18.addLayout(self.horizontalLayout_69, 2, 1, 1, 1)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_220 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setStyleSheet(u"")

        self.horizontalLayout_70.addWidget(self.label_220, 0, Qt.AlignRight)

        self.label_221 = QLabel(self.facilitiesInfoBodyFrame)
        self.label_221.setObjectName(u"label_221")
        sizePolicy2.setHeightForWidth(self.label_221.sizePolicy().hasHeightForWidth())
        self.label_221.setSizePolicy(sizePolicy2)
        self.label_221.setStyleSheet(u"")

        self.horizontalLayout_70.addWidget(self.label_221)


        self.gridLayout_18.addLayout(self.horizontalLayout_70, 3, 1, 1, 1)

        self.gridLayout_18.setColumnStretch(0, 1)
        self.gridLayout_18.setColumnStretch(1, 1)
        self.gridLayout_18.setColumnStretch(2, 1)

        self.verticalLayout_40.addLayout(self.gridLayout_18)


        self.verticalLayout_39.addWidget(self.facilitiesInfoBodyFrame)


        self.verticalLayout_32.addWidget(self.facilitiesInfoFrame)

        self.otherFacilitiesInfoFrame = QFrame(self.buildingInfoFrame)
        self.otherFacilitiesInfoFrame.setObjectName(u"otherFacilitiesInfoFrame")
        self.otherFacilitiesInfoFrame.setStyleSheet(u"")
        self.otherFacilitiesInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.otherFacilitiesInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.otherFacilitiesInfoFrame)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.ownerInfoTitle_5 = QLabel(self.otherFacilitiesInfoFrame)
        self.ownerInfoTitle_5.setObjectName(u"ownerInfoTitle_5")
        self.ownerInfoTitle_5.setStyleSheet(u"")

        self.verticalLayout_42.addWidget(self.ownerInfoTitle_5)

        self.otherFacilitiesInfoBodyFrame = QFrame(self.otherFacilitiesInfoFrame)
        self.otherFacilitiesInfoBodyFrame.setObjectName(u"otherFacilitiesInfoBodyFrame")
        self.otherFacilitiesInfoBodyFrame.setStyleSheet(u"")
        self.otherFacilitiesInfoBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.otherFacilitiesInfoBodyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.otherFacilitiesInfoBodyFrame)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_51 = QFrame(self.otherFacilitiesInfoBodyFrame)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_51)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_177 = QLabel(self.frame_51)
        self.label_177.setObjectName(u"label_177")

        self.verticalLayout_44.addWidget(self.label_177)


        self.verticalLayout_43.addWidget(self.frame_51)


        self.verticalLayout_42.addWidget(self.otherFacilitiesInfoBodyFrame)


        self.verticalLayout_32.addWidget(self.otherFacilitiesInfoFrame)

        self.materialInfoFrame = QFrame(self.buildingInfoFrame)
        self.materialInfoFrame.setObjectName(u"materialInfoFrame")
        self.materialInfoFrame.setEnabled(True)
        self.materialInfoFrame.setStyleSheet(u"")
        self.materialInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.materialInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.materialInfoFrame)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.ownerInfoTitle_6 = QLabel(self.materialInfoFrame)
        self.ownerInfoTitle_6.setObjectName(u"ownerInfoTitle_6")
        self.ownerInfoTitle_6.setStyleSheet(u"")

        self.verticalLayout_45.addWidget(self.ownerInfoTitle_6)

        self.materialInfoBodyFrame = QFrame(self.materialInfoFrame)
        self.materialInfoBodyFrame.setObjectName(u"materialInfoBodyFrame")
        self.materialInfoBodyFrame.setStyleSheet(u"")
        self.materialInfoBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.materialInfoBodyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.materialInfoBodyFrame)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_52 = QFrame(self.materialInfoBodyFrame)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_52)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setSpacing(50)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(15, 15, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 13, -1, -1)
        self.label_222 = QLabel(self.frame_52)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setStyleSheet(u"value")

        self.horizontalLayout_6.addWidget(self.label_222)

        self.label_178 = QLabel(self.frame_52)
        self.label_178.setObjectName(u"label_178")
        sizePolicy2.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_178)


        self.gridLayout_19.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.frame_52)
        self.widget_7.setObjectName(u"widget_7")

        self.gridLayout_19.addWidget(self.widget_7, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_19)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_53)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setSpacing(50)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 0, -1, -1)
        self.label_223 = QLabel(self.frame_52)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setStyleSheet(u"value")

        self.horizontalLayout_44.addWidget(self.label_223)

        self.label_212 = QLabel(self.frame_52)
        self.label_212.setObjectName(u"label_212")
        sizePolicy2.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy2)

        self.horizontalLayout_44.addWidget(self.label_212)


        self.gridLayout_20.addLayout(self.horizontalLayout_44, 0, 1, 1, 1)

        self.widget_8 = QWidget(self.frame_52)
        self.widget_8.setObjectName(u"widget_8")

        self.gridLayout_20.addWidget(self.widget_8, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_20)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_54)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setSpacing(50)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(-1, 0, -1, -1)
        self.label_227 = QLabel(self.frame_52)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setStyleSheet(u"value")

        self.horizontalLayout_71.addWidget(self.label_227)

        self.label_228 = QLabel(self.frame_52)
        self.label_228.setObjectName(u"label_228")
        sizePolicy2.setHeightForWidth(self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy2)

        self.horizontalLayout_71.addWidget(self.label_228)


        self.gridLayout_23.addLayout(self.horizontalLayout_71, 0, 1, 1, 1)

        self.widget_11 = QWidget(self.frame_52)
        self.widget_11.setObjectName(u"widget_11")

        self.gridLayout_23.addWidget(self.widget_11, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_23)

        self.frame_59 = QFrame(self.frame_52)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_59)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setSpacing(50)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(-1, 0, -1, -1)
        self.label_229 = QLabel(self.frame_52)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setStyleSheet(u"value")

        self.horizontalLayout_72.addWidget(self.label_229)

        self.label_230 = QLabel(self.frame_52)
        self.label_230.setObjectName(u"label_230")
        sizePolicy2.setHeightForWidth(self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy2)

        self.horizontalLayout_72.addWidget(self.label_230)


        self.gridLayout_24.addLayout(self.horizontalLayout_72, 0, 1, 1, 1)

        self.widget_12 = QWidget(self.frame_52)
        self.widget_12.setObjectName(u"widget_12")

        self.gridLayout_24.addWidget(self.widget_12, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_24)

        self.frame_58 = QFrame(self.frame_52)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_58)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setSpacing(50)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(-1, 0, -1, -1)
        self.label_235 = QLabel(self.frame_52)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setStyleSheet(u"value")

        self.horizontalLayout_75.addWidget(self.label_235)

        self.label_236 = QLabel(self.frame_52)
        self.label_236.setObjectName(u"label_236")
        sizePolicy2.setHeightForWidth(self.label_236.sizePolicy().hasHeightForWidth())
        self.label_236.setSizePolicy(sizePolicy2)

        self.horizontalLayout_75.addWidget(self.label_236)


        self.gridLayout_27.addLayout(self.horizontalLayout_75, 0, 1, 1, 1)

        self.widget_15 = QWidget(self.frame_52)
        self.widget_15.setObjectName(u"widget_15")

        self.gridLayout_27.addWidget(self.widget_15, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_27)

        self.frame_60 = QFrame(self.frame_52)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_60)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setSpacing(50)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(-1, 0, -1, -1)
        self.label_233 = QLabel(self.frame_52)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setStyleSheet(u"value")

        self.horizontalLayout_74.addWidget(self.label_233)

        self.label_234 = QLabel(self.frame_52)
        self.label_234.setObjectName(u"label_234")
        sizePolicy2.setHeightForWidth(self.label_234.sizePolicy().hasHeightForWidth())
        self.label_234.setSizePolicy(sizePolicy2)

        self.horizontalLayout_74.addWidget(self.label_234)


        self.gridLayout_26.addLayout(self.horizontalLayout_74, 0, 1, 1, 1)

        self.widget_14 = QWidget(self.frame_52)
        self.widget_14.setObjectName(u"widget_14")

        self.gridLayout_26.addWidget(self.widget_14, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_26)

        self.frame_61 = QFrame(self.frame_52)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_61)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setSpacing(50)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(-1, 0, -1, -1)
        self.label_231 = QLabel(self.frame_52)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setStyleSheet(u"value")

        self.horizontalLayout_73.addWidget(self.label_231)

        self.label_232 = QLabel(self.frame_52)
        self.label_232.setObjectName(u"label_232")
        sizePolicy2.setHeightForWidth(self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy2)

        self.horizontalLayout_73.addWidget(self.label_232)


        self.gridLayout_25.addLayout(self.horizontalLayout_73, 0, 1, 1, 1)

        self.widget_13 = QWidget(self.frame_52)
        self.widget_13.setObjectName(u"widget_13")

        self.gridLayout_25.addWidget(self.widget_13, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_25)

        self.frame_62 = QFrame(self.frame_52)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_62)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setSpacing(50)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(-1, 0, -1, -1)
        self.label_237 = QLabel(self.frame_52)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setStyleSheet(u"value")

        self.horizontalLayout_76.addWidget(self.label_237)

        self.label_238 = QLabel(self.frame_52)
        self.label_238.setObjectName(u"label_238")
        sizePolicy2.setHeightForWidth(self.label_238.sizePolicy().hasHeightForWidth())
        self.label_238.setSizePolicy(sizePolicy2)

        self.horizontalLayout_76.addWidget(self.label_238)


        self.gridLayout_28.addLayout(self.horizontalLayout_76, 0, 1, 1, 1)

        self.widget_16 = QWidget(self.frame_52)
        self.widget_16.setObjectName(u"widget_16")

        self.gridLayout_28.addWidget(self.widget_16, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_28)

        self.frame_63 = QFrame(self.frame_52)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_63)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setSpacing(50)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(-1, 0, -1, -1)
        self.label_239 = QLabel(self.frame_52)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setStyleSheet(u"value")

        self.horizontalLayout_77.addWidget(self.label_239)

        self.label_240 = QLabel(self.frame_52)
        self.label_240.setObjectName(u"label_240")
        sizePolicy2.setHeightForWidth(self.label_240.sizePolicy().hasHeightForWidth())
        self.label_240.setSizePolicy(sizePolicy2)

        self.horizontalLayout_77.addWidget(self.label_240)


        self.gridLayout_29.addLayout(self.horizontalLayout_77, 0, 1, 1, 1)

        self.widget_17 = QWidget(self.frame_52)
        self.widget_17.setObjectName(u"widget_17")

        self.gridLayout_29.addWidget(self.widget_17, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_29)

        self.frame_64 = QFrame(self.frame_52)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_64)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setSpacing(50)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(-1, 0, -1, -1)
        self.label_241 = QLabel(self.frame_52)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setStyleSheet(u"value")

        self.horizontalLayout_78.addWidget(self.label_241)

        self.label_242 = QLabel(self.frame_52)
        self.label_242.setObjectName(u"label_242")
        sizePolicy2.setHeightForWidth(self.label_242.sizePolicy().hasHeightForWidth())
        self.label_242.setSizePolicy(sizePolicy2)

        self.horizontalLayout_78.addWidget(self.label_242)


        self.gridLayout_30.addLayout(self.horizontalLayout_78, 0, 1, 1, 1)

        self.widget_18 = QWidget(self.frame_52)
        self.widget_18.setObjectName(u"widget_18")

        self.gridLayout_30.addWidget(self.widget_18, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_30)

        self.frame_65 = QFrame(self.frame_52)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_65)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setSpacing(50)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(-1, 0, -1, -1)
        self.label_243 = QLabel(self.frame_52)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setStyleSheet(u"value")

        self.horizontalLayout_79.addWidget(self.label_243)

        self.label_244 = QLabel(self.frame_52)
        self.label_244.setObjectName(u"label_244")
        sizePolicy2.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy2)

        self.horizontalLayout_79.addWidget(self.label_244)


        self.gridLayout_31.addLayout(self.horizontalLayout_79, 0, 1, 1, 1)

        self.widget_19 = QWidget(self.frame_52)
        self.widget_19.setObjectName(u"widget_19")

        self.gridLayout_31.addWidget(self.widget_19, 0, 0, 1, 1)


        self.verticalLayout_47.addLayout(self.gridLayout_31)


        self.verticalLayout_46.addWidget(self.frame_52)


        self.verticalLayout_45.addWidget(self.materialInfoBodyFrame)

        self.materialInfoFrame_2 = QFrame(self.materialInfoFrame)
        self.materialInfoFrame_2.setObjectName(u"materialInfoFrame_2")
        self.materialInfoFrame_2.setEnabled(True)
        self.materialInfoFrame_2.setStyleSheet(u"")
        self.materialInfoFrame_2.setFrameShape(QFrame.StyledPanel)
        self.materialInfoFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.materialInfoFrame_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.ownerInfoTitle_7 = QLabel(self.materialInfoFrame_2)
        self.ownerInfoTitle_7.setObjectName(u"ownerInfoTitle_7")
        self.ownerInfoTitle_7.setStyleSheet(u"")

        self.verticalLayout_48.addWidget(self.ownerInfoTitle_7)

        self.materialInfoBodyFrame_2 = QFrame(self.materialInfoFrame_2)
        self.materialInfoBodyFrame_2.setObjectName(u"materialInfoBodyFrame_2")
        self.materialInfoBodyFrame_2.setStyleSheet(u"")
        self.materialInfoBodyFrame_2.setFrameShape(QFrame.StyledPanel)
        self.materialInfoBodyFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.materialInfoBodyFrame_2)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_55 = QFrame(self.materialInfoBodyFrame_2)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_55)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_213 = QLabel(self.frame_55)
        self.label_213.setObjectName(u"label_213")

        self.verticalLayout_50.addWidget(self.label_213)


        self.verticalLayout_49.addWidget(self.frame_55)


        self.verticalLayout_48.addWidget(self.materialInfoBodyFrame_2)


        self.verticalLayout_45.addWidget(self.materialInfoFrame_2)


        self.verticalLayout_32.addWidget(self.materialInfoFrame)


        self.verticalLayout_27.addWidget(self.buildingInfoFrame)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_26.addWidget(self.scrollArea_5)

        self.pages.addWidget(self.page_estate)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_29 = QVBoxLayout(self.page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_29.addWidget(self.label_12)

        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_30 = QVBoxLayout(self.tab)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_30.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_37 = QVBoxLayout(self.tab_3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_13 = QFrame(self.tab_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 400))
        self.frame_13.setMaximumSize(QSize(16777215, 500))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(100)
        self.gridLayout_4.setVerticalSpacing(20)
        self.comboBox = QComboBox(self.frame_13)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 3, 2, 1, 1)

        self.label_52 = QLabel(self.frame_13)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_4.addWidget(self.label_52, 0, 0, 1, 1)

        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_13)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 0, 1, 1)

        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_54 = QLabel(self.frame_13)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_4.addWidget(self.label_54, 4, 2, 1, 1)

        self.label_53 = QLabel(self.frame_13)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_4.addWidget(self.label_53, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame_13)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_13)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_4.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 5, 2, 1, 1)

        self.label_55 = QLabel(self.frame_13)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_4.addWidget(self.label_55, 4, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_4.addWidget(self.lineEdit_9, 5, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)

        self.verticalLayout_37.addWidget(self.frame_13)

        self.pushButton_12 = QPushButton(self.tab_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_37.addWidget(self.pushButton_12, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_38 = QVBoxLayout(self.tab_2)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_14 = QFrame(self.tab_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_14)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(-1, -1, -1, 49)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_2 = QComboBox(self.frame_14)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.label_56 = QLabel(self.frame_14)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_4.addWidget(self.label_56)


        self.verticalLayout_51.addLayout(self.horizontalLayout_4)

        self.verticalFrame = QFrame(self.frame_14)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_52 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.checkBox_6 = QCheckBox(self.verticalFrame)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_52.addWidget(self.checkBox_6)

        self.frame_15 = QFrame(self.verticalFrame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_15)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(30)
        self.gridLayout_13.setVerticalSpacing(15)
        self.radioButton_14 = QRadioButton(self.frame_15)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_14, 2, 2, 1, 1)

        self.radioButton_18 = QRadioButton(self.frame_15)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_18, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.radioButton_9 = QRadioButton(self.frame_15)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_9, 1, 1, 1, 1)

        self.label_61 = QLabel(self.frame_15)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_13.addWidget(self.label_61, 2, 3, 1, 1)

        self.radioButton_7 = QRadioButton(self.frame_15)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_7, 0, 1, 1, 1)

        self.label_57 = QLabel(self.frame_15)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_13.addWidget(self.label_57, 0, 3, 1, 1)

        self.radioButton_8 = QRadioButton(self.frame_15)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_8, 1, 2, 1, 1)

        self.radioButton_15 = QRadioButton(self.frame_15)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_15, 2, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.frame_15)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_6, 0, 2, 1, 1)

        self.radioButton_19 = QRadioButton(self.frame_15)
        self.radioButton_19.setObjectName(u"radioButton_19")
        self.radioButton_19.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_13.addWidget(self.radioButton_19, 3, 1, 1, 1)

        self.label_58 = QLabel(self.frame_15)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_13.addWidget(self.label_58, 1, 3, 1, 1)

        self.label_76 = QLabel(self.frame_15)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_13.addWidget(self.label_76, 3, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)


        self.verticalLayout_52.addWidget(self.frame_15)


        self.verticalLayout_51.addWidget(self.verticalFrame)

        self.verticalFrame_2 = QFrame(self.frame_14)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalLayout_53 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.checkBox_7 = QCheckBox(self.verticalFrame_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_53.addWidget(self.checkBox_7)

        self.frame_25 = QFrame(self.verticalFrame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_25)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(30)
        self.gridLayout_17.setVerticalSpacing(15)
        self.radioButton_12 = QRadioButton(self.frame_25)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_12, 1, 2, 1, 1)

        self.label_75 = QLabel(self.frame_25)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_17.addWidget(self.label_75, 2, 3, 1, 1)

        self.radioButton_17 = QRadioButton(self.frame_25)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_17, 2, 1, 1, 1)

        self.radioButton_10 = QRadioButton(self.frame_25)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_10, 1, 1, 1, 1)

        self.radioButton_16 = QRadioButton(self.frame_25)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_16, 2, 2, 1, 1)

        self.radioButton_13 = QRadioButton(self.frame_25)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_13, 0, 2, 1, 1)

        self.label_60 = QLabel(self.frame_25)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_17.addWidget(self.label_60, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.radioButton_21 = QRadioButton(self.frame_25)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_21, 3, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.frame_25)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_11, 0, 1, 1, 1)

        self.label_59 = QLabel(self.frame_25)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_17.addWidget(self.label_59, 0, 3, 1, 1)

        self.label_77 = QLabel(self.frame_25)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_17.addWidget(self.label_77, 3, 3, 1, 1)

        self.radioButton_20 = QRadioButton(self.frame_25)
        self.radioButton_20.setObjectName(u"radioButton_20")
        self.radioButton_20.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_17.addWidget(self.radioButton_20, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)


        self.verticalLayout_53.addWidget(self.frame_25)


        self.verticalLayout_51.addWidget(self.verticalFrame_2)

        self.verticalLayout_51.setStretch(0, 1)

        self.verticalLayout_38.addWidget(self.frame_14)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_29.addWidget(self.tabWidget)

        self.pages.addWidget(self.page)

        self.horizontalLayout_5.addWidget(self.pages)

        self.sidebarMenuFrame = QFrame(self.centralwidget)
        self.sidebarMenuFrame.setObjectName(u"sidebarMenuFrame")
        self.sidebarMenuFrame.setMinimumSize(QSize(152, 0))
        self.sidebarMenuFrame.setStyleSheet(u"")
        self.sidebarMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.sidebarMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebarMenuFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(self.sidebarMenuFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:#ffffff;")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(False)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_11 = QLabel(self.sidebarMenuFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(25, 25))
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setPixmap(QPixmap(u":/icons/icons/username.png"))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.sidebarMenuFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.sidebar_dashboard_btn = QPushButton(self.sidebarMenuFrame)
        self.sidebar_dashboard_btn.setObjectName(u"sidebar_dashboard_btn")
        font = QFont()
        font.setFamilies([u"IRANSansWebFaNum Medium"])
        font.setBold(True)
        font.setItalic(False)
        self.sidebar_dashboard_btn.setFont(font)
        self.sidebar_dashboard_btn.setStyleSheet(u"")
        self.sidebar_dashboard_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.sidebar_dashboard_btn)

        self.pushButton_20 = QPushButton(self.sidebarMenuFrame)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout.addWidget(self.pushButton_20)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_23)


        self.horizontalLayout_5.addWidget(self.sidebarMenuFrame)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 886, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.form_stackwidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashboardFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenu", None))
        self.register_rent_building.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenuItem", None))
        self.label_14.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0645\u0644\u06a9 \u0627\u062c\u0627\u0631\u0647", None))
        self.label_13.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardItemTitle", None))
        self.all_rent_building.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenuItem", None))
        self.label_10.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627\u06cc \u0627\u062c\u0627\u0631\u0647", None))
        self.label_7.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardItemTitle", None))
        self.users.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenuItem", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.label_15.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardItemTitle", None))
        self.register_sale_building.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenuItem", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0645\u0644\u06a9 \u0641\u0631\u0648\u0634", None))
        self.label_2.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardItemTitle", None))
        self.all_sale_building.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenuItem", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627\u06cc \u0641\u0631\u0648\u0634", None))
        self.label_9.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardItemTitle", None))
        self.profile.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardMenuItem", None))
        self.label_224.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u0648\u0641\u0627\u06cc\u0644 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.label_3.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"dashboardItemTitle", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0645\u0644\u06a9", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u06f8", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u06f7", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u06f6", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u06f5", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u06f4", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u06f3", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u06f2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u06f1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u0648\u0639", None))
        self.melkCategoryLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u0645\u0644\u06a9", None))
        self.melkCategoryLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633", None))
        self.regionFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646\u0637\u0642\u0647", None))
        self.regionFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.cityFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0647\u0631", None))
        self.cityFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.streetFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644\u0647", None))
        self.streetFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.addressFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633", None))
        self.addressFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u0627\u0644\u06a9", None))
        self.owner1PhoneNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062b\u0627\u0628\u062a \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644", None))
        self.owner1PhoneNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.guardPhoneNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0646\u06af\u0647\u0628\u0627\u0646", None))
        self.guardPhoneNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ownerName1FormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644", None))
        self.ownerName1FormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.guardNameFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0646\u06af\u0647\u0628\u0627\u0646", None))
        self.guardNameFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ownerName2FormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0627\u0644\u06a9 \u062f\u0648\u0645", None))
        self.ownerName2FormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.owner2MobileNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0627\u0644\u06a9 \u062f\u0648\u0645", None))
        self.owner2MobileNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.tenantNameFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0633\u062a\u0627\u062c\u0631", None))
        self.tenantNameFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.owner1MobileNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644", None))
        self.owner1MobileNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.tenantPhoneNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0633\u062a\u0627\u062c\u0631", None))
        self.tenantPhoneNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ownerDescriptionFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a ", None))
        self.ownerDescriptionFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0644\u06cc", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698", None))
        self.label_21.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u062a\u0631 \u0645\u0631\u0628\u0639", None))
        self.label_23.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0627\u0633\u0628\u0647 \u0642\u06cc\u0645\u062a \u0628\u0631\u0627\u0633\u0627\u0633", None))
        self.label_20.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u06a9\u0644", None))
        self.label_22.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u06a9\u0644", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u0631\u062a\u0631", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0631\u0647\u0646", None))
        self.label_24.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0627\u062c\u0627\u0631\u0647", None))
        self.label_25.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u0633\u0627\u0632\u06cc \u0634\u062f\u0647", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u0631", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0647\u06cc\u0686\u06a9\u062f\u0627\u0645", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0647\u062a \u0646\u0648\u0631\u06af\u06cc\u0631\u06cc", None))
        self.label_28.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u0648\u0627\u062d\u062f\u0647\u0627", None))
        self.label_31.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0648\u0627\u062d\u062f \u062f\u0631 \u0637\u0628\u0642\u0647", None))
        self.label_32.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u0637\u0628\u0642\u0627\u062a", None))
        self.label_30.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0628\u0627\u0632\u0633\u0627\u0632\u06cc", None))
        self.label_33.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0644 \u0633\u0627\u062e\u062a", None))
        self.label_27.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0633\u0646\u062f", None))
        self.label_26.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0639\u0627\u0648\u0636\u0647:", None))
        self.label_134.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u0627\u06cc\u0637 \u0645\u0639\u0627\u0648\u0636\u0647", None))
        self.label_181.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0628\u0642\u0647", None))
        self.label_29.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u06a9\u0627\u0646\u0627\u062a", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u067e\u0627\u0631\u06a9\u06cc\u0646\u06af", None))
        self.label_37.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0634\u0639\u0627\u0628\u0627\u062a", None))
        self.label_48.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631\u06cc", None))
        self.label_43.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u0628\u0647\u0627\u0631\u062e\u0648\u0627\u0628", None))
        self.label_41.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u06cc\u0631 \u0627\u0645\u06a9\u0627\u0646\u0627\u062a", None))
        self.label_50.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0644\u06a9\u0646", None))
        self.label_40.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u0627\u0646\u0628\u0627\u0631\u06cc", None))
        self.label_44.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u0631\u06a9\u06cc\u0646\u06a9", None))
        self.label_38.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u067e\u0627\u0631\u06a9\u06cc\u0646\u06a9", None))
        self.label_36.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0633\u0627\u0646\u0633\u0648\u0631", None))
        self.label_47.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u062d\u06cc\u0627\u0637 \u0627\u062e\u062a\u0635\u0627\u0635\u06cc", None))
        self.label_45.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u0628\u0627\u0644\u06a9\u0646", None))
        self.label_39.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0647\u0627\u0631\u062e\u0648\u0627\u0628", None))
        self.label_42.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u062d\u06cc\u0627\u062a \u0627\u062e\u062a\u0635\u0627\u0635\u06cc", None))
        self.label_46.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u062a\u0631\u06cc\u0627\u0644", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0646\u062c\u0631\u0647", None))
        self.label_71.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u0633\u0631\u0645\u0627\u06cc\u0634\u06cc", None))
        self.label_66.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u0648\u0627\u0631\u0647\u0627", None))
        self.label_64.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628", None))
        self.label_72.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u06af\u0631\u0645\u0627\u06cc\u0634\u06cc", None))
        self.label_65.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0645\u0627\u0645", None))
        self.label_74.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0648\u06cc\u0633 \u0628\u0647\u062f\u0627\u0634\u062a\u06cc", None))
        self.label_73.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0641", None))
        self.label_62.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0634\u067e\u0632\u062e\u0627\u0646\u0647", None))
        self.label_68.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0642\u0641", None))
        self.label_63.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0628\u06cc\u0646\u062a\u200c\u200c\u0647\u0627", None))
        self.label_69.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0627\u0648\u06cc\u0631", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u06af\u0630\u0627\u0631\u06cc", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631 \u0634\u0627\u062e\u0635", None))
        self.label_88.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0627\u0644\u0631\u06cc \u062a\u0635\u0627\u0648\u06cc\u0631", None))
        self.label_89.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u06cc\u0627\u0646", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u062a\u06a9\u0644\u0645\u06cc\u0644\u06cc", None))
        self.label_90.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0639\u062f\u06cc", None))
        self.pushButton_2.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-btn", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0642\u0628\u0644\u06cc", None))
        self.pushButton.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-btn", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0644\u06a9 \u06f5\u06f3\u06f8", None))
        self.label_93.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0639\u0627\u0644", None))
        self.horizontalFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"buildingPageTopSection", None))
        self.priceBoxFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"buildingPriceInfo", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u06a9\u0644", None))
        self.label_135.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"\u06f1\u06f2", None))
        self.label_136.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u062a\u0631 \u0645\u0631\u0628\u0639", None))
        self.label_137.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"\u06f1\u06f2", None))
        self.label_138.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0631\u0647\u0646", None))
        self.label_140.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"\u06f1\u06f2", None))
        self.label_139.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0627\u062c\u0627\u0631\u0647", None))
        self.label_142.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"\u06f2\u06f0\u06f0", None))
        self.label_141.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.frame_40.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"buildingTopInfo", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u0622\u067e\u0627\u0631\u062a\u0645\u0627\u0646", None))
        self.label_94.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"buildingType", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u06f1\u06f2", None))
        self.label_96.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646\u0637\u0642\u0647:", None))
        self.label_95.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0644\u06a9\u0634\u0647\u0631", None))
        self.label_105.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u062f\u0648\u062f\u0647:", None))
        self.label_106.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631", None))
        self.label_133.setProperty("styleClass", "")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"\u06f2\u06f1\u06f0", None))
        self.label_107.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698:", None))
        self.label_108.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"\u06f1\u06f3\u06f9\u06f5", None))
        self.label_109.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0644 \u0633\u0627\u062e\u062a:", None))
        self.label_110.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0644\u06cc", None))
        self.label_129.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0647\u062a \u0646\u0648\u0631\u06af\u06cc\u0631\u06cc:", None))
        self.label_130.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"\u062a\u06a9 \u0628\u0631\u06af", None))
        self.label_131.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0633\u0646\u062f:", None))
        self.label_132.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.buildingInfoFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"buildingInfo", None))
        self.ownerInfoFrame_2.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.ownerInfoFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.ownerInfoTitle.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u0627\u0644\u06a9", None))
        self.ownerInfoTitle.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.ownerInfoBodyFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sectionBody", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0628\u0627\u0633\u06cc", None))
        self.label_151.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0627\u0644\u06a9 \u062f\u0648\u0645:", None))
        self.label_152.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0628\u0627\u0633\u06cc", None))
        self.label_146.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644:", None))
        self.label_145.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0628\u0627\u0633\u06cc", None))
        self.label_155.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0633\u062a\u0627\u062c\u0631:", None))
        self.label_156.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0628\u0627\u0633\u06cc", None))
        self.label_159.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0646\u06af\u0647\u0628\u0627\u0646:", None))
        self.label_160.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"0913", None))
        self.label_148.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0645\u0631\u0627\u0647:", None))
        self.label_147.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"091333", None))
        self.label_153.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0645\u0631\u0627\u0647:", None))
        self.label_154.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"0912", None))
        self.label_161.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0645\u0631\u0627\u0647:", None))
        self.label_162.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"0912", None))
        self.label_157.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0645\u0631\u0627\u0647:", None))
        self.label_158.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"0913", None))
        self.label_163.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062b\u0627\u0628\u062a", None))
        self.label_164.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a:", None))
        self.label_143.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"\u0646\u062f\u0627\u0631\u062f", None))
        self.label_144.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.FurtherInfoFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.FurtherInfoTitle.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u062a\u06a9\u0645\u06cc\u0644\u06cc", None))
        self.FurtherInfoTitle.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.FurtherInfoBodyFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sectionBody", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_165.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u0648\u0627\u062d\u062f\u0647\u0627:", None))
        self.label_166.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"\u06f5", None))
        self.label_167.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0628\u0642\u0647:", None))
        self.label_168.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u0631", None))
        self.label_169.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0628\u0627\u0632\u0633\u0627\u0632\u06cc:", None))
        self.label_170.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0627\u0631\u062f", None))
        self.label_171.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0639\u0627\u0648\u0636\u0647:", None))
        self.label_172.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"\u06f4", None))
        self.label_173.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u0637\u0628\u0642\u0627\u062a", None))
        self.label_174.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"\u06f2", None))
        self.label_175.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0648\u0627\u062d\u062f \u062f\u0631 \u0637\u0628\u0642\u0647:", None))
        self.label_176.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u0627\u06cc\u0637 \u0645\u0639\u0627\u0648\u0638\u0647:", None))
        self.label_183.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"\u0646\u062f\u0627\u0631\u062f", None))
        self.label_184.setProperty("styleClass", "")
        self.facilitiesInfoFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.ownerInfoTitle_4.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u06a9\u0627\u0646\u0627\u062a \u0627\u0635\u0644\u06cc", None))
        self.ownerInfoTitle_4.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.facilitiesInfoBodyFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sectionBody", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0644\u06a9\u0646", None))
        self.label_180.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"\u06f4", None))
        self.label_208.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f:", None))
        self.label_209.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0647\u0627\u0631\u062e\u0648\u0627\u0628", None))
        self.label_214.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631\u06cc", None))
        self.label_182.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u0631\u06a9\u06cc\u0646\u06af", None))
        self.label_179.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"\u06f2", None))
        self.label_210.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698", None))
        self.label_211.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u0642\u0641", None))
        self.label_216.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a:", None))
        self.label_217.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0633\u0627\u0646\u0633\u0648\u0631", None))
        self.label_215.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"\u06f2", None))
        self.label_218.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698", None))
        self.label_219.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"\u06f2", None))
        self.label_220.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698", None))
        self.label_221.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.otherFacilitiesInfoFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.ownerInfoTitle_5.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u06cc\u0631 \u0627\u0645\u06a9\u0627\u0646\u0627\u062a", None))
        self.ownerInfoTitle_5.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.otherFacilitiesInfoBodyFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sectionBody", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u06a9\u0627\u0646\u0627\u062a:", None))
        self.label_177.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.materialInfoFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.ownerInfoTitle_6.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u06cc\u0627\u0644 \u0648 \u062c\u0632\u0626\u06cc\u0627\u062a", None))
        self.ownerInfoTitle_6.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.materialInfoBodyFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sectionBody", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_222.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0641:", None))
        self.label_178.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_53.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_223.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0642\u0641:", None))
        self.label_212.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_54.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_227.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u0648\u0627\u0631\u0647\u0627:", None))
        self.label_228.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_59.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_229.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0628\u06cc\u0646\u062a:", None))
        self.label_230.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_58.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_235.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u0633\u0631\u0645\u0627\u06cc\u0634\u06cc:", None))
        self.label_236.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_60.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_233.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u06af\u0631\u0645\u0627\u06cc\u0634\u06cc:", None))
        self.label_234.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_61.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_231.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0634\u067e\u0632\u062e\u0627\u0646\u0647:", None))
        self.label_232.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_62.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_237.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0645\u0627\u0645:", None))
        self.label_238.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_63.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_239.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0648\u06cc\u0633 \u0628\u0647\u062f\u0627\u0634\u062a\u06cc:", None))
        self.label_240.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_64.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_241.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628", None))
        self.label_242.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.frame_65.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"seperator", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0627\u0645\u06cc\u06a9", None))
        self.label_243.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"value", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0646\u062c\u0631\u0647", None))
        self.label_244.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"label", None))
        self.materialInfoFrame_2.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"section", None))
        self.ownerInfoTitle_7.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u062a\u06a9\u0645\u06cc\u0644\u06cc", None))
        self.ownerInfoTitle_7.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"header", None))
        self.materialInfoBodyFrame_2.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sectionBody", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0633 \u062a\u0648\u0636\u06cc\u062d\u0627\u062a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u" \u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0645\u0631\u0627\u0647", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0642\u0634 \u06a9\u0627\u0631\u0628\u0631\u06cc", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u06f1", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u06cc\u0631", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0644\u06a9 \u0632\u0627\u062f\u0647", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"09398787515", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0648\u0631", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u06f1\u06f5", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0645\u0631\u0627\u0647", None))
        self.label_52.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None))
        self.label_18.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645", None))
        self.label_17.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.label_54.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0642\u0634 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.label_53.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.label_55.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0646\u0627\u0645", None))
        self.pushButton_12.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-btn", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0627\u0641\u0632\u0648\u062f\u0646 \u06a9\u0627\u0631\u0628\u0631", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc:", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0645\u0644\u06a9 \u0641\u0631\u0648\u0634", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0634\u0645\u0627\u0631\u0647\u200c\u0647\u0627:", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u0645\u0644\u06a9 \u0641\u0631\u0648\u0634:", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u0645\u0644\u06a9 \u0641\u0631\u0648\u0634:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0622\u062f\u0631\u0633:", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0645\u0644\u06a9 \u0641\u0631\u0648\u0634", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0634\u0645\u0627\u0631\u0647\u200c\u0647\u0627:", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u0645\u0644\u06a9 \u0627\u062c\u0627\u0631\u0647:", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0641\u0627\u06cc\u0644\u200c\u0647\u0627", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u0645\u0644\u06a9 \u0627\u062c\u0627\u0631\u0647:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0622\u062f\u0631\u0633:", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0642\u0637 \u0641\u0627\u06cc\u0644 \u062e\u0648\u062f \u0641\u0631\u062f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc", None))
        self.sidebarMenuFrame.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"sideMenu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u06cc\u0631\u062d\u0633\u06cc\u0646\n"
" \u062e\u0648\u0634 \u0622\u0645\u062f\u06cc\u062f", None))
        self.label_11.setText("")
        self.sidebar_dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0627\u0634\u0628\u0648\u0631\u062f", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c", None))
    # retranslateUi


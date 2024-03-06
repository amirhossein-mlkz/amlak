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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(913, 743)
        MainWindow.setMinimumSize(QSize(0, 0))
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
"QLabel[styleClass=\"form-field-error\"]{\n"
"\n"
"color:rgb(197, 63, 59);\n"
"\n"
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
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, sto"
                        "p:0 rgba(189, 189, 191, 255), stop:1 rgba(189, 189, 191, 255));\n"
"	color: rgba(120, 120, 120, 255);\n"
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

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 31, -1, -1)
        self.frame_32 = QFrame(self.form_step1)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_32, 0, 1, 1, 1)

        self.melkCategoryFormFrame = QFrame(self.form_step1)
        self.melkCategoryFormFrame.setObjectName(u"melkCategoryFormFrame")
        self.verticalLayout_55 = QVBoxLayout(self.melkCategoryFormFrame)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(1, 1, -1, -1)
        self.melkCategoryFormLbl = QLabel(self.melkCategoryFormFrame)
        self.melkCategoryFormLbl.setObjectName(u"melkCategoryFormLbl")

        self.verticalLayout_55.addWidget(self.melkCategoryFormLbl)

        self.melkCategoryFormError = QLabel(self.melkCategoryFormFrame)
        self.melkCategoryFormError.setObjectName(u"melkCategoryFormError")

        self.verticalLayout_55.addWidget(self.melkCategoryFormError)

        self.melkCategoryFormInpt = QComboBox(self.melkCategoryFormFrame)
        self.melkCategoryFormInpt.setObjectName(u"melkCategoryFormInpt")
        self.melkCategoryFormInpt.setMinimumSize(QSize(87, 37))

        self.verticalLayout_55.addWidget(self.melkCategoryFormInpt)


        self.gridLayout_11.addWidget(self.melkCategoryFormFrame, 0, 2, 1, 1)

        self.frame_33 = QFrame(self.form_step1)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_33, 0, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_11)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_22)

        self.form_stackwidget.addWidget(self.form_step1)
        self.form_step2 = QWidget()
        self.form_step2.setObjectName(u"form_step2")
        self.verticalLayout_11 = QVBoxLayout(self.form_step2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_34 = QLabel(self.form_step2)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_11.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.gridLayout_1_1 = QGridLayout()
        self.gridLayout_1_1.setObjectName(u"gridLayout_1_1")
        self.gridLayout_1_1.setContentsMargins(0, 24, -1, -1)
        self.regionFormFrame = QFrame(self.form_step2)
        self.regionFormFrame.setObjectName(u"regionFormFrame")
        self.verticalLayout_57 = QVBoxLayout(self.regionFormFrame)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.regionFormLbl = QLabel(self.regionFormFrame)
        self.regionFormLbl.setObjectName(u"regionFormLbl")

        self.verticalLayout_57.addWidget(self.regionFormLbl)

        self.regionFormError = QLabel(self.regionFormFrame)
        self.regionFormError.setObjectName(u"regionFormError")

        self.verticalLayout_57.addWidget(self.regionFormError)

        self.regionFormInpt = QSpinBox(self.regionFormFrame)
        self.regionFormInpt.setObjectName(u"regionFormInpt")

        self.verticalLayout_57.addWidget(self.regionFormInpt)


        self.gridLayout_1_1.addWidget(self.regionFormFrame, 0, 1, 1, 1)

        self.cityFormFrame = QFrame(self.form_step2)
        self.cityFormFrame.setObjectName(u"cityFormFrame")
        self.verticalLayout_56 = QVBoxLayout(self.cityFormFrame)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.cityFormLbl = QLabel(self.cityFormFrame)
        self.cityFormLbl.setObjectName(u"cityFormLbl")

        self.verticalLayout_56.addWidget(self.cityFormLbl)

        self.cityFormError = QLabel(self.cityFormFrame)
        self.cityFormError.setObjectName(u"cityFormError")

        self.verticalLayout_56.addWidget(self.cityFormError)

        self.cityFormInpt = QComboBox(self.cityFormFrame)
        self.cityFormInpt.setObjectName(u"cityFormInpt")

        self.verticalLayout_56.addWidget(self.cityFormInpt)


        self.gridLayout_1_1.addWidget(self.cityFormFrame, 0, 2, 1, 1)

        self.streetFormFrame = QFrame(self.form_step2)
        self.streetFormFrame.setObjectName(u"streetFormFrame")
        self.verticalLayout_58 = QVBoxLayout(self.streetFormFrame)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.streetFormLbl = QLabel(self.streetFormFrame)
        self.streetFormLbl.setObjectName(u"streetFormLbl")

        self.verticalLayout_58.addWidget(self.streetFormLbl)

        self.streetFormError = QLabel(self.streetFormFrame)
        self.streetFormError.setObjectName(u"streetFormError")

        self.verticalLayout_58.addWidget(self.streetFormError)

        self.streetFormInpt = QLineEdit(self.streetFormFrame)
        self.streetFormInpt.setObjectName(u"streetFormInpt")

        self.verticalLayout_58.addWidget(self.streetFormInpt)


        self.gridLayout_1_1.addWidget(self.streetFormFrame, 0, 0, 1, 1)

        self.gridLayout_1_1.setColumnStretch(0, 1)
        self.gridLayout_1_1.setColumnStretch(1, 1)
        self.gridLayout_1_1.setColumnStretch(2, 1)

        self.verticalLayout_11.addLayout(self.gridLayout_1_1)

        self.gridLayout_1_2 = QGridLayout()
        self.gridLayout_1_2.setObjectName(u"gridLayout_1_2")
        self.gridLayout_1_2.setContentsMargins(-1, 13, -1, -1)
        self.addressFormFrame = QFrame(self.form_step2)
        self.addressFormFrame.setObjectName(u"addressFormFrame")
        self.verticalLayout_60 = QVBoxLayout(self.addressFormFrame)
        self.verticalLayout_60.setSpacing(6)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(-1, 1, -1, -1)
        self.addressFormLbl = QLabel(self.addressFormFrame)
        self.addressFormLbl.setObjectName(u"addressFormLbl")

        self.verticalLayout_60.addWidget(self.addressFormLbl)

        self.addressFormError = QLabel(self.addressFormFrame)
        self.addressFormError.setObjectName(u"addressFormError")

        self.verticalLayout_60.addWidget(self.addressFormError)

        self.addressFormInpt = QTextEdit(self.addressFormFrame)
        self.addressFormInpt.setObjectName(u"addressFormInpt")

        self.verticalLayout_60.addWidget(self.addressFormInpt)


        self.gridLayout_1_2.addWidget(self.addressFormFrame, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_1_2)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -445, 677, 1086))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_49 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_20.addWidget(self.label_49, 0, Qt.AlignHCenter)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(50)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.verticalFrame_8 = QFrame(self.scrollAreaWidgetContents_3)
        self.verticalFrame_8.setObjectName(u"verticalFrame_8")
        self.owner1PhoneNumberFormFrame = QVBoxLayout(self.verticalFrame_8)
        self.owner1PhoneNumberFormFrame.setObjectName(u"owner1PhoneNumberFormFrame")
        self.owner1PhoneNumberFormLbl = QLabel(self.verticalFrame_8)
        self.owner1PhoneNumberFormLbl.setObjectName(u"owner1PhoneNumberFormLbl")

        self.owner1PhoneNumberFormFrame.addWidget(self.owner1PhoneNumberFormLbl)

        self.owner1PhoneNumberFormError = QLabel(self.verticalFrame_8)
        self.owner1PhoneNumberFormError.setObjectName(u"owner1PhoneNumberFormError")

        self.owner1PhoneNumberFormFrame.addWidget(self.owner1PhoneNumberFormError)

        self.owner1PhoneNumberFormInpt = QLineEdit(self.verticalFrame_8)
        self.owner1PhoneNumberFormInpt.setObjectName(u"owner1PhoneNumberFormInpt")

        self.owner1PhoneNumberFormFrame.addWidget(self.owner1PhoneNumberFormInpt)


        self.gridLayout_2.addWidget(self.verticalFrame_8, 0, 0, 1, 1)

        self.owner1MobileNumberFormFrame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.owner1MobileNumberFormFrame_2.setObjectName(u"owner1MobileNumberFormFrame_2")
        self.owner1MobileNumberFormFrame = QVBoxLayout(self.owner1MobileNumberFormFrame_2)
        self.owner1MobileNumberFormFrame.setObjectName(u"owner1MobileNumberFormFrame")
        self.owner1MobileNumberFormLbl = QLabel(self.owner1MobileNumberFormFrame_2)
        self.owner1MobileNumberFormLbl.setObjectName(u"owner1MobileNumberFormLbl")

        self.owner1MobileNumberFormFrame.addWidget(self.owner1MobileNumberFormLbl)

        self.owner1MobileNumberFormError = QLabel(self.owner1MobileNumberFormFrame_2)
        self.owner1MobileNumberFormError.setObjectName(u"owner1MobileNumberFormError")

        self.owner1MobileNumberFormFrame.addWidget(self.owner1MobileNumberFormError)

        self.owner1MobileNumberFormInpt = QLineEdit(self.owner1MobileNumberFormFrame_2)
        self.owner1MobileNumberFormInpt.setObjectName(u"owner1MobileNumberFormInpt")

        self.owner1MobileNumberFormFrame.addWidget(self.owner1MobileNumberFormInpt)


        self.gridLayout_2.addWidget(self.owner1MobileNumberFormFrame_2, 0, 1, 1, 1)

        self.owner2MobileNumberFormFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.owner2MobileNumberFormFrame.setObjectName(u"owner2MobileNumberFormFrame")
        self.verticalLayout_64 = QVBoxLayout(self.owner2MobileNumberFormFrame)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.owner2MobileNumberFormLbl = QLabel(self.owner2MobileNumberFormFrame)
        self.owner2MobileNumberFormLbl.setObjectName(u"owner2MobileNumberFormLbl")

        self.verticalLayout_64.addWidget(self.owner2MobileNumberFormLbl)

        self.owner2MobileNumberFormError = QLabel(self.owner2MobileNumberFormFrame)
        self.owner2MobileNumberFormError.setObjectName(u"owner2MobileNumberFormError")

        self.verticalLayout_64.addWidget(self.owner2MobileNumberFormError)

        self.owner2MobileNumberFormInpt = QLineEdit(self.owner2MobileNumberFormFrame)
        self.owner2MobileNumberFormInpt.setObjectName(u"owner2MobileNumberFormInpt")

        self.verticalLayout_64.addWidget(self.owner2MobileNumberFormInpt)


        self.gridLayout_2.addWidget(self.owner2MobileNumberFormFrame, 1, 1, 1, 1)

        self.ownerName2FormFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.ownerName2FormFrame.setObjectName(u"ownerName2FormFrame")
        self.verticalLayout_63 = QVBoxLayout(self.ownerName2FormFrame)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.ownerName2FormLbl = QLabel(self.ownerName2FormFrame)
        self.ownerName2FormLbl.setObjectName(u"ownerName2FormLbl")

        self.verticalLayout_63.addWidget(self.ownerName2FormLbl)

        self.ownerName2FormError = QLabel(self.ownerName2FormFrame)
        self.ownerName2FormError.setObjectName(u"ownerName2FormError")

        self.verticalLayout_63.addWidget(self.ownerName2FormError)

        self.ownerName2FormInpt = QLineEdit(self.ownerName2FormFrame)
        self.ownerName2FormInpt.setObjectName(u"ownerName2FormInpt")

        self.verticalLayout_63.addWidget(self.ownerName2FormInpt)


        self.gridLayout_2.addWidget(self.ownerName2FormFrame, 1, 2, 1, 1)

        self.verticalFrame_11 = QFrame(self.scrollAreaWidgetContents_3)
        self.verticalFrame_11.setObjectName(u"verticalFrame_11")
        self.tenantNameFormFrame = QVBoxLayout(self.verticalFrame_11)
        self.tenantNameFormFrame.setObjectName(u"tenantNameFormFrame")
        self.tenantNameFormLbl = QLabel(self.verticalFrame_11)
        self.tenantNameFormLbl.setObjectName(u"tenantNameFormLbl")

        self.tenantNameFormFrame.addWidget(self.tenantNameFormLbl)

        self.tenantNameFormError = QLabel(self.verticalFrame_11)
        self.tenantNameFormError.setObjectName(u"tenantNameFormError")

        self.tenantNameFormFrame.addWidget(self.tenantNameFormError)

        self.tenantNameFormInpt = QLineEdit(self.verticalFrame_11)
        self.tenantNameFormInpt.setObjectName(u"tenantNameFormInpt")

        self.tenantNameFormFrame.addWidget(self.tenantNameFormInpt)


        self.gridLayout_2.addWidget(self.verticalFrame_11, 2, 2, 1, 1)

        self.verticalFrame_6 = QFrame(self.scrollAreaWidgetContents_3)
        self.verticalFrame_6.setObjectName(u"verticalFrame_6")
        self.ownerName1FormFrame = QVBoxLayout(self.verticalFrame_6)
        self.ownerName1FormFrame.setObjectName(u"ownerName1FormFrame")
        self.ownerName1FormLbl = QLabel(self.verticalFrame_6)
        self.ownerName1FormLbl.setObjectName(u"ownerName1FormLbl")

        self.ownerName1FormFrame.addWidget(self.ownerName1FormLbl)

        self.ownerName1FormError = QLabel(self.verticalFrame_6)
        self.ownerName1FormError.setObjectName(u"ownerName1FormError")

        self.ownerName1FormFrame.addWidget(self.ownerName1FormError)

        self.ownerName1FormInpt = QLineEdit(self.verticalFrame_6)
        self.ownerName1FormInpt.setObjectName(u"ownerName1FormInpt")

        self.ownerName1FormFrame.addWidget(self.ownerName1FormInpt)


        self.gridLayout_2.addWidget(self.verticalFrame_6, 0, 2, 1, 1)

        self.verticalFrame_12 = QFrame(self.scrollAreaWidgetContents_3)
        self.verticalFrame_12.setObjectName(u"verticalFrame_12")
        self.tenantPhoneNumberFormFrame = QVBoxLayout(self.verticalFrame_12)
        self.tenantPhoneNumberFormFrame.setObjectName(u"tenantPhoneNumberFormFrame")
        self.tenantPhoneNumberFormLbl = QLabel(self.verticalFrame_12)
        self.tenantPhoneNumberFormLbl.setObjectName(u"tenantPhoneNumberFormLbl")

        self.tenantPhoneNumberFormFrame.addWidget(self.tenantPhoneNumberFormLbl)

        self.tenantPhoneNumberFormError = QLabel(self.verticalFrame_12)
        self.tenantPhoneNumberFormError.setObjectName(u"tenantPhoneNumberFormError")

        self.tenantPhoneNumberFormFrame.addWidget(self.tenantPhoneNumberFormError)

        self.tenantPhoneNumberFormInpt = QLineEdit(self.verticalFrame_12)
        self.tenantPhoneNumberFormInpt.setObjectName(u"tenantPhoneNumberFormInpt")

        self.tenantPhoneNumberFormFrame.addWidget(self.tenantPhoneNumberFormInpt)


        self.gridLayout_2.addWidget(self.verticalFrame_12, 2, 1, 1, 1)

        self.guardNameFormFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.guardNameFormFrame.setObjectName(u"guardNameFormFrame")
        self.verticalLayout_67 = QVBoxLayout(self.guardNameFormFrame)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.guardNameFormLbl = QLabel(self.guardNameFormFrame)
        self.guardNameFormLbl.setObjectName(u"guardNameFormLbl")

        self.verticalLayout_67.addWidget(self.guardNameFormLbl)

        self.guardNameFormError = QLabel(self.guardNameFormFrame)
        self.guardNameFormError.setObjectName(u"guardNameFormError")

        self.verticalLayout_67.addWidget(self.guardNameFormError)

        self.guardNameFormInpt = QLineEdit(self.guardNameFormFrame)
        self.guardNameFormInpt.setObjectName(u"guardNameFormInpt")

        self.verticalLayout_67.addWidget(self.guardNameFormInpt)


        self.gridLayout_2.addWidget(self.guardNameFormFrame, 3, 2, 1, 1)

        self.guardPhoneNumberFormFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.guardPhoneNumberFormFrame.setObjectName(u"guardPhoneNumberFormFrame")
        self.verticalLayout_68 = QVBoxLayout(self.guardPhoneNumberFormFrame)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.guardPhoneNumberFormLbl = QLabel(self.guardPhoneNumberFormFrame)
        self.guardPhoneNumberFormLbl.setObjectName(u"guardPhoneNumberFormLbl")

        self.verticalLayout_68.addWidget(self.guardPhoneNumberFormLbl)

        self.guardPhoneNumberFormError = QLabel(self.guardPhoneNumberFormFrame)
        self.guardPhoneNumberFormError.setObjectName(u"guardPhoneNumberFormError")

        self.verticalLayout_68.addWidget(self.guardPhoneNumberFormError)

        self.guardPhoneNumberFormInpt = QLineEdit(self.guardPhoneNumberFormFrame)
        self.guardPhoneNumberFormInpt.setObjectName(u"guardPhoneNumberFormInpt")

        self.verticalLayout_68.addWidget(self.guardPhoneNumberFormInpt)


        self.gridLayout_2.addWidget(self.guardPhoneNumberFormFrame, 3, 1, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_2)

        self.ownerDescriptionFormFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.ownerDescriptionFormFrame.setObjectName(u"ownerDescriptionFormFrame")
        self.cc = QVBoxLayout(self.ownerDescriptionFormFrame)
        self.cc.setObjectName(u"cc")
        self.cc.setContentsMargins(1, 25, -1, -1)
        self.ownerDescriptionFormLbl = QLabel(self.ownerDescriptionFormFrame)
        self.ownerDescriptionFormLbl.setObjectName(u"ownerDescriptionFormLbl")

        self.cc.addWidget(self.ownerDescriptionFormLbl)

        self.ownerDescriptionFormError = QLabel(self.ownerDescriptionFormFrame)
        self.ownerDescriptionFormError.setObjectName(u"ownerDescriptionFormError")

        self.cc.addWidget(self.ownerDescriptionFormError)

        self.ownerDescriptionFormInpt = QTextEdit(self.ownerDescriptionFormFrame)
        self.ownerDescriptionFormInpt.setObjectName(u"ownerDescriptionFormInpt")

        self.cc.addWidget(self.ownerDescriptionFormInpt)


        self.verticalLayout_20.addWidget(self.ownerDescriptionFormFrame)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -804, 676, 1684))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_14.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(30)
        self.gridLayout_6.setContentsMargins(-1, 20, -1, 20)
        self.lightDirectionFrame = QFrame(self.scrollAreaWidgetContents)
        self.lightDirectionFrame.setObjectName(u"lightDirectionFrame")
        self.lightDirectionFrame.setFrameShape(QFrame.StyledPanel)
        self.lightDirectionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.lightDirectionFrame)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.lightDirectionLbl = QLabel(self.lightDirectionFrame)
        self.lightDirectionLbl.setObjectName(u"lightDirectionLbl")
        self.lightDirectionLbl.setStyleSheet(u"label")

        self.verticalLayout_59.addWidget(self.lightDirectionLbl)

        self.lightDirectionError = QLabel(self.lightDirectionFrame)
        self.lightDirectionError.setObjectName(u"lightDirectionError")

        self.verticalLayout_59.addWidget(self.lightDirectionError)

        self.lightDirectionInpt = QComboBox(self.lightDirectionFrame)
        self.lightDirectionInpt.setObjectName(u"lightDirectionInpt")

        self.verticalLayout_59.addWidget(self.lightDirectionInpt)


        self.gridLayout_6.addWidget(self.lightDirectionFrame, 3, 0, 1, 1)

        self.meterageFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.meterageFormFrame.setObjectName(u"meterageFormFrame")
        self.verticalLayout_70 = QVBoxLayout(self.meterageFormFrame)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.meterageFormLbl = QLabel(self.meterageFormFrame)
        self.meterageFormLbl.setObjectName(u"meterageFormLbl")
        self.meterageFormLbl.setStyleSheet(u"label")

        self.verticalLayout_70.addWidget(self.meterageFormLbl)

        self.meterageFormError = QLabel(self.meterageFormFrame)
        self.meterageFormError.setObjectName(u"meterageFormError")

        self.verticalLayout_70.addWidget(self.meterageFormError)

        self.meterageFormInpt = QSpinBox(self.meterageFormFrame)
        self.meterageFormInpt.setObjectName(u"meterageFormInpt")

        self.verticalLayout_70.addWidget(self.meterageFormInpt)


        self.gridLayout_6.addWidget(self.meterageFormFrame, 0, 2, 1, 1)

        self.floorCounFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.floorCounFormFrame.setObjectName(u"floorCounFormFrame")
        self.floorCounFormFrame.setMinimumSize(QSize(0, 0))
        self.floorCounFormFrame.setFrameShape(QFrame.StyledPanel)
        self.floorCounFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.floorCounFormFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.floorCounFormLbl = QLabel(self.floorCounFormFrame)
        self.floorCounFormLbl.setObjectName(u"floorCounFormLbl")
        self.floorCounFormLbl.setStyleSheet(u"label")

        self.verticalLayout_13.addWidget(self.floorCounFormLbl)

        self.floorCounFormError = QLabel(self.floorCounFormFrame)
        self.floorCounFormError.setObjectName(u"floorCounFormError")

        self.verticalLayout_13.addWidget(self.floorCounFormError)

        self.floorCounFormInpt = QSpinBox(self.floorCounFormFrame)
        self.floorCounFormInpt.setObjectName(u"floorCounFormInpt")

        self.verticalLayout_13.addWidget(self.floorCounFormInpt)


        self.gridLayout_6.addWidget(self.floorCounFormFrame, 5, 2, 1, 1)

        self.rebuildingFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.rebuildingFormFrame.setObjectName(u"rebuildingFormFrame")
        self.rebuildingFormFrame.setMinimumSize(QSize(0, 0))
        self.rebuildingFormFrame.setFrameShape(QFrame.StyledPanel)
        self.rebuildingFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.rebuildingFormFrame)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.rebuildingFormLbl = QLabel(self.rebuildingFormFrame)
        self.rebuildingFormLbl.setObjectName(u"rebuildingFormLbl")
        self.rebuildingFormLbl.setStyleSheet(u"label")

        self.verticalLayout_74.addWidget(self.rebuildingFormLbl)

        self.rebuildingFormError = QLabel(self.rebuildingFormFrame)
        self.rebuildingFormError.setObjectName(u"rebuildingFormError")

        self.verticalLayout_74.addWidget(self.rebuildingFormError)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 20, -1)
        self.radioButton_5 = QRadioButton(self.rebuildingFormFrame)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_16.addWidget(self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.rebuildingFormFrame)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_16.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.rebuildingFormFrame)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_16.addWidget(self.radioButton_3)


        self.verticalLayout_74.addLayout(self.verticalLayout_16)


        self.gridLayout_6.addWidget(self.rebuildingFormFrame, 6, 2, 1, 1)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_38)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_32 = QLabel(self.frame_38)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"label")

        self.verticalLayout_73.addWidget(self.label_32)

        self.floorFormError_4 = QLabel(self.frame_38)
        self.floorFormError_4.setObjectName(u"floorFormError_4")

        self.verticalLayout_73.addWidget(self.floorFormError_4)

        self.spinBox_7 = QSpinBox(self.frame_38)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.verticalLayout_73.addWidget(self.spinBox_7)


        self.gridLayout_6.addWidget(self.frame_38, 5, 0, 1, 1)

        self.floorFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.floorFormFrame.setObjectName(u"floorFormFrame")
        self.verticalLayout_69 = QVBoxLayout(self.floorFormFrame)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.floorFormLbl = QLabel(self.floorFormFrame)
        self.floorFormLbl.setObjectName(u"floorFormLbl")
        self.floorFormLbl.setStyleSheet(u"label")

        self.verticalLayout_69.addWidget(self.floorFormLbl)

        self.floorFormError = QLabel(self.floorFormFrame)
        self.floorFormError.setObjectName(u"floorFormError")

        self.verticalLayout_69.addWidget(self.floorFormError)

        self.floorFormInpt = QSpinBox(self.floorFormFrame)
        self.floorFormInpt.setObjectName(u"floorFormInpt")

        self.verticalLayout_69.addWidget(self.floorFormInpt)


        self.gridLayout_6.addWidget(self.floorFormFrame, 4, 2, 1, 1)

        self.rentPriceFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.rentPriceFormFrame.setObjectName(u"rentPriceFormFrame")
        self.rentPriceFormFrame.setFrameShape(QFrame.StyledPanel)
        self.rentPriceFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.rentPriceFormFrame)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.rentPriceFormLbl = QLabel(self.rentPriceFormFrame)
        self.rentPriceFormLbl.setObjectName(u"rentPriceFormLbl")
        self.rentPriceFormLbl.setStyleSheet(u"label")

        self.verticalLayout_71.addWidget(self.rentPriceFormLbl)

        self.rentPriceFormError = QLabel(self.rentPriceFormFrame)
        self.rentPriceFormError.setObjectName(u"rentPriceFormError")

        self.verticalLayout_71.addWidget(self.rentPriceFormError)

        self.rentPriceFormInpt = QLineEdit(self.rentPriceFormFrame)
        self.rentPriceFormInpt.setObjectName(u"rentPriceFormInpt")

        self.verticalLayout_71.addWidget(self.rentPriceFormInpt)


        self.gridLayout_6.addWidget(self.rentPriceFormFrame, 2, 1, 1, 1)

        self.mortgagePriceFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.mortgagePriceFormFrame.setObjectName(u"mortgagePriceFormFrame")
        self.mortgagePriceFormFrame.setMinimumSize(QSize(0, 0))
        self.mortgagePriceFormFrame.setFrameShape(QFrame.StyledPanel)
        self.mortgagePriceFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.mortgagePriceFormFrame)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.mortgagePriceFormLbl = QLabel(self.mortgagePriceFormFrame)
        self.mortgagePriceFormLbl.setObjectName(u"mortgagePriceFormLbl")
        self.mortgagePriceFormLbl.setStyleSheet(u"label")

        self.verticalLayout_66.addWidget(self.mortgagePriceFormLbl)

        self.mortgagePriceFormError = QLabel(self.mortgagePriceFormFrame)
        self.mortgagePriceFormError.setObjectName(u"mortgagePriceFormError")

        self.verticalLayout_66.addWidget(self.mortgagePriceFormError)

        self.mortgagePriceFormInpt = QLineEdit(self.mortgagePriceFormFrame)
        self.mortgagePriceFormInpt.setObjectName(u"mortgagePriceFormInpt")

        self.verticalLayout_66.addWidget(self.mortgagePriceFormInpt)


        self.gridLayout_6.addWidget(self.mortgagePriceFormFrame, 2, 2, 1, 1)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 0))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_36)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_20 = QLabel(self.frame_36)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"label")

        self.verticalLayout_61.addWidget(self.label_20)

        self.meterageFormError_2 = QLabel(self.frame_36)
        self.meterageFormError_2.setObjectName(u"meterageFormError_2")

        self.verticalLayout_61.addWidget(self.meterageFormError_2)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, 20, -1)
        self.radioButton_2 = QRadioButton(self.frame_36)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_15.addWidget(self.radioButton_2, 0, Qt.AlignLeft)

        self.radioButton = QRadioButton(self.frame_36)
        self.buttonGroup_2.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_15.addWidget(self.radioButton, 0, Qt.AlignLeft)


        self.verticalLayout_61.addLayout(self.verticalLayout_15)


        self.gridLayout_6.addWidget(self.frame_36, 1, 2, 1, 1)

        self.unitPriceFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.unitPriceFormFrame.setObjectName(u"unitPriceFormFrame")
        self.unitPriceFormFrame.setFrameShape(QFrame.StyledPanel)
        self.unitPriceFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.unitPriceFormFrame)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.unitPriceFormLbl = QLabel(self.unitPriceFormFrame)
        self.unitPriceFormLbl.setObjectName(u"unitPriceFormLbl")
        self.unitPriceFormLbl.setStyleSheet(u"label")

        self.verticalLayout_65.addWidget(self.unitPriceFormLbl)

        self.unitPriceFormError = QLabel(self.unitPriceFormFrame)
        self.unitPriceFormError.setObjectName(u"unitPriceFormError")

        self.verticalLayout_65.addWidget(self.unitPriceFormError)

        self.unitPriceFormInpt = QLineEdit(self.unitPriceFormFrame)
        self.unitPriceFormInpt.setObjectName(u"unitPriceFormInpt")

        self.verticalLayout_65.addWidget(self.unitPriceFormInpt)


        self.gridLayout_6.addWidget(self.unitPriceFormFrame, 1, 0, 1, 1)

        self.constructionYearFrame = QFrame(self.scrollAreaWidgetContents)
        self.constructionYearFrame.setObjectName(u"constructionYearFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.constructionYearFrame.sizePolicy().hasHeightForWidth())
        self.constructionYearFrame.setSizePolicy(sizePolicy)
        self.constructionYearFrame.setFrameShape(QFrame.StyledPanel)
        self.constructionYearFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.constructionYearFrame)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.constructionYearLbl = QLabel(self.constructionYearFrame)
        self.constructionYearLbl.setObjectName(u"constructionYearLbl")
        self.constructionYearLbl.setStyleSheet(u"label")

        self.verticalLayout_54.addWidget(self.constructionYearLbl)

        self.constructionYearError = QLabel(self.constructionYearFrame)
        self.constructionYearError.setObjectName(u"constructionYearError")

        self.verticalLayout_54.addWidget(self.constructionYearError)

        self.constructionYearInpt = QSpinBox(self.constructionYearFrame)
        self.constructionYearInpt.setObjectName(u"constructionYearInpt")

        self.verticalLayout_54.addWidget(self.constructionYearInpt)


        self.gridLayout_6.addWidget(self.constructionYearFrame, 3, 1, 1, 1)

        self.totalPriceFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.totalPriceFormFrame.setObjectName(u"totalPriceFormFrame")
        self.totalPriceFormFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPriceFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.totalPriceFormFrame)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.totalPriceFormLbl = QLabel(self.totalPriceFormFrame)
        self.totalPriceFormLbl.setObjectName(u"totalPriceFormLbl")
        self.totalPriceFormLbl.setStyleSheet(u"label")

        self.verticalLayout_62.addWidget(self.totalPriceFormLbl)

        self.totalPriceFormError = QLabel(self.totalPriceFormFrame)
        self.totalPriceFormError.setObjectName(u"totalPriceFormError")

        self.verticalLayout_62.addWidget(self.totalPriceFormError)

        self.totalPriceFormInpt = QLineEdit(self.totalPriceFormFrame)
        self.totalPriceFormInpt.setObjectName(u"totalPriceFormInpt")

        self.verticalLayout_62.addWidget(self.totalPriceFormInpt)


        self.gridLayout_6.addWidget(self.totalPriceFormFrame, 1, 1, 1, 1)

        self.totalBuildingUnitFrame = QFrame(self.scrollAreaWidgetContents)
        self.totalBuildingUnitFrame.setObjectName(u"totalBuildingUnitFrame")
        self.totalBuildingUnitFrame.setFrameShape(QFrame.StyledPanel)
        self.totalBuildingUnitFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.totalBuildingUnitFrame)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.totalBuildingUnitLbl = QLabel(self.totalBuildingUnitFrame)
        self.totalBuildingUnitLbl.setObjectName(u"totalBuildingUnitLbl")
        self.totalBuildingUnitLbl.setStyleSheet(u"label")

        self.verticalLayout_72.addWidget(self.totalBuildingUnitLbl)

        self.totalBuildingError = QLabel(self.totalBuildingUnitFrame)
        self.totalBuildingError.setObjectName(u"totalBuildingError")

        self.verticalLayout_72.addWidget(self.totalBuildingError)

        self.totalBuildingInpt = QSpinBox(self.totalBuildingUnitFrame)
        self.totalBuildingInpt.setObjectName(u"totalBuildingInpt")

        self.verticalLayout_72.addWidget(self.totalBuildingInpt)


        self.gridLayout_6.addWidget(self.totalBuildingUnitFrame, 5, 1, 1, 1)

        self.documentStatusFrame = QFrame(self.scrollAreaWidgetContents)
        self.documentStatusFrame.setObjectName(u"documentStatusFrame")
        self.documentStatusFrame.setFrameShape(QFrame.StyledPanel)
        self.documentStatusFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.documentStatusFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.documentStatusLbl = QLabel(self.documentStatusFrame)
        self.documentStatusLbl.setObjectName(u"documentStatusLbl")
        self.documentStatusLbl.setStyleSheet(u"label")

        self.verticalLayout_21.addWidget(self.documentStatusLbl)

        self.documentStatusError = QLabel(self.documentStatusFrame)
        self.documentStatusError.setObjectName(u"documentStatusError")

        self.verticalLayout_21.addWidget(self.documentStatusError)

        self.documentStatusInpt = QComboBox(self.documentStatusFrame)
        self.documentStatusInpt.setObjectName(u"documentStatusInpt")

        self.verticalLayout_21.addWidget(self.documentStatusInpt)


        self.gridLayout_6.addWidget(self.documentStatusFrame, 3, 2, 1, 1)

        self.compensationFormFrame = QFrame(self.scrollAreaWidgetContents)
        self.compensationFormFrame.setObjectName(u"compensationFormFrame")
        self.compensationFormFrame.setMinimumSize(QSize(0, 0))
        self.compensationFormFrame.setFrameShape(QFrame.StyledPanel)
        self.compensationFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.compensationFormFrame)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.compensationFormLbl = QLabel(self.compensationFormFrame)
        self.compensationFormLbl.setObjectName(u"compensationFormLbl")
        self.compensationFormLbl.setStyleSheet(u"label")

        self.verticalLayout_75.addWidget(self.compensationFormLbl)

        self.compensationFormError = QLabel(self.compensationFormFrame)
        self.compensationFormError.setObjectName(u"compensationFormError")

        self.verticalLayout_75.addWidget(self.compensationFormError)

        self.compensationFormOptionsFrame = QFrame(self.compensationFormFrame)
        self.compensationFormOptionsFrame.setObjectName(u"compensationFormOptionsFrame")
        self.compensationFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.compensationFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.compensationFormOptionsFrame)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")

        self.verticalLayout_75.addWidget(self.compensationFormOptionsFrame)


        self.gridLayout_6.addWidget(self.compensationFormFrame, 7, 2, 1, 1)

        self.frame_46 = QFrame(self.scrollAreaWidgetContents)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_46)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.compensationConditionFormLbl = QLabel(self.frame_46)
        self.compensationConditionFormLbl.setObjectName(u"compensationConditionFormLbl")
        self.compensationConditionFormLbl.setStyleSheet(u"label")

        self.verticalLayout_76.addWidget(self.compensationConditionFormLbl)

        self.compensationConditionFormError = QLabel(self.frame_46)
        self.compensationConditionFormError.setObjectName(u"compensationConditionFormError")

        self.verticalLayout_76.addWidget(self.compensationConditionFormError)

        self.compensationConditionFormInpt = QTextEdit(self.frame_46)
        self.compensationConditionFormInpt.setObjectName(u"compensationConditionFormInpt")

        self.verticalLayout_76.addWidget(self.compensationConditionFormInpt)


        self.gridLayout_6.addWidget(self.frame_46, 7, 1, 1, 1)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_34, 6, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 1)

        self.verticalLayout_14.addLayout(self.gridLayout_6)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -804, 676, 1234))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))
        self.label_35.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_18.addWidget(self.label_35, 0, Qt.AlignHCenter)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 20, -1, 20)
        self.privateYardMeterageFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.privateYardMeterageFormFrame.setObjectName(u"privateYardMeterageFormFrame")
        self.privateYardMeterageFormFrame.setFrameShape(QFrame.StyledPanel)
        self.privateYardMeterageFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.privateYardMeterageFormFrame)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.privateYardMeterageFormLbl = QLabel(self.privateYardMeterageFormFrame)
        self.privateYardMeterageFormLbl.setObjectName(u"privateYardMeterageFormLbl")

        self.verticalLayout_95.addWidget(self.privateYardMeterageFormLbl)

        self.privateYardMeterageFormError = QLabel(self.privateYardMeterageFormFrame)
        self.privateYardMeterageFormError.setObjectName(u"privateYardMeterageFormError")

        self.verticalLayout_95.addWidget(self.privateYardMeterageFormError)

        self.privateYardMeterageFormInpt = QSpinBox(self.privateYardMeterageFormFrame)
        self.privateYardMeterageFormInpt.setObjectName(u"privateYardMeterageFormInpt")

        self.verticalLayout_95.addWidget(self.privateYardMeterageFormInpt)


        self.gridLayout_5.addWidget(self.privateYardMeterageFormFrame, 4, 1, 1, 1)

        self.trassMeterageFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.trassMeterageFormFrame.setObjectName(u"trassMeterageFormFrame")
        self.trassMeterageFormFrame.setFrameShape(QFrame.StyledPanel)
        self.trassMeterageFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.trassMeterageFormFrame)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.trassMeterageFormLbl = QLabel(self.trassMeterageFormFrame)
        self.trassMeterageFormLbl.setObjectName(u"trassMeterageFormLbl")

        self.verticalLayout_87.addWidget(self.trassMeterageFormLbl)

        self.trassMeterageFormError = QLabel(self.trassMeterageFormFrame)
        self.trassMeterageFormError.setObjectName(u"trassMeterageFormError")

        self.verticalLayout_87.addWidget(self.trassMeterageFormError)

        self.trassMeterageFormInpt = QSpinBox(self.trassMeterageFormFrame)
        self.trassMeterageFormInpt.setObjectName(u"trassMeterageFormInpt")

        self.verticalLayout_87.addWidget(self.trassMeterageFormInpt)


        self.gridLayout_5.addWidget(self.trassMeterageFormFrame, 2, 1, 1, 1)

        self.parkingStatusFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.parkingStatusFormFrame.setObjectName(u"parkingStatusFormFrame")
        self.parkingStatusFormFrame.setFrameShape(QFrame.StyledPanel)
        self.parkingStatusFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.parkingStatusFormFrame)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.parkingStatusFormLbl = QLabel(self.parkingStatusFormFrame)
        self.parkingStatusFormLbl.setObjectName(u"parkingStatusFormLbl")

        self.verticalLayout_82.addWidget(self.parkingStatusFormLbl)

        self.parkingStatusFormError = QLabel(self.parkingStatusFormFrame)
        self.parkingStatusFormError.setObjectName(u"parkingStatusFormError")

        self.verticalLayout_82.addWidget(self.parkingStatusFormError)

        self.parkingStatusFormInpt = QComboBox(self.parkingStatusFormFrame)
        self.parkingStatusFormInpt.setObjectName(u"parkingStatusFormInpt")

        self.verticalLayout_82.addWidget(self.parkingStatusFormInpt)


        self.gridLayout_5.addWidget(self.parkingStatusFormFrame, 0, 0, 1, 1)

        self.privateYardFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.privateYardFormFrame.setObjectName(u"privateYardFormFrame")
        self.privateYardFormFrame.setFrameShape(QFrame.StyledPanel)
        self.privateYardFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.privateYardFormFrame)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.privateYardFormLbl = QLabel(self.privateYardFormFrame)
        self.privateYardFormLbl.setObjectName(u"privateYardFormLbl")

        self.verticalLayout_93.addWidget(self.privateYardFormLbl)

        self.privateYardFormError = QLabel(self.privateYardFormFrame)
        self.privateYardFormError.setObjectName(u"privateYardFormError")

        self.verticalLayout_93.addWidget(self.privateYardFormError)

        self.privateYardFormOptionsFrame = QFrame(self.privateYardFormFrame)
        self.privateYardFormOptionsFrame.setObjectName(u"privateYardFormOptionsFrame")
        self.privateYardFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.privateYardFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.privateYardFormOptionsFrame)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")

        self.verticalLayout_93.addWidget(self.privateYardFormOptionsFrame)


        self.gridLayout_5.addWidget(self.privateYardFormFrame, 4, 2, 1, 1)

        self.elevatorFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.elevatorFormFrame.setObjectName(u"elevatorFormFrame")
        self.elevatorFormFrame.setFrameShape(QFrame.StyledPanel)
        self.elevatorFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.elevatorFormFrame)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.elevatorFormLbl = QLabel(self.elevatorFormFrame)
        self.elevatorFormLbl.setObjectName(u"elevatorFormLbl")

        self.verticalLayout_96.addWidget(self.elevatorFormLbl)

        self.elevatorYardFormError = QLabel(self.elevatorFormFrame)
        self.elevatorYardFormError.setObjectName(u"elevatorYardFormError")

        self.verticalLayout_96.addWidget(self.elevatorYardFormError)

        self.elevatorFormOptionsFrame = QFrame(self.elevatorFormFrame)
        self.elevatorFormOptionsFrame.setObjectName(u"elevatorFormOptionsFrame")
        self.elevatorFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.elevatorFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.elevatorFormOptionsFrame)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")

        self.verticalLayout_96.addWidget(self.elevatorFormOptionsFrame)


        self.gridLayout_5.addWidget(self.elevatorFormFrame, 5, 2, 1, 1)

        self.balconyFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.balconyFormFrame.setObjectName(u"balconyFormFrame")
        self.balconyFormFrame.setFrameShape(QFrame.StyledPanel)
        self.balconyFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.balconyFormFrame)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.balconyFormLbl = QLabel(self.balconyFormFrame)
        self.balconyFormLbl.setObjectName(u"balconyFormLbl")

        self.verticalLayout_81.addWidget(self.balconyFormLbl)

        self.balconyFormError = QLabel(self.balconyFormFrame)
        self.balconyFormError.setObjectName(u"balconyFormError")

        self.verticalLayout_81.addWidget(self.balconyFormError)

        self.balconyFormOptionsFrame = QFrame(self.balconyFormFrame)
        self.balconyFormOptionsFrame.setObjectName(u"balconyFormOptionsFrame")
        self.balconyFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.balconyFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.balconyFormOptionsFrame)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")

        self.verticalLayout_81.addWidget(self.balconyFormOptionsFrame)


        self.gridLayout_5.addWidget(self.balconyFormFrame, 1, 2, 1, 1)

        self.warehouseFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.warehouseFormFrame.setObjectName(u"warehouseFormFrame")
        self.warehouseFormFrame.setFrameShape(QFrame.StyledPanel)
        self.warehouseFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.warehouseFormFrame)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.warehouseFormLbl = QLabel(self.warehouseFormFrame)
        self.warehouseFormLbl.setObjectName(u"warehouseFormLbl")

        self.verticalLayout_88.addWidget(self.warehouseFormLbl)

        self.warehouseFormError = QLabel(self.warehouseFormFrame)
        self.warehouseFormError.setObjectName(u"warehouseFormError")

        self.verticalLayout_88.addWidget(self.warehouseFormError)

        self.warehouseFormOptionsFrame = QFrame(self.warehouseFormFrame)
        self.warehouseFormOptionsFrame.setObjectName(u"warehouseFormOptionsFrame")
        self.warehouseFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.warehouseFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.warehouseFormOptionsFrame)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")

        self.verticalLayout_88.addWidget(self.warehouseFormOptionsFrame)


        self.gridLayout_5.addWidget(self.warehouseFormFrame, 3, 2, 1, 1)

        self.parkingCountFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.parkingCountFormFrame.setObjectName(u"parkingCountFormFrame")
        self.parkingCountFormFrame.setFrameShape(QFrame.StyledPanel)
        self.parkingCountFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.parkingCountFormFrame)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.parkingCountFormLbl = QLabel(self.parkingCountFormFrame)
        self.parkingCountFormLbl.setObjectName(u"parkingCountFormLbl")

        self.verticalLayout_80.addWidget(self.parkingCountFormLbl)

        self.parkingCountFormError = QLabel(self.parkingCountFormFrame)
        self.parkingCountFormError.setObjectName(u"parkingCountFormError")

        self.verticalLayout_80.addWidget(self.parkingCountFormError)

        self.parkingCountFormInpt = QSpinBox(self.parkingCountFormFrame)
        self.parkingCountFormInpt.setObjectName(u"parkingCountFormInpt")

        self.verticalLayout_80.addWidget(self.parkingCountFormInpt)


        self.gridLayout_5.addWidget(self.parkingCountFormFrame, 0, 1, 1, 1)

        self.balconyMeterageFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.balconyMeterageFormFrame.setObjectName(u"balconyMeterageFormFrame")
        self.balconyMeterageFormFrame.setFrameShape(QFrame.StyledPanel)
        self.balconyMeterageFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.balconyMeterageFormFrame)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.balconyMeterageFormLbl = QLabel(self.balconyMeterageFormFrame)
        self.balconyMeterageFormLbl.setObjectName(u"balconyMeterageFormLbl")

        self.verticalLayout_84.addWidget(self.balconyMeterageFormLbl)

        self.balconyMeterageFormError = QLabel(self.balconyMeterageFormFrame)
        self.balconyMeterageFormError.setObjectName(u"balconyMeterageFormError")

        self.verticalLayout_84.addWidget(self.balconyMeterageFormError)

        self.balconyMeterageFormInpt = QSpinBox(self.balconyMeterageFormFrame)
        self.balconyMeterageFormInpt.setObjectName(u"balconyMeterageFormInpt")

        self.verticalLayout_84.addWidget(self.balconyMeterageFormInpt)


        self.gridLayout_5.addWidget(self.balconyMeterageFormFrame, 1, 1, 1, 1)

        self.trassFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.trassFormFrame.setObjectName(u"trassFormFrame")
        self.trassFormFrame.setFrameShape(QFrame.StyledPanel)
        self.trassFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.trassFormFrame)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.trassFormLbl = QLabel(self.trassFormFrame)
        self.trassFormLbl.setObjectName(u"trassFormLbl")

        self.verticalLayout_85.addWidget(self.trassFormLbl)

        self.trassFormError = QLabel(self.trassFormFrame)
        self.trassFormError.setObjectName(u"trassFormError")

        self.verticalLayout_85.addWidget(self.trassFormError)

        self.trassFormOptionsFrame = QFrame(self.trassFormFrame)
        self.trassFormOptionsFrame.setObjectName(u"trassFormOptionsFrame")
        self.trassFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.trassFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.trassFormOptionsFrame)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")

        self.verticalLayout_85.addWidget(self.trassFormOptionsFrame)


        self.gridLayout_5.addWidget(self.trassFormFrame, 2, 2, 1, 1)

        self.warehouseMeterageFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.warehouseMeterageFormFrame.setObjectName(u"warehouseMeterageFormFrame")
        self.warehouseMeterageFormFrame.setFrameShape(QFrame.StyledPanel)
        self.warehouseMeterageFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.warehouseMeterageFormFrame)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.warehouseMeterageFormLbl = QLabel(self.warehouseMeterageFormFrame)
        self.warehouseMeterageFormLbl.setObjectName(u"warehouseMeterageFormLbl")

        self.verticalLayout_90.addWidget(self.warehouseMeterageFormLbl)

        self.warehouseMeterageFormError = QLabel(self.warehouseMeterageFormFrame)
        self.warehouseMeterageFormError.setObjectName(u"warehouseMeterageFormError")

        self.verticalLayout_90.addWidget(self.warehouseMeterageFormError)

        self.warehouseMeterageFormInpt = QSpinBox(self.warehouseMeterageFormFrame)
        self.warehouseMeterageFormInpt.setObjectName(u"warehouseMeterageFormInpt")

        self.verticalLayout_90.addWidget(self.warehouseMeterageFormInpt)


        self.gridLayout_5.addWidget(self.warehouseMeterageFormFrame, 3, 1, 1, 1)

        self.parkingFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.parkingFormFrame.setObjectName(u"parkingFormFrame")
        self.parkingFormFrame.setFrameShape(QFrame.StyledPanel)
        self.parkingFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.parkingFormFrame)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.parkingFormLbl = QLabel(self.parkingFormFrame)
        self.parkingFormLbl.setObjectName(u"parkingFormLbl")

        self.verticalLayout_78.addWidget(self.parkingFormLbl)

        self.parkingFormError = QLabel(self.parkingFormFrame)
        self.parkingFormError.setObjectName(u"parkingFormError")

        self.verticalLayout_78.addWidget(self.parkingFormError)

        self.parkingFormOptionsFrame = QFrame(self.parkingFormFrame)
        self.parkingFormOptionsFrame.setObjectName(u"parkingFormOptionsFrame")
        self.parkingFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.parkingFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.parkingFormOptionsFrame)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")

        self.verticalLayout_78.addWidget(self.parkingFormOptionsFrame)


        self.gridLayout_5.addWidget(self.parkingFormFrame, 0, 2, 1, 1)

        self.branchFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.branchFormFrame.setObjectName(u"branchFormFrame")
        self.branchFormFrame.setFrameShape(QFrame.StyledPanel)
        self.branchFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.branchFormFrame)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.branchFormLbl = QLabel(self.branchFormFrame)
        self.branchFormLbl.setObjectName(u"branchFormLbl")

        self.verticalLayout_98.addWidget(self.branchFormLbl)

        self.branchFormError = QLabel(self.branchFormFrame)
        self.branchFormError.setObjectName(u"branchFormError")

        self.verticalLayout_98.addWidget(self.branchFormError)

        self.branchFormOptionsFrame = QFrame(self.branchFormFrame)
        self.branchFormOptionsFrame.setObjectName(u"branchFormOptionsFrame")
        self.branchFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.branchFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.branchFormOptionsFrame)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")

        self.verticalLayout_98.addWidget(self.branchFormOptionsFrame)


        self.gridLayout_5.addWidget(self.branchFormFrame, 6, 2, 1, 1)

        self.otherFeaturesFormFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.otherFeaturesFormFrame.setObjectName(u"otherFeaturesFormFrame")
        self.otherFeaturesFormFrame.setFrameShape(QFrame.StyledPanel)
        self.otherFeaturesFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.otherFeaturesFormFrame)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.otherFeaturesFormLbl = QLabel(self.otherFeaturesFormFrame)
        self.otherFeaturesFormLbl.setObjectName(u"otherFeaturesFormLbl")

        self.verticalLayout_100.addWidget(self.otherFeaturesFormLbl)

        self.otherFeaturesFormError = QLabel(self.otherFeaturesFormFrame)
        self.otherFeaturesFormError.setObjectName(u"otherFeaturesFormError")

        self.verticalLayout_100.addWidget(self.otherFeaturesFormError)

        self.otherFeaturesFormOptionsFrame = QFrame(self.otherFeaturesFormFrame)
        self.otherFeaturesFormOptionsFrame.setObjectName(u"otherFeaturesFormOptionsFrame")
        self.otherFeaturesFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.otherFeaturesFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.otherFeaturesFormOptionsFrame)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")

        self.verticalLayout_100.addWidget(self.otherFeaturesFormOptionsFrame)


        self.gridLayout_5.addWidget(self.otherFeaturesFormFrame, 6, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_5)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -343, 676, 1168))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_51 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_23.addWidget(self.label_51)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.floorMaterialFormFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.floorMaterialFormFrame.setObjectName(u"floorMaterialFormFrame")
        self.floorMaterialFormFrame.setFrameShape(QFrame.StyledPanel)
        self.floorMaterialFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.floorMaterialFormFrame)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.floorMaterialFormLbl = QLabel(self.floorMaterialFormFrame)
        self.floorMaterialFormLbl.setObjectName(u"floorMaterialFormLbl")

        self.verticalLayout_102.addWidget(self.floorMaterialFormLbl)

        self.floorMaterialFormError = QLabel(self.floorMaterialFormFrame)
        self.floorMaterialFormError.setObjectName(u"floorMaterialFormError")

        self.verticalLayout_102.addWidget(self.floorMaterialFormError)

        self.floorMaterialFormOptionsFrame = QFrame(self.floorMaterialFormFrame)
        self.floorMaterialFormOptionsFrame.setObjectName(u"floorMaterialFormOptionsFrame")
        self.floorMaterialFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.floorMaterialFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.floorMaterialFormOptionsFrame)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")

        self.verticalLayout_102.addWidget(self.floorMaterialFormOptionsFrame)

        self.otherFloorMaterialFormInpt = QLineEdit(self.floorMaterialFormFrame)
        self.otherFloorMaterialFormInpt.setObjectName(u"otherFloorMaterialFormInpt")

        self.verticalLayout_102.addWidget(self.otherFloorMaterialFormInpt)


        self.gridLayout_3.addWidget(self.floorMaterialFormFrame, 0, 2, 1, 1)

        self.wallsMaterialFormFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.wallsMaterialFormFrame.setObjectName(u"wallsMaterialFormFrame")
        self.wallsMaterialFormFrame.setFrameShape(QFrame.StyledPanel)
        self.wallsMaterialFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.wallsMaterialFormFrame)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.wallsMaterialFormLbl = QLabel(self.wallsMaterialFormFrame)
        self.wallsMaterialFormLbl.setObjectName(u"wallsMaterialFormLbl")

        self.verticalLayout_104.addWidget(self.wallsMaterialFormLbl)

        self.wallsMaterialFormError = QLabel(self.wallsMaterialFormFrame)
        self.wallsMaterialFormError.setObjectName(u"wallsMaterialFormError")

        self.verticalLayout_104.addWidget(self.wallsMaterialFormError)

        self.wallsMaterialFormOptionsFrame = QFrame(self.wallsMaterialFormFrame)
        self.wallsMaterialFormOptionsFrame.setObjectName(u"wallsMaterialFormOptionsFrame")
        self.wallsMaterialFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.wallsMaterialFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.wallsMaterialFormOptionsFrame)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")

        self.verticalLayout_104.addWidget(self.wallsMaterialFormOptionsFrame)

        self.otherWallsMaterialFormInpt = QLineEdit(self.wallsMaterialFormFrame)
        self.otherWallsMaterialFormInpt.setObjectName(u"otherWallsMaterialFormInpt")

        self.verticalLayout_104.addWidget(self.otherWallsMaterialFormInpt)


        self.gridLayout_3.addWidget(self.wallsMaterialFormFrame, 0, 1, 1, 1)

        self.kitchenMaterialFormFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.kitchenMaterialFormFrame.setObjectName(u"kitchenMaterialFormFrame")
        self.kitchenMaterialFormFrame.setFrameShape(QFrame.StyledPanel)
        self.kitchenMaterialFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.kitchenMaterialFormFrame)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.kitchenMaterialFormLbl = QLabel(self.kitchenMaterialFormFrame)
        self.kitchenMaterialFormLbl.setObjectName(u"kitchenMaterialFormLbl")

        self.verticalLayout_110.addWidget(self.kitchenMaterialFormLbl)

        self.kitchenMaterialFormError = QLabel(self.kitchenMaterialFormFrame)
        self.kitchenMaterialFormError.setObjectName(u"kitchenMaterialFormError")

        self.verticalLayout_110.addWidget(self.kitchenMaterialFormError)

        self.kitchenMaterialFormOptionsFrame = QFrame(self.kitchenMaterialFormFrame)
        self.kitchenMaterialFormOptionsFrame.setObjectName(u"kitchenMaterialFormOptionsFrame")
        self.kitchenMaterialFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.kitchenMaterialFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.kitchenMaterialFormOptionsFrame)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")

        self.verticalLayout_110.addWidget(self.kitchenMaterialFormOptionsFrame)

        self.otherKitchenMaterialFormInpt = QLineEdit(self.kitchenMaterialFormFrame)
        self.otherKitchenMaterialFormInpt.setObjectName(u"otherKitchenMaterialFormInpt")

        self.verticalLayout_110.addWidget(self.otherKitchenMaterialFormInpt)


        self.gridLayout_3.addWidget(self.kitchenMaterialFormFrame, 1, 1, 1, 1)

        self.cabinetsMaterialFormFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.cabinetsMaterialFormFrame.setObjectName(u"cabinetsMaterialFormFrame")
        self.cabinetsMaterialFormFrame.setFrameShape(QFrame.StyledPanel)
        self.cabinetsMaterialFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.cabinetsMaterialFormFrame)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.cabinetsMaterialFormLbl = QLabel(self.cabinetsMaterialFormFrame)
        self.cabinetsMaterialFormLbl.setObjectName(u"cabinetsMaterialFormLbl")

        self.verticalLayout_108.addWidget(self.cabinetsMaterialFormLbl)

        self.cabinetsMaterialFormError = QLabel(self.cabinetsMaterialFormFrame)
        self.cabinetsMaterialFormError.setObjectName(u"cabinetsMaterialFormError")

        self.verticalLayout_108.addWidget(self.cabinetsMaterialFormError)

        self.cabinetsMaterialFormOptionsFrame = QFrame(self.cabinetsMaterialFormFrame)
        self.cabinetsMaterialFormOptionsFrame.setObjectName(u"cabinetsMaterialFormOptionsFrame")
        self.cabinetsMaterialFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.cabinetsMaterialFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.cabinetsMaterialFormOptionsFrame)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")

        self.verticalLayout_108.addWidget(self.cabinetsMaterialFormOptionsFrame)

        self.otherCabinetsMaterialFormInpt = QLineEdit(self.cabinetsMaterialFormFrame)
        self.otherCabinetsMaterialFormInpt.setObjectName(u"otherCabinetsMaterialFormInpt")

        self.verticalLayout_108.addWidget(self.otherCabinetsMaterialFormInpt)


        self.gridLayout_3.addWidget(self.cabinetsMaterialFormFrame, 1, 2, 1, 1)

        self.ceilingMaterialFormFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.ceilingMaterialFormFrame.setObjectName(u"ceilingMaterialFormFrame")
        self.ceilingMaterialFormFrame.setFrameShape(QFrame.StyledPanel)
        self.ceilingMaterialFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.ceilingMaterialFormFrame)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.ceilingMaterialFormLbl = QLabel(self.ceilingMaterialFormFrame)
        self.ceilingMaterialFormLbl.setObjectName(u"ceilingMaterialFormLbl")

        self.verticalLayout_106.addWidget(self.ceilingMaterialFormLbl)

        self.ceilingMaterialFormError = QLabel(self.ceilingMaterialFormFrame)
        self.ceilingMaterialFormError.setObjectName(u"ceilingMaterialFormError")

        self.verticalLayout_106.addWidget(self.ceilingMaterialFormError)

        self.ceilingMaterialFormOptionsFrame = QFrame(self.ceilingMaterialFormFrame)
        self.ceilingMaterialFormOptionsFrame.setObjectName(u"ceilingMaterialFormOptionsFrame")
        self.ceilingMaterialFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.ceilingMaterialFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.ceilingMaterialFormOptionsFrame)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")

        self.verticalLayout_106.addWidget(self.ceilingMaterialFormOptionsFrame)

        self.otherCeilingMaterialFormInpt = QLineEdit(self.ceilingMaterialFormFrame)
        self.otherCeilingMaterialFormInpt.setObjectName(u"otherCeilingMaterialFormInpt")

        self.verticalLayout_106.addWidget(self.otherCeilingMaterialFormInpt)


        self.gridLayout_3.addWidget(self.ceilingMaterialFormFrame, 0, 0, 1, 1)

        self.coolingSystemFormFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.coolingSystemFormFrame.setObjectName(u"coolingSystemFormFrame")
        self.coolingSystemFormFrame.setFrameShape(QFrame.StyledPanel)
        self.coolingSystemFormFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.coolingSystemFormFrame)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.coolingSystemFormLbl = QLabel(self.coolingSystemFormFrame)
        self.coolingSystemFormLbl.setObjectName(u"coolingSystemFormLbl")

        self.verticalLayout_112.addWidget(self.coolingSystemFormLbl)

        self.coolingSystemFormError = QLabel(self.coolingSystemFormFrame)
        self.coolingSystemFormError.setObjectName(u"coolingSystemFormError")

        self.verticalLayout_112.addWidget(self.coolingSystemFormError)

        self.coolingSystemFormOptionsFrame = QFrame(self.coolingSystemFormFrame)
        self.coolingSystemFormOptionsFrame.setObjectName(u"coolingSystemFormOptionsFrame")
        self.coolingSystemFormOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.coolingSystemFormOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.coolingSystemFormOptionsFrame)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")

        self.verticalLayout_112.addWidget(self.coolingSystemFormOptionsFrame)

        self.otherCoolingSystemFormInpt = QLineEdit(self.coolingSystemFormFrame)
        self.otherCoolingSystemFormInpt.setObjectName(u"otherCoolingSystemFormInpt")

        self.verticalLayout_112.addWidget(self.otherCoolingSystemFormInpt)


        self.gridLayout_3.addWidget(self.coolingSystemFormFrame, 2, 2, 1, 1)

        self.cabinetsMaterialFormFrame_3 = QFrame(self.scrollAreaWidgetContents_4)
        self.cabinetsMaterialFormFrame_3.setObjectName(u"cabinetsMaterialFormFrame_3")
        self.cabinetsMaterialFormFrame_3.setFrameShape(QFrame.StyledPanel)
        self.cabinetsMaterialFormFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.cabinetsMaterialFormFrame_3)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.cabinetsMaterialFormLbl_3 = QLabel(self.cabinetsMaterialFormFrame_3)
        self.cabinetsMaterialFormLbl_3.setObjectName(u"cabinetsMaterialFormLbl_3")

        self.verticalLayout_114.addWidget(self.cabinetsMaterialFormLbl_3)

        self.cabinetsMaterialFormError_3 = QLabel(self.cabinetsMaterialFormFrame_3)
        self.cabinetsMaterialFormError_3.setObjectName(u"cabinetsMaterialFormError_3")

        self.verticalLayout_114.addWidget(self.cabinetsMaterialFormError_3)

        self.cabinetsMaterialFormOptionsFrame_3 = QFrame(self.cabinetsMaterialFormFrame_3)
        self.cabinetsMaterialFormOptionsFrame_3.setObjectName(u"cabinetsMaterialFormOptionsFrame_3")
        self.cabinetsMaterialFormOptionsFrame_3.setFrameShape(QFrame.StyledPanel)
        self.cabinetsMaterialFormOptionsFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.cabinetsMaterialFormOptionsFrame_3)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")

        self.verticalLayout_114.addWidget(self.cabinetsMaterialFormOptionsFrame_3)

        self.otherCabinetsMaterialFormInpt_3 = QLineEdit(self.cabinetsMaterialFormFrame_3)
        self.otherCabinetsMaterialFormInpt_3.setObjectName(u"otherCabinetsMaterialFormInpt_3")

        self.verticalLayout_114.addWidget(self.otherCabinetsMaterialFormInpt_3)


        self.gridLayout_3.addWidget(self.cabinetsMaterialFormFrame_3, 2, 1, 1, 1)


        self.verticalLayout_23.addLayout(self.gridLayout_3)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(100)
        self.gridLayout_12.setVerticalSpacing(20)
        self.lineEdit_26 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_12.addWidget(self.lineEdit_26, 3, 0, 1, 1)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 50))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_21, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 50))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_22, 1, 0, 1, 1)

        self.frame_23 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 50))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_23, 5, 1, 1, 1)

        self.label_72 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_12.addWidget(self.label_72, 0, 1, 1, 1)

        self.lineEdit_27 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_12.addWidget(self.lineEdit_27, 6, 1, 1, 1)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_12.addWidget(self.label_71, 0, 0, 1, 1)

        self.lineEdit_28 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.gridLayout_12.addWidget(self.lineEdit_28, 6, 0, 1, 1)

        self.label_74 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_12.addWidget(self.label_74, 4, 1, 1, 1)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_24, 5, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_12.addWidget(self.lineEdit_25, 3, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_19, 2, 1, 1, 1)

        self.label_73 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_12.addWidget(self.label_73, 4, 0, 1, 1)

        self.gridLayout_12.setColumnStretch(0, 1)

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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 822, 3257))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy1)
        self.label_135.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_135, 0, Qt.AlignHCenter)

        self.label_136 = QLabel(self.priceBoxFrame)
        self.label_136.setObjectName(u"label_136")
        sizePolicy1.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy1)
        self.label_136.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_136, 0, Qt.AlignHCenter)

        self.label_137 = QLabel(self.priceBoxFrame)
        self.label_137.setObjectName(u"label_137")
        sizePolicy1.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy1)
        self.label_137.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_137, 0, Qt.AlignHCenter)

        self.label_138 = QLabel(self.priceBoxFrame)
        self.label_138.setObjectName(u"label_138")
        sizePolicy1.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy1)
        self.label_138.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_138, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_140 = QLabel(self.priceBoxFrame)
        self.label_140.setObjectName(u"label_140")
        sizePolicy1.setHeightForWidth(self.label_140.sizePolicy().hasHeightForWidth())
        self.label_140.setSizePolicy(sizePolicy1)
        self.label_140.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_140, 0, Qt.AlignHCenter)

        self.label_139 = QLabel(self.priceBoxFrame)
        self.label_139.setObjectName(u"label_139")
        sizePolicy1.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy1)
        self.label_139.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_139, 0, Qt.AlignHCenter)

        self.label_142 = QLabel(self.priceBoxFrame)
        self.label_142.setObjectName(u"label_142")
        sizePolicy1.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy1)
        self.label_142.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_142, 0, Qt.AlignHCenter)

        self.label_141 = QLabel(self.priceBoxFrame)
        self.label_141.setObjectName(u"label_141")
        sizePolicy1.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy1)
        self.label_106.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_106)


        self.verticalLayout_28.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.label_133 = QLabel(self.frame_40)
        self.label_133.setObjectName(u"label_133")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy2)
        self.label_133.setStyleSheet(u"title")

        self.horizontalLayout_14.addWidget(self.label_133)

        self.label_107 = QLabel(self.frame_40)
        self.label_107.setObjectName(u"label_107")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy3)
        self.label_107.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_40)
        self.label_108.setObjectName(u"label_108")
        sizePolicy1.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy1)
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
        sizePolicy3.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_221.sizePolicy().hasHeightForWidth())
        self.label_221.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_236.sizePolicy().hasHeightForWidth())
        self.label_236.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_234.sizePolicy().hasHeightForWidth())
        self.label_234.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_238.sizePolicy().hasHeightForWidth())
        self.label_238.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_240.sizePolicy().hasHeightForWidth())
        self.label_240.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_242.sizePolicy().hasHeightForWidth())
        self.label_242.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy3)

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

        self.label_79 = QLabel(self.sidebarMenuFrame)
        self.label_79.setObjectName(u"label_79")

        self.verticalLayout.addWidget(self.label_79)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_23)


        self.horizontalLayout_5.addWidget(self.sidebarMenuFrame)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 913, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.form_stackwidget.setCurrentIndex(5)
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
        self.melkCategoryFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u0645\u0644\u06a9", None))
        self.melkCategoryFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.melkCategoryFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.melkCategoryFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.melkCategoryFormInpt.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633", None))
        self.regionFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646\u0637\u0642\u0647", None))
        self.regionFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.regionFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.regionFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.cityFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0647\u0631", None))
        self.cityFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.cityFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.cityFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.streetFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644\u0647", None))
        self.streetFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.streetFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.streetFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.addressFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633", None))
        self.addressFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.addressFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.addressFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u0627\u0644\u06a9", None))
        self.owner1PhoneNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062b\u0627\u0628\u062a \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644", None))
        self.owner1PhoneNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.owner1PhoneNumberFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.owner1PhoneNumberFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.owner1MobileNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644", None))
        self.owner1MobileNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.owner1MobileNumberFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.owner1MobileNumberFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.owner2MobileNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0627\u0644\u06a9 \u062f\u0648\u0645", None))
        self.owner2MobileNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.owner2MobileNumberFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.owner2MobileNumberFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.ownerName2FormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0627\u0644\u06a9 \u062f\u0648\u0645", None))
        self.ownerName2FormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ownerName2FormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.ownerName2FormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.tenantNameFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0633\u062a\u0627\u062c\u0631", None))
        self.tenantNameFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.tenantNameFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.tenantNameFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.ownerName1FormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0627\u0644\u06a9 \u0627\u0648\u0644", None))
        self.ownerName1FormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ownerName1FormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.ownerName1FormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.tenantPhoneNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0645\u0633\u062a\u0627\u062c\u0631", None))
        self.tenantPhoneNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.tenantPhoneNumberFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.tenantPhoneNumberFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.guardNameFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0646\u06af\u0647\u0628\u0627\u0646", None))
        self.guardNameFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.guardNameFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.guardNameFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.guardPhoneNumberFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0646\u06af\u0647\u0628\u0627\u0646", None))
        self.guardPhoneNumberFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.guardPhoneNumberFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.guardPhoneNumberFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.ownerDescriptionFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a ", None))
        self.ownerDescriptionFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ownerDescriptionFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.ownerDescriptionFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0644\u06cc", None))
        self.lightDirectionLbl.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0647\u062a \u0646\u0648\u0631\u06af\u06cc\u0631\u06cc", None))
        self.lightDirectionLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.lightDirectionError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.lightDirectionError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.meterageFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698", None))
        self.meterageFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.meterageFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.meterageFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.floorCounFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u0637\u0628\u0642\u0627\u062a", None))
        self.floorCounFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.floorCounFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.floorCounFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.rebuildingFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0628\u0627\u0632\u0633\u0627\u0632\u06cc", None))
        self.rebuildingFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.rebuildingFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.rebuildingFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u0633\u0627\u0632\u06cc \u0634\u062f\u0647", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u0631", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0647\u06cc\u0686\u06a9\u062f\u0627\u0645", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0648\u0627\u062d\u062f \u062f\u0631 \u0637\u0628\u0642\u0647", None))
        self.label_32.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.floorFormError_4.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.floorFormError_4.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.floorFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0628\u0642\u0647", None))
        self.floorFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.floorFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.floorFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.rentPriceFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0627\u062c\u0627\u0631\u0647", None))
        self.rentPriceFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.rentPriceFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.rentPriceFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.mortgagePriceFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0631\u0647\u0646", None))
        self.mortgagePriceFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.mortgagePriceFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.mortgagePriceFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0627\u0633\u0628\u0647 \u0642\u06cc\u0645\u062a \u0628\u0631\u0627\u0633\u0627\u0633", None))
        self.label_20.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.meterageFormError_2.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.meterageFormError_2.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u06a9\u0644", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u0631\u062a\u0631", None))
        self.unitPriceFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u062a\u0631 \u0645\u0631\u0628\u0639", None))
        self.unitPriceFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.unitPriceFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.unitPriceFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.constructionYearLbl.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0644 \u0633\u0627\u062e\u062a", None))
        self.constructionYearLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.constructionYearError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.constructionYearError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.totalPriceFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u06a9\u0644", None))
        self.totalPriceFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.totalPriceFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.totalPriceFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.totalBuildingUnitLbl.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u0648\u0627\u062d\u062f\u0647\u0627", None))
        self.totalBuildingUnitLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.totalBuildingError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.totalBuildingError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.documentStatusLbl.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0633\u0646\u062f", None))
        self.documentStatusLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.documentStatusError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.documentStatusError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.compensationFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0639\u0627\u0648\u0636\u0647:", None))
        self.compensationFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.compensationFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.compensationFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.compensationConditionFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u0627\u06cc\u0637 \u0645\u0639\u0627\u0648\u0636\u0647", None))
        self.compensationConditionFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.compensationConditionFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.compensationConditionFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u06a9\u0627\u0646\u0627\u062a", None))
        self.privateYardMeterageFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u062d\u06cc\u0627\u062a \u0627\u062e\u062a\u0635\u0627\u0635\u06cc", None))
        self.privateYardMeterageFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.privateYardMeterageFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.privateYardMeterageFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.trassMeterageFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u0628\u0647\u0627\u0631\u062e\u0648\u0627\u0628", None))
        self.trassMeterageFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.trassMeterageFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.trassMeterageFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.parkingStatusFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u067e\u0627\u0631\u06a9\u06cc\u0646\u06af", None))
        self.parkingStatusFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.parkingStatusFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.parkingStatusFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.privateYardFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u062d\u06cc\u0627\u0637 \u0627\u062e\u062a\u0635\u0627\u0635\u06cc", None))
        self.privateYardFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.privateYardFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.privateYardFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.elevatorFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0633\u0627\u0646\u0633\u0648\u0631", None))
        self.elevatorFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.elevatorYardFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.elevatorYardFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.balconyFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0644\u06a9\u0646", None))
        self.balconyFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.balconyFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.balconyFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.warehouseFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631\u06cc", None))
        self.warehouseFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.warehouseFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.warehouseFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.parkingCountFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u067e\u0627\u0631\u06a9\u06cc\u0646\u06a9", None))
        self.parkingCountFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.parkingCountFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.parkingCountFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.balconyMeterageFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u0628\u0627\u0644\u06a9\u0646", None))
        self.balconyMeterageFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.balconyMeterageFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.balconyMeterageFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.trassFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0647\u0627\u0631\u062e\u0648\u0627\u0628", None))
        self.trassFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.trassFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.trassFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.warehouseMeterageFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0631\u0627\u0698 \u0627\u0646\u0628\u0627\u0631\u06cc", None))
        self.warehouseMeterageFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.warehouseMeterageFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.warehouseMeterageFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.parkingFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u0631\u06a9\u06cc\u0646\u06a9", None))
        self.parkingFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.parkingFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.parkingFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.branchFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0634\u0639\u0627\u0628\u0627\u062a", None))
        self.branchFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.branchFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.branchFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.otherFeaturesFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u06cc\u0631 \u0627\u0645\u06a9\u0627\u0646\u0627\u062a", None))
        self.otherFeaturesFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.otherFeaturesFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.otherFeaturesFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u062a\u0631\u06cc\u0627\u0644", None))
        self.floorMaterialFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0641", None))
        self.floorMaterialFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.floorMaterialFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.floorMaterialFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.wallsMaterialFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u0648\u0627\u0631\u0647\u0627", None))
        self.wallsMaterialFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.wallsMaterialFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.wallsMaterialFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.kitchenMaterialFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0634\u067e\u0632\u062e\u0627\u0646\u0647", None))
        self.kitchenMaterialFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.kitchenMaterialFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.kitchenMaterialFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.cabinetsMaterialFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0628\u06cc\u0646\u062a\u200c\u200c\u0647\u0627", None))
        self.cabinetsMaterialFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.cabinetsMaterialFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.cabinetsMaterialFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.ceilingMaterialFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0642\u0641", None))
        self.ceilingMaterialFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.ceilingMaterialFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.ceilingMaterialFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.coolingSystemFormLbl.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u0633\u0631\u0645\u0627\u06cc\u0634\u06cc", None))
        self.coolingSystemFormLbl.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.coolingSystemFormError.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.coolingSystemFormError.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.cabinetsMaterialFormLbl_3.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u06af\u0631\u0645\u0627\u06cc\u0634\u06cc", None))
        self.cabinetsMaterialFormLbl_3.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.cabinetsMaterialFormError_3.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.cabinetsMaterialFormError_3.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628", None))
        self.label_72.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0646\u062c\u0631\u0647", None))
        self.label_71.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0645\u0627\u0645", None))
        self.label_74.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u0648\u06cc\u0633 \u0628\u0647\u062f\u0627\u0634\u062a\u06cc", None))
        self.label_73.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-label", None))
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
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0637\u0627 \u0631\u062e \u062f\u0627\u062f\u0647", None))
        self.label_79.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"form-field-error", None))
    # retranslateUi


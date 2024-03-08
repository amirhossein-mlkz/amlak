import sys
import time


from PySide6.QtWidgets import QMainWindow, QHeaderView, QApplication
from PySide6 import QtCore


from uiFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from uiUtils.uiStyler import Styler
from pagesUI.dashboardUI import dashboardPageUI
from estateForm.estateFormHandler import formUI


# ui_file = QFile("mainwindow.ui")
# ui_file.open(QFile.ReadOnly)

# loader = QUiLoader()
# window = loader.load(ui_file)
# window.show()


class mainUI(QMainWindow):

    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_

    """
    def __init__(self):
        """this function is used to laod ui file and build GUI application"""
        super(mainUI, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        uiStyler = Styler(self.ui)
        uiStyler.render()

        self.dashboard_menu_items = {
            'dashboard':{'btn':self.ui.sidebar_dashboard_btn, 'page':self.ui.page_dashboard},
        }

        self.dashboardPageUI = dashboardPageUI(self.ui) 
        self.formUI = formUI(self.ui)  
        
        self._center()
        self.__sidebar_buttons_connector()

    def __sidebar_buttons_connector(self,):
        for name, menu in self.dashboard_menu_items.items():
            GUIBackend.button_connector_argument_pass(menu['btn'],
                                                      self.page_change_event,
                                                      args=(name,)
                                                      )
    
    def page_change_event(self, name ):
        """this function called when page change
        """
        GUIBackend.set_stack_widget_page(self.ui.pages, 
                                         self.dashboard_menu_items[name]['page'] 
                                         )

    def _center(self):
        # Get primary screen
        primary_screen = QApplication.primaryScreen()

        if primary_screen:
            # Get geometry of the primary screen
            screen_geometry = primary_screen.geometry()

            # Calculate center point
            center_point = screen_geometry.center()

            # Set window position to be centered
            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)


    
 
    def go_to_page(self, page_name:str):
        """change page to the page with page_name
        """
        GUIBackend.set_stack_widget_page(self.ui.page,
                                         self.dashboard_menu_items[page_name]['page'])
        self.current_page_name = page_name



    
            
        
    def set_access_pages(self, pages:list[str], flag:bool = True):
        """enable or disable some pages

        Args:
            pages (list[str]): list of page names 
            flag (bool): if True, make pages enable. if False, make pages disable
        """
        # if isinstance(pages, str):
        #     if pages == 'all':
        #         pages = list(self.sidebar_pages_buttons.keys())

        # for page_name in self.sidebar_pages_buttons.keys():
        #     btn = self.sidebar_pages_buttons[page_name]
        #     if page_name in pages:
        #         GUIBackend.set_wgt_visible( btn, flag )
        #     else:
        #         GUIBackend.set_wgt_visible(btn , not(flag))
        
        # self.go_to_page(pages[0])

    
    # def set_access_tabs(self, tabs_access: dict[str,list], flag:bool = True):
    #     """enable or disable some tabs
    #     """
    #     for tabgropup_name in self.tabs.keys():
    #         tab_group_widget, sub_tabs = self.tabs[tabgropup_name]
    #         if tabgropup_name in tabs_access.keys():
    #             GUIBackend.set_wgt_visible(tab_group_widget, True)
    #             sub_tabs_access = tabs_access[tabgropup_name]

    #             if isinstance(sub_tabs_access, str):
    #                 if sub_tabs_access == 'all':
    #                     sub_tabs_access = list(sub_tabs.keys())
                    
    #             for sub_tab_name in sub_tabs.keys():
    #                 if sub_tab_name in sub_tabs_access:
    #                     GUIBackend.set_visible_tab(tab_group_widget,
    #                                                    sub_tabs[sub_tab_name],True )
    #                 else:
    #                     GUIBackend.set_visible_tab(tab_group_widget,
    #                                                    sub_tabs[sub_tab_name],False )
    #         else:
    #             GUIBackend.set_wgt_visible(tab_group_widget, False)


   

    def change_page_connector(self, func):
        self.external_page_change_event = func

    def buttons_connection(self):
        """main butoons connect -- exit , minize , maximize, help --"""
        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.minimize_btn.clicked.connect(self.minimize)
        self.ui.maximize_btn.clicked.connect(self.maxmize_minimize)
        self.ui.menu_btn.clicked.connect(self.move_side_frame)

    def minimize(self):
        """Minimize winodw"""
        self.showMinimized()

    def close_win(self):
        """
        this function closes the app
        Inputs: None
        Returns: None
        """

        res = self.common_func.show_confirm_box(title="Exit",
                                                message="Do you want to exit?",
                                                buttons=['yes', 'cancel'],
                                                icon_type='question')

        if res=='yes':
            self.app_close_flag = True
            self.close()
            sys.exit()

    def maxmize_minimize(self):
        """Maximize or Minimize window"""
        if self.isMaximized():
            self.showNormal()
            GUIBackend.set_button_icon(self.ui.maximize_btn, IconsPath.IconsPath.MAXIMIZE_ICON)
        else:
            self.showMaximized()
            GUIBackend.set_button_icon(self.ui.maximize_btn, IconsPath.IconsPath.MINIMIZE_ICON)

        #--------------------------------------------------------
        self.Page_LiveView.sliderMenu.disapear()
        

    def move_side_frame(self):
        w = self.ui.side_frame.width()
        if w <= Constant.SideBarAnimation.WIDTH_START_VALUE:
            self.minWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"minimumWidth")
            self.minWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.minWidth.setStartValue(w)
            self.minWidth.setEndValue(Constant.SideBarAnimation.WIDTH_STOP_VALUE)
            self.minWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group = QtCore.QParallelAnimationGroup()
            self.group.addAnimation(self.minWidth)

            self.maxWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"maximumWidth")
            self.maxWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.maxWidth.setStartValue(w)
            self.maxWidth.setEndValue(Constant.SideBarAnimation.WIDTH_STOP_VALUE)
            self.maxWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group.addAnimation(self.maxWidth)
            self.group.start()

            GUIBackend.set_button_icon(self.ui.menu_btn, IconsPath.IconsPath.OPEN_MENU_ICON)

        else:
            self.minWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"minimumWidth")
            self.minWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.minWidth.setStartValue(w)
            self.minWidth.setEndValue(Constant.SideBarAnimation.WIDTH_START_VALUE)
            self.minWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group = QtCore.QParallelAnimationGroup()
            self.group.addAnimation(self.minWidth)

            self.maxWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"maximumWidth")
            self.maxWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.maxWidth.setStartValue(w)
            self.maxWidth.setEndValue(Constant.SideBarAnimation.WIDTH_START_VALUE)
            self.maxWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group.addAnimation(self.maxWidth)
            self.group.start()

            GUIBackend.set_button_icon(self.ui.menu_btn, IconsPath.IconsPath.CLOSE_MENU_ICON)



import sys
import time


from uiFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend


# ui_file = QFile("mainwindow.ui")
# ui_file.open(QFile.ReadOnly)

# loader = QUiLoader()
# window = loader.load(ui_file)
# window.show()


class dashboardPageUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui

        self.dashboard_menu_items = {
            'register_sale':{'btn':self.ui.register_sale_building, 
                             'page':self.ui.page_register_property,
                             },

            'register_rent':{'btn':self.ui.register_rent_building, 
                             'page':self.ui.page_register_property, 
                            }
        }

        self.menuConnector()

    
    def menuConnector(self,):
        for name, item in self.dashboard_menu_items.items():
            GUIBackend.widget_press_connector(item['btn'], self.menuHandler, args=(name,))
    
    def menuHandler(self, page_name,):
        GUIBackend.set_stack_widget_page(self.ui.pages,
                                             self.dashboard_menu_items[page_name]['page'])
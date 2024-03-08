import sys
import time


from uiFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from Form.formHandler import FormHandler
from estateForm.estateGlossaries import build_estate_gellosaries
from estateForm.estateFormInfo import build_estate_form_info

from PySide6 import QtWidgets


# ui_file = QFile("mainwindow.ui")
# ui_file.open(QFile.ReadOnly)

# loader = QUiLoader()
# window = loader.load(ui_file)
# window.show()


class formUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.estate_form = FormHandler(
            form_fields_info= build_estate_form_info(self.ui),
            gloassaries= build_estate_gellosaries()
        )
        

        #self.render_options(self.estate_form_meta, self.estate_form_glossaries)

        GUIBackend.button_connector(self.ui.form_next_btn, self.next_step)
        GUIBackend.button_connector(self.ui.form_prev_btn, self.prev_step)
        
    def next_step(self,):
        step = GUIBackend.get_stack_widget_idx(self.ui.form_stackwidget)
        step_count = GUIBackend.get_stack_widget_count(self.ui.form_stackwidget)
        step+=1
        step = min(step, step_count-1)
        GUIBackend.set_stack_widget_idx(self.ui.form_stackwidget, step)

    def prev_step(self,):
        step = GUIBackend.get_stack_widget_idx(self.ui.form_stackwidget)
        step-=1
        step = max(step, 0)
        GUIBackend.set_stack_widget_idx(self.ui.form_stackwidget, step)

    

    



  
    


    
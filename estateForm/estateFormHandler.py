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
            gloassaries= build_estate_gellosaries(),
            form_ui = {
                'next_btn': self.ui.form_next_btn,
                'prev_btn': self.ui.form_prev_btn,
                'pages': self.ui.form_stackwidget,
                'error_label': self.ui.estateStepErrorLabel
            }
        )
        

        #self.render_options(self.estate_form_meta, self.estate_form_glossaries)

    

    

    

    



  
    


    
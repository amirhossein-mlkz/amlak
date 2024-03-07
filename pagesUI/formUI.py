import sys
import time


from uiFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from meta import Form
from glassoryies import melk
from PySide6 import QtWidgets

# ui_file = QFile("mainwindow.ui")
# ui_file.open(QFile.ReadOnly)

# loader = QUiLoader()
# window = loader.load(ui_file)
# window.show()


class formUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        form_meta = Form(self.ui)
        self.render_options(form_meta.melk_post_type)
        self.hide_all_errors(form_meta.melk_post_type)

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

    def hide_all_errors(self, form_meta:dict[str,dict]):
        for field_name, field_meta in form_meta.items():
            lbl = field_meta.get('error')
            if lbl is not None:
                GUIBackend.set_wgt_visible(lbl, False)

    def render_options(self, form_meta:dict[str,dict]):
        glossarie = melk

        for field_name, field_meta in form_meta.items():
            options_id = field_meta.get('options-id')
            options_type = field_meta.get('type')

            if 'reb' in field_name:
                x=0
    
            
            #check if field need options
            if options_id is not None:
                
                #get options glossarie
                options_glossarie = glossarie.get(options_id)

                if options_glossarie is None:
                    print('Error for', options_id)
                    continue

                if options_type=='combobox':
                    field = field_meta.get('input')
                    items = list(glossarie.get(options_id).values())
                    GUIBackend.set_combobox_items(field, items)

                elif options_type in ['radio','checkbox']:

                    options_container:QtWidgets.QFrame = field_meta.get('options-container')
                    layout = options_container.layout()
                    GUIBackend.set_layout_alignment(layout,'r')

                    options_input_field = []
                    for option_text in options_glossarie.values():
                        if options_type=='radio':
                            opt = QtWidgets.QRadioButton(option_text)

                        elif options_type =='checkbox':
                            opt = QtWidgets.QCheckBox(option_text)
                        
                        GUIBackend.set_layout_direction(opt,'rtl')
                        GUIBackend.add_widget(layout, opt)

                        options_input_field.append(opt)

                    form_meta[field_name]['input'] = options_input_field
                    

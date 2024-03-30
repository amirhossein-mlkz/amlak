import sys
import time


from uiFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from Form.formHandler import FormHandler, Field
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
                'submit_btn': self.ui.estateFormSubmit,
                'pages': self.ui.form_stackwidget,
                'error_label': self.ui.estateStepErrorLabel
            }
        )

        self.steps_buttons = [
            self.ui.estateFormStep1Btn,
            self.ui.estateFormStep2Btn,
            self.ui.estateFormStep3Btn,
            self.ui.estateFormStep4Btn,
            self.ui.estateFormStep5Btn,
            self.ui.estateFormStep6Btn,
            self.ui.estateFormStep7Btn,
            self.ui.estateFormStep8Btn,
        ]

        self.calc_price_mode = None

        self.estate_form.set_next_callback( lambda : self.change_step_event('next'))
        self.estate_form.set_prev_callback( lambda : self.change_step_event('prev'))
        self.estate_form.set_field_change_callback(self.change_field_event)
        self.steps_button_init()
        self.handle_step_buttons()


    def steps_button_init(self,):
        for i, btn in enumerate(self.steps_buttons):
            GUIBackend.button_connector_argument_pass(btn, self.button_step_click_event, (i,))
            if i==0:
                continue
            GUIBackend.set_disable_enable(btn, False)

    def button_step_click_event(self, step):
        self.estate_form.go_to_step(step)
        self.handle_step_buttons()
    
    def change_field_event(self, field:Field):
        if field.name == 'price-calculation':
            self.calc_price_mode = field.get_value()

            total_price = self.estate_form.get_field('total-price')
            unit_price = self.estate_form.get_field('unit-price')

            if self.calc_price_mode == 'total-price':
                total_price.set_enablity(True)
                unit_price.set_enablity(False)

            elif self.calc_price_mode == 'unit-price':
                total_price.set_enablity(False)
                unit_price.set_enablity(True)
        
        if  self.calc_price_mode == 'total-price':
            if field.name in ['total-price', 'meterage']:
                total_meterage = self.estate_form.get_field('meterage')
                total_price = self.estate_form.get_field('total-price')
                unit_price = self.estate_form.get_field('unit-price')
                if total_meterage.get_value() !=0:
                    res = total_price.get_value() / total_meterage.get_value()
                    unit_price.set_value(int(res))

                else:
                    unit_price.set_value(0)
            

        elif self.calc_price_mode == 'unit-price':
            if field.name in ['unit-price', 'meterage']:
                total_meterage = self.estate_form.get_field('meterage')
                total_price = self.estate_form.get_field('total-price')
                unit_price = self.estate_form.get_field('unit-price')
                
                res = unit_price.get_value() * total_meterage.get_value()
                total_price.set_value(int(res))







        # if field.name == 'total-price':
        #     price = field.get_value()
        #     metergare = self.estate_form.get_field('meterage').get_value()



        
    def change_step_event(self, state):
        self.handle_step_buttons()
    
    def handle_step_buttons(self,):
        for i,step_btn in enumerate(self.steps_buttons):

            if i == self.estate_form.curent_step:
                GUIBackend.set_dynalic_property(step_btn, 'stateStyle', 2, repolish_style=True)

            elif i <= self.estate_form.last_complete_step:
                GUIBackend.set_dynalic_property(step_btn, 'stateStyle', 1, repolish_style=True)

            else:
                GUIBackend.set_dynalic_property(step_btn, 'stateStyle', 0, repolish_style=True)

            #enable step button
            if i <= self.estate_form.last_complete_step:
                GUIBackend.set_disable_enable(step_btn, True)


        #self.render_options(self.estate_form_meta, self.estate_form_glossaries)

    

    

    

    



  
    


    
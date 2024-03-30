from __future__ import annotations

from PySide6 import QtWidgets


from Backend.Utils.Glossary import GlossaryHandler
from uiUtils.guiBackend import GUIBackend
from .fieldHandler import Field



#_______________________________________________________________________________________________
#
#
#
#_______________________________________________________________________________________________
#form_ui_keys = 'next_btn', 'prev_btn', 'pages', 'submit'

class FormHandler:
    VALID_FORM_UI_KEYS = ['next_btn', 'prev_btn', 'pages', 'error_label']

    def __init__(self, 
                 form_fields_info:dict[str,dict], 
                 gloassaries:GlossaryHandler,
                 form_ui: dict[str, QtWidgets.QWidget] = {},
                 is_multi_step = False
                 ) -> None:
        """_summary_

        Args:
            form_fields_info (dict[str,dict]): _description_
            gloassaries (GlossaryHandler): _description_
            form_ui (dict[str, QtWidgets.QWidget], optional): descibe form ui widgets
                the keys could be ['next_btn', 'prev_btn', 'pages', 'error_label'
        """
        
        self.gloassaries = gloassaries
        self.form_fields_dict = form_fields_info
        self.form_ui = form_ui
        self.is_multi_step = is_multi_step

        self.curent_step = 0
        self.last_complete_step = self.curent_step

        self.next_callback = None
        self.prev_callback = None
        self.field_change_callback = None
        self.enable_fields = []
        
        self.handle_form_ui()
        self.render_options()
        
        self.conditions_field = self.generate_map_conditions()
        self.form_values = self.update_form_values()

        self.fields_event_connector()
        self.hide_all_errors()
        self.refresh_visibility()
        self.go_to_step(0)

    def set_next_callback(self, func):
        self.next_callback = func

    def set_prev_callback(self, func):
        self.prev_callback = func
    
    def set_field_change_callback(self, func):
        self.field_change_callback = func
    
    def handle_form_ui(self, ):
        for key,wgt in self.form_ui.items():

            if key == 'next_btn':
                GUIBackend.button_connector(wgt, self.next_step)
                assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui is neccesury in multi step_form"
                
            elif key == 'prev_btn':
                GUIBackend.button_connector(wgt, self.prev_step)
                assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui is neccesury in multi step_form"
            
            elif key == 'submit_btn':
                GUIBackend.button_connector(wgt, self.submit)
                if self.is_multi_step:
                    GUIBackend.set_wgt_visible(wgt, False)

            elif key in ['pages', 'error_label']:
                pass

            else:
                raise f"{key} is not a valid form. only {self.VALID_FORM_UI_KEYS} could be used"

        

    def render_options(self,):

        for field_name in self.get_fields_list():
            field = self.get_field(field_name)

            #ignore field if dose not need options
            if not field.is_option_field():
                continue

            options_id = field.get_options_id()
            options_values = self.gloassaries.get_values(options_id)

            if not options_values:
                print('Error for', options_id)
                continue

            field.render_options(options_values)

    def fields_event_connector(self,):
        for field_name in self.get_fields_list():
            field = self.get_field(field_name)
            field.connect(self.change_evnet)


    def hide_all_errors(self,):
        for field_name in self.get_fields_list():
            feild = self.get_field(field_name)
            feild.show_error(None)


    def generate_map_conditions(self,):
        conditions_field = {}
        for field_name in self.get_fields_list():
            field = self.get_field(field_name)
            master_fields = field.get_visibility_master_fields()

            for master_field in master_fields:
                child_fields:list[str] = conditions_field.get(master_field, [])
                child_fields.append(field_name)
                conditions_field[master_field] = child_fields
        return conditions_field
    
    
    def update_form_values(self,):
        results = {}
        for field_name in self.get_fields_list():
            field = self.get_field(field_name)
            value = field.get_value()
            results[field_name] = value
        return results
    
    def update_form_value(self, field_name, field_value=None):
        if field_value is None: 
            field = self.get_field(field_name)
            field_value = field.get_value()

        self.form_values[field_name] = field_value
            
    
    def get_child_field_visibility(self, field_name:str):
        return self.conditions_field.get(field_name, [])
    
    def get_field(self, name:str) -> Field:
        options_id = self.form_fields_dict[name].get('options-id')
        glossary = None
        if options_id:
            glossary = self.gloassaries.get_glossary(options_id)
        return Field(name, self.form_fields_dict.get(name), glossary)
    
    def get_fields_list(self,)->list[str]:
        return self.form_fields_dict.keys()


    def change_evnet(self, value, field_name:str):
        field = self.get_field(field_name)
        field_value = field.get_value()
        self.update_form_value(field_name, field_value)

        #check field validation and show error if not valid

        field.check_validation(self.form_values)

        #check visibility of other fields base on this field
        relative_fields_names = self.get_child_field_visibility(field_name)
        self.refresh_visibility(relative_fields_names)

        
        self.field_change_callback(field)
    
    def get_fields_of_step(self, step:int):
        """step start from 0

        Args:
            step (int): _description_
        """
        step+=1 #beacuse in code step is from 0 but in form dictionary start from 1
        res = []
        for field_name in self.get_fields_list():
            field = self.get_field(field_name)
            if field.is_for_this_step(step):
                res.append(field_name)
        return res

    
    def check_validation(self, fields_name:list[str]):
        validation = True
        
        for field_name in fields_name:
            if field_name not in self.enable_fields:
                continue

            field = self.get_field(field_name)
            field_validation = field.check_validation(self.form_values)
            if not field_validation:
                validation = False
        
        if validation:
            self.write_form_error(None)
        else:
            self.write_form_error('لطفا مقادیر را به درستی وارد نمایید')
        
        return validation
    
    def refresh_visibility(self, fields_name:list[str]=None):
        """refresh visibility of fields_name base on current situation

        Args:
            fields_name (list[str]): if be None, check all fields
        """
        if fields_name is None:
            fields_name = self.get_fields_list()
            
        for field_name in fields_name:
            field = self.get_field(field_name)
            state = field.refresh_field_visibility(self.form_values)
            if state:
                if field_name not in self.enable_fields:
                    self.enable_fields.append(field_name)
            else:
                if field_name in self.enable_fields:
                    self.enable_fields.remove(field_name)



    def go_to_step(self, step):
        pages_wgt= self.form_ui['pages']

        step_count = GUIBackend.get_stack_widget_count(pages_wgt)
        step = min(step, step_count-1)
        step = max(step, 0)

        #check validation if we want go to next steps
        if step > self.curent_step:
            fields_name = self.get_fields_of_step(self.curent_step)
            if not self.check_validation(fields_name):
                return False
            
        #if step <= self.last_complete_step:
        self.curent_step = step
        self.last_complete_step = max(self.last_complete_step, self.curent_step)

        GUIBackend.set_stack_widget_idx(pages_wgt, self.curent_step)

        prev_btn = self.form_ui.get('prev_btn')
        if prev_btn is not None:
            if self.curent_step == 0:
                GUIBackend.set_wgt_visible(prev_btn, False)
            else:
                GUIBackend.set_wgt_visible(prev_btn, True)

        next_btn = self.form_ui.get('next_btn')
        if next_btn is not None:
            if self.curent_step == step_count-1:
                GUIBackend.set_wgt_visible(next_btn, False)
            else:
                GUIBackend.set_wgt_visible(next_btn, True)

        submit_btn = self.form_ui.get('submit_btn')
        if submit_btn is not None:
            if self.curent_step == step_count-1:
                GUIBackend.set_wgt_visible(submit_btn, True)
            else:
                GUIBackend.set_wgt_visible(submit_btn, False)





        return True
        #return False
    
    def write_form_error(self, txt):
        wgt = self.form_ui.get('error_label')
        if wgt is None:
            return
        
        if txt is None:
            GUIBackend.set_wgt_visible(wgt, False)
        else:
            GUIBackend.set_wgt_visible(wgt, True)
            GUIBackend.set_label_text(wgt, str(txt))


    def next_step(self,):
        assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui dict is neccessury for multi step form"
        pages_wgt= self.form_ui['pages']

        self.curent_step = GUIBackend.get_stack_widget_idx(pages_wgt)
        self.go_to_step(self.curent_step+1)
        
        if self.next_callback is not None:
            self.next_callback()


    def prev_step(self,):
        assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui dict is neccessury for multi step form"
        self.go_to_step(self.curent_step-1)
        
        self.write_form_error(None)

        if self.prev_callback is not None:
            self.prev_callback()
    
    def submit(self,):
        print('submit')

    
    
            
            





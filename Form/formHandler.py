from __future__ import annotations
import copy
import re

from PySide6 import QtWidgets


from Backend.Utils.Glossary import singleGlossary, GlossaryHandler
from uiUtils.guiBackend import GUIBackend
from uiFiles.main_UI import Ui_MainWindow
from Backend.Utils.conditionsChecker import conditionsChecker



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
        self.curent_step = 1
        
        self.handle_form_ui()
        self.render_options()
        
        self.conditions_field = self.generate_map_conditions()
        self.form_values = self.update_form_values()

        self.fields_event_connector()
        self.hide_all_errors()
    
    def handle_form_ui(self, ):
        for key,wgt in self.form_ui.items():

            if key == 'next_btn':
                GUIBackend.button_connector(wgt, self.next_step)
                assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui is neccesury in multi step_form"
                
            elif key == 'prev_btn':
                GUIBackend.button_connector(wgt, self.prev_step)
                assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui is neccesury in multi step_form"
            
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
        field.check_validation()

        #check visibility of other fields base on this field
        corespond_fields_names = self.get_child_field_visibility(field_name)
        for corespond_field_name in corespond_fields_names:
            corespond_field = self.get_field(corespond_field_name)
            corespond_field.refresh_field_visibility(self.form_values)
    
    def check_step_validation(self, step):
        validation = True
        for field_name in self.get_fields_list():
            field = self.get_field(field_name)
            if field.is_for_this_step(step):
                field_validation = field.check_validation()
                if not field_validation:
                    validation = False
        
        return validation
    

    def next_step(self,):
        assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui dict is neccessury for multi step form"
        pages_wgt= self.form_ui['pages']

        step = GUIBackend.get_stack_widget_idx(pages_wgt)
        if self.check_step_validation(step+1):
            step_count = GUIBackend.get_stack_widget_count(pages_wgt)
            step+=1
            step = min(step, step_count-1)
            GUIBackend.set_stack_widget_idx(pages_wgt, step)
            self.write_form_error(None)
        else:
            self.write_form_error('لطفا مقادیر را به درستی وارد نمایید')


    def prev_step(self,):
        assert 'pages' in self.form_ui.keys(), "'pages' key in form_ui dict is neccessury for multi step form"
        pages_wgt= self.form_ui['pages']

        step = GUIBackend.get_stack_widget_idx(pages_wgt)
        step-=1
        step = max(step, 0)
        GUIBackend.set_stack_widget_idx(pages_wgt, step)
        self.write_form_error(None)
    
    def write_form_error(self, txt):
        wgt = self.form_ui.get('error_label')
        if wgt is None:
            return
        
        if txt is None:
            GUIBackend.set_wgt_visible(wgt, False)
        else:
            GUIBackend.set_wgt_visible(wgt, True)
            GUIBackend.set_label_text(wgt, str(txt))




    
    
            
            




#_______________________________________________________________________________________________
#
#
#
#_______________________________________________________________________________________________
class Field:

    def __init__(self,name:str, dict_info:dict, glassory:singleGlossary=None):
        self.name = name
        self.dict_info = dict_info
        self.glassory = glassory
    
    def is_option_field(self,) -> bool:
        return bool(self.dict_info.get('options-id'))
    
    def is_for_this_step(self, step):
        return step == self.dict_info.get('step', -1)
    
    def get_error_label(self,) -> QtWidgets.QLabel:
        return self.dict_info.get('error')
    
    def get_options_id(self,) -> str:
        return self.dict_info.get('options-id')
    
    
    def get_type(self,) -> str:
        return self.dict_info.get('type')
    
    def get_input(self,):
        return self.dict_info.get('input')
    
    def get_options_container(self,) ->QtWidgets.QFrame:
        return self.dict_info.get('options-container')
    
    def get_visibility_conditions(self,)-> dict:
        return copy.deepcopy(self.dict_info.get('visible-conditions'))
    
    def get_container(self,) -> QtWidgets.QFrame:
        return self.dict_info.get('frame')
    
    def show_error(self, text):
        error_lbl = self.get_error_label()
        if error_lbl:
            if text is None:
                GUIBackend.set_wgt_visible(error_lbl, False)
            else:
                GUIBackend.set_label_text(error_lbl, text)
                GUIBackend.set_wgt_visible(error_lbl, True)

    
    def get_value(self,):
        ftype = self.get_type()
        finput = self.get_input()
        if ftype == 'radio':
            for key, _finput in finput.items():
                if GUIBackend.get_radio_value(_finput):
                    return key
            return None
                
        elif ftype == 'checkbox':
            reults = []
            for key, _finput in finput.items():
                if GUIBackend.get_checkbox_value(_finput):
                    reults.append(key)
            return reults
        
        elif ftype == 'combobox':
            value = GUIBackend.get_combobox_selected(combo=finput)
            key = self.glassory.value2key(value)
            return key
        
        return GUIBackend.get_input(finput)
    
    def connect(self, event_func):
        field_input = self.get_input()
        if isinstance(field_input, dict):
            for single_field in field_input.values():
                GUIBackend.connector(single_field, event_func, args=(self.name,))
        else:
            GUIBackend.connector(field_input, event_func, args=(self.name,))
    
        
    
    def get_visibility_master_fields(self,)->list[str]:
        """returns list of fields that effect on visibility
        of this field

        Returns:
            list[str]: 
        """
        conds = self.get_visibility_conditions()
        if conds:
            return list(map(lambda x:x['key'], conds))
        else:
            return []
    
    def render_options(self, options_values:list[str]):
        ftype = self.get_type()

        if ftype=='combobox':
            field = self.get_input()
            options_values = self.glassory.get_values()
            GUIBackend.set_combobox_items(field, options_values)

        

        elif ftype in ['radio','checkbox']:
            options_container = self.get_options_container()
            options_keys = self.glassory.get_keys()

            layout = options_container.layout()
            GUIBackend.set_layout_alignment(layout,'r')

            options_input_field = {}
            for key in options_keys:
                value = self.glassory.key2value(key)
                if ftype=='radio':
                    opt = QtWidgets.QRadioButton(text=value)

                elif ftype =='checkbox':
                    opt = QtWidgets.QCheckBox(text=value)
                    
                GUIBackend.set_layout_direction(opt,'rtl')
                GUIBackend.add_widget(layout, opt)
                options_input_field[key] =opt

            self.dict_info['input'] = options_input_field
    
    def check_validation(self,) -> tuple[bool,str]:
        value = self.get_value()
        validation_info = self.dict_info.get('validation')

        validation = True
        text = None

        if validation_info:
            for cond_info in validation_info:
                if cond_info['cond'] == 'require':
                    if not value:
                        text =  'این فیلد ضروری است'
                        validation = False
                        break

                if cond_info['cond'] == 'regex':
                    pattern = cond_info['pattern']
                    if not re.match(pattern, value):
                        text =  'به درستی وارد نمایید'
                        validation = False
        
        self.show_error(text)
        return validation

    def refresh_field_visibility(self, forms_value:dict):
        conds = self.get_visibility_conditions()
        frame = self.get_container()
 
        for cond in conds:
            oprand_fname = cond['key']
            oprand_value = forms_value[oprand_fname]
            cond['key'] = oprand_value
            #result_cond.append(cond)

        checker = conditionsChecker(conds)
        if checker.check():
            GUIBackend.set_wgt_visible(frame, True)
        else:
            GUIBackend.set_wgt_visible(frame, False)


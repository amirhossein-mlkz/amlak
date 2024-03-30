from __future__ import annotations
import copy

from PySide6 import QtWidgets


from Backend.Utils.Glossary import singleGlossary
from uiUtils.guiBackend import GUIBackend
from Backend.Utils.conditionsChecker import conditionsChecker




class Field:

    def __init__(self,name:str, dict_info:dict, glassory:singleGlossary=None):
        self.name = name
        self.dict_info = dict_info
        self.glassory = glassory
    
    def is_option_field(self,) -> bool:
        return bool(self.dict_info.get('options-id'))
    
    def is_for_this_step(self, step):
        return step == self.dict_info.get('step', -1)
    
    def set_enablity(self, state):
        inpt = self.get_input()
        GUIBackend.set_disable_enable(inpt, state)

    def set_value(self, value):
        inpt = self.get_input()
        GUIBackend.set_input(inpt, value, block_signal=True)
    
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
        return copy.deepcopy(self.dict_info.get('visible-conditions',[]))
    
    def get_validation_conditions(self,)-> dict:
        return copy.deepcopy(self.dict_info.get('validation-conditions',[]))
    
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
        
        elif ftype == 'input-number':
            value = GUIBackend.get_input(finput)
            if value:
                return int(value)
            return 0
                
            
        
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
        
        else:
            raise Exception(f"{self.name} field type is incorect")
    
    def check_validation(self,forms_value) -> tuple[bool,str]:
        value = self.get_value()
        conds = self.get_validation_conditions()

        for cond in conds:
            oprand_fname = cond.get('key')
            if oprand_fname is not None:
                oprand_value = forms_value[oprand_fname]
                cond['key'] = oprand_value
            else:
                cond['key'] = self.get_value()

        text = None

        checker = conditionsChecker(conds)
        result, reject_cond_info = checker.check()

        if not result:
            cond = reject_cond_info['cond']
            text = reject_cond_info.get('error')
            if not text:
                if cond == 'require':
                    text =  'این فیلد ضروری است'

                elif cond == 'regex':
                    text =  'به درستی وارد نمایید'

        self.show_error(text)

                
                # else:
                #     raise Exception(f"{self.name} field {cond_info['cond']} condition is not valid")
        
        
        return result

    def refresh_field_visibility(self, forms_value:dict):
        conds = self.get_visibility_conditions()
        frame = self.get_container()
 
        for cond in conds:
            oprand_fname = cond['key']
            oprand_value = forms_value[oprand_fname]
            cond['key'] = oprand_value
            #result_cond.append(cond)

        checker = conditionsChecker(conds)
        result,_ = checker.check()
        if result:
            GUIBackend.set_wgt_visible(frame, True)
            return True
        else:
            GUIBackend.set_wgt_visible(frame, False)
            return False


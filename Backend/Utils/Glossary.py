class GlossaryHandler:

    def __init__(self,glossaries:dict[str,dict]) -> None:
        self.glossaries = glossaries

    def add_glossary(self, glossary_name:str, glossary:dict):
        self.glossaries[glossary_name] = glossary

    def get_glossaries_names(self,):
        return list(self.glossaries.keys())

    def get_values(self, glossary_name):
        glossary = self.glossaries.get(glossary_name)
        if glossary is None:
            return []
        return list(glossary.values())
    
    def get_keys(self, glossary_name):
        glossary = self.glossaries.get(glossary_name)
        if glossary is None:
            return []
        return list(glossary.keys())
    
    def glossary_exist(self, glossary_name):
        return glossary_name in self.glossaries.keys()
    
    def value2key(self, glossary_name:str, value):
        glossary = self.glossaries.get(glossary_name)
        if glossary is None:
            return None
        
        return  self.__find_key(
                _dict = glossary,
                subject_value = value
            )
    
    def key2value(self, glossary_name:str, key:str):
        glossary = self.glossaries.get(glossary_name)
        if glossary is None:
            return None
        
        return self.glossaries[glossary_name][key]
        
    

    def multi_key2value(self, transitions:dict):
        """a dictionary that keys are glossary name and values are
           transition_key. if glossary_name doesn't exist,
           it returns self value

        Args:
            transitions (dict): _description_

        Returns:
            _type_: _description_
        """
        for glossary_name, key in transitions.items():
            transitions[glossary_name] = self.key2value(glossary_name, key=key)
        return transitions
    

    def multi_value2key(self, transitions:dict):
        """a dictionary that keys are glossary name and values are
           transition_key. if glossary_name doesn't exist,
           it returns self value

        Args:
            transitions (dict): _description_

        Returns:
            _type_: _description_
        """
        for glossary_name, value in transitions.items():
            if self.glossary_exist(glossary_name):
                transitions[glossary_name] = self.value2key(glossary_name, value=value)
                
        return transitions

    
    def __find_key(self, _dict:dict, subject_value):
        for key, value in _dict.items():
            if value == subject_value:
                return key
        return None
    

    def get_glossary(self, name:str):
        return singleGlossary(name, self.glossaries[name])
    





class singleGlossary:

    def __init__(self,name:str, glossary:dict[str,dict]) -> None:
        self.name = name
        self.glossary = glossary

    def get_name(self,) -> str:
        return self.name

    def get_values(self):
        return list(self.glossary.values())
    
    def get_keys(self,):
        return list(self.glossary.keys())
    

    def value2key(self, value):
        return  self.__find_key(
                _dict = self.glossary,
                subject_value = value
            )
    
    def key2value(self, key:str):
        return self.glossary[key]

    
    def __find_key(self, _dict:dict, subject_value):
        for key, value in _dict.items():
            if value == subject_value:
                return key
        return None
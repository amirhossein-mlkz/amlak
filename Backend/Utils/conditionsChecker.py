import numbers

{'condition':[
                {'operator':'=', 'key':'compensation','value':'yes'},
            ]

}

class conditionsChecker:

    def __init__(self, conditions:list[dict]) -> None:
        self.conditions = conditions

    def check(self,):
        for condition in self.conditions:
            operator = condition['operator']
            key = condition['key']
            value = condition['value']

            if operator == '=':
                if key != value:
                    return False
            if operator == '>':
                if key <= value:
                    return False
            if operator == '<':
                if key >= value:
                    return False
                
            if operator == '>=':
                if key < value:
                    return False
                
            if operator == '<=':
                if key > value:
                    return False   

            if operator == 'in':
                if key not in value:
                    return False  
            
            if operator == 'contain':
                if value not in key:
                    return False
            
        return True
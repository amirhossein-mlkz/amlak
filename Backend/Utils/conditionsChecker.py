import numbers
import re

{'condition':[
                {'operator':'=', 'key':'compensation','value':'yes'},
            ]

}

class conditionsChecker:

    def __init__(self, conditions:list[dict]) -> None:
        self.conditions = conditions

    def check(self,):
        for condition in self.conditions:
            operator = condition['cond']
            key = condition.get('key')
            value = condition.get('compare-value')

            if operator == '=':
                if key != value:
                    return False, condition
            if operator == '>':
                if key <= value:
                    return False, condition
            if operator == '<':
                if key >= value:
                    return False, condition
                
            if operator == '>=':
                if key < value:
                    return False, condition
                
            if operator == '<=':
                if key > value:
                    return False, condition 

            if operator == 'in':
                if key not in value:
                    return False, condition
            
            if operator == 'contain':
                if value not in key:
                    return False, condition
                
            elif operator == 'regex':
                if not re.match(value, key):
                    return False, condition
                
            if operator == 'require':
                if not key:
                    return False, condition
            
        return True, None
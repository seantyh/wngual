from enum import Enum
from .expr import wngComplexExpr

class ActionType(Enum):
    CREATE = 1
    UPDATE = 2
    DELETE = 3

class wngMutation:
    def __init__(self, 
            action: ActionType,
            expr: wngComplexExpr):
        self.action = action
        self.expr = expr

    def __repr__(self):
        return ("<wngMutation[{}]: \n" 
            + "  {}>").format(
                self.action, self.expr
            )

class wngAssignment:
    def __init__(self,
            identifier: str,
            expr: wngComplexExpr):
        self.identifier = identifier
        self.expr = expr

    
    def __repr__(self):
        return ("<wngAssignment: {} = \n" 
            + "  {}>").format(
                self.identifier, self.expr
            )
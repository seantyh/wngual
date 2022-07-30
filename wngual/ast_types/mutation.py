from enum import Enum
from .expr import wngComplexExpr
from .base import wngBase

class ActionType(Enum):
    CREATE = 1
    UPDATE = 2
    DELETE = 3

class wngMutation(wngBase):
    def __init__(self, 
            action: ActionType,
            expr: wngComplexExpr):
        self.action = action
        self.expr = expr
        self.fields = ["action", "expr"]

    def __repr__(self):
        return ("<wngMutation[{}]: \n" 
            + "  {}>").format(
                self.action, self.expr
            )

class wngAssignment(wngBase):
    def __init__(self,
            identifier: str,
            expr: wngComplexExpr):
        self.identifier = identifier
        self.expr = expr
        self.fields = ["identifier", "expr"]

    
    def __repr__(self):
        return ("<wngAssignment: {} = \n" 
            + "  {}>").format(
                self.identifier, self.expr
            )
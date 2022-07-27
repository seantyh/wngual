from typing import List

class wngRelationSpec:
    def __init__(self, relation: str, params: List[str] = []):
        self.relation = relation
        self.params = params
    
    def __repr__(self):
        return "<{}({})>".format(
            self.relation,
            ",".join(self.params)
        )

class wngRelationOp:
    def __init__(self, equality=False, negation=False):
        self.equality = equality
        self.negation = negation

    def __repr__(self):
        label = "IS NOT" if self.negation else "IS"
        label += "" if self.equality else " IN"
        return f"<{label}>"

from enum import Enum
class ArrowType(Enum):
    forward = "->"
    backward = "<-"
    bidirectional = "<->"
    para_forward = "~>"



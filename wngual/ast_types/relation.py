from typing import List
from .base import wngBase

class wngRelationSpec(wngBase):
    def __init__(self, relation: str, params: List[str] = []):
        self.relation = relation
        self.params = params
        self.fields = ["relation", "params"]
    
    def __repr__(self):
        return "<{}({})>".format(
            self.relation,
            ",".join(self.params)
        )

class wngRelationOp(wngBase):
    def __init__(self, equality=False, negation=False):
        self.equality = equality
        self.negation = negation
        self.fields = ["equality", "negation"]

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



from typing import List

class RelationSpec:
    def __init__(self, relation: str, params: List[str]):
        self.relation = relation
        self.params = params

class RelationOp:
    def __init__(self, equality=False, negation=False):
        self.equality = equality
        self.negation = negation

from enum import Enum
class ArrowType(Enum):
    forward = 1
    backward = 2
    bidirectional = 3

class ArrowSpec:
    def __init__(self, 
            backward=ArrowType.forward, 
            one_src=False, one_tgt=False):
        "The default ArrowSpec is forward all-to-all *->*"
        self.backward = backward
        self.one_src = one_src
        self.one_tgt = one_tgt


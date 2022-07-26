from typing import Union, Optional
from .relation import *

class wngSenseClause:
    def __init__(self, text_constraint: str):
        self.constraint = text_constraint

class wngSenseExpr:
    def __init__(self, 
            lemma: Optional[str]=None, 
            clauses: List[wngSenseClause]=[]):
        self.lemma = lemma
        self.clauses = []

class wngSenseRelClause:
    def __init__(self, 
            rel_spec: wngRelationSpec,
            rel_op: wngRelationOp, 
            tgt_sense: wngSenseExpr):
        self.rel_spec = rel_spec
        self.rel_op = rel_op
        self.tgt_sense = tgt_sense

class wngRelationExpr:
    def __init__(self, 
        src: wngSenseExpr,
        arrow_spec: wngArrowSpec,
        tgt: wngSenseExpr,
        rel_spec: Optional[wngRelationSpec]=None):
        self.src = src
        self.arrow_spec = arrow_spec
        self.tgt = tgt        
        self.rel_sepc = rel_spec

wngExpr = Union[wngSenseExpr, wngRelationExpr]

class wngComplexExpr:
    def __init__(self, 
            expr1: wngExpr, 
            expr2: Optional[wngExpr]=None, 
            op=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op
    
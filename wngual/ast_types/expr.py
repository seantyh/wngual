from typing import Union, Optional
from .relation import *

class wngSenseExpr:
    def __init__(self, lemma=None, clauses=[]):
        self.lemma = lemma
        self.clauses = []

class wngSenseClause:
    def __init__(self, text_constraint):
        self.constraint = text_constraint

class wngSenseRelClause:
    def __init__(self, 
            rel_spec: RelationSpec,
            rel_op: RelationOp, 
            tgt_sense: wngSenseExpr):
        self.rel_spec = rel_spec
        self.rel_op = rel_op
        self.tgt_sense = tgt_sense

class wngRelationExpr:
    def __init__(self, 
        src: wngSenseExpr,
        tgt: wngSenseExpr,
        rel_spec: RelationSpec):
        self.src = src
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
    
from typing import Union, Optional
from .relation import *

class wngSenseClause:
    def __init__(self, text_constraint: str):
        self.constraint = text_constraint

    def __repr__(self):
        return f"<wngSenseClause: {self.constraint}>"

class wngSenseRelClause:
    def __init__(self, 
            rel_spec: wngRelationSpec,
            rel_op: wngRelationOp, 
            tgt_values: Union[str,"wngSenseExpr"]):
        self.rel_spec = rel_spec
        self.rel_op = rel_op
        self.tgt_values = tgt_values
    
    def __repr__(self):
        return "<wngSenseRelClause: {} {} {}>".format(
            self.rel_spec, self.rel_op, self.tgt_values
        )
class wngSenseVariable:
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __repr__(self):
        return f"<wngSenseVariable: {self.identifier}>"

wngSenseClauseType = Union[wngSenseClause, wngSenseRelClause]

class wngSenseExpr:
    def __init__(self, 
            lemma: Optional[str]=None, 
            senseid: Optional[str]=None,
            clauses: List[wngSenseClauseType]=[]):
        self.lemma = lemma
        self.senseid = senseid
        self.clauses = clauses
    
    def __repr__(self):
        if not (self.lemma or self.senseid or self.clauses):
            return "<wngSenseExpr: *>"
        elif self.senseid:
            return f"<wngSenseExpr: #{self.senseid}>"
        elif self.clauses:
            return "<wngSenseExpr: {} with {} clauses>".format(
                self.lemma,
                len(self.clauses)
            )
        else:
            return f"<wngSenseExpr: {self.lemma}>"


class wngRelationExpr:
    def __init__(self, 
        src: wngSenseExpr,
        arrow: ArrowType,
        tgt: wngSenseExpr,
        rel_spec: Optional[wngRelationSpec]=None):
        self.src = src
        self.arrow = arrow
        self.tgt = tgt        
        self.rel_spec = rel_spec
    
    def __repr__(self):
        if self.rel_spec:
            return ("<wngRelationExpr: {} \n" +
                "   {} {}: {}>").format(
                self.src,
                self.arrow,
                self.tgt,
                self.rel_spec
            )
        else:
            return ("<wngRelationExpr: {} \n" +
                "   {} {}>").format(
                self.src,
                self.arrow,
                self.tgt                
            )

wngExpr = Union[wngSenseExpr, wngRelationExpr]

class wngComplexExpr:
    def __init__(self, 
            expr1: wngExpr, 
            expr2: Optional[wngExpr]=None, 
            op: Optional[str]=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op
    
    def __repr__(self):
        return "<wngComplexExpr: {} {} {}>".format(
            self.expr1,
            self.op,
            self.expr2
        )
    
class wngGenitiveExpr:
    def __init__(self, 
            expr: wngComplexExpr, 
            rel_spec: wngRelationSpec):
        self.expr = expr
        self.rel_spec = rel_spec

    def __repr__(self):
        return f"<wngGenitiveExpr: {self.expr}.{self.rel_spec}>"
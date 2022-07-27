from .wn_lexer import lexer, tokens
from .ply import yacc as yacc
from .wn_errors import WngSyntaxError
from .ast_types import *

start = 'statement'

def p_statement(p):
    """
    statement : complex_expr
        | mutation
        | assignment
    """
    p[0] = p[1]

def p_mutation(p):
    """
    mutation : action complex_expr
    """
    p[0] = wngMutation(p[1], p[2])

def p_action(p):
    """
    action : CREATE
        | DELETE
    """
    try:
        p[0] = ActionType[p[1]]
    except IndexError:
        raise WngSyntaxError("Unknown action: "+ 
            p[1], p.lineno(1), p.lexpos(1))    

def p_assignment(p):
    """      
    assignment : TEXT '=' complex_expr
    """
    p[0] = wngAssignment(p[1], p[3])

def p_comlex_expr(p):
    """
    complex_expr : expr        
        | expr '+' expr
        | expr '-' expr
        | '(' complex_expr ')'       
        | complex_expr '.' relation_spec
    """

    if len(p)==4 and p[1] == '(':
        p[0] = p[2]
    elif len(p) == 4 and p[2] == '.':
        p[0] = wngGenitiveExpr(p[1], p[3])
    elif len(p) == 4:
        p[0] = wngComplexExpr(p[1], p[3], p[2])
    else:
        p[0] = p[1]   

def p_expr(p):
    """
    expr : sense_expr
        | relation_expr    
    """
    p[0] = p[1]

def p_sense_expr(p):
    """
    sense_expr : '@'
        | TEXT '@'
        | '$' TEXT
        | '#' TEXT
        | '@' sense_constraints
        | TEXT '@' sense_constraints        
    """
    if len(p) == 2 and p[1] == '@':
        # wildcard sense expr
        p[0] = wngSenseExpr("")    
    elif len(p) == 3 and p[2] == '@':
        p[0] = wngSenseExpr(p[1])
    elif len(p) == 3 and p[1] == '$':        
        p[0] = wngSenseVariable(p[2])
    elif len(p) == 3 and p[1] == "#":
        p[0] = wngSenseExpr(senseid=p[2])
    elif len(p) == 3 and p[1] == "@":
        p[0] = wngSenseExpr("", clauses=p[2])
    else:
        p[0] = wngSenseExpr(p[1], clauses=p[3])

def p_sense_constraints(p):
    """
    sense_constraints : sense_constraint
        | sense_constraints ',' sense_constraint
    """
    if len(p) > 2:
        clauses = p[1][::1]
        clauses.append(p[3])
        p[0] = clauses
    else:
        p[0] = [p[1]]

def p_sense_constraint(p):
    """
    sense_constraint : TEXT
        | relation_spec rel_op sense_expr
        | relation_spec rel_op TEXT
    """
    if len(p) > 2:
        p[0] = wngSenseRelClause(p[1], p[2], p[3])
    else:
        p[0] = wngSenseClause(p[1])

def p_relation_spec(p):
    """
    relation_spec : TEXT
        | TEXT '<' rel_param '>'
    """
    if len(p) == 5:
        p[0] = wngRelationSpec(p[1], p[3])
    else:
        p[0] = wngRelationSpec(p[1])

def p_rel_param(p):
    """
    rel_param : TEXT
        | rel_param ',' TEXT
    """
    if len(p) > 2:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_rel_op(p):
    """
    rel_op : IS
        | IS IN
        | IS NOT
        | IS NOT IN
    """
    if len(p) == 2:
        p[0] = wngRelationOp(equality=True, negation=False)
    elif len(p) == 3 and p[2]=="in":
        p[0] = wngRelationOp(equality=False, negation=False)
    elif len(p) == 3 and p[2]=="not":
        p[0] = wngRelationOp(equality=True, negation=True)
    else:
        p[0] = wngRelationOp(equality=False, negation=True)    

def p_relation_expr(p):
    """
    relation_expr : sense_expr arrow sense_expr    
        | sense_expr arrow sense_expr ':' relation_spec
    """
    if len(p) <= 4:
        p[0] = wngRelationExpr(p[1], p[2], p[3])
    else:
        p[0] = wngRelationExpr(p[1], p[2], p[3], p[5])

def p_arrow(p):
    """
    arrow : LARROW
        | RARROW
        | RPARROW
        | BIARROW        
    """
    p[0] = {
        "->": ArrowType.forward,
        "<-": ArrowType.backward,
        "<->": ArrowType.bidirectional,
        "~>": ArrowType.para_forward
    }.get(p[1], None)           
    if not p[0]:
        raise WngSyntaxError(
            "Unknown arrow type: "+p[1], 
            p.lineno(1), p.lexpos(1))

def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         # Just discard the token and tell the parser it's okay.
         raise Exception("SyntaxError")
    else:
         print("Syntax error at EOF")

parser = yacc.yacc()
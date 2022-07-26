from .wn_lexer import lexer, tokens
from .ply import yacc as yacc

start = 'statement'

def p_statement(p):
    """
    statement : complex_expr
        | mutation
        | assignment
    """
    p[0] = [*p[1:]]

def p_mutation(p):
    """
    mutation : action complex_expr
    """
    p[0] = (p[1], p[2])

def p_action(p):
    """
    action : CREATE
        | DELETE
    """
    p[0] = p[1]   

def p_assignment(p):
    """      
    assignment : TEXT '=' complex_expr
    """
    p[0] = []

def p_comlex_expr(p):
    """
    complex_expr : expr        
        | expr '+' expr
        | expr '-' expr
        | '(' complex_expr ')'       
    """

    if len(p)==4 and p[1] == '(':
        p[0] = p[2]
    elif len(p) == 4:
        p[0] = [p[1], p[3]]
    else:
        p[0] = p[0]    

def p_expr(p):
    """
    expr : sense_expr
        | relation_expr    
    """
    p[0] = []

def p_sense_expr(p):
    """
    sense_expr : TEXT
        | '#' TEXT
        | '@' sense_constraints
        | TEXT '@' sense_constraints        
    """
    p[0] = ["sense_expr", *p[1:]]

def p_sense_constraints(p):
    """
    sense_constraints : sense_constraint
        | sense_constraints ',' sense_constraint
    """
    p[0] = []

def p_sense_constraint(p):
    """
    sense_constraint : TEXT
        | relation_spec rel_op sense_expr
    """
    p[0] = []

def p_relation_spec(p):
    """
    relation_spec : TEXT
        | TEXT '<' rel_param '>'
    """
    if len(p) == 3:
        p[0] = (p[2], p[1])
    else:
        p[0] = (p[1], '')

def p_rel_param(p):
    """
    rel_param : TEXT
        | rel_param ',' TEXT
    """
    p[0] = []

def p_rel_op(p):
    """
    rel_op : IS
        | IS IN
        | IS NOT
        | IS NOT IN
    """
    p[0] = []
    

def p_relation_expr(p):
    """
    relation_expr : sense_expr arrow_spec sense_expr    
        | sense_expr arrow_spec sense_expr ':' relation_spec
    """
    p[0] = []

def p_arrow_spec(p):
    """
    arrow_spec : arrow
        | RELMOD arrow
        | arrow RELMOD
        | RELMOD arrow RELMOD    
    """
    p[0] = []

def p_arrow(p):
    """
    arrow : LARROW
        | RARROW
        | BIARROW
    """
    p[0] = '->'


def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         # Just discard the token and tell the parser it's okay.
         raise Exception("SyntaxError")
    else:
         print("Syntax error at EOF")

parser = yacc.yacc()
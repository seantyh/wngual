from .ply import lex as lex

reserved = (
    'CREATE', 'DELETE', 
    'is', 'not', 'in', 
)

tokens = [       
    'RARROW', 'RPARROW', 'LARROW', 'BIARROW',    
    'TEXT'
    ] + [x.upper() for x in reserved]

literals = list("!@#$%^&()<>=~:;/.,")
t_RARROW = r"->"
t_RPARROW = r"~>"
t_LARROW = r"<-"
t_BIARROW = r"<->"
t_ignore = ' \t\r\n'

def t_TEXT(t):
    r"[a-zA-Z0-9_\u4e00-\u9fff]+"
    if t.value in reserved:
        t.type = t.value.upper()
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

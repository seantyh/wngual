from .ply import lex as lex

tokens = (
    'LEMMA', 
    'HYPER', "HYPO")

t_HYPER = r'@'; t_HYPO = r'~'
t_LEMMA = r"[a-zA-Z0-9_\u4e00-\u9fff]+"

t_ignore = ' \t\r\n'
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

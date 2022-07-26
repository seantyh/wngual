from fixture import *

def test_lexer(wnese):
    lexer = wnese.lexer
    lexer.input("asdfd @ asdfsd")
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok)    

    assert False


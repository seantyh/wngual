from fixture import *

def test_lexer(wg):
    lexer = wg.lexer
    lexer.input("CREATE: 動物@的生物 -> 生物; hypernymy")
    while True:
        tok = lexer.token()
        print(tok)
        if not tok: break            
    


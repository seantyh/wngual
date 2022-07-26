from fixture import *

def test_parser(wg):
    tree = wg.parser.parse("CREATE 動物 .->* 植物")
    print(tree)    

def test_sense_expr(wg):
    tree = wg.parser.parse("@Na, hyper is 動物@的生物, hyper<R> is in @實體")
    # tree = wg.parser.parse("牛@Na, hyper is 動物@的生物, rec.hyper is in @實體")
    print(tree)    
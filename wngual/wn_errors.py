
class WngSyntaxError(Exception):
    def __init__(self, msg, lineno, lexpos):
        self.msg = msg
        self.lineno = lineno
        self.lexpos = lexpos

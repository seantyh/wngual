
class wngBase:

    def __init__(self):
        self.fields = []

    def iter_ast(self):
        for x in self.fields:
            yield getattr(self, x)
class editor:
    def functionalities(self):
        self.funcs=["create","exe","save"]
        return self.funcs
class pycharm(editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("[debug,vc]")
        return funcs
pyc=pycharm()
print(pyc.functionalities())
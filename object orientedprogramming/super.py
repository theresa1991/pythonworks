class parent:
    def properties(self):
        self.prpos={"mobile":"iphone","bike":"yamaha"}
        return self.prpos
class child(parent):
    def properties(self):
        prpos=super().properties()
        prpos["car"]="swift"

        self.prpos={"car":"tiago"}
        return prpos
ch=child()
print(ch.properties())


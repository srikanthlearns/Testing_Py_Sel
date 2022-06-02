class Sri:
    def Characters(self,a,b):
        self.a=a
        self.b=b
        return ('He is a good guy', a*b)
s=Sri()
s1=Sri()
#print(s.Characters())
print(s.Characters(2,3))
print(s.Characters(6,4))


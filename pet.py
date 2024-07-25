class Pet(object):
    anoAtual = 2024 #atributo
       #object é um param obrigatorio em python
    def __init__(self, name, anoNasc):
       self.name = name;
       self.anoNasc = anoNasc;

    def getIdade(self):
        return Pet.anoAtual - self.anoNasc
    
    @classmethod
    def getAnoAtual(cls):
        return cls.anoAtual
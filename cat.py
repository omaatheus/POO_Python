from pet import Pet

class Cat(Pet):
   
    def __init__(self, name, anoNasc):
      super().__init__(name, anoNasc) #fizemos polimorfismo com __init__ e acrescentamos um print ao método
      print(f'Olá, eu sou {self.name}, sua nova gata!')

    def emitirSom(self):
      print(f'{self.name} miou')

    def getAnoNasc(self):
      a = self.anoNasc
      return a

    def getName(self):
       i = self.name
       return i
    
    def setName(self, nome):
       self.nome = nome;
       return None;
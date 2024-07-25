from pet import Pet

class Dog(Pet):

   #self é obrigatorio para TODOS os métodos, ele aponta para o objeto que estamos criando.
    def __init__(self, name, anoNasc):
    #iremos criar os atributos abaixo utilizando self.<nomeAtributo> = <nomeAtributo> 
        super().__init__(name, anoNasc) #fizemos polimorfismo com __init__ e acrescentamos um print ao método
        print(f'Eu sou {self.name}, seu novo cachorro!')

    def emitirSom(self):
      print(f'{self.name} latiu')

    def anoNasc(self):
       print(f'{self.name} nasceu em {self.anoNasc}')

    #metodo get ele permite obter o valor de um atributo de forma segura e controlada.
    def getName(self):
       n = self.name
       return n
    #metodo get permite modificar o valor de um atributo de forma segura e controlada.
    def setName(self, nome):
       self.name = nome
       return None

    def getAnoNasc(self):
       return self.anoNasc
    
    def setAnoNasc(self, ano):
       self.anoNasc = ano;

    def getIdade(self):
       a = super().getIdade()
       return a

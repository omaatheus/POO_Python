from pet import Pet
from cat import Cat
from dog import Dog

#instanciando abaixo
print(f'Ano Atual é: {Pet.getAnoAtual()}')

print(f'====================================')

caramelo = Dog('Rodri', 2017)

#métodos abaixo
caramelo.emitirSom()

caramelo.setName('Leandro')
caramelo.getName()

caramelo.getIdade()

print(f'{caramelo.getName()} tem {caramelo.getIdade()} anos e nasceu em {caramelo.getAnoNasc()}')

print(f'====================================')

belinha = Cat('Belinha', 2015)

belinha.emitirSom()

belinha.getAnoNasc()

print(f'{belinha.getName()} tem {belinha.getIdade()} anos e nasceu em {belinha.getAnoNasc()}')


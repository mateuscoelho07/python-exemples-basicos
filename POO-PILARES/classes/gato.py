# Classe cachorro herda de animal tudo ( herança )
from classes.animal import Animal

class cachorro (Animal):
    def __int__(self, nome, raca):
        #chamando construtor da classe pai 
        super(). _init__(nome)
        self.raca = raca

# Implementação do (polimorfismo)
    def fazer_som(self):
        return "Miau!"
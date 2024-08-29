# Importante ABC  ( Abstrato Base Classes) para criar classes 
from abc import ABC, abstractmethod

class Animal (ABC):
    def __init__(self, nome):
        # Atributo privado (Encapsulado)
        self.__nome = nome 

# Método getter para acessar o atributo privado (Encapsulado)
def get_nome(self) :
    return self.__nome

# Método abstrato (Abstração)
@abstractmethod
def fazer_som(self):
    pass 
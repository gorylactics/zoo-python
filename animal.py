import random
from animo import *
class Animal:
    def __init__(self ,  nombre ,  edad):
        self.nombre = nombre
        self.edad = edad
        self.salud = nivelSalud()
        self.felicidad = nivelFelicidad()

    def alimentar(self):
            self.salud += 10
            self.felicidad += 10

    def displayInfo(self):
        return f'Tipo de animal: {self.tipo}\nNombre del animal: {self.nombre}\ntiene: {self.edad} años\nPorcentaje de salud: {self.salud}\nPorcentaje de felicidad: {self.felicidad}\nSu atributo Caracteristico es: {self.atributo}'
from animal import Animal
class Oso(Animal):
    def __init__(self, tipo , nombre , edad , atributo):
        super().__init__(nombre , edad)
        self.tipo =  tipo
        self.atributo = atributo
    
    def alimentar(self):
            self.salud += 12
            self.felicidad += 15
if __name__ == '__main__':
    oso1 = Oso('meloso' , 'buu buu' , 3 , 'cazador')
    print(oso1.displayInfo())
    oso1.alimentar()
    print(oso1.displayInfo())
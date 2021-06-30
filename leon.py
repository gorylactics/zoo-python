from animal import Animal
class Leon(Animal):
    def __init__(self, tipo , nombre , edad , atributo):
        super().__init__(nombre , edad)
        self.tipo =  tipo
        self.atributo = atributo
    
    def alimentar(self):
            self.salud += 15
            self.felicidad += 8
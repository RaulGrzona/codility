class Motor:
    def __init__(self, marca):
        self.marca = marca
        self.cilindradas = 0
    def bujias(self):
        return 5
    def velocimetro(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima
    def add_cilindradas(self, cilindradas):
        self.cilindradas = cilindradas
    # raul


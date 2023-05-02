class Motor:
    def __init__(self, marca):
        self.marca = marca
        self.cilindradas = 0

    def add_cilindradas(self, cilindradas):
        self.cilindradas = cilindradas

    def __str__(self):
        return "Ete motor es groso"

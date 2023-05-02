class Rueda:
    def __init__(self, numero_llanta, tipo_rodado):
        self.numero_llanta = numero_llanta
        self.tipo_rodado = tipo_rodado

    def __str__(self):
        return (
            f"Numero de llanta: {self.numero_llanta}- Tipo rodado: {self.tipo_rodado}"
        )


r1 = Rueda(numero_llanta=23, tipo_rodado="todo terreno")

print(r1)

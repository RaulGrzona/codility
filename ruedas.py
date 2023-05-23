class Tuerca:
    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return f"Marca: {self.marca}"


class Rueda:
    def __init__(self, numero_llanta, tipo_rodado):
        self.numero_llanta = numero_llanta
        self.tipo_rodado = tipo_rodado
        self.tuercas = [Tuerca(marca="pirelli")] * 5

    def __str__(self):
        return (
            f"Numero de llanta: {self.numero_llanta} -"
            f" Tipo rodado: {self.tipo_rodado} -"
            f"Tuercas: {self.tuercas}"
        )


r1 = Rueda(numero_llanta=23, tipo_rodado="todo terreno")

print(r1)

class Aire_acondic
    def __init__(self, refrigerante, tip_refrig, cantidad_gas):
        self.refrigerante = refrigerante
        self.tip_refrig = tip_refrig
        self.cantidad_gas = cantidad_gas

    def cambiar_cantidad_gas(self, nuevo_cantidad_gas):
        self.nuevo_cantidad_gas = nuevo_cantidad_gas
        if nuevo_cantidad_gas > 2000 :
            return "error de cantidad"
        return "800 gr"

    # prueba de cambio directamente en github

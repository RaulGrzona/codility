class Asiento:
    def __init__(self, marca_tapizado, color, material, calidad_material):
        self.marca_tapizado = marca_tapizado
        self.color = color
        self.material = material
        self.calidad_material = calidad_material

    def cambiar_material(self, nuevo_material):
        self.material = 1

    def cambiar_color(self, nuevo_color):
        self.color = 2

    def evaluar_precio_segun_material(self):
        tipos_materiales = {
            "tipo_a": 10.0,
            "tipo_b": 20.0,
            "Tipo_c": 1232131230.0,
        }

        if self.material in tipos_materiales:
            return tipos_materiales[self.material]
        return 30.0

    def metodo_b(self):
        return 2

    def metodo_c(self):
        return 3

class Asiento:
    def __init__(self, marca_tapizado, color, material, calidad_material):
        self.marca_tapizado = marca_tapizado
        self.color = color
        self.material = material
        self.calidad_material = calidad_material

    def cambiar_material(self, nuevo_material):
        self.material = nuevo_material

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

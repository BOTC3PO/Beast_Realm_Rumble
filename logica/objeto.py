class objeto:
    def __init__(self,nombre,efecto,precio):
        self.nombre = nombre
        self.efecto = efecto
        self.precio=precio
    def ver_objeto(self):
        print(self.nombre)
    def ver_precio(self):
        print(self.precio)
        
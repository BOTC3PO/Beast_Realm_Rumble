class Personaje:
    def __init__(self,nombre,id,mochila):
        self.id=id
        self.nombre = nombre
        self.posicionx=0
        self.posiciony=0
        self.mochila=mochila
    def Mostrar_nombre(self):
        return(self.nombre)
    def cambiar_nombre(self):
        aux= input("introduzca nuevo nombre")
        self.nombre = aux
    def mover_arriba(self):
        self.posiciony+1
    def mover_abajo(self):
        self.posiciony-1
    def mover_derecha(self):
        self.posicionx+1
    def mover_izquierda(self):
        self.posicionx-1
    
        
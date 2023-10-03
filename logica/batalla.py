import math
import Criatura as Criatura
import keyboard as kb

class batalla:
    def __init__(self,turno,campo,criatura_jugador,criatura_contrincante):
        self.turno=turno
        self.campo=campo
        self.criatura_jugador=criatura_jugador
        self.criatura_contrincante=criatura_contrincante
     
    def zona_battalla(self,start):
        fin = True
        contador = 0
        while fin:
            if start and contador:
                kb.add_hotkey('a',batalla)
                kb.add_hotkey('s',batalla)
                kb.add_hotkey('d',batalla)
            else:
                opcion=0
                posible = True
                while posible:
                    opcion=math.random(1,3)
                    if opcion>3:
                        if  self.criatura_contrincante.manares > self.criatura_contrincante.id_habilidad3.costo:
                            
                            pass
                    else:
                        pass
    def empezar(self,jugador,contrincante):
        fastplayer=False
        if self.criatura_jugador.vel > self.criatura_contrincante.vel:
            print("empieza "+ jugador)
            fastplayer=True
        else: 
            print("empieza "+ contrincante)
        return fastplayer
        
    def calculo_de_dano(self):
        pass
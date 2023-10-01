#import logica.Personaje
import platform
import os
import time
import keyboard

def limpiar_pantalla():
    time.sleep(2)
    
    if platform.system()== 'Windows':
        os.system('cls')
    else:
        os.system('clear')
 
def salir():
     print("cerrando..") 
     return False      
        
limpiar_pantalla()
key=""
truedkey= True
print("Precione \"n\" para jugar una la demo\nPrecione \"s\" para salir")
while truedkey:
    keyboard.add_hotkey('a',print,args="iniciando demo")
    keyboard.add_hotkey('s',truedkey = False )
    keyboard.wait('esc')
        
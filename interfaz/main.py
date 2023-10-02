#import logica.Personaje
import platform
import os
import time
import keyboard
from threading import Timer

def limpiar_pantalla():
    time.sleep(2)
    
    if platform.system()== 'Windows':
        os.system('cls')
    else:
        os.system('clear')
 
def salir():
    print("cerrando..")      
def iniciar():
    print("iniciando nuevo juego")
    batalla()
      
def batalla():
    dialog0=Timer(5,dialogotimeout,args=(0))
    dialog1=Timer(1,dialogotimeout,args=(1))
    dialog2=Timer(2,dialogotimeout,args=(2))
    limpiar_pantalla()
    print("Instrucciones\nlos dialogos se pueden pasar apretando \"Q\"")   
    keyboard.wait('q')  
    limpiar_pantalla()
    print('Beast Realm...')
    dialog0.start()
    dialog1.start()
    dialog2.start()
    keyboard.wait('q') 
    dialog0.cancel()
    dialog1.cancel()
    dialog2.cancel()
    
def dialogotimeout(aux):
    if aux==0:
        print('\n\npreciona Q para continuar')
    if aux==1:
        print('un mundo lleno de creaturas y bestias magicas...')
    if aux==2:
        print('un mundo lleno de creaturas miticas...')    
    
limpiar_pantalla()
key=""
truedkey= True
print("Precione \"N\" para jugar una la demo\nPrecione \"esc\" para salir")
keyboard.add_hotkey('n',iniciar)
keyboard.wait('esc')
print("cerrando..")  
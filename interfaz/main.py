#import logica.Personaje
import platform
import os
import time
import keyboard as kb
from threading import Timer
import logica.Criatura as Criatura
import logica.Habilidad as Habilidad
import logica.efecto as Efecto
import logica.batalla as Battle
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
    siguiente=True
    dialog0=Timer(4,dialogotimeout,args=(0,))
    limpiar_pantalla()
    print("Instrucciones\nlos dialogos se pueden pasar apretando \"Q\"")  
    while siguiente:
        if kb.is_pressed("q"):
            siguiente=False
            
    dialog1=Timer(1,dialogotimeout,args=(1,))
    dialog2=Timer(2,dialogotimeout,args=(2,))   
    limpiar_pantalla()
    siguiente=True
    print('Beast Realm...')
    dialog0.start()
    dialog1.start()
    dialog2.start()
    while siguiente:
        if kb.is_pressed("q"):
            siguiente=False
    dialog0.cancel()
    dialog1.cancel()
    dialog2.cancel()
    limpiar_pantalla()
    nombre = input("¿cómo te llamabas tengo amnesia selectiva?\n")
    limpiar_pantalla()
    dialog4=Timer(2,dialogotimeout,args=(0,))
    dialog5=Timer(2,dialogotimeout,args=(3,))
    dialog4.start()
    dialog5.start()
    print("hola "+nombre+" soy el profesor Haya")
    siguiente= True
    while siguiente:
        if kb.is_pressed("q"):
            siguiente=False
    dialog4.cancel()
    dialog5.cancel()
    limpiar_pantalla()
    efecto = Efecto(1,"elemental fuego","los monstruos pueden quemar a los monstruos menos a los de agua")
    id_habilidad1=Habilidad(1,"golpe llameante","fuego",5,0,efecto)
    id_habilidad2=Habilidad(2,"lanzallamas","fuego",100,0,efecto)
    id_habilidad3=Habilidad(3,'meteoro',"fuego",0.5,0,efecto)
    jugador = Criatura(1,1,'Fuego',"legendario dragon de las llamas de ojos cerulios",5,5,5,5,50,0,600,210,140,300,3000,"",id_habilidad1,id_habilidad2,id_habilidad3) 
    efecto = Efecto(2,"elemental tierra","los monstuos de tierra son mas resistentes")
    id_habilidad1=Habilidad(1,"golpe","tierra",5,0,efecto)
    id_habilidad2=Habilidad(2,"sismo","tierra",100,0,efecto)
    id_habilidad3=Habilidad(3,'goblin golpear',"tierra",0.5,0,efecto)
    oponente = Criatura(1,1,'tierra',"goblin",5,5,5,5,70,0,400,500,140,300,4000,"",id_habilidad1,id_habilidad2,id_habilidad3)
    Battle(0,"zona cuantica",jugador,oponente)
    
def dialogotimeout(aux):
    if aux==0:
        print('\n\npreciona Q para continuar')
    if aux==1:
        print('un mundo lleno de creaturas y bestias magicas...')
    if aux==2:
        print('un mundo lleno de creaturas miticas...')    
    if aux==3:
        print("el es tu rival lavir")
  
limpiar_pantalla()
key=""
truedkey= True
print("Precione \"N\" para jugar una la demo\nPrecione \"esc\" para salir")
kb.add_hotkey('n',batalla)
kb.add_hotkey('esc',salir)
kb.wait('esc')
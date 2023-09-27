class Criatura:
    def __init__(self,id_creatura,id_jugador,tipo,subtipo,base_hp,base_atk,base_def,base_mana,nivel,xp,hp,atk,defensa,vel,mana,pasiva,id_habilidad1,id_habilidad2,id_habilidad3):
        self.id_creatura= id_creatura
        self.idjugador= id_jugador
        self.tipo = tipo
        self.subtipo = subtipo
        self.base_hp = base_hp
        self.base_atk=base_atk
        self.base_def=base_def
        self.base_mana=base_mana
        self.nivel=nivel
        self.xp=xp
        self.hp=hp
        self.atk=atk
        self.defensa=defensa
        self.vel=vel
        self.mana=mana
        self.pasiva=pasiva
        self.id_habilidad1=id_habilidad1
        self.id_habilidad2=id_habilidad2
        self.id_habilidad3=id_habilidad3
    def calculo_dano(self,vida):
        self.hp-vida
    def estadisticas(self):
        print(self.hp + self.atk + self.defensa + self.vel + self.mana)
        
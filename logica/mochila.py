class mochila:
    def __init__(self):
        self.objetos=[]
        self.creaturas=[]
        self.monedas=[{"gold":0,"silver":0}]
    def ver_mochila(self):
        print(self.objetos)
    def anadir_objeto(self):
        self.objetos.insert()
    def ver_monedas(self):
        return(self.monedas)
    def modificar_oro(self,coin):
        if self.monedas.index("gold") < 0:
            self.monedas.index("gold")+coin
        else:
            print("no hay monedas")
    def modificar_silver(self,coin):
       if self.monedas.index("silver") < 0:
            self.monedas.index("silver")+coin
       else:
            print("no hay monedas")



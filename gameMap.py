from tile import *

class gameMap:
    def __init__(self,data=None):
        if data is not None:
            self.map = data
        else:
            self.map = []
            for i in range(100):
                self.map.append(tile())

            self.map[0].isOpen = True
            self.map[1].mana = 5
            self.map[2].state = ('chance',None,None)
            self.map[3].state = ('heal',30,None)
            self.map[4].state = ('battle','wolf',None)
            self.map[5].state = ('move','push',3)
            self.map[6].state = ('move','portal',1)
            self.map[7].state = ('move','player',0)
            self.map[8].state = ('trap','poison',10)
            self.map[9].state = ('trap','overLoad',None)
            self.map[10].state = ('trap','atomic',None)
            
            

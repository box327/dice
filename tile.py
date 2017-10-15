class tile:
    def __init__(self,data=None):
        if data is not None:
            self.isOpen = False
            self.mana = data.mana
            self.state = data.state
            
        else:
            self.isOpen = False
            self.mana = 3
            self.state = ('normal',None,None)


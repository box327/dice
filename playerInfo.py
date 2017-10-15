class playerInfo(object):
    def __init__(self,job,playerType,number):
        self.hp = 100
        self.mana = 3

        self.card = []
        self.state = []
        
        self.job = job
        self.position = 0

        self.playerType = playerType
        self.playerNum = number

        self.battleDice = 6
        self.battleDiceNum = 2
        
        self.moveDice = 6

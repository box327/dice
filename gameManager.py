import messageManager
import playerInfo

class gameManager(object):
    def __init__(self,messageManager,gameInfo):
        self.gameInfo = gameInfo

        self.messageManager = messageManager

        self.messageManager.listen("moveCheck",self.moveCheck)
        self.messageManager.listen("addMoveCheck",self.addMoveCheck)
        self.messageManager.listen("drawCardCheck",self.drawCardCheck)
        self.messageManager.listen("jobActCheck",self.jobActCheck)
        self.messageManager.listen("move",self.normalMove)
        self.messageManager.listen("addMove",self.addMove)
        
    def moveCheck(self,player):
        if self.turnCheck(player) == False:
            return
        if self.gameInfo.turn.moveFlag is True:
            self.messageManager.send("warningMessage","you cant move now turn")
            return

        self.messageManager.send("createDice",("move",player,True))
        
    def move(self,parameter):
        parameter[0].position += parameter[1]

        if parameter[0].position >= 100:
            pass

        targetPlayer = parameter[0]
        nowTile = self.gameInfo.gameMap.map[parameter[0].position]

        
        if nowTile.isOpen is False:
            nowTile.isOpen = True

        addMana = nowTile.mana
        
        for i in targetPlayer.state:
            if i[0] == 'overLoad':
                addMana = 0
                
        targetPlayer.mana += addMana
        if targetPlayer.mana > 5:
            targetPlayer.mana = 5


        for i in self.gameInfo.player:
            if i.position == targetPlayer.position:
                if i.playerNum != targetPlayer.playerNum:
                    self.messageManager.send("battle",(targetPlayer,i))
                    return

        if nowTile.state[0] == 'move':
            if nowTile.state[1] == 'push':
                self.move((targetPlayer,nowTile.state[2]))
            elif nowTile.state[1] == 'portal':
                self.move((targetPlayer,nowTile.state[2] - targetPlayer.position))
            elif nowTile.state[1] == 'player':
                pass

        elif nowTile.state[0] == 'battle':
            battleTarget = playerInfo.playerInfo('monster','',9)
            if nowTile.state[1] == 'wolf':
                battleTarget.playerType = 'wolf'
                battleTarget.hp = 30
                battleTarget.battleDice = 6
                battleTarget.battleDiceNum = 1
            elif nowTile.state[1] == 'dragon':
                battleTarget.playerType = 'dragon'
                battleTarget.hp = 100
                battleTarget.battleDice = 6
                battleTarget.battleDiceNum = 2
            elif nowTile.state[1] == 'bee':
                battleTarget.playerType = 'bee'
                battleTarget.hp = 20
                battleTarget.battleDice = 4
                battleTarget.battleDiceNum = 1
            elif nowTile.state[1] == 'ice':
                battleTarget.playerType = 'ice'
                battleTarget.hp = 20
                battleTarget.battleDice = 4
                battleTarget.battleDiceNum = 2
            elif nowTile.state[1] == 'boom':
                battleTarget.playerType = 'boom'
                battleTarget.hp = 1
                battleTarget.battleDice = 6
                battleTarget.battleDiceNum = 1
            elif nowTile.state[1] == 'tiger':
                battleTarget.playerType = 'tiger'
                battleTarget.hp = 40
                battleTarget.battleDice = 12
                battleTarget.battleDiceNum = 1
            self.messageManager.send('battle',(targetPlayer,battleTarget))
        elif nowTile.state[0] == 'heal':
            targetPlayer.hp += nowTile.state[2]
            if targetPlayer.hp > 100:
                targetPlayer.hp = 100
        elif nowTile.state[0] == 'trap':
            if nowTile.state[1] == 'poison':
                targetPlayer.state.append(['poison',3,nowTile.state[2]])
            elif nowTile.state[1] == 'overLoad':
                targetPlayer.state.append(['overLoad',1])
                targetPlayer.mana = 0
            elif nowTile.state[1] == 'atomic':
                targetPlayer.state.append(['atomic',2])
    def normalMove(self,parameter):
        self.messageManager.send("destroyDice",None)

        self.gameInfo.turn.moveFlag = True
        
        self.move(parameter)


    def addMoveCheck(self,player):
        if self.turnCheck(player) == False:
            return
        if self.gameInfo.turn.addMoveFlag is True:
            self.messageManager.send("warningMessage","you use your addition move chance")
            return
        if player.mana < 1:
            self.messageManager.send("warningMessage","not enough mana")
            return
        
        self.messageManager.send("createDice",("addMove",player,False))

    def addMove(self,parameter):
        self.messageManager.send("destroyDice",None)
        
        self.gameInfo.turn.nowPlayer.mana -= 1
        self.gameInfo.turn.addMoveFlag = True
        
        self.move(parameter)

        
    
    def drawCardCheck(self,player):
        if self.turnCheck(player) == False:
            return
        if self.gameInfo.turn.drawCardFlag is True:
            self.messageManager.send("warningMessage","you use your draw card chance")
            return
        if player.mana < 1:
            self.messageManager.send("warningMessage","not enough mana")
            return
        
    def jobActCheck(self,player):
        if self.turnCheck(player) == False:
            return

        if self.gameInfo.turn.jobActFlag is True:
            self.messageManager.send("warningMessage","you use your job action chance")
            return

        if player.job is 'wizard' and player.mana < 2:
            self.messageManager.send("warningMessage","not enough mana")
            return
        elif player.job is 'fighter' and player.mana < 3:
            self.messageManager.send("warningMessage","not enough mana")
            return
        elif player.job is 'hunter' and player.mana < 2:
            self.messageManager.send("warningMessage","not enough mana")
            return
        else:
            return ""

    def turnCheck(self,player):
        for state in player.state:
            if state[0] == 'stun':
                self.messageManager.send("warningMessage","STUN")
                return False
                
        if player != self.gameInfo.turn.nowPlayer or player.playerType == 'cpu':
            self.messageManager.send("warningMessage","is not your turn")
            return False

import random

class battleInfo(object):
    def __init__(self,players):
        self.attackPlayer = players[0]
        self.targetPlayer = players[1]
        self.attackPlayerEven = 0
        self.targetPlayerEven = 0

        self.attackPlayerCritical = False
        self.targetPlayerCritical = False

        self.damage = 0

        self.start = False

        self.eventFlag = False

class battleManager(object):
    def __init__(self,messageManager,gameInfo):
        self.messageManager = messageManager
        self.gameInfo = gameInfo

        self.messageManager.listen("battle",self.battleInit)
        self.messageManager.listen('attack',self.attack)
        self.messageManager.listen('finishBattle',self.battleFinish)
        
    def battleInit(self,players):
        self.nowBattle = battleInfo(players)
        self.messageManager.send("createBattle",self.nowBattle)

    def battleFinish(self,player):
        self.messageManager.send('destroyBattle',None)
        player[0].state.append(['stun',1])

        if len(player[0].card) != 0:
            card = player[0].card[random.randRange(0,len(player[0].card))]
            player[0].card.remove(card)
            player[1].card.append(card)
    
    def attack(self,dummy):
        if self.nowBattle.attackPlayer.hp == 0:
            self.messageManager.send('finishBattle',(self.nowBattle.attackPlayer,self.nowBattle.targetPlayer))
            return
        elif self.nowBattle.targetPlayer.hp == 0:
            self.messageManager.send('finishBattle',(self.nowBattle.targetPlayer,self.nowBattle.attackPlayer))
            return
        self.start = True
        
        player1Dice1 = random.randrange(1,self.nowBattle.attackPlayer.battleDice + 1)
        if self.nowBattle.attackPlayer.battleDiceNum == 2:
            player1Dice2 = random.randrange(1,self.nowBattle.attackPlayer.battleDice + 1)
            player1Sum = player1Dice1 + player1Dice2
        else:
            player1Sum = player1Dice1
        player2Dice1 = random.randrange(1,self.nowBattle.targetPlayer.battleDice + 1)
        if self.nowBattle.targetPlayer.battleDiceNum == 2:
            player2Dice2 = random.randrange(1,self.nowBattle.targetPlayer.battleDice + 1)
            player2Sum = player2Dice1 + player2Dice2
        else:
            player2Sum = player2Dice1


        damage = player1Sum - player2Sum

        if player1Sum == 12 and player2Sum != 12 and self.nowBattle.attackPlayer.battleDiceNum == 2:
            self.nowBattle.attackPlayerCritical = True
            damage = 12
        elif player2Sum == 12 and player1Sum == 12 and self.nowBattle.targetPlayer.battleDiceNum == 2:
            self.nowBattle.targetPlayerCritical = True
            damage = -12
        else:
            self.nowBattle.attackPlayerCritical = False
            self.nowBattle.targetPlayerCritical = False

        if damage >= 0:
            temp = damage * (self.nowBattle.attackPlayerEven + 1)
            damage = temp
            self.nowBattle.targetPlayer.hp -= damage
                
        elif damage < 0:
            temp = damage  * (self.nowBattle.targetPlayerEven + 1)
            damage = temp
            self.nowBattle.attackPlayer.hp += damage
            if self.nowBattle.targetPlayer.playerType == 'boom':
                self.nowBattle.attackPlayer.hp  -= 30
                self.nowBattle.targetPlayer.hp = 0
            elif self.nowBattle.targetPlayer.playerType == 'bee' and self.nowBattle.eventFlag == False:
                self.nowBattle.attackPlayer.state.append(['poison',3,10])
                self.nowBattle.eventFlag = True
            elif self.nowBattle.targetPlayer.playerType == 'ice' and self.nowBattle.eventFlag == False:
                self.nowBattle.attackPlayer.state.append(['frozen',2])
                self.nowBattle.eventFlag = True

        
        if self.nowBattle.attackPlayer.battleDiceNum == 2 and player1Dice1 == player1Dice2:
            self.nowBattle.attackPlayerEven += 1
        else:
            self.nowBattle.attackPlayerEven = 0

        if self.nowBattle.targetPlayer.battleDiceNum == 2 and player2Dice1 == player2Dice2:
            self.nowBattle.targetPlayerEven += 1
        else:
            self.nowBattle.targetPlayerEven = 0
        
        self.nowBattle.damage = damage

        if self.nowBattle.attackPlayer.hp < 0:
            self.nowBattle.attackPlayer.hp = 0
            self.nowBattle.start = False
            
        if self.nowBattle.targetPlayer.hp < 0:
            self.nowBattle.targetPlayer.hp = 0
            self.nowBattle.start = False

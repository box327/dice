class turnManager(object):
    def __init__(self,messageManager,gameInfo):
        self.messageManager = messageManager
        self.gameInfo = gameInfo

        self.messageManager.listen('endTurn',self.endTurn)
    def endTurn(self,dummy):
        turnInfo = self.gameInfo.turn
        playerNum = len(self.gameInfo.player)

        if turnInfo.moveFlag == False:
            turnInfo.nowPlayer.hp += 20
            if turnInfo.nowPlayer.hp > 100:
                turnInfo.nowPlayer.hp = 100


        for state in turnInfo.nowPlayer.state:
            if state[0] == 'stun':                
                state[1] -= 1
                if state[1] == 0:
                    turnInfo.nowPlayer.state.remove(state)
                    turnInfo.nowPlayer.hp = 100
            elif state[0] == 'poison':                
                state[1] -= 1
                turnInfo.nowPlayer.hp -= state[2]
                if turnInfo.nowPlayer.hp <= 0:
                    turnInfo.nowPlayer.hp = 1
                if state[1] == 0:
                    turnInfo.nowPlayer.state.remove(state)
            elif state[0] == 'frozen':                
                state[1] -= 1
                if state[1] == 0:
                    turnInfo.nowPlayer.state.remove(state)
        
        turnInfo.moveFlag = False
        turnInfo.addMoveFlag = False
        turnInfo.drawCardFlag = False
        turnInfo.jobActFlag = False

        nextPlayerNum = turnInfo.nowPlayer.playerNum + 1
        if nextPlayerNum == len(self.gameInfo.player):
            nextPlayerNum = 0
        nextPlayer = self.gameInfo.player[nextPlayerNum]
        turnInfo.nowPlayer = nextPlayer

            
        if nextPlayer.playerType == 'cpu':
            self.messageManager.send("aiRequest",nextPlayer)
        elif nextPlayer.playerType == 'creature':
            self.messageManager.send("creatureRequest",nextPlayer)

        turnInfo.turn += 1

        

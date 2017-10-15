import messageManager
import screen
import gameScreen
import diceScreen
import battleScreen

class screenManager(object):
    def __init__(self,pygame,messageManager,screenList):
        self.pygame = pygame
        self.messageManager = messageManager
        self.screenList = screenList

        self.messageManager.listen('createGame',self.createGameScreen)
        self.messageManager.listen('createDice',self.createDiceScreen)
        self.messageManager.listen('createBattle',self.createBattleScreen)
        self.messageManager.listen('destroyDice',self.destroyDiceScreen)
        self.messageManager.listen('destroyBattle',self.destroyBattleScreen)

    def createGameScreen(self,gameInfo):
        self.screenList.insert(len(self.screenList),gameScreen.gameScreen(self.pygame,self.messageManager,gameInfo))

    def createDiceScreen(self,returningTarget):
        self.screenList.insert(len(self.screenList),diceScreen.diceScreen(self.pygame,self.messageManager,returningTarget))

    def createBattleScreen(self,battleInfo):
        self.screenList.insert(len(self.screenList),battleScreen.battleScreen(self.pygame,self.messageManager,battleInfo))
        
    def destroyDiceScreen(self,dummy):
        target = None
        for screen in self.screenList:
            if type(screen) == diceScreen.diceScreen:
                target = screen

        self.screenList.remove(target)

    def destroyBattleScreen(self,dummy):
        target = None
        for screen in self.screenList:
            if type(screen) == battleScreen.battleScreen:
                target = screen

        self.screenList.remove(target)

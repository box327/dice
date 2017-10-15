from screen import *


class gameScreen(screen):
    def __init__(self,pygame,messageManager,gameInfo):
        screen.__init__(self,pygame)
        self.messageManager = messageManager
        self.gameInfo = gameInfo
        self.viewPort = 10

        self.tileFont = pygame.font.Font('freesansbold.ttf',10)
        self.turnFont = pygame.font.Font('freesansbold.ttf',15)
        self.statusFont = pygame.font.Font('freesansbold.ttf',15)
        
    def draw(self,window):
        window.fill(self.pygame.Color(255,255,255))

        turnMsg = self.turnFont.render('turn ' + str(self.gameInfo.turn.turn),False,self.pygame.Color(0,0,255))
        rect = turnMsg.get_rect().topleft = (300, 50)
        window.blit(turnMsg,rect)

        status = 'playerNum ' + str(self.gameInfo.turn.nowPlayer.playerNum)
        statusHp = 'hp : ' + str(self.gameInfo.turn.nowPlayer.hp)
        statusMana = 'mana : ' + str(self.gameInfo.turn.nowPlayer.mana)
        state = 'state : '
        for i in self.gameInfo.turn.nowPlayer.state:
            state += i[0] + ' '

        statusMsg = self.statusFont.render(status,False,self.pygame.Color(0,0,0))
        statusRect = statusMsg.get_rect().topleft = (400,50)
        window.blit(statusMsg,statusRect)
        statusHpMsg = self.statusFont.render(statusHp,False,self.pygame.Color(0,0,0))
        statusHpRect = statusHpMsg.get_rect().topleft = (400,62)
        window.blit(statusHpMsg,statusHpRect)
        statusManaMsg = self.statusFont.render(statusMana,False,self.pygame.Color(0,0,0))
        statusManaRect = statusManaMsg.get_rect().topleft = (400,74)
        window.blit(statusManaMsg,statusManaRect)
        stateManaMsg = self.statusFont.render(state,False,self.pygame.Color(0,0,0))
        stateManaRect = stateManaMsg.get_rect().topleft = (400,86)
        window.blit(stateManaMsg,stateManaRect)
        
        for i in range(0,100):

            tileNumMsg = self.tileFont.render(str(i),False,self.pygame.Color(0,0,255))
            tileNumRect = tileNumMsg.get_rect().topleft = (i * 60 + 10 - self.viewPort, 280)
            window.blit(tileNumMsg,tileNumRect)
                
            if self.gameInfo.gameMap.map[i].isOpen is False:
                self.pygame.draw.rect(window,(200,200,200),(i*60 - self.viewPort,300,50,50))

                manaMsg = self.tileFont.render('mana ' + str(self.gameInfo.gameMap.map[i].mana),False,self.pygame.Color(0,0,255))
                manaRect = manaMsg.get_rect().topleft = (i * 60 + 10 - self.viewPort, 320)
                window.blit(manaMsg,manaRect)

                message = str(self.gameInfo.gameMap.map[i].state[1])
                if self.gameInfo.gameMap.map[i].state[0] == 'move':
                    message = str(self.gameInfo.gameMap.map[i].state[1]) + ' ' + str(self.gameInfo.gameMap.map[i].state[2])
                    
                tileMsg = self.tileFont.render(message,False,self.pygame.Color(0,0,255))
                tileRect = tileMsg.get_rect().topleft = (i * 60 + 10 - self.viewPort, 330)
                window.blit(tileMsg,tileRect)

            else:
                self.pygame.draw.rect(window,(100,100,100),(i*60 - self.viewPort,300,50,50))

                if self.gameInfo.gameMap.map[i].mana is 5:
                    tileMsg = self.tileFont.render('mana 5',False,self.pygame.Color(0,0,255))
                    rect = tileMsg.get_rect().topleft = (i * 60 + 10 - self.viewPort, 320)
                    window.blit(tileMsg,rect)

                if self.gameInfo.gameMap.map[i].state[0] == 'chance':
                    tileMsg = self.tileFont.render('chance',False,self.pygame.Color(0,0,255))
                    rect = tileMsg.get_rect().topleft = (i * 60 + 10 - self.viewPort, 320)
                    window.blit(tileMsg,rect)
                
                if self.gameInfo.gameMap.map[i].state[0] == 'heal':
                    tileMsg = self.tileFont.render('heal ' + str(self.gameInfo.gameMap.map[i].state[1]),False,self.pygame.Color(0,0,255))
                    rect = tileMsg.get_rect().topleft = (i * 60 + 10 - self.viewPort, 320)
                    window.blit(tileMsg,rect)
                    
                
        for player in self.gameInfo.player:
            self.pygame.draw.rect(window,(255,0,0),(player.position*60 + 10 - self.viewPort,310,30,30))

    def update(self):
        for event in self.pygame.event.get():
            if event.type == QUIT:
                self.pygame.quit()
                self.messageManager.send('quit',0)
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.viewPort -= 50
                if event.key == K_RIGHT:
                    self.viewPort += 50
                if event.key == K_1:
                    self.messageManager.send('moveCheck',self.gameInfo.turn.nowPlayer)
                if event.key == K_2:
                    self.messageManager.send('addMoveCheck',self.gameInfo.turn.nowPlayer)
                if event.key == K_5:
                    self.messageManager.send('endTurn',self.gameInfo.turn.nowPlayer)

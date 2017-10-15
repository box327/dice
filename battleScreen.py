from screen import *
class battleScreen(screen):
    def __init__(self,pygame,messageManager,battleInfo):
        screen.__init__(self,pygame)
        self.messageManager = messageManager
        self.battleInfo = battleInfo

        self.diceImage = self.pygame.image.load('dice.jpg')
        self.hpFont = self.pygame.font.Font('freesansbold.ttf',20)
        self.evenFont = self.pygame.font.Font('freesansbold.ttf',30)
        self.criticalFont = self.pygame.font.Font('freesansbold.ttf',30)
        self.drawFont = self.pygame.font.Font('freesansbold.ttf',50)
        
    def draw(self,window):
        window.fill(self.pygame.Color(255,255,255))

        self.pygame.draw.line(window,self.pygame.Color(0,0,0),(320,0),(320,680),4)

        if self.battleInfo.damage < 0:
            damageMsg = self.hpFont.render('Damage : ' + str(-self.battleInfo.damage),False,self.pygame.Color(255,0,0))
            damageRect = damageMsg.get_rect().topleft = (50,120)
            window.blit(damageMsg,damageRect)
            
        if self.battleInfo.attackPlayerEven > 0:
            evenMsg = self.evenFont.render('E V E N  ' + str(self.battleInfo.attackPlayerEven * 2) + 'X' , False, self.pygame.Color(255,255,0))
            evenRect = evenMsg.get_rect().topleft = (50,50)
            window.blit(evenMsg,evenRect)

        if self.battleInfo.attackPlayerCritical == True:
            criticalMsg = self.criticalFont.render('C R I T I C A L !!!', False, self.pygame.Color(255,0,0))
            criticalRect = criticalMsg.get_rect().topleft = (50,20)
            window.blit(criticalMsg,criticalRect)
        
        window.blit(self.diceImage,(20,200))
        window.blit(self.diceImage,(120,200))

        player1HpMsg = self.hpFont.render('HP : ' + str(self.battleInfo.attackPlayer.hp),False,self.pygame.Color(0,0,255))
        player1HpRect = player1HpMsg.get_rect().topleft = (50,100)
        window.blit(player1HpMsg,player1HpRect)

        if self.battleInfo.damage > 0:
            damageMsg = self.hpFont.render('Damage : ' + str(self.battleInfo.damage),False,self.pygame.Color(255,0,0))
            damageRect = damageMsg.get_rect().topleft = (370,120)
            window.blit(damageMsg,damageRect)
            
        if self.battleInfo.targetPlayerEven > 0:
            evenMsg = self.evenFont.render('E V E N  ' + str(self.battleInfo.targetPlayerEven * 2) + 'X' , False, self.pygame.Color(255,255,0))
            evenRect = evenMsg.get_rect().topleft = (370,50)
            window.blit(evenMsg,evenRect)

        if self.battleInfo.targetPlayerCritical == True:
            criticalMsg = self.criticalFont.render('C R I T I C A L !!!', False, self.pygame.Color(255,0,0))
            criticalRect = criticalMsg.get_rect().topleft = (370,20)
            window.blit(criticalMsg,criticalRect)
   
        
        window.blit(self.diceImage,(340,200))
        window.blit(self.diceImage,(460,200))

        player2HpMsg = self.hpFont.render('HP : ' + str(self.battleInfo.targetPlayer.hp),False,self.pygame.Color(0,0,255))
        player2HpRect = player2HpMsg.get_rect().topleft = (370,100)
        window.blit(player2HpMsg,player2HpRect)


        
    def update(self):
        for event in self.pygame.event.get():
            if event.type == QUIT:
                self.pygame.quit()
                self.messageManager.send('quit',0)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.messageManager.send("attack",None)
                    

from screen import *
from pygame.locals import *
import random

class diceScreen(screen):
    def __init__(self,pygame,messageManager,parameter):
        screen.__init__(self,pygame)
        self.messageManager = messageManager

        self.animateTime = 0
        self.animateImage = []

        self.animateImage.append(self.pygame.image.load('dice.jpg'))
        
        self.returningDiceTarget = parameter[0]
        self.targetPlayer = parameter[1]
        self.addFlag = parameter[2]
        
    def draw(self,window):
        window.blit(self.animateImage[0],(300,300))
        if self.addFlag == True:
            window.blit(self.animateImage[0],(400,300))
        
    def update(self):
        for event in self.pygame.event.get():
            if event.type == QUIT:
                self.pygame.quit()
                self.messageManager.send('quit',0)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    dice = random.randrange(1,self.targetPlayer.moveDice + 1)
                    if self.addFlag == True:
                        dice2 = random.randrange(1,self.targetPlayer.moveDice + 1)
                        temp = dice + dice2
                        dice = temp

                    for state in self.targetPlayer.state:
                        if state[0] == 'frozen':
                            dice -= 1
                        
                    self.messageManager.send(self.returningDiceTarget,(self.targetPlayer,dice))
                    

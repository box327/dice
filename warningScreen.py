from screen import *

class warningScreen(screen):
    def __init__(self,pygame,messageManager):
        screen.__init__(self,pygame)
        self.messageManager = messageManager

        self.message = None
        self.time = 0

        self.messageFont = pygame.font.Font('freesansbold.ttf',50)

        self.messageManager.listen('warningMessage',self.showMessage)

    def showMessage(self,message):
        self.message = message
        self.time = 0

    def draw(self,window):
        if self.message != None and self.time < 60:
            msg = self.messageFont.render(self.message,False,self.pygame.Color(0,0,0))
            rect = msg.get_rect().topleft = (100,200)
            window.blit(msg,rect)
            self.time += 1

    def update(self):
        pass

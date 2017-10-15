from pygame.locals import *

class screen(object):
    pygame = 0;

    
    def __init__(self,pygame):
        self.pygame = pygame

    def __del__(self):
        pass
        
    def draw(self,window):
        window.fill(self.pygame.Color(255,255,255))

    def update(self):
        for event in self.pygame.event.get():
            if event.type == QUIT:
                self.pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.pygame.event.post(self.pygame.event.Event(QUIT))         

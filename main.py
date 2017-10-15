import pygame, sys
from pygame.locals import *

import gameManager
import playerInfo
import turnInfo
import gameMap
import gameInfo
import messageManager
import screenManager
import turnManager
import battleManager
import warningScreen
import mapMaker

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640,480))
pygame.display.set_caption('test')

def quit(i):
    sys.exit()

mapMaker = mapMaker.mapMaker()

gameMap = mapMaker.create()
player = []
player.append(playerInfo.playerInfo('wizard','pc',0))
player.append(playerInfo.playerInfo('wizard','pc',1))
turn = turnInfo.turnInfo(player[0])

gameInfo = gameInfo.gameInfo(gameMap,player,turn)

messageManager = messageManager.messageManager()

messageManager.listen('quit',quit)

gameManager = gameManager.gameManager(messageManager,gameInfo)
turnManager = turnManager.turnManager(messageManager,gameInfo)
battleManager = battleManager.battleManager(messageManager,gameInfo)

screenList = []

screenManager = screenManager.screenManager(pygame,messageManager,screenList)

messageManager.send("createGame",gameInfo)

warningScreen = warningScreen.warningScreen(pygame,messageManager)

while True:
    for i in screenList:
        i.draw(windowSurfaceObj)

    warningScreen.draw(windowSurfaceObj)

    screenList[len(screenList)-1].update()

    pygame.display.update()

    fpsClock.tick(30)

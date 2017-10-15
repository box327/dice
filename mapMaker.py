import gameMap
import tile
import random

class mapMaker(object):
    def __init__(self):
        self.mapMakingValue = []
        self.mapMakingManaValue = []

        for i in range(0,100):
            self.mapMakingValue.append([])
            self.mapMakingManaValue.append([])

        
        mapFile = open('map.txt')
        try:
            for line in mapFile:
                line = line.strip('\r\n')
                values = line.split('\t')
                for i in range(int(values[0]),int(values[1])):
                    if values[3] == 'mana':
                        self.mapMakingManaValue[i].append((values[2],values[4]))
                    elif values[3] == 'battle':
                        self.mapMakingValue[i].append((values[2],(values[3],values[4],None)))
                    elif values[3] == 'move':
                        self.mapMakingValue[i].append((values[2],(values[3],values[4],int(values[5]))))
                    elif values[3] == 'heal':
                        self.mapMakingValue[i].append((values[2],(values[3],'heal',int(values[4]))))
                    elif values[3] == 'trap':
                        if values[4] == 'poison':
                            self.mapMakingValue[i].append((values[2],(values[3],values[4],int(values[5]))))
                        else:
                            self.mapMakingValue[i].append((values[2],(values[3],values[4],None)))

                            
        finally:
            mapFile.close()

        self.mapMakingValue[0].append(('1',(None,None,None)))
        self.mapMakingManaValue[0].append(('1','0'))

    def create(self):
        mapData = []
        for i in range(0,100):
            tempTile = tile.tile()
            
            manaValue = self.mapMakingManaValue[i]
            valueSum = 0
            for j in manaValue:
                valueSum += int(j[0])

            randomValue = random.randrange(0,valueSum)

            valueSum = 0
            target = None
            for j in manaValue:
                valueSum += int(j[0])
                if randomValue < valueSum:
                    target = j
                    break
            tempTile.mana = int(target[1])

            stateValue = self.mapMakingValue[i]
            valueSum = 0
            for j in stateValue:
                valueSum += int(j[0])

            randomValue = random.randrange(0,valueSum)

            valueSum = 0
            target = None
            for j in stateValue:
                valueSum += int(j[0])
                if randomValue < valueSum:
                    target = j
                    break

            if target[1][0] == 'move':
                moveValue = 0
                while moveValue == 0:
                    moveValue = random.randrange(-target[1][2],target[1][2])
                if target[1][1] == 'portal':
                    moveValue += i
                    if moveValue < 0:
                        moveValue = 0
                    elif moveValue > 100:
                        moveValue = 100
                tempTile.state = (target[1][0],target[1][1],moveValue)
            else:                 
                tempTile.state = target[1]

            mapData.append(tempTile)

        makingMap = gameMap.gameMap(mapData)

        return makingMap

a = mapMaker()
b = a.create()

from cs1graphics import *
from random import *

class Block(object):
    def __init__(self, value, text):
        self.value = value
        self.text = text # Canvas 상에 표시될 text

    def merge(self, block):
        if self.value == block.value: return Block(self.value + block.value)
        else: return None
        
class Board(object):
    def __init__(self, numberOfColumns, numberOfRows):
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.blocks = [[None] * numberOfRows for i in range(numberOfColumns)]
        
    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks
    
    def setBlock(self, coord, block):
        self.blocks[coord[0]][coord[1]] = block

    def getFree(self):
        pass # 모든 빈칸의 위치를 반환

    def addBlock(self, coord):
        pass # 빈칸 중 1개의 랜덤한 위치에 새 블록 하나 추가

    def move(self, direction):
        pass # 플레이어의 조작, 블록들이 움직이고 충돌하는 것 처리

class Game2048(object):
    def __init__(self, canvas, numberOfColumns,numberOfRows):
        self.__canvas = canvas
        self.__L2048 = Layer()
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows          
        self.__squareWidth=canvas.getWidth()//numberOfColumns
        self.__squareHeight=canvas.getHeight()//numberOfRows
        self.__L2048.setDepth(0)
        canvas.add(self.__L2048)

        self.__GridLayer= Layer()
        self.__displayGrid()
    
    def __displayGrid(self):
        for column in range(0,self.__numberOfColumns+1):
            p=Path(Point(self.__squareWidth*column,0),
                   Point(self.__squareWidth*column,self.__canvas.getHeight()))
            p.setBorderColor('black')
            p.setBorderWidth(1)
            self.__GridLayer.add(p)
        
        for row in range(0,self.__numberOfRows+1):
            p=Path(Point(0,self.__squareHeight*row),
                   Point(self.__canvas.getWidth(),self.__squareHeight*row))
            p.setBorderColor('black')
            p.setBorderWidth(1)
            self.__GridLayer.add(p)
        self.__canvas.add(self.__GridLayer) 

def runGame():
    NumberOfColumns = 6
    NumberOfRows = 6
    canvas = Canvas(100*NumberOfColumns , 100*NumberOfRows,'white','2048')
    
    G2048 = Game2048(canvas, NumberOfColumns, NumberOfRows)

runGame()

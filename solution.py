from cs1graphics import *
from random import *

class Block(object):
    def __init__(self, value, column, row):
        self.value = value
        self.column = column
        self.row = row
        self.__squareWidth= 100
        self.__squareHeight= 100
        self.blockSquare, self.blockText = self.setDisplay()

    def setDisplay(self):
        column = self.column; row = self.row
        x=(column*self.__squareWidth)+(self.__squareWidth//2)
        y=(row*self.__squareHeight)+(self.__squareHeight//2)        
        blockSquare= Square(min(self.__squareWidth*4//5,self.__squareHeight*4//5),Point(x,y))
        blockSquare.setFillColor("yellow")
        blockText = Text(str(self.value), 30, Point(x,y))
        return blockSquare, blockText

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
    
    def setBlock(self, block):
        if block.value != 0:
            self.blocks[block.column][block.row] = block
        else:
            self.blocks[block.column][block.row] = None

    def addBlock(self, coord):
        pass # 빈칸 중 1개의 랜덤한 위치에 새 블록 하나 추가

    def move(self, direction):
        pass # 플레이어의 조작, 블록들이 움직이고 충돌하는 것 처리

class Game2048(object):
    def __init__(self, canvas, numberOfColumns, numberOfRows):
        self.__canvas = canvas
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.gameBoard = Board(numberOfColumns, numberOfRows)
        self.__squareWidth=canvas.getWidth()//numberOfColumns
        self.__squareHeight=canvas.getHeight()//numberOfRows

        self.__blockLayer = Layer()
        self.__blockLayer.setDepth(0)
        canvas.add(self.__blockLayer)

        self.__GridLayer= Layer()
        self.__displayGrid()

    def getBoard(self):
        return self.gameBoard
    
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

    def displayBlocks(self):
        self.__blockLayer.clear()
        for column in range(0,self.__numberOfColumns):
            for row in range(0,self.__numberOfRows):
                blocks = self.getBoard().getBlocks()
                if blocks[column][row] != None:
                    self.__blockLayer.add(blocks[column][row].blockSquare)
                    self.__blockLayer.add(blocks[column][row].blockText)

        

def runGame():
    NumberOfColumns = 6
    NumberOfRows = 6
    canvas = Canvas(100*NumberOfColumns , 100*NumberOfRows,'white','2048')
    
    G2048 = Game2048(canvas, NumberOfColumns, NumberOfRows)
    G2048Board = G2048.getBoard()
    G2048Board.setBlock(Block(2, 1, 1))
    G2048.displayBlocks()
    while True:
        e = canvas.wait()
        key = e.getKey()
        print(key)
        if key == "w":
            G2048Board.move((-1, 0))
        G2048.displayBlocks()

runGame()

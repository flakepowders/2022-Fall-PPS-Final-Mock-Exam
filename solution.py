from cs1graphics import *
from random import *

squareWidth = 100
squareHeight = 100

class Block(object):
    def __init__(self, value, column, row):
        self.value = value
        self.column = column
        self.row = row
        self.blockSquare, self.blockText = self.setDisplay()

    def setDisplay(self):
        column = self.column; row = self.row
        x = (column * squareWidth) + (squareWidth // 2)
        y = (row * squareHeight) + (squareHeight // 2)        
        blockSquare = Square(min(squareWidth * 4 // 5, squareHeight * 4 // 5), Point(x, y))
        blockSquare.setFillColor("yellow")
        blockText = Text(str(self.value), 30, Point(x, y))
        return blockSquare, blockText
        
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

        self.__blockLayer = Layer()
        self.__blockLayer.setDepth(0)
        canvas.add(self.__blockLayer)

        self.__gridLayer = Layer()
        self.__displayGrid()

    def getBoard(self):
        return self.gameBoard
    
    def __displayGrid(self):
        for column in range(self.__numberOfColumns + 1):
            p = Path(Point(squareWidth * column, 0),
                   Point(squareWidth * column, self.__canvas.getHeight()))
            p.setBorderColor('black')
            p.setBorderWidth(1)
            self.__gridLayer.add(p)
        
        for row in range(self.__numberOfRows + 1):
            p = Path(Point(0, squareHeight * row),
                   Point(self.__canvas.getWidth(), squareHeight * row))
            p.setBorderColor('black')
            p.setBorderWidth(1)
            self.__gridLayer.add(p)
        self.__canvas.add(self.__gridLayer) 

    def displayBlocks(self):
        self.__blockLayer.clear()
        for column in range(self.__numberOfColumns):
            for row in range(self.__numberOfRows):
                blocks = self.getBoard().getBlocks()
                if blocks[column][row] != None:
                    self.__blockLayer.add(blocks[column][row].blockSquare)
                    self.__blockLayer.add(blocks[column][row].blockText)

def runGame():
    NumberOfColumns = 6
    NumberOfRows = 6
    canvas = Canvas(squareHeight * NumberOfColumns, squareWidth * NumberOfRows, 'white', '2048')
    
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

from cs1graphics import *
from random import *

squareWidth = 100
squareHeight = 100

class Board(object):
    def __init__(self, numberOfColumns, numberOfRows):
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.blocks = [[None] * numberOfRows for i in range(numberOfColumns)]
        
    def getBlocks(self, column, row):
        return self.blocks[column][row]
    
    def setBlock(self, block, column, row):
        self.blocks[column][row] = block

    def addBlock(self):
        # https://github.com/gabrielecirulli/2048/blob/master/js/game_manager.js
        # 확률은 여기서 가져옴
        empty = []
        for i in range(self.__numberOfColumns):
            for j in range(self.__numberOfRows):
                if self.blocks[i][j] is None:
                    empty.append((i, j))
        c = choice(empty)
        block = 2 if randrange(10)<9 else 4
        self.blocks[c[0]][c[1]] = block

    def move(self, direction):
        # 블록들을 합침
        def collapse(blocks):
            filtered = list(filter(lambda x:x is not None, blocks))
            # None을 뺀 숫자들을 합침
            def collapseNums(b):
                if len(b) < 2:
                    return b
                if b[0] == b[1]:
                    return [2*b[0]]+collapseNums(b[2:])
                else:
                    return [b[0]]+collapseNums(b[1:])
            collapsed = collapseNums(filtered)
            answer = collapsed+[None]*(len(blocks)-len(collapsed))
            return answer

        def collapseCoords(coords):
            blocks = [self.blocks[c[0]][c[1]] for c in coords]
            newBlocks = collapse(blocks)
            for i, c in enumerate(coords):
                self.blocks[c[0]][c[1]] = newBlocks[i]

        if direction == "s":
            for i in range(self.__numberOfColumns):
                collapseCoords([(i, j) for j in range(self.__numberOfRows)])
        elif direction == "w":
            for i in range(self.__numberOfColumns):
                collapseCoords([(i, j) for j in range(self.__numberOfRows-1, -1, -1)])
        elif direction == "a":
            for j in range(self.__numberOfRows):
                collapseCoords([(i, j) for i in range(self.__numberOfColumns)])
        elif direction == "d":
            for j in range(self.__numberOfRows):
                collapseCoords([(i, j) for i in range(self.__numberOfColumns-1, -1, -1)])

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

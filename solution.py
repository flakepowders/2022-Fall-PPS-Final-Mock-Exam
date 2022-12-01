import copy
from cs1graphics import *
from random import *

squareWidth = 100
squareHeight = 100

class Board(object):
    def __init__(self, numberOfColumns, numberOfRows):
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.__blocks = [[None] * numberOfRows for i in range(numberOfColumns)]
        self.__newBlockCoord = None

    def getBlocks(self):
        return self.__blocks    
    
    def getBlock(self, column, row):
        return self.__blocks[column][row]
    
    def setBlock(self, block, column, row):
        self.__blocks[column][row] = block

    def getNewBlockCoord(self):
        return self.__newBlockCoord

    def addBlock(self):
        # https://github.com/gabrielecirulli/2048/blob/master/js/game_manager.js
        # 확률은 여기서 가져옴
        empty = []
        for i in range(self.__numberOfColumns):
            for j in range(self.__numberOfRows):
                if self.__blocks[i][j] is None:
                    empty.append((i, j))

        assert len(empty) != 0

        c = choice(empty)
        block = 2 if randrange(10)<9 else 4
        self.__newBlockCoord = (c[0], c[1])
        self.setBlock(block, c[0], c[1])

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
            blocks = [self.__blocks[c[0]][c[1]] for c in coords]
            newBlocks = collapse(blocks)
            for i, c in enumerate(coords):
                self.__blocks[c[0]][c[1]] = newBlocks[i]

        if direction == "w":
            for i in range(self.__numberOfColumns):
                collapseCoords([(i, j) for j in range(self.__numberOfRows)])
        elif direction == "s":
            for i in range(self.__numberOfColumns):
                collapseCoords([(i, j) for j in range(self.__numberOfRows-1, -1, -1)])
        elif direction == "a":
            for j in range(self.__numberOfRows):
                collapseCoords([(i, j) for i in range(self.__numberOfColumns)])
        elif direction == "d":
            for j in range(self.__numberOfRows):
                collapseCoords([(i, j) for i in range(self.__numberOfColumns-1, -1, -1)])

    def canMove(self, direction):
        newBoard = copy.deepcopy(self)
        newBoard.move(direction)
        return self.getBlocks() != newBoard.getBlocks()

    def gameOver(self):
        return not any(map(self.canMove, ["w", "s", "a", "d"]))

class Game2048(object):
    def __init__(self, canvas, numberOfColumns, numberOfRows):
        self.__canvas = canvas
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.__gameBoard = Board(numberOfColumns, numberOfRows)

        self.__blockLayer = Layer()
        self.__blockLayer.setDepth(0)
        canvas.add(self.__blockLayer)

        self.__displayGrid()

    def getBoard(self):
        return self.__gameBoard

    def __displayGrid(self):
        self.__gridLayer = Layer()

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
                block = self.getBoard().getBlock(column, row)
                if block != None:
                    x = (column * squareWidth) + (squareWidth // 2)
                    y = (row * squareHeight) + (squareHeight // 2)
                    blockSquare = Square(min(squareWidth * 4 // 5, squareHeight * 4 // 5), Point(x,y))
                    if (column, row) != self.getBoard().getNewBlockCoord():
                        blockSquare.setFillColor("yellow")
                    else: blockSquare.setFillColor("orange")
                    blockText = Text(str(block), 30, Point(x,y))
                    self.__blockLayer.add(blockSquare)
                    self.__blockLayer.add(blockText)

    def showGameOverMessage(self):
        self.__messageLayer = Layer()
        self.__messageLayer.setDepth(-100)
        gameOverMessage = Text("Game Over!", 20, Point(self.__canvas.getWidth() // 2, self.__canvas.getHeight() // 2))
        self.__messageLayer.add(gameOverMessage)
        self.__canvas.add(self.__messageLayer) 

def runGame():
    NumberOfColumns = 3
    NumberOfRows = 3

    canvas = Canvas(squareHeight * NumberOfColumns, squareWidth * NumberOfRows, 'white', '2048')
    G2048 = Game2048(canvas, NumberOfColumns, NumberOfRows)
    G2048Board = G2048.getBoard()

    G2048Board.addBlock()
    G2048.displayBlocks()
    while True:
        e = canvas.wait()
        key = e.getKey()
        if key in ["w", "s", "a", "d"]:
            if G2048Board.canMove(key):
                G2048Board.move(key)
                G2048Board.addBlock()
                G2048.displayBlocks()
                if G2048Board.gameOver(): break
    G2048.showGameOverMessage()
runGame()

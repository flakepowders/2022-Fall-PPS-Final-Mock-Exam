from cs1graphics import *
from random import *

class Block(object):
    def __init__(self, value):
        self.value = value

    def merge(self, block):
        if self.value == block.value: return Block(self.value + block.value)
        else: return None
        
class Board(object):
    def __init__(self, N, M):
        self.blocks = [[None] * M for i in range(N)]
        
    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks
    
    def addBlock(self, coord, block):
        self.blocks[coord[0]][coord[1]] = block

    def getFree(self):
        pass

class Game2048(object):
    pass
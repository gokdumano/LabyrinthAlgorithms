from matplotlib import pyplot as plt
from random import choice
import numpy as np

class Cell:
    def __init__(self, CellRow=0, CellCol=0, GridRows=1000, GridCols=1000):
        self.CellRow    = CellRow
        self.CellCol    = CellCol
        self.GridRows   = GridRows
        self.GridCols   = GridCols
        self.Visited    = False
        self.links()
        
    def __repr__(self):        
        directions      = ["West", "North", "South", "East"]
            
        return "".join(["1" if self[direction]["Linked"] else "0" for direction in directions])

    def __str__(self):
        return self.__repr__()

    def __setitem__(self, direction, linked):
        if self.Links.__contains__(direction)   : self.Links[direction]["Linked"] = linked
        

    def __getitem__(self, direction):
        # default = {'Linked': False, 'Coord': None}
        # return self.Grid.get(key, None)
        if self.Links.__contains__(direction)   : return self.Links[direction]
        else                                    : return {'Linked': False, 'Coord': None}
        
    def withinBorder(self, dstRow, dstCol):
        return (-1 < dstRow < self.GridRows) and (-1 < dstCol < self.GridCols)
    
    def links(self):
        directions = {"West" : [self.CellRow+0, self.CellCol-1],
                      "North": [self.CellRow-1, self.CellCol+0],
                      "South": [self.CellRow+1, self.CellCol+0],
                      "East" : [self.CellRow+0, self.CellCol+1]}
        
        self.Links = {direction: {"Linked":False, "Coord":(dstRow, dstCol)}
                      for direction, (dstRow, dstCol) in directions.items()
                      if self.withinBorder(dstRow, dstCol)}

class Grid:
    def __init__(self, GridRows, GridCols):
        self.GridRows   = GridRows
        self.GridCols   = GridCols
        self.Grid       = {(CellRow, CellCol): Cell(CellRow, CellCol, self.GridRows, self.GridCols)
                           for CellCol in range(self.GridCols)
                           for CellRow in range(self.GridRows)}

    def __repr__(self):
       return "\n".join([" ".join([str(self.Grid[(CellRow, CellCol)])
                         for CellCol in range(self.GridCols)])
                         for CellRow in range(self.GridRows)]) 

    def __getitem__(self, key):
        return self.Grid.get(key, None)

class Maze(Grid):
    def __init__(self, GridRows, GridCols):
        super().__init__(GridRows, GridCols)

    def link(self, srcCell, direction):
        if   direction == "South":
            srcCell["South"]    = True
            dstCoord            = srcCell[direction]["Coord"]
            dstCell             = self[dstCoord]
            dstCell["North"]    = True
            
        elif direction == "East":
            srcCell["East"]     = True
            dstCoord            = srcCell[direction]["Coord"]
            dstCell             = self[dstCoord]
            dstCell["West"]     = True
        
    def gen(self):
        for CellRow in range(self.GridRows):
            for CellCol in range(self.GridCols):
                cell        = self[(CellRow,CellCol)]
                hasNorth    = cell.Links.__contains__("South")
                hasWest     = cell.Links.__contains__("East")

                if   hasNorth and hasWest   : direction = choice(["South", "East"])
                elif hasNorth               : direction = "South"
                elif hasWest                : direction = "East"
                else                        : direction = None

                if direction is not None:
                    self.link(cell, direction)
                    
    def vis(self):
        west    = np.array([[0,0,0], [1,0,0], [0,0,0]])
        north   = np.array([[0,1,0], [0,0,0], [0,0,0]])
        south   = np.array([[0,0,0], [0,0,0], [0,1,0]])
        east    = np.array([[0,0,0], [0,0,1], [0,0,0]])
        center  = np.array([[0,0,0], [0,1,0], [0,0,0]])
        blocks  = [west,north,south,east]
        col     = []
        
        for CellRow in range(self.GridRows):
            row = []
            for CellCol in range(self.GridCols):
                block = sum([arr for char, arr in zip(str(self[(CellRow,CellCol)]), blocks) if char == "1"]) + center
                row.append(block)
            row = np.hstack(row)
            col.append(row)
        col = np.vstack(col)
        return col

maze = Maze(100,100)
maze.gen()
plt.imshow(maze.vis(), cmap="bone"); plt.show();

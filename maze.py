from random import choice

class Cell:
    def __init__(self, Col, Row):
        self.Col, self.Row = Col, Row
        self.numVisited    = 0
        
        self.DirPairs = {
            'East' :'West' ,
            'North':'South',
            'West' :'East' ,
            'South':'North'
            }
        
        self.Walls    = {Dir: True for Dir in self.DirPairs.keys()}
        
    def __repr__(self):
        return f'<Cell({self.Col},{self.Row})>'
        
    def __str__(self):
        # Is there a Wall at '{East}{North}{West}{South}' ?
        return ''.join(['1' if Wall else '0' for Wall in self.Walls.values()])
    
    def __format__(self, formatspec='s'):
        return self.__str__()
    
    def __getitem__(self, key):
        return self.Walls.get(key)

    def __setitem__(self, key, value):
        self.Walls[key] = value
        
    def relDir(self, other):
        delta = (other.Col - self.Col, other.Row - self.Row)
        
        return {( 1, 0): 'East' ,
                ( 0,-1): 'North',
                (-1, 0): 'West' ,
                ( 0, 1): 'South'}.get(delta)
    
    def linkCell(self, other):
        Dir = self.relDir(other)
        if Dir is not None:
            self[Dir]      = False
            DirPair        = self.DirPairs[Dir]
            other[DirPair] = False
            
class Maze:
    def __init__(self, maze_size, maze_start=(0,0)):
        self.nCol, self.nRow = maze_size
        self.iCol, self.iRow = maze_start
        self.Board           = {(Col,Row): Cell(Col,Row) for Col in range(self.nCol) for Row in range(self.nRow)}
    
    def __repr__(self):
        return f'<Maze({self.nCol},{self.nRow})>'
    
    def __str__(self):
        text = ''
        for num, cell in enumerate(self.Board.values(), start = 1):
            text += str(cell) + ' '
            if num % self.nCol == 0: text += '\n'
        return text
            
    def __getitem__(self, index):
        return self.Board.get(index)
    
    def find_neighboors(self, iCell, include_visited=True):
        iCol, iRow = iCell.Col, iCell.Row
        nCells     = {}
        
        for dCol, dRow in ((1,0), (-1,0), (0,1), (0,-1)):
            jCol, jRow = iCol + dCol, iRow + dRow
            jCell      = self[jCol, jRow]
            if jCell is not None and (jCell.numVisited == 0 or include_visited and jCell.numVisited != 0):
                Dir    = iCell.relDir(jCell)
                nCells[Dir] = jCell
        return nCells
        
    def BinaryTree(self):
        for Row in range(self.nRow):
            for Col in range(self.nCol):
                iCell = self[Col, Row]
                iCell.numVisited += 1
                nCells = self.find_neighboors(iCell, False)
                if   "South" in nCells and "East" in nCells: jCell = nCells[choice(['South', 'East'])];
                elif "South" in nCells                     : jCell = nCells['South'];
                elif "East"  in nCells                     : jCell = nCells['East' ];
                iCell.linkCell(jCell)
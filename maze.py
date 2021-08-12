from random import choice
class Cell:
    def __init__(self, Row, Col):
        self.Row, self.Col = Row, Col
        self.numVisited    = 0
        
        self.DirPairs = {
            'East' :'West' ,
            'North':'South',
            'West' :'East' ,
            'South':'North'
            }
        
        self.Walls    = {Dir: True for Dir in self.DirPairs.keys()}
        
    def __repr__(self):
        return f'<Cell({self.Row},{self.Col})>'
        
    def __str__(self):
        # Is there a Wall at '{East}{North}{West}{South}' ?
        return ''.join(['1' if Wall else '0' for Wall in self.Walls.values()]) + ' '
    
    def __getitem__(self, key):
        return self.Walls.get(key)

    def __setitem__(self, key, value):
        self.Walls[key] = value
        
    def relDir(self, other):
        delta = (other.Row - self.Row, other.Col - self.Col)
        
        return {( 0, 1): 'East' ,
                (-1, 0): 'North',
                ( 0,-1): 'West' ,
                ( 1, 0): 'South'}.get(delta)
    
    def linkCell(self, other):
        Dir = self.relDir(other)
        if Dir is not None:
            self[Dir]      = False
            DirPair        = self.DirPairs[Dir]
            other[DirPair] = False
        
class Maze:
    def __init__(self, maze_size, maze_start=(0,0)):
        self.nRow, self.nCol = maze_size
        self.iRow, self.iCol = maze_start
        self.Board           = {(Col,Row): Cell(Col,Row) for Col in range(self.nCol) for Row in range(self.nRow)}
    
    def __repr__(self):
        return f'<Maze({self.nRow},{self.nCol})>'
    
    def __str__(self):
        text = ""
        for num, cell in enumerate(self.Board.values(), start = 1):
            text += str(cell)
            if num % self.nCol == 0: text += '\n'
        return text
            
    def __getitem__(self, index):
        return self.Board.get(index)
    
    def find_neighboors(self, iCell, include_visited=True):
        iRow, iCol = iCell.Row, iCell.Col
        nCells     = {}
        
        for dRow, dCol in ((1,0), (-1,0), (0,1), (0,-1)):
            jRow, jCol = iRow + dRow, iCol + dCol
            jCell      = self[jRow, jCol]
            if jCell is not None and (jCell.numVisited == 0 or include_visited and jCell.numVisited != 0):
                Dir    = iCell.relDir(jCell)
                nCells[Dir] = jCell
        return nCells
        
    def gen(self):
        for Row in range(self.nRow):
            for Col in range(self.nCol):
                iCell = self[Col, Row]
                if  iCell.numVisited == 0:
                    iCell.numVisited += 1
                    nCells = self.find_neighboors(iCell)
                    if   "South" in nCells and "East" in nCells: jCell = nCells[choice(['South', 'East'])];
                    elif "South" in nCells                     : jCell = nCells['South'];
                    elif "East"  in nCells                     : jCell = nCells['East' ];
                    iCell.linkCell(jCell)
                    
size   = (10, 10)
maze   = Maze(size)
nCells = maze.find_neighboors(maze[1,2])
print(maze)
maze.gen()
print(maze)

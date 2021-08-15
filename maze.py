class Cell:
    def __init__(self, Col, Row):
        self.Col, self.Row = Col, Row
        self.numVisited    = 0
        
        self.DirPairs = {'East':'West', 'North':'South', 'West':'East', 'South':'North'}        
        self.Walls    = {Dir: True for Dir in self.DirPairs.keys()}
        
    def __repr__(self):
        return f'<Cell(Col:{self.Col},Row:{self.Row})>'
    
    def __format__(self, formatspec='s'):
        # Is there a Wall at '{East}{North}{West}{South}' ?
        return ''.join(['1' if Wall else '0' for Wall in self.Walls.values()])
    
    def __getitem__(self, key):
        return self.Walls.get(key)

    def __setitem__(self, key, value):
        self.Walls[key] = value
        
    def relDir(self, other):
        if other is not None:
            delta = (other.Col - self.Col, other.Row - self.Row)        
            return {( 1, 0): 'East' , ( 0,-1): 'North', (-1, 0): 'West' , ( 0, 1): 'South'}.get(delta)
        return None
    
    def link_cells(self, other):
        Dir     = self.relDir(other)
        if Dir is not None:
            DirPair        = self.DirPairs[Dir]
            self[Dir]      = False
            other[DirPair] = False
        
    def find_neighboor(self, Dir:str, maze=None):
        delta = {'East':(1,0), 'North':(0,-1), 'West':(-1,0), 'South':(0,1)}.get(Dir)
        if   delta is None: return None
        elif maze  is None: dCol, dRow = delta; return (self.Col + dCol, self.Row + dRow)
        else              : dCol, dRow = delta; return maze[(self.Col + dCol, self.Row + dRow)]
            
class Maze:
    def __init__(self, maze_size:tuple):
        self.nCol, self.nRow = maze_size
        self.Status          = '#Blank'
        self.Board           = {(Col,Row): Cell(Col,Row) for Col in range(self.nCol) for Row in range(self.nRow)}
        
    def __repr__(self):
        return f'<Maze(nCol:{self.nCol},nRow:{self.nRow})>{self.Status}'
    
    def __str__(self):
        text = ''
        for num, cell in enumerate(self.Board.values(), start = 1):
            text += f'{cell:s} '
            if num % self.nCol == 0: text += '\n'
        return text
            
    def __getitem__(self, index:tuple):
        return self.Board.get(index)
    
    def _reset(self):
        for key in self.Board.keys():
            self.Board[key].Walls = {'East':True,'North':True,'West':True,'South':True}
        
    def find_neighboors(self, iCell:Cell, include_visited:bool=True):
        nCells = {}
        for Dir in ('East','North','West','South'):
            jCell = iCell.find_neighboor(Dir, self)
            if jCell is not None and (jCell.numVisited == 0 or include_visited and jCell.numVisited != 0):
                nCells[Dir] = jCell
                
        return nCells
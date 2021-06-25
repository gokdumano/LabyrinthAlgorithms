class Cell:
    def __init__(self, CellRow, CellCol, GridRows=999, GridCols=999):
        self.CellRow    = CellRow
        self.CellCol    = CellCol
        self.GridRows   = GridRows
        self.GridCols   = GridCols
        self.Visited    = False
        self.Neighbors  = self.neighbors()

    def __repr__(self):
        directions      = ["West", "North", "East", "South"]
        return "".join(["0" if self.Neighbors.get(direction, None) is None
                        else "1"
                        for direction in directions])

    def __str__(self):
        return self.__repr__()
            
    def withinBorder(self, dstRow, dstCol, GridRows, GridCols):
        return (-1 < dstRow < self.GridRows) and (-1 < dstCol < self.GridCols)
    
    def neighbors(self):
        directions      = ["North", "South", "West", "East"]
        destinations    = [[self.CellRow-1, self.CellCol+0],
                           [self.CellRow+1, self.CellCol+0],
                           [self.CellRow+0, self.CellCol-1],
                           [self.CellRow+0, self.CellCol+1]]
        
        return {direction:(dstRow, dstCol)
                for direction, (dstRow, dstCol) in zip(directions, destinations)
                if self.withinBorder(dstRow, dstCol, self.GridRows, self.GridCols)}

class Grid:
    def __init__(self, GridRows, GridCols):
        self.GridRows   = GridRows
        self.GridCols   = GridCols
        self.Grid       = {(CellRow,CellCol): Cell(CellRow, CellCol, GridRows, GridCols)
                           for CellRow in range(GridRows)
                           for CellCol in range(GridCols)}

    def __repr__(self):
       return "\n".join([" ".join([str(self.Grid[(Row, Col)]) for Row in range(self.GridRows)]) for Col in range(self.GridCols)]) 
    


    def __getitem__(self, key):
        return self.Grid.get(key, None)

GridRows, GridCols  = 15, 10
temp = Grid(GridRows, GridCols)

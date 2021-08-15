from random import randint, choice
from time import perf_counter
from collections import deque
import pygame

def SurfRect(path, nWidth=None, nHeight=None, HasAlphaChannel=True, **pos):
    if   HasAlphaChannel: imSurf = pygame.image.load(path).convert_alpha()
    else                : imSurf = pygame.image.load(path).convert()
    
    Width, Height = imSurf.get_size()
    if   nWidth  == nHeight == None: nWidth, nHeight = Width, Height;
    elif nWidth  == None           : scale = nHeight / Height; nWidth  = int(Width  * scale)
    elif nHeight == None           : scale = nWidth  / Width ; nHeight = int(Height * scale)
    
    imSurf = pygame.transform.scale(imSurf, (nWidth, nHeight))
    imRect = imSurf.get_rect(**pos)
    return imSurf, imRect

def RecursiveBacktrackerAlgorithm(maze):
    ...
    
def EllersAlgorithm():
    ...
    
def KruskalsAlgorithm(maze):
    ...
    
def PrimsAlgorithm(maze):
    ...
    
def RecursiveDivisionAlgorithm(maze):
    ...
    
def AldousBroderAlgorithm(maze):
    Start        = perf_counter()
    NumUnvisited = maze.nCol * maze.nRow
    
    iCol   = randint(0, maze.nCol - 1)
    iRow   = randint(0, maze.nRow - 1)
    iCell  = maze[iCol, iRow]; iCell.numVisited += 1; NumUnvisited -= 1
    
    while NumUnvisited > 0:
        nCells = maze.find_neighboors(iCell)
        jCell  = choice(list(nCells.values()))
        
        if jCell.numVisited == 0:
            iCell.link_cells(jCell); jCell.numVisited += 1; NumUnvisited -= 1
            
        iCell  = jCell
    Stop  = perf_counter()
    Delta = Stop - Start
    maze.Status = f'#CreatedByAldousBroder({Delta:.5f})'
    return Delta
    
def WilsonsAlgorithm(maze):
    ...
    
def HuntAndKillAlgorithm(maze):
    ...
    
def GrowingTreeAlgorithm(maze):
    Start  = perf_counter()
    
    iCol   = randint(0, maze.nCol - 1)
    iRow   = randint(0, maze.nRow - 1)
    Cells  = deque([maze[iCol, iRow]])
    iCell  = choice(Cells)
    iCell.numVisited += 1
    
    while len(Cells) > 0:
        nCells = maze.find_neighboors(iCell, False)
        if nCells:
            jCell = choice(list(nCells.values()))
            jCell.numVisited += 1
            iCell.link_cells(jCell)
            Cells.append(jCell)
            iCell = jCell
        else:
            iCell = Cells.pop()
    
    Stop = perf_counter() 
    Delta = Stop - Start   
    maze.Status = f'#CreatedByGrowingTree({Delta:.5f})'
    return Delta

def BinaryTreeAlgorithm(maze):
    Start = perf_counter()
    
    for Row in reversed(range(maze.nRow)):
        for Col in range(maze.nCol):
            iCell  = maze[Col, Row]
            nCells = maze.find_neighboors(iCell, False)
            if "North" in nCells or "East" in nCells:
                if   "North" in nCells and "East" in nCells: jCell = nCells[choice(['North', 'East'])];
                elif "North" in nCells                     : jCell = nCells['North'];
                elif "East"  in nCells                     : jCell = nCells['East' ];
                iCell.numVisited += 1            
                iCell.link_cells(jCell)
                
    Stop = perf_counter()
    Delta = Stop - Start
    maze.Status = f'#CreatedByBinaryTree({Delta:.5f})'
    return Delta

def SidewinderAlgorithm(maze):
    Start = perf_counter()
    
    for Row in range(maze.nRow):
        RunSet = deque()
        for Col in range(maze.nCol):
            iCell  = maze[Col,Row]
            nCells = maze.find_neighboors(iCell)
            RunSet.append(iCell)
            
            if   'East'  in nCells and 'North' in nCells: Dir = choice(['East', 'North'])
            elif 'East'  in nCells                      : Dir = 'East'
            elif 'North' in nCells                      : Dir = 'North'
            
            if Dir == 'East':
                jCell  = iCell.find_neighboor('East', maze)
                iCell.link_cells(jCell)
                RunSet.append(jCell)
                iCell  = jCell
            
            elif Dir == 'North':
                iCell  = choice(RunSet)
                jCell  = iCell.find_neighboor('North', maze)
                iCell.link_cells(jCell)
                RunSet = deque()
                
    Stop  = perf_counter()
    Delta = Stop - Start  
    maze.Status = f'#CreatedBySidewinder({Delta:.5f})'
    return Delta
    

    

            
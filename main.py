from utils import SurfRect
from maze import Maze
import pygame, sys
pygame.init()

MAZECOL        = 25
MAZEROW        = 25
MAZESIZE       = (MAZECOL, MAZEROW)

TILEWIDTH      = 10
TILEHEIGHT     = 10

DISPLAYWIDTH   = MAZECOL * TILEWIDTH
DISPLAYHEIGHT  = MAZEROW * TILEHEIGHT

DISPLAYSURF    = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
DISPLAYRECT    = DISPLAYSURF.get_rect()

CLOCK          = pygame.time.Clock()
FRAMERATE      = 60
PLAY           = True

Path           = 'C:/Users/Punisher_12/Documents/GitHub/LabyrinthAlgorithms/Tiles/{:s}.png'.format
maze           = Maze(MAZESIZE)
maze.BinaryTree()

DISPLAYSURF.fill('#ffffff')

for NumRow in range(maze.nRow):
    for NumCol in range(maze.nCol):
        TilePath    = Path(maze[NumCol, NumRow])
        TileTopleft = (NumCol * TILEWIDTH, NumRow * TILEHEIGHT)
        TileSurf, TileRect = SurfRect(TilePath, TILEWIDTH, TILEHEIGHT, topleft=TileTopleft)
        DISPLAYSURF.blit(TileSurf, TileRect)
        
while PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            PLAY = False
            
    if PLAY:
        pygame.display.update()
        CLOCK.tick(FRAMERATE)
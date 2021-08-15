from maze import Maze
import pygame, sys, utils
pygame.init()

MAZECOL        = 20
MAZEROW        = 20
MAZESIZE       = (MAZECOL, MAZEROW)

Path           = 'C:/Users/Punisher_12/Documents/GitHub/LabyrinthAlgorithms/Tiles/{:s}.png'.format
maze           = Maze(MAZESIZE)
#utils.BinaryTree(maze)
#utils.Sidewinder(maze)
#utils.GrowingTree(maze)
utils.AldousBroder(maze)

#maze._reset()

TILEWIDTH      = 20
TILEHEIGHT     = 20
DISPLAYWIDTH   = MAZECOL * TILEWIDTH
DISPLAYHEIGHT  = MAZEROW * TILEHEIGHT
DISPLAYSURF    = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
pygame.display.set_caption(repr(maze))
DISPLAYRECT    = DISPLAYSURF.get_rect()
CLOCK          = pygame.time.Clock()
FRAMERATE      = 60
PLAY           = True

DISPLAYSURF.fill('#ffffff')
for NumRow in range(maze.nRow):
    for NumCol in range(maze.nCol):
        TilePath    = Path(maze[NumCol, NumRow])
        TileTopleft = (NumCol * TILEWIDTH, NumRow * TILEHEIGHT)
        TileSurf, TileRect = utils.SurfRect(TilePath, TILEWIDTH, TILEHEIGHT, topleft=TileTopleft)
        DISPLAYSURF.blit(TileSurf, TileRect)   

while PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            PLAY = False
            
    if PLAY:
        pygame.display.update()
        CLOCK.tick(FRAMERATE)
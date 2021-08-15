from maze import Maze
import pygame, sys, utils
pygame.init()

MAZECOL        = 20
MAZEROW        = 20
MAZESIZE       = (MAZECOL, MAZEROW)

#Path           = '../images/tiles/{:s}.png'.format
#maze          = Maze(MAZESIZE)
#utils.BinaryTreeAlgorithm(maze)
#utils.SidewinderAlgorithm(maze)
#utils.GrowingTreeAlgorithm(maze)

size1 = (  50,  50); maze1 = Maze(size1); time1 = utils.SidewinderAlgorithm(maze1); print(time1)
size2 = ( 250, 250); maze2 = Maze(size2); time2 = utils.SidewinderAlgorithm(maze2); print(time2)
size3 = (1000,1000); maze3 = Maze(size3); time3 = utils.SidewinderAlgorithm(maze3); print(time3)
size4 = (5000,5000); maze4 = Maze(size4); time4 = utils.SidewinderAlgorithm(maze4); print(time4)

#maze._reset()
"""
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
"""
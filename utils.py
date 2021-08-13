import pygame

def SurfRect(path, nWidth=None, nHeight=None, HasAlphaChannel=True, **pos):
    if   HasAlphaChannel: imSurf = pygame.image.load(path).convert_alpha()
    else                : imSurf = pygame.image.load(path).convert()
    
    Width, Height = imSurf.get_size()
    if   nWidth  == nHeight == None: nWidth, nHeight = Width, Height;
    elif nWidth  == None           : scale = nHeight / Height; nWidth  = Width  * scale
    elif nHeight == None           : scale = nWidth  / Width ; nHeight = Height * scale
    
    imSurf = pygame.transform.scale(imSurf, (nWidth, nHeight))
    imRect = imSurf.get_rect(**pos)
    return imSurf, imRect
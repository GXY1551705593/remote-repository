import pygame
pygame.init()
window=pygame.display.set_mode((640,600))
window.fill([255,255,255])#rgb值
skierman=pygame.image.load('./skier_down.png')
x=20
y=20
window.blit(skierman,[x,y])
pygame.display.flip()







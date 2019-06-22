import pygame#导入pagame
import random
pygame.init()

window=pygame.display.set_mode((640,600))
window.fill([255,255,255])

class SkierClass(pygame.sprite.Sprite):
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left=location[0]
        self.rect.top=location[1]
        #self.speed=speed
#创建多个小人实例
ski_list=[]
for i in range(0,1):
    x=random.randint(0,200)
    y=random.randint(0,200)
    ski=SkierClass('./skier_down.png', [x,y])
    ski_list.append(ski)

for obj in ski_list:
    x=random.randint(100,200)
    y=random.randint(100,200)
    window.blit(obj.image,obj.rect)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('关闭窗口')
            exit()

    pygame.display.update()






import pygame
pygame.init()
window = pygame.display.set_mode((640,600))
window.fill([255, 255, 255]) # rgb 值
# 加载图像并且与窗口融合
skierman = pygame.image.load('./skier_down.png')
# 让小人动起来
# pygame.time.delay(20000)
x = 20
y = 20
window.blit(skierman,[x,y])
pygame.display.flip()
for i in range(1,100):
    pygame.time.delay(20)
    pygame.draw.rect(window,[255,255,255],[x,y,30,64])
    x += 1
    y += 5
    window.blit(skierman,[x,y])
    pygame.display.flip()

# pygame.draw.rect(window,[255,255,255],[20,20,30,64])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('关闭窗口')
            exit()

    pygame.display.update()
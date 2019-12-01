
import pygame, sys
successes, failures = pygame.init()

screen = pygame.display.set_mode((700, 426))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

rect = pygame.Rect((0, 0), (32, 32))

main_image = pygame.image.load("background.jpg")
screen.blit(pygame.transform.scale(main_image, (700, 426)), (0, 0))
pygame.display.update()

fontObj = pygame.font.Font('Daum_Regular.ttf', 32)
TitleSurfObj = fontObj.render('따방 잡기', True, WHITE)
TitleRectObj = TitleSurfObj.get_rect()
TitleRectObj.center = (350, 125)

MesSurfObj = fontObj.render('Press Start or Quit', True, WHITE)
MesRectObj = MesSurfObj.get_rect()
MesRectObj.center = (350, 200)


StSurfObj = fontObj.render('Start', True, WHITE)
StRectObj = StSurfObj.get_rect()
StRectObj.center = (400, 295)

EdSurfObj = fontObj.render('Quit', True, WHITE)
EdRectObj = EdSurfObj.get_rect()
EdRectObj.center = (350, 375)

Startbutton = pygame.Rect(300, 270, 100, 50)
Quitbutton = pygame.Rect(300, 350, 100, 50)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Startbutton.collidepoint(event.pos):
                    print("게임 시작")
                if Quitbutton.collidepoint(event.pos):
                    print("게임 종료")
                    quit()

    pygame.draw.rect(screen, BLACK, Startbutton)
    screen.blit(StSurfObj, StRectObj)
    pygame.display.update()















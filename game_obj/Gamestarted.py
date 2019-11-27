
import pygame, sys
successes, failures = pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image .fill(WHITE)

main_image = pygame.image.load("gisuksar.jpg")
screen.blit(pygame.transform.scale(main_image, (500, 500)), (0, 0))
pygame.display.update()

fontObj = pygame.font.Font('Daum_Regular.ttf', 32)
TitleSurfObj = fontObj.render('따 방 잡 기 !', True, BLACK, WHITE)
TitleRectObj = TitleSurfObj.get_rect()
TitleRectObj.center = (250, 125)

MesSurfObj = fontObj.render('Press Start or Quit', True, BLACK, WHITE)
MesRectObj = MesSurfObj.get_rect()
MesRectObj.center = (250, 200)

StSurfObj = fontObj.render('Start', True, BLACK, GREEN)
StRectObj = StSurfObj.get_rect()
StRectObj.center = (250, 295)

EdSurfObj = fontObj.render('Quit', True, BLACK, RED)
EdRectObj = EdSurfObj.get_rect()
EdRectObj.center = (250, 375)

Startbutton = pygame.Rect(200, 270, 100, 50)
Quitbutton = pygame.Rect(200, 350, 100, 50)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # `event.pos` is the mouse position.
                if Startbutton.collidepoint(event.pos):
                    print("게임 시작")
                if Quitbutton.collidepoint(event.pos):
                    print("게임 종료")
                    quit()

    pygame.draw.rect(screen, GREEN, Startbutton)
    pygame.draw.rect(screen, RED, Quitbutton)
    screen.blit(TitleSurfObj, TitleRectObj)
    screen.blit(MesSurfObj, MesRectObj)
    screen.blit(StSurfObj, StRectObj)
    screen.blit(EdSurfObj, EdRectObj)
    pygame.display.update()  # Or pygame.display.flip()















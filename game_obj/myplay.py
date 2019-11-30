# Import a library of functions called 'pygame'
import pygame
import dynamic
import static_obj
import gameplay


# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [1200, 675]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("따방 잡아버리기")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
img_li = []

four = 0
five = 0
cupbaps = 0
pit = 0

four_student = []
five_student = []
cupbabs = []
pits = []

world = []


def write(text, x, y, size):
    font = pygame.font.Font('NanumSquare_acL.ttf', size)  # 폰트 설정
    text = font.render(text, True, (28, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
    screen.blit(text, (x, y))  # 화면에 표시


def mk_img_li():
    img = pygame.image.load('cupbap.jpg')
    img_li.append(img)
    img = pygame.image.load('hamjung.jpg')
    img_li.append(img)
    img = pygame.image.load('4gi.jpg')
    img_li.append(img)
    img = pygame.image.load('5gi.jpg')
    img_li.append(img)
    img = pygame.image.load('pig.jpg')
    img_li.append(img)


def draw_map():
    pygame.draw.lines(screen, BLACK, True, [[265, 10], [265, 665], [920, 665], [920, 10]], 5)
    for i in range(1, 10):
        pygame.draw.line(screen, BLACK, [265 + 65.5 * i, 10], [265 + 65.5 * i, 665], 5)
        pygame.draw.line(screen, BLACK, [265, 10 + 65.5 * i], [920, 10 + 65.5 * i], 5)

    for i in range(11):
        for j in range(11):
            if world[i][j] == '4':
                draw_img('4gi.jpg',i,j)
            if world[i][j] == '5':
                draw_img('5gi.jpg',i,j)
            if world[i][j] == 's':
                draw_img('pig.jpg',i,j)
            if world[i][j] == 'c':
                draw_img('cupbap.jpg',i,j)
            if world[i][j] == 'o':
                draw_img('hamjung.jpg',i,j)

def draw_img(img, x, y):
    nx = 265+16.375*(2*2*(y-1)+1)
    ny = 10+16.375*(2*2*(x-1)+1)
    screen.blit(img, (nx, ny))


def func_dis2():
    global four, five, cupbaps, pit
    is_fourgi = False
    is_fivegi = False
    is_cupbap = False
    is_hamjung = False
    num = 0
    write("이 게임은 당신이 사감선생님이 되어 4기와 5기를 잡는 게임입니다! 원하는 4기와 5기, 컵밥과 함정의 수를 순서대로 입력 해 주세요 모두 15를 넘어선 안됩니다!", 10, 10, 35)
    pygame.display.flip()
    write("4기 수", 90, 10, 30)
    write("5기 수", 90, 50, 30)
    write("컵밥 수", 90, 90, 30)
    write("함정 수", 90, 130, 30)
    while not is_fourgi:
        write("4기를 몇 명으로 할지 입력해주세요", 50, 10, 30)
        pygame.display.flip()
        pygame.event.get()
        if event.type() == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
            if buttons[0] != "return" and buttons[0].isdigit() is False:
                write("숫자를 입력해주세요", 500, 300, 30)
            elif buttons[0].isdigit() is True:
                num *= 10
                num += int(buttons[0])
            else:
                if num == 0:
                    write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                if num > 15:
                    write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 500, 300, 30)
                    num = 0
                else:
                    four = num
                    num = 0
                    is_fourgi = True
        pygame.display.flip()

    while not is_fivegi:
        write("5기를 몇 명으로 할지 입력해주세요", 50, 10, 30)
        pygame.display.flip()
        write("5기를 몇 명으로 할지 입력해주세요", 50, 10, 30)
        pygame.event.get()
        if event.type() == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
            if buttons[0] != "return" and buttons[0].isdigit() is False:
                write("숫자를 입력해주세요", 500, 300, 30)
            elif buttons[0].isdigit() is True:
                num *= 10
                num += int(buttons[0])
            else:
                if num == 0:
                    write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                if num > 15:
                    write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 500, 300, 30)
                    num = 0
                else:
                    write("좋아요, 5기는 {}명입니다".format(num), 500, 300, 30)
                    five = num
                    num = 0
                    is_fivegi = True
        pygame.display.flip()

    while not is_cupbap:
        write("컵밥을 몇 개로 할지 입력해주세요", 50, 10, 30)
        pygame.display.flip()
        write("컵밥을 몇 개로 할지 입력해주세요", 50, 10, 30)
        pygame.event.get()
        if event.type() == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
            if buttons[0] != "return" and buttons[0].isdigit() is False:
                write("숫자를 입력해주세요", 500, 300, 30)
            elif buttons[0].isdigit() is True:
                num *= 10
                num += int(buttons[0])
            else:
                if num == 0:
                    write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                if num > 15:
                    write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 500, 300, 30)
                    num = 0
                else:
                    write("좋아요, 컵밥은 {}개입니다".format(num), 500, 300, 30)
                    cupbaps = num
                    num = 0
                    is_cupbap = True
        pygame.display.flip()

    while not is_hamjung:
        write("함정을 몇 개로 할지 입력해주세요", 50, 10, 30)
        pygame.display.flip()
        write("함정을 몇 개로 할지 입력해주세요", 50, 10, 30)
        pygame.event.get()
        if event.type() == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
            if buttons[0] != "return" and buttons[0].isdigit() is False:
                write("숫자를 입력해주세요", 500, 300, 30)
            elif buttons[0].isdigit() is True:
                num *= 10
                num += int(buttons[0])
            else:
                if num == 0:
                    write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                if num > 15:
                    write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 500, 300, 30)
                    num = 0
                else:
                    write("좋아요, 함정은 {}개입니다".format(num), 500, 300, 30)
                    pit = num
                    num = 0
                    is_hamjung = True
        pygame.display.flip()

mk_img_li()

dis1 = True
dis2 = False
dis3 = False

while not done:

    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    if dis1:
        pass

    if dis2:
        draw_map()

        draw_img(img_li[0], 1, 1)
        draw_img(img_li[0], 2, 1)
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    if dis3:
        draw_map()

        draw_img(img_li[0], 1, 1)
        draw_img(img_li[0], 2, 1)


        for i in range(0, 15):
            a = []
            for j in range(0, 15):
                a.append(0)
            world.append(a)

        player = dynamic.sagam()
        player.generate(world, 's')

        for i in range(int(four)):
            x = dynamic.FourGi()
            x.generate(world, '4')
            four_student.append(x)

        for i in range(int(five)):
            x = dynamic.FiveGi()
            x.generate(world, '5')
            five_student.append(x)

        for i in range(int(cupbaps)):
            x = static_obj.cupbab(world)
            cupbabs.append(x)

        for i in range(int(pit)):
            x = static_obj.trap(world)
            pits.append(x)
        while True:
            if player.dead_or_alive() == 'dead':

                fontObj = pygame.font.Font('Daum_Regular.ttf', 32)
                TitleSurfObj = fontObj.render('"사감선생님의 손전등 배터리가 끝났습니다 - GAME OVER"', True, RED)
                TitleRectObj = TitleSurfObj.get_rect()
                TitleRectObj.center = (350, 125)
                quit()

            else:
                gameplay.update_map()
                draw_map()
                write("손전등 배터 : "+str(player.health),10,10,30)
                write("점수 : "+str(player.point), 10, 50, 30)
                write("4기 수 : "+str(len(four_student)), 10, 90, 30)
                write("5기 수 : "+str(len(five_student)), 10, 130, 30)

                events = pygame.event.get()
                x = 'p'
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            x = 'w'
                        elif event.key == pygame.K_a:
                            x = 'a'
                        elif event.key == pygame.K_s:
                            x = 's'
                        elif event.key == pygame.K_d:
                            x = 'd'
                        elif event.key == pygame.K_q:
                            x = 'q'
                        elif event.key == pygame.K_e:
                            x = 'e'
                        elif event.key == pygame.K_z:
                            x = 'z'
                        elif event.key == pygame.K_c:
                            x = 'c'

                player.move(x)
                player.catch_student(four_student, five_student)
                player.minus_health()

                for i in four_student:
                    i.move4(world, four_student, five_student, pits)
                    i.minus_health()
                    if i.dead_or_alive() == 'dead':
                        four_student.remove(i)
                for i in five_student:
                    i.move5(world, cupbabs, five_student, pits)
                    i.minus_health()
                if i.dead_or_alive() == 'dead':
                    five_student.remove(i)

    pygame.display.flip()



# Be IDLE friendly
pygame.quit()

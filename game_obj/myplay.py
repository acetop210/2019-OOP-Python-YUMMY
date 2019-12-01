# Import a library of functions called 'pygame'
import pygame
import dynamic
import static_obj


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

rect = pygame.Rect((0, 0), (32, 32))

main_image = pygame.image.load("background.jpg")
screen.blit(pygame.transform.scale(main_image, (1200, 675)), (0, 0))
pygame.display.update()

fontObj = pygame.font.Font('Daum_Regular.ttf', 32)
TitleSurfObj = fontObj.render('따방 잡기', True, WHITE)
TitleRectObj = TitleSurfObj.get_rect()
TitleRectObj.center = (600, 125)

MesSurfObj = fontObj.render('Press Start or Quit', True, WHITE)
MesRectObj = MesSurfObj.get_rect()
MesRectObj.center = (600, 200)


StSurfObj = fontObj.render('Start', True, WHITE)
StRectObj = StSurfObj.get_rect()
StRectObj.center = (600, 295)
StRectObj2 = StSurfObj.get_rect()
StRectObj2.center = (870, 322)

EdSurfObj = fontObj.render('Quit', True, WHITE)
EdRectObj = EdSurfObj.get_rect()
EdRectObj.center = (600, 375)

Startbutton = pygame.Rect(550, 270, 100, 50)
Startbutton2 = pygame.Rect(823, 296, 100, 50)
Quitbutton = pygame.Rect(550, 350, 100, 50)
four_student = []
five_student = []
cupbap = []
pits = []

world = []


def make_map():
    global world
    world = []
    for i in range(10):
        a = []
        for j in range(10):
            a.append(0)
        world.append(a)


def update_map(player):
    global world, cupbap, pits, four_student, five_student
    for i in range(10):
        for j in range(10):
            world[i][j] = 0
    for i in cupbap:
        world[i.x_pos][i.y_pos] = 'c'
    for i in pits:
        world[i.x_pos][i.y_pos] = 'o'
    for i in four_student:
        world[i.x_pos][i.y_pos] = '4'
    for i in five_student:
        world[i.x_pos][i.y_pos] = '5'

    world[player.x_pos][player.y_pos] = 's'


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

    for i in range(10):
        for j in range(10):
            if world[i][j] == 'c':
                draw_img(img_li[0], i+1, j+1)
            if world[i][j] == 'o':
                draw_img(img_li[1], i+1, j+1)
            if world[i][j] == '4':
                draw_img(img_li[2], i+1, j+1)
            if world[i][j] == '5':
                draw_img(img_li[3], i+1, j+1)
            if world[i][j] == 's':
                draw_img(img_li[4], i+1, j+1)


def draw_img(img, x, y):
    nx = 265+16.375*(2*2*(y-1)+1)
    ny = 10+16.375*(2*2*(x-1)+1)
    screen.blit(img, (nx, ny))


def func_dis1():
    screen.fill(WHITE)
    screen.blit(pygame.transform.scale(main_image, (1200, 675)), (0, 0))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Startbutton.collidepoint(event.pos):
                        return False, True
                    if Quitbutton.collidepoint(event.pos):
                        return True, False
        pygame.draw.rect(screen, BLACK, Startbutton)
        pygame.draw.rect(screen, BLACK, Quitbutton)
        screen.blit(TitleSurfObj, TitleRectObj)
        screen.blit(MesSurfObj, MesRectObj)
        screen.blit(StSurfObj, StRectObj)
        screen.blit(EdSurfObj, EdRectObj)
        pygame.display.update()


def func_dis2():
    global four, five, cupbaps, pit
    is_fourgi = True
    is_fivegi = True
    is_cupbap = True
    is_hamjung = True
    num = 0
    get_input = True
    print_input = False

    while get_input:
        clock.tick(60)
        screen.fill(WHITE)
        write("이 게임은 당신이 사감선생님이 되어 4기와 5기를 잡는 게임입니다!", 10, 10, 30)
        write("원하는 4기와 5기, 컵밥과 함정의 수를 순서대로 입력 해 주세요 모두 15를 넘어선 안됩니다!", 10, 45, 30)
        write("아무 키나 입력해주세요", 500, 300, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                is_fourgi = False
            else:
                continue
        pygame.display.flip()
        screen.fill(WHITE)
        while not is_fourgi:
            write("4기를 몇 명으로 할지 입력해주세요", 10, 50, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    screen.fill(WHITE)
                    pressed = pygame.key.get_pressed()
                    buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                    if buttons[0] != "return" and buttons[0] != "backspace" and buttons[0].isdigit() is False:
                        write("숫자를 입력해주세요", 500, 300, 30)
                    elif buttons[0].isdigit() is True:
                        num *= 10
                        num += int(buttons[0])
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    elif buttons[0] == "backspace":
                        num //= 10
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    else:
                        if num == 0:
                            write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 350, 300, 30)
                        elif num > 15:
                            write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 300, 300, 30)
                            num = 0
                        else:
                            four = num
                            num = 0
                            is_fourgi = True
                            is_fivegi = False
            pygame.display.flip()

        screen.fill(WHITE)
        while not is_fivegi:
            write("5기를 몇 명으로 할지 입력해주세요", 10, 50, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    screen.fill(WHITE)
                    pressed = pygame.key.get_pressed()
                    buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                    if buttons[0] != "return" and buttons[0] != "backspace" and buttons[0].isdigit() is False:
                        write("숫자를 입력해주세요", 500, 300, 30)
                    elif buttons[0].isdigit() is True:
                        num *= 10
                        num += int(buttons[0])
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    elif buttons[0] == "backspace":
                        num //= 10
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    else:
                        if num == 0:
                            write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                        elif num > 15:
                            write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 300, 300, 30)
                            num = 0
                        else:
                            five = num
                            num = 0
                            is_fivegi = True
                            is_cupbap = False
            pygame.display.flip()

        screen.fill(WHITE)
        while not is_cupbap:
            write("컵밥을 몇 개로 할지 입력해주세요", 10, 50, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    screen.fill(WHITE)
                    pressed = pygame.key.get_pressed()
                    buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                    if buttons[0] != "return" and buttons[0] != "backspace" and buttons[0].isdigit() is False:
                        write("숫자를 입력해주세요", 500, 300, 30)
                    elif buttons[0].isdigit() is True:
                        num *= 10
                        num += int(buttons[0])
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    elif buttons[0] == "backspace":
                        num //= 10
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    else:
                        if num == 0:
                            write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                        elif num > 15:
                            write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 300, 300, 30)
                            num = 0
                        else:
                            cupbaps = num
                            num = 0
                            is_cupbap = True
                            is_hamjung = False
            pygame.display.flip()

        screen.fill(WHITE)
        while not is_hamjung:
            write("함정을 몇 개로 할지 입력해주세요", 10, 50, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    screen.fill(WHITE)
                    pressed = pygame.key.get_pressed()
                    buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                    if buttons[0] != "return" and buttons[0] != "backspace" and buttons[0].isdigit() is False:
                        write("숫자를 입력해주세요", 500, 300, 30)
                    elif buttons[0].isdigit() is True:
                        num *= 10
                        num += int(buttons[0])
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    elif buttons[0] == "backspace":
                        num //= 10
                        write("{}명으로 입력하셨습니다".format(num), 500, 300, 30)
                    else:
                        if num == 0:
                            write("숫자를 입력하지 않아 입력을 종료할 수 없습니다", 500, 300, 30)
                        elif num > 15:
                            write("숫자가 15가 넘어 가는군요. 처음부터 다시 입력해주세요", 300, 300, 30)
                            num = 0
                        else:
                            pit = num
                            num = 0
                            is_hamjung = True
                            get_input = False
                            print_input = True
            pygame.display.flip()

    screen.fill(WHITE)
    while print_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Startbutton2.collidepoint(event.pos):
                        return False, True

        write("4기 수: {}".format(four), 300, 50, 30)
        write("5기 수: {}".format(five), 300, 200, 30)
        write("컵밥 수: {}".format(cupbaps), 300, 350, 30)
        write("함정 수: {}".format(pit), 300, 500, 30)
        write("게임을 시작하려면 start 를 눌러주세요", 600, 300, 30)
        pygame.draw.rect(screen, BLACK, Startbutton2)
        screen.blit(StSurfObj, StRectObj2)
        pygame.display.flip()


def func_dis3():
    global four, five, cupbaps, pit, four_student, five_student, pits, cupbap, world

    game = True
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
        cupbap.append(x)
    for i in range(int(pit)):
        x = static_obj.trap(world)
        pits.append(x)

    x = ""
    while game:
        screen.fill(WHITE)

        if player.dead_or_alive() == 'dead':
            screen.fill(WHITE)
            write("사감선생님의 손전등 배터리가 끝났습니다", 400, 200, 30)
            write("점수: {}".format(player.point), 560, 300, 30)
            write("Game Over", 510, 400, 40)
            write("Enter를 누르세요", 500, 500, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                    if buttons[0] == "return":
                        return False, True
            pygame.display.flip()

        else:
            update_map(player)
            draw_map()
            if x != "":
                write("{}를 누르셨습니다".format(x), 10, 300, 20)
            write("손전등 배터리 : " + str(player.health), 10, 10, 30)
            write("점수 : " + str(player.point), 10, 50, 30)
            write("4기 수 : " + str(len(four_student)), 10, 90, 30)
            write("5기 수 : " + str(len(five_student)), 10, 130, 30)
            write("방향키를 입력하세요", 10, 200, 20)
            pygame.display.flip()

            get_event = False
            while not get_event:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.KEYDOWN:
                        get_event = True
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
                        else:
                            get_event = False
            player.move(x)
            player.catch_student(four_student, five_student)
            player.minus_health()
            update_map(player)
            for i in four_student:
                i.move4(world, four_student, five_student, pits)
                i.minus_health()
                update_map(player)
                if i.dead_or_alive() == 'dead' and i in four_student:
                    four_student.remove(i)
            for i in five_student:
                i.move5(world, cupbap, five_student, pits)
                i.minus_health()
                update_map(player)
                if i.dead_or_alive() == 'dead' and i in five_student:
                    five_student.remove(i)


def func_dis4():
    regame = True
    while regame:
        screen.fill(WHITE)
        write("다시하려면 y를 누르시고 아니라면 n을 누르세요", 350, 200, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                if buttons[0] == 'y':
                    make_map()
                    return True
                elif buttons[0] == 'n':
                    return False
        pygame.display.flip()


mk_img_li()
make_map()
dis1 = True
dis2 = False
dis3 = False
dis4 = False
while not done:

    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    if dis1:
        ch, dis2 = func_dis1()
        if not ch:
            dis1 = ch
        else:
            quit()

    if dis2:
        dis2, dis3 = func_dis2()

    if dis3:
        dis3, dis4 = func_dis3()

    if dis4:
        regame = func_dis4()
        if regame is True:
            make_map()
            dis4 = False
            dis1 = True
        else:
            dis4 = False
            done = True


# Be IDLE friendly
pygame.quit()

import pygame
import myplay
import dynamic
import static_obj
import sys


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
    img = pygame.image.load('fivegi.jpg')
    img_li.append(img)
    img = pygame.image.load('pig.jpg')
    img_li.append(img)


def draw_map():
    pygame.draw.lines(screen, BLACK, True, [[265, 10], [265, 665], [920, 665], [920, 10]], 5)
    for i in range(1, 10):
        pygame.draw.line(screen, BLACK, [265 + 65.5 * i, 10], [265 + 65.5 * i, 665], 5)
        pygame.draw.line(screen, BLACK, [265, 10 + 65.5 * i], [920, 10 + 65.5 * i], 5)


def draw_img(img, x, y):
    nx = 265+16.375*(2*2*(y-1)+1)
    ny = 10+16.375*(2*2*(x-1)+1)
    screen.blit(img, (nx, ny))

def update_map():
    for i in range(15):
        for j in range(15):
            world[i][j] = '0'
    for i in cupbabs:
        world[i.x_pos][i.y_pos] = 'c'
    for i in pits:
        world[i.x_pos][i.y_pos] = 'o'
    for i in four_student:
        world[i.x_pos][i.y_pos] = '4'
    for i in five_student:
        world[i.x_pos][i.y_pos] = '5'

    world[player.x_pos][player.y_pos] = 's'


four_student = []
five_student = []
cupbabs = []
pits = []

world = []

for i in range(0,15):
    a = []
    for j in range(0,15):
        a.append(0)
    world.append(a)

player = sagam()
player.generate(world, 's')


def draw_map():
    for i in range(1,11):
        for j in range(1,11):
            print(world[i][j], end=' ')
        print()


draw_map()
print("안녕하세요, 사감선생님의 술래잡기에 오신 것을 환영합니다! 게임을 진행하고 싶으시면 Yes를 정확하게 입력 해 주시고 하기 싫으시다면 No를 정확히 입력해주세요")

while True:
    answer = input()

    if answer == 'No':
        print("게임을 종료합니다")
        sys.exit()
    elif answer == 'Yes':
        print("게임을 시작합니다")
        break
    else:
        print("정확히 입력해 주세요")


print("이 게임은 당신이 사감선생님이 되어 4기와 5기를 잡는 게임입니다! 원하는 4기와 5기, 컵밥과 함정의 수를 순서대로 입력 해 주세요 모두 15를 넘어선 안됩니다!")
while True:
    four = input()
    if four.isdigit() and int(four) <= 15:
        print("4기 ", four, "명")
        break
    else:
        print("다시 입력하세요")

while True:
    five = input()
    if five.isdigit() and int(five) <= 15:
        print("5기 ", five, "명")
        break
    else:
        print("다시 입력하세요")

while True:
    cupbaps = input()
    if cupbaps.isdigit() and int(cupbaps) <= 15:
        print("컵밥 ", cupbaps, "개")
        break
    else:
        print("다시 입력하세요")

while True:
    pit = input()
    if pit.isdigit() and int(pit) <= 15:
        print("함정 ", pit, "개")
        break
    else:
        print("다시 입력하세요")


for i in range(int(four)):
    x = FourGi()
    x.generate(world,'4')
    four_student.append(x)

for i in range(int(five)):
    x = FiveGi()
    x.generate(world,'5')
    five_student.append(x)

for i in range(int(cupbaps)):
    x = cupbab(world)
    cupbabs.append(x)

for i in range(int(pit)):
    x = trap(world)
    pits.append(x)











print("게임이 시작되었습니다 w,a,s,d,q,e,z,c로 사감쌤을 이동시켜 따방하는 학생들을 잡으세요")
while True:
    print("남은 목숨:", player.health)
    print("4기 수:", len(four_student))
    print("5기 수:", len(five_student))
    if player.dead_or_alive() == 'dead':
        print("사감선생님의 손전등 배터리가 끝났습니다 - GAME OVER")
        sys.exit()
    else:
        update_map()
        draw_map()
        player.move()
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







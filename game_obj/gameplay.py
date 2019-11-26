from dynamic import*
from static_obj import*
import random
import sys

def update_map():
    for i in range(15):
        for j in range(15):
            world[i][j] = 0
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

while True:
    if player.dead_or_alive() == 'dead':
        print("사감선생님의 손전등 배터리가 끝났습니다 - GAME OVER")
        sys.exit()
    else:
        update_map()
        draw_map()
        print("게임이 시작되었습니다 w,a,s,d,q,e,z,c로 사감쌤을 이동시켜 따방하는 학생들을 잡으세요")
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






import random


class Dynamic():
    def __init__(self):
        self.health = 0
        self.x_pos = 0
        self.y_pos = 0

    def generate(self, world, character):
        flag = 0
        if len(world) == 0:
            self.x_pos = random.randint(1, 10)
            self.y_pos = random.randint(1, 10)
            flag = 1
        else:
            while True:
                flag = 0
                r_rand = random.randint(1, 10)
                c_rand = random.randint(1, 10)
                if world[r_rand][c_rand] == 0:
                    self.x_pos = r_rand
                    self.y_pos = c_rand
                    flag = 1
                    break
        if flag:
            world[self.x_pos][self.y_pos] = character
    def move(self):
        while True:
            direction = input()
            if direction in ['w', 'a', 's', 'd']:
                if direction == 'w':
                    self.x_pos = self.x_pos - 1
                elif direction == 'a':
                    self.y_pos = self.y_pos - 1
                elif direction == 's':
                    self.x_pos = self.x_pos + 1
                else:
                    self.y_pos = self.y_pos + 1

                break

            else:
                print("다시 제대로 입력하세여")



    def random_move(self, world):
        point = [1, 0, -1]
        pointx = [1, -1]
        new_x = self.x_pos
        new_y = self.y_pos

        while world[new_x][new_y] != '0':
            new_x = self.x_pos
            new_y = self.y_pos

            x_dir = random.choice(point)

            if x_dir == 0:
                y_dir = random.choice(pointx)
            else:
                y_dir = 0

            new_x += x_dir
            new_y += y_dir

        self.x_pos = new_x
        self.y_pos = new_y

    def minus_health(self):
        self.health = self.health - 1

    def dead_or_alive(self):
        if self.health == 0:
            return 'dead'
        else:
            return 'alive'

class sagam(Dynamic):
    def __init__(self):
        Dynamic.__init__(self)
        self.health = 5
        self.point = 0


    def catch_student(self, student_field_4, student_field_5):
        for i in student_field_4:
            if self.x_pos == i.x_pos and self.x_pos == i.y_pos:
                self.point = self.point + 2
                student_field_4.remove(i)

        for i in student_field_5:
            if self.x_pos == i.x_pos and self.y_pos == i.y_pos:
                self.point = self.point + 1
                student_field_5.remove(i)


class FourGi(Dynamic):
    def __init__(self):
        Dynamic.__init__(self)
        self.health = 3

    def eat5(self, five_list):
        for i in five_list:
            if i.x_pos == self.x_pos and i.y_pos == self.y_pos:
                five_list.remove(i)
                break

    def move4(self, world, four_list, five_list, trap_list):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        find5 = False
        for i in range(4):
            nx = self.x_pos + dx[i]
            ny = self.y_pos + dy[i]
            if nx <= 0 or nx > 10 or ny <= 0 or ny > 10:
                continue
            if world[nx][ny] == '5':
                self.x_pos = nx
                self.y_pos = ny
                self.eat5(five_list)
                find5 = True
                break
        if find5 is False:
            self.random_move(world)
            self.fallen(four_list, trap_list)

    def fallen(self, four_list, trap_list):
        die = False
        for i in trap_list:
            if self.x_pos == i.x_pos and self.y_pos == i.y_pos:
                die = True
                break
        if die is True:
            four_list.remove(self)




class FiveGi(Dynamic):
    def __init__(self):
        Dynamic.__init__(self)
        self.health = 3

    def eatcup(self, cup_list):
        for i in cup_list:
            if i.x_pos == self.x_pos and i.y_pos == self.y_pos:
                cup_list.remove(i)
                break

    def move5(self, world, cup_list, five_list, trap_list):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        find_cup = False
        for i in range(4):
            nx = self.x_pos + dx[i]
            ny = self.y_pos + dy[i]
            if nx <= 0 or nx > 10 or ny <= 0 or ny > 10:
                continue
            if world[nx][ny] == 'c':
                self.x_pos = nx
                self.y_pos = ny
                self.eatcup(cup_list)
                find_cup = True
                break
        if find_cup is False:
            self.random_move(world)
            self.fallen(five_list, trap_list)

    def fallen(self, five_list, trap_list):
        die = False
        for i in trap_list:
            if self.x_pos == i.x_pos and self.y_pos == i.y_pos:
                die = True
                break
        if die is True:
            five_list.remove(self)

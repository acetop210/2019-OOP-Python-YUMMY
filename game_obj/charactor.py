from .dynamic import Dynamic


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
            nx = self.x_pos + dx
            ny = self.y_pos + dy
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
            nx = self.x_pos + dx
            ny = self.y_pos + dy
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

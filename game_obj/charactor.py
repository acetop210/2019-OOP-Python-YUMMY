from .dynamic import dynamic


class FourGi(dynamic):
    def __init__(self):
        dynamic.__init__(self)
        self.health = 3

    def eat5(self, five_list):
        for i in five_list:
            if i.x_pos == self.x_pos and i.y_pos == self.y_pos:
                five_list.remove(i)
                break

    def move4(self, world, five_list):
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


class FiveGi(dynamic):
    def __init__(self):
        dynamic.__init__(self)
        self.health = 3

    def eatcup(self, cup_list):
        for i in cup_list:
            if i.x_pos == self.x_pos and i.y_pos == self.y_pos:
                cup_list.remove(i)
                break

    def move5(self, world, cup_list):
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

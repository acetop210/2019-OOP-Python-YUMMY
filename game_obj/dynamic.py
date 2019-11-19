import random


class dynamic():
    def __init__(self):
        self.health = 0
        self.x_pos = 0
        self.y_pos = 0

    def move(self):
        direction = input()

        if direction in ['w', 'a', 's', 'd']:
            if direction == 'w':
                self.y_pos = self.y_pos + 1
            elif direction == 'a':
                self.x_pos = self.x_pos - 1
            elif direction == 's':
                self.x_pos = self.x_pos + 1
            else:
                self.y_pos = self.y_pos - 1

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

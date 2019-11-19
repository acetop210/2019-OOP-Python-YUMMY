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

    def random_move(self):
        point = [1, 0, -1]
        pointx = [1, -1]
        x_direction = random.choice(point)

        if x_direction == 0:
            y_direction = random.choice(pointx)
        else:
            y_direction = 0

        self.x_pos = x_direction
        self.y_pos = y_direction

    def minus_health(self):
        self.health = self.health - 1

    def dead_or_alive(self):
        if self.health == 0:
            return 'dead'
        else:
            return 'alive'

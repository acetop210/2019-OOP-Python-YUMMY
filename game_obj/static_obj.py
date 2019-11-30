
import random


class static(): #움직이지 않는 객체의 클래스

    def __init__(self, field): # 판의 정보 field를 받아서 비어있는 곳에 객체를 생성.
        self.x_pos = 0
        self.y_pos = 0

        flag = 0
        if len(field) == 0:
            self.x_pos = random.randint(1, 10)
            self.y_pos = random.randint(1, 10)
            flag=1
        else:
            while True:
                flag = 0
                r_rand = random.randint(1,10)
                c_rand = random.randint(1,10)
                if field[r_rand][c_rand] == 0:
                    self.x_pos = r_rand
                    self.y_pos = c_rand
                    flag = 1
                    break
        if flag:
            field[self.x_pos][self.y_pos] = 1

    def draw(self, screen):
        position = (self.y_pos * 10, self.x_pos * 10, 30, 30)
        screen.blit(self.kind, position)
    


class cupbab(static): #컵밥 클래스

    def __init__(self, field):
        static.__init__(self, field)
        self.health = 3

    def eaten(self, bab, field): # 컵밥의 정보가 든 리스트 bab, 판의 정보 field를 받아서 객체를 삭제.
        for i in bab:
            if self.x_pos == i.r_pos and self.y_pos == i.c_pos:
                bab.remove(i)
                
        field[self.x_pos][self.y_pos] = 0


class trap(static): #함정 클래스

    def __init__(self, field):
        static.__init__(self, field)
    
    def delete(self, Trap):
        for i in Trap:
            if self.x_pos == i.r_pos and self.y_pos == i.c_pos:
                Trap.remove(i)

    def fellin(self):
        self.health -= 1

    def istrap(self):
        if self.health > 0:
            return 1
        else:
            return 0
        












    
    
    
        

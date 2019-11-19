
import random    

class static(): #움직이지 않는 객체의 클래스

    def __init__(self, field): # 객체 전부의 정보가 들어있는  리스트 field를 받아서 비어있는 곳에 객체를 생성.
        self.r_pos = 0
        self.c_pos = 0

        flag = 0
        if len(field) == 0:
            self.r_pos = random.randint(1, 10)
            self.c_pos = random.randint(1, 10)
            flag=1
        else:
            while True:
                flag = 0
                r_rand = random.randint(1,10)
                c_rand = random.randint(1,10)
                if field[r_rand][c_rand] == 0:
                    self.r_pos = r_rand
                    self.c_pos = c_rand
                    flag = 1
                    break
        if flag:
            field[self.r_pos][self.c_pos] = 1


class cupbab(static): #컵밥 클래스
    
    def eaten(bab, field): # 컵밥의 정보가 든 리스트 bab, 객체 전부의 정보가 든 리스트 field를 받아서 객체를 삭제.
        for i in bab:
            if self.r_pos == i.r_pos and self.c_pos == i.c_pos:
                bab.remove(i)
        for i in field:
            if self.r_pos == i.r_pos and self.y_pos == i.c_pos:
                field.remove(i)


class trap(static): #함정 클래스
    pass #함정이 생성되고 나서는 아무것도 안 함.



field = []
for i in range(15):
    line = []
    for j in range(15):
        line.append(0)
    field.append(line)
    
cnt = 0

while True:
    a = cupbab(field)
    print(a.r_pos, a.c_pos, cnt, a)
    cnt += 1


















    
    
    
        

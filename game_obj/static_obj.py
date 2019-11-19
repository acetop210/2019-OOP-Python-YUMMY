
import random    

class static(): #움직이지 않는 객체의 클래스

    def __init__(self, field): # 객체 전부의 정보가 들어있는  리스트 field를 받아서 비어있는 곳에 객체를 생성.
        self.x_pos = 0
        self.y_pos = 0
        
        if len(field) == 0:
            self.x_pos = random.randint(1, 10)
            self.y_pos = random.randint(1, 10)
        else:
            while True:
                flag = 0
                x_rand = random.randint(1,10)
                y_rand = random.randint(1,10)
                for i in field:
                    if i.x_pos == x_rand and i.y_pos == y_rand:
                        flag = 1
                if flag == 0:
                    self.x_pos = x_rand
                    self.y_pos = y_rand
                    break


class cupbab(static): #컵밥 클래스
    
    def eaten(bab, field): # 컵밥의 정보가 든 리스트 bab, 객체 전부의 정보가 든 리스트 field를 받아서 객체를 삭제.
        for i in bab:
            if self.x_pos == i.x_pos and self.y_pos == i.y_pos:
                bab.remove(i)
        for i in field:
            if self.x_pos == i.x_pos and self.y_pos == i.y_pos:
                field.remove(i)


class trap(static): #함정 클래스
    pass #함정이 생성되고 나서는 아무것도 안 함.


















    
    
    
        

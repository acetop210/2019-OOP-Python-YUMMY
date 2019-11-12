class Charactor (object):

   def __init__(self):
      self.vote_cnt = 1

   def vote(self, id_li):
      nominate = ""
      while nominate not in id_li:
         nominate = input("투표하고자 하는 사람의 ID를 입력하세요")
      return nominate
   
   def night_act(self):
      pass
      

class Mafia (Charactor):
   
   def __init__(self, id):
      self.id = id
      self.job = "Mafia"
   
   def night_act(self):
      select_die = input("죽일 사람의 ID를 입력하세요")
      return select_die
      

class Police (Charactor):
   
   def __init__(self, id):
      self.id = id
      self.job = "Police"
   
   def night_act(self):
      select_search = input("조사할 사람의 ID를 입력하세요")
      return select_search


class Doctor (Charactor):
   
   def __init__(self, id):
      self.id = id
      self.job = "Doctor"
   
   def night_act(self):
      select_heal = input("살릴 사람의 ID를 입력하세요")
      return select_heal
      
      
class Citizen(Charactor):
   
   def __init__(self):
      self.id = id
      self.job = "Citizen"

   def night_act(self):
      print("날이 밝을 때까지 기다리세요")
      return None

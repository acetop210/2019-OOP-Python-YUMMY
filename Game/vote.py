import threading

class Vote_system(object):
   
   def __init__(self, player_num):
      self.player_num = player_num
   
   def first_vote(self, player_li):
      for player in player_li:
         threading.Thread(target=player.vote, args=player_li)
   
   def last_time(self):
      pass
   
   def second_vote(self):
      pass
   
   def vote_kill(self):
      pass
   

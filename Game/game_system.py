from .charactor import *
from .vote import *


class Game_System (object):
   def __init__(self):
      self.player_dic = {"mafia": [], "police": [], "doctor": [], "citizen": []}
      self.dead_player = []
      self.timer = 0.0
      self.is_end = False
      
   def add_player(self, ID):
      pass
   
   def daytime(self):
      pass
   
   def nighttime(self):
      pass
   
   def check_end(self):
      pass

from dataclasses import dataclass
from designer import *
from random import randint

@dataclass
class World:
    player_speed:int
    player_icon:DesignerObject


#def create_world() -> World:

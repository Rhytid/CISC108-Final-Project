from dataclasses import dataclass
from designer import *
from random import randint
import time


@dataclass
class World:
    obstacle_speed: int
    player_icon: DesignerObject
    in_space: bool
    timer: float




def create_playericon() -> DesignerObject:
    """Creates the bird icon for the player"""
    bird = emoji("bird")
    bird.y = 550
    bird.x = 100
    bird.flip_x = True
    return bird


def movement(world: World):
    """Makes sure that the world is constantly moving"""
    if world.in_space:
        world.player_icon.y -= 100
    else:
        world.player_icon.y += 2



def create_world()->World:
    """Creates the world for game"""
    player_icon = create_playericon()
    return World(5, player_icon,False, time.time())


def jump(world: World):
    world.in_space = True
    world.player_icon.y -= 50

def space_released(world: World):
    """ Allows the bird to fall when "space" key is released (user stops pressing "space" key"""
    world.in_space = False

def game_loop(world: World):
    """Allows the game to have continuous movement of the bird"""
    movement(world)

    passing_time = time.time() - world.timer
    if passing_time > 100:
        world.obstacle_speed += 1
        world.timer = time.time()

  





# when('updating', constant_movement)
when("typing", jump)
when('starting', create_world)
when("typing", space_released)
when("updating", game_loop)
start()

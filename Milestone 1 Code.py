from dataclasses import dataclass
from designer import *
from random import randint


@dataclass
class World:
    obstacle_speed: int
    player_icon: DesignerObject


def create_playericon() -> DesignerObject:
    """Creates the bird icon for the player"""
    alien = emoji("bird")
    alien.y = 550
    alien.x = 100
    alien.flip_x = True
    return alien


def constant_movement(world: World):
    """Makes sure that the world is constantly moving"""
    world.player_icon.x


def create_world() -> World:
    """Creates the world for game"""
    return World(5, create_playericon())


def jump(world: World, input: str):
    if input == "space":
        world.player_icon.y -= 15


# when('updating', constant_movement)
when("typing", jump)
when('starting', create_world)
start()
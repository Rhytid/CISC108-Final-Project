from dataclasses import dataclass
from designer import *
from random import randint
import time

@dataclass
class World:
    obstacle_speed: int
    player_icon: DesignerObject
    in_space: bool
    obstacles: list[DesignerObject]
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

def create_world() -> World:
    """Creates the world for the game"""
    player_icon = create_playericon()
    return World(5, player_icon, False, [], time.time())

def jump(world: World):
    """Allows the Bird to fly up into the air"""
    world.in_space = True
    world.player_icon.y -= 50

def space_released(world: World):
    """Allows the bird to fall when the "space" key is released"""
    world.in_space = False

def game_loop(world: World):
    """Allows the game to have continuous movement of the bird"""
    movement(world)
    if collision(world):
        world.in_space = False  
        world.player_icon.y = max(0, world.player_icon.y)  
        pause()

def collision(world: World) -> bool:
    """ Makes the bird pause and stop the game with it collides with the obstacles or edge of the screen"""
    collides = False
    for obstacle in world.obstacles:
        if colliding(obstacle, world.player_icon) or world.player_icon.y <= 0:
            collides = True
    return collides

def obstacle_spawn(world:World):
    """ Creation of the icons that will be the obstacle"""
    if world.obstacle_speed > 10:
        obstacle = emoji('rock')
    elif world.obstacle_speed > 15:
        obstacle = emoji("baby")
    elif world.obstacle_speed > 20:
        obstacle = emoji("dog")
    elif world.obstacle_speed > 25:
        obstacle = emoji("cloud")
    else:
        obstacle = emoji("bug")
    
    obstacle.scale_x = 1
    obstacle.scale_y = 1
    obstacle.x = get_width()
    obstacle.y = randint(0, get_height())
    return obstacle

def obstacles(world: World):
    """Creating the obstacle that the player icon will have to avoid hitting"""
    if len(world.obstacles) < 1:
        world.obstacles.append(obstacle_spawn(world))

def obstacle_movement(world: World):
    """Moves the obstacles"""
    for obstacle in world.obstacles:
        obstacle.x -= world.obstacle_speed

def obstacle_deletion(world: World):
    """Removes excess obstacles"""
    newlist = []
    for obstacle in world.obstacles:
        if obstacle.x > 10:
            newlist.append(obstacle)
        else:
            destroy(obstacle)
    world.obstacles = newlist

def speed_up(world: World):
    """Speeds up the obstacles"""
    passing_time = time.time() - world.timer
    if int(passing_time) % 5 == 0 and int(passing_time) > 3:
        world.obstacle_speed += 0.01
        

when("typing", jump)
when('starting', create_world)
when("typing", space_released)
when("updating", game_loop)
when("updating", obstacle_deletion)
when("updating", movement)
when("updating", obstacle_movement)
when("updating", obstacles)
when("updating", speed_up)
when(collision, pause)
start()

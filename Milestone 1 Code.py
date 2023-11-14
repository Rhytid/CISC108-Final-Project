from dataclasses import dataclass
from designer import *
from random import randint
import time


@dataclass
class World:
    obstacle_speed: int
    player_icon: DesignerObject
    in_space: bool
    bugs: list[DesignerObject]
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
    """Creates the world for game"""
    player_icon = create_playericon()
    return World(5, player_icon, False, [], time.time())




def jump(world: World):
    world.in_space = True
    world.player_icon.y -= 50

def space_released(world: World):
    """ Allows the bird to fall when "space" key is released (user stops pressing "space" key"""
    world.in_space = False

def game_loop(world: World):
    """Allows the game to have continuous movement of the bird"""
    movement(world)

def collision(world:World)->bool:
    collides = False
    for bug in world.bugs:
        if colliding(bug, world.player_icon):
            collides = True
    return collides
            

def obstacle_spawn():
    bug = emoji('bug')
    bug.scale_x = 1
    bug.scale_y = 1
   # bug.anchor = 'midbottom'
    bug.x = get_width()
    bug.y = randint(0,get_height())
    return bug

    
def obstacle_movement(world:World):
    passing_time = time.time() - world.timer
    print (passing_time)
    newlist = []
    oglist = []
    newlist.append(int(passing_time))
    
    
    if ((passing_time))%2==0:
        world.bugs.append(obstacle_spawn())
    
    newlist = []
    
    
def bug_movement(world:World):
    for bug in world.bugs:
        bug.x -= world.obstacle_speed

def bug_deletion(world:World):
    """Removes excess bugs"""
    newlist = []
    for bug in world.bugs:
        if bug.x >10 :
            newlist.append(bug)
        else:
            destroy(bug)
    world.bugs = newlist
    
    


# when('updating', constant_movement)
when("typing", jump)
when('starting', create_world)
when("typing", space_released)
when("updating", game_loop)
when("updating", obstacle_movement)
when("updating",movement)
when("updating",bug_movement)
when("updating",bug_deletion)
when(collision, pause)
start()

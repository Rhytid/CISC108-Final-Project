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
    point: int
    counter: DesignerObject
    balloons: list[DesignerObject]

def create_playericon() -> DesignerObject:
    """Creates the bird icon for the player"""
    bird = emoji("bird")
    bird.y = 450
    bird.x = 100
    bird.flip_x = True
    return bird

def player_movement(world: World):
    """Makes sure that the world is constantly moving"""
    if world.in_space:
        world.player_icon.y -= 100  
    else:
        world.player_icon.y += 2

def create_world() -> World:
    """Creates the world for the game"""
    player_icon = create_playericon()
    return World(5, player_icon, False, [], time.time(), 0, text("black"," 0",20,400,65), [])

def jump(world: World):
    """Allows the Bird to fly up into the air"""
    world.in_space = True
    world.player_icon.y -= 50

def space_released(world: World):
    """Allows the bird to fall when the "space" key is released"""
    world.in_space = False

def game_loop(world: World):
    """Allows the game to have continuous movement of the bird"""
    player_movement(world)
    if collision(world):
        world.in_space = False  
        world.player_icon.y = max(0, world.player_icon.y)  
        pause()

def collision(world: World) -> bool:
    """ Makes the bird pause and stop the game with it collides with the obstacles or edge of the screen"""
    collides = False
    for obstacle in world.obstacles:
        if colliding(obstacle, world.player_icon):
            collides = True
        if (world.player_icon.y <=0 or world.player_icon.y >= 600):
            collides = True
    return collides

def generate_obstacle(world:World):
    """ Creation of the icons that will be the obstacle"""
    if 10> world.point >= 5:
        obstacle = emoji('rock')
    elif 15>world.point >= 10:
        obstacle = emoji("baby")
    elif 20>world.point >= 15:
        obstacle = emoji("dog")
    elif world.point >= 20:
        obstacle = emoji("cloud")
    else:
        obstacle = emoji("bug")
    
    obstacle.scale_x = 1
    obstacle.scale_y = 1
    obstacle.x = get_width()
    obstacle.y = randint(0, get_height())
    return obstacle

def celebration(world:World):
    """Spawns celebratory balloons if the player makes it to the final level"""
    if world.point >= 20:
        if len(world.balloons) < 11:
            world.balloons.append(balloon_creation(world))

def balloon_creation(world:World):
    """Creates the balloon emoji"""
    balloon = emoji("balloon")
    balloon.scale_x = 2
    balloon.scale_y = 2
    balloon.x = randint(0,get_width())
    balloon.y = get_height()
    return balloon

def balloon_movement(world: World):
    """Moves the balloons"""
    for balloon in world.balloons:
        balloon.y -= randint(5,15)
def obstacle_creation(world: World):
    """Creating the obstacle that the player icon will have to avoid hitting"""
    if len(world.obstacles) < 1:
        world.obstacles.append(generate_obstacle(world))

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
            world.point += 1
            world.obstacle_speed += 1.5
    world.obstacles = newlist
    
def balloon_deletion(world:World):
    """Removes excess balloons"""
    newlist =[]
    for balloon in world.balloons:
        if balloon.y > 10:
            newlist.append(balloon)
        else:
            destroy(balloon)
    world.balloons = newlist


def display_points(world):
    """Show the point value"""
    world.counter.text = "Points: " + str(world.point)
    #print(world.player_icon.y)
    
def game_over(world):
    """ Show the game over message """
    world.counter.text = "GAME OVER! Your score was " + str(world.point)

when("typing", jump)
when('starting', create_world)
when("typing", space_released)
when("updating", game_loop)
when("updating", celebration)
when("updating", player_movement)
when("updating", obstacle_creation)
when("updating", obstacle_movement)
when("updating", balloon_movement)
when("updating", display_points)
when("updating", obstacle_deletion)
when("updating", balloon_deletion)
when(collision, game_over, pause)
start()

from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_0, SDLK_2, SDLK_1

import game_framework
import game_world
import play_mode
import title_mode
from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events

from pannel import Pannel


def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def finish():
    game_world.remove_object(pannel)

def update():
    pass

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            play_mode.boy.set_item('None')
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            play_mode.boy.set_item('SmallBall')
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            play_mode.boy.set_item('BigBall')

def pause():
    pass

def resume():
    pass
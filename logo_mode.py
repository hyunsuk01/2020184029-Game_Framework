import game_framework
import title_mode
from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events


def init():
    global image
    global logo_start_time
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def finish():
    global image #logo_mode 전체에서 사용
    del image #강제적으로 메모리에서 이미지 삭제

def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()

def pause():
    pass

def resume():
    pass
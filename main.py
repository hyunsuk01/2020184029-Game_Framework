import game_framework
# 게임 기본 구조
from pico2d import open_canvas, delay, close_canvas
# title mode를 import 하되, 이름을 바꿔친다.
import logo_mode as start_mode

open_canvas()
game_framework.run(start_mode)
close_canvas()
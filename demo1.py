# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-27 22:56
import sys
import pygame

# pygame初始化
pygame.init()
# 设置窗口title
pygame.display.set_caption("pysnake")

# 画面更新
game_clock = pygame.time.Clock()
game_speed = 60

# 设置窗口大小
game_screen_width, game_screen_height = 640, 480
game_screen = pygame.display.set_mode(size=(game_screen_width, game_screen_height))
game_field = game_screen.get_rect()

game_running = True
game_playing = True

# 游戏背景RGB数值
game_backgroundcolor = 0, 0, 0
game_line_color = 33, 66, 33

# 游戏区域颜色
square_color = 33, 255, 33
square_color2 = 33, 192, 33

# 蛇大小（边长）
cell_size = 20

# 蛇头的位置
square_rect = pygame.Rect(game_screen_width / 2, game_screen_height / 2, cell_size, cell_size)
up, down, left, right = (0, -cell_size), (0, cell_size), (-cell_size, 0), (cell_size, 0)

# 设置蛇的初始移动方向为右
square_direct = right
square_turn = right

# 每秒走几格
square_speed = 5

# 蛇每次运动的间隔
square_delay = 1000 / square_speed

square_time2move = pygame.time.get_ticks() + square_delay

square_body = [pygame.Rect(0, 0, 0, 0)] * 1

# 主循环
while game_running:
    # 用户请求
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen = False

        # 键盘输入上下左右时，x,y轴的变化
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and square_direct != down:
                square_turn = up
            elif event.key == pygame.K_DOWN and square_direct != up:
                square_turn = down
            elif event.key == pygame.K_LEFT and square_direct != right:
                square_turn = left
            elif event.key == pygame.K_RIGHT and square_direct != left:
                square_turn = right

    # 更新数据
    if pygame.time.get_ticks() >= square_time2move:
        square_time2move = pygame.time.get_ticks() + square_delay
        # 增加一节身体
        square_body = [square_rect] + square_body
        # 截取尾部
        square_body.pop()
        square_direct = square_turn
        square_rect = square_rect.move(square_direct)

    # 判断是否撞到而导致game over
    if game_playing:
        # 撞到墙
        if not game_field.contains(square_rect):
            game_playing = False
        # 撞到自己身体
        for cell in square_body:
            if square_rect == cell:
                game_playing = False
        if not game_playing:
            print("GAME OVER")

    if game_playing:
        # 改变画面颜色
        game_screen.fill(game_backgroundcolor)
        # 游戏矩形的位置
        # 画头
        game_screen.fill(square_color, square_rect)
        game_screen.fill(square_color2, square_rect.inflate(-4, -4))

        # 画身体
        for cell in square_body:
            game_screen.fill(square_color, cell)
            game_screen.fill(square_color2, cell.inflate(-4, -4))

        # 画格子
        for i in range(cell_size, game_screen_width, cell_size):
            pygame.draw.line(game_screen, game_line_color, (i, 0), (i, game_screen_height))
        for i in range(cell_size, game_screen_height, cell_size):
            pygame.draw.line(game_screen, game_line_color, (0, i), (game_screen_width, i))

    # 更新画面
    game_clock.tick(game_speed)
    pygame.display.update()

# 退出pygame
pygame.quit()
# 退出sys
sys.exit(0)

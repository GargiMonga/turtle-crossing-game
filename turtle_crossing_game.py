import time
from turtle import Screen
from t_cross_oop import Player, CarManager, ScoreBoard

try:
    import winsound
    play_sound = lambda f: winsound.PlaySound(f, winsound.SND_ASYNC)
except ImportError:
    play_sound = lambda f: None

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
Car = CarManager()
scoreboard = ScoreBoard()

TOTAL_TIME = 30
start_time = time.time()
g_on = True

def restart():
    global player, Car, scoreboard, g_on, start_time
    screen.clear()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()

    player = Player()
    Car = CarManager()
    scoreboard = ScoreBoard()

    screen.onkey(player.up, 'Up')
    screen.onkey(player.down, 'Down')
    screen.onkey(restart, 'r')
    screen.onkey(restart, 'R')

    g_on = True
    start_time = time.time()

screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')
screen.onkey(restart, 'r')
screen.onkey(restart, 'R')

while True:
    if g_on:
        time.sleep(0.1)
        screen.update()
        Car.create_car()
        Car.move_cars()

        for car in Car.all_cars:
            if car.distance(player) < 30:
                scoreboard.lose_life()
                play_sound('SystemHand')
                if scoreboard.lives == 0:
                    g_on = False
                    scoreboard.g_over()
                else:
                    player.go_to_start()

        if player.is_at_finish_line():
            player.go_to_start()
            Car.level_up()
            scoreboard.inc_level()
            play_sound('SystemAsterisk')
            start_time = time.time()

        remaining = TOTAL_TIME - int(time.time() - start_time)
        scoreboard.update_timer(remaining)
        if remaining <= 0:
            g_on = False
            scoreboard.g_over()

    screen.update()
screen.exitonclick()

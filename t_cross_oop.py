from turtle import Turtle
from random import randint, choice

random_c = ['red', 'yellow', 'green', 'orange', 'blue', 'purple', 'pink']
starting_pos = -280
move_dis = 10
finish_line = 280
MAX_LIVES = 3

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def move(self):
        pass

    def is_at_finish_line(self):
        if self.ycor() > finish_line:
            return True
        return False

    def go_to_start(self):
        self.goto(0, starting_pos)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(random_c))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

font = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 1
        self.lives = MAX_LIVES

        self.level_display = Turtle()
        self.level_display.penup()
        self.level_display.hideturtle()
        self.level_display.goto(-280, 250)

        self.lives_display = Turtle()
        self.lives_display.penup()
        self.lives_display.hideturtle()
        self.lives_display.goto(120, 250)

        self.timer_display = Turtle()
        self.timer_display.penup()
        self.timer_display.hideturtle()
        self.timer_display.goto(-60, 220)

        self.update_hud()

    def update_hud(self):
        self.level_display.clear()
        self.level_display.write(f'Level: {self.level}', align='left', font=font)

        self.lives_display.clear()
        self.lives_display.write(f'Lives: {self.lives}', align='left', font=font)

    def update_timer(self, time_remaining):
        self.timer_display.clear()
        self.timer_display.write(f'Time: {time_remaining}', align='left', font=('Courier', 18, 'normal'))

    def inc_level(self):
        self.level += 1
        self.update_hud()

    def lose_life(self):
        self.lives -= 1
        self.update_hud()

    def g_over(self, car_manager):
        for car in car_manager.all_cars:
            car.goto(1000, 1000)  # Move cars far away
        self.goto(-60, 0)
        self.write(f'GAME OVER', align='left', font=font)
        self.goto(-120, -40)
        self.write('Press  R  to Restart', align='left', font=('Courier', 18, 'normal'))

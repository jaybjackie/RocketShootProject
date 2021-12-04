from aircraft import Aircraft
from bullets import Bulltes
from enemy import Enemy
from stage import Stage
from vector import Vector
from border import Border 
from turtle import Screen, begin_fill, textinput

import os
import time
import random
import turtle

ENEMIES_NUM = 5
STAGE_WIDTH = 900
STAGE_HEIGHT = 600
init_x = -395
init_y = 0

outside = (-800,800)
deploy_area = [208, 156, 104, 52, 0, -52, -104, -156, -208]

# Initailize display window and border
border = Border(Vector(0, 0), width=STAGE_WIDTH, height=STAGE_HEIGHT)
stage = Stage()
# Initialize stage
stage.init_screen()

painter = turtle

# Initialize Border; Playing area
border.draw(painter)

# User Preferance
player_name = textinput("What's your name pilot?", "Enter your name:")
color = textinput("What's color would you like to be?", "Enter the color\n(red,green,blue,yellow,pink,white)")

# Create objects
aircraft = Aircraft(shape="triangle",color=color,pos=(init_x, init_y))
bullet = Bulltes("square", color=color, pos=outside ,player = aircraft)

enemies = []
for _ in range(ENEMIES_NUM):
    enemies.append(Enemy("turtle", "purple",pos=(390, random.choice(deploy_area))))

# Keyboard Bindings
turtle.onkey(aircraft.move_up, 'w')
turtle.onkey(aircraft.move_down, 's')
turtle.onkey(aircraft.move_forward, 'd')
turtle.onkey(aircraft.move_backward, 'a')
turtle.onkey(bullet.firing,'space')
turtle.listen()

# Show score on the display screen
border.show_status(painter, aircraft)

# Player lives
aircraft.lives = 3

while True:
    aircraft.move()
    # enemy.move()
    bullet.move()
    
    for enemy in enemies:
        enemy.move()
        # Border check for enemies
        if enemy.xcor() <= -400:
            enemy.goto(390, random.choice(deploy_area))

        # Enemy colided aircraft checking
        if aircraft.is_collided(enemy):
            aircraft.lives -= 1
            enemy.goto(390, random.choice(deploy_area))
            border.show_status(painter, aircraft)

        # Bullet colided Enemy checking
        if bullet.is_collided(enemy):
            border.score += 100
            enemy.goto(390, random.choice(deploy_area))
            border.show_status(painter, aircraft)
        
        if aircraft.lives == 0:
            break
        
        ### adding sound, bg, game conditon, scoreboard
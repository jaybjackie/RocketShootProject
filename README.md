# RocketShootProject

Rocket Shoot Game by Python Turtle Graphic.

<img width="1292" alt="representpic" src="https://user-images.githubusercontent.com/88821578/144994155-f4585640-fcb6-4cc4-9e62-7f0e3f3809a0.png">

# Class Description

Rocket Shoot Game is created by many source code. 
Description below Here.

### 1. `Mold` class

This Class is the Super class of Python turtle inherit object for the flying objects in this program.
This module requires serveral attributes which are shape to shape the turtle, color to paint the turtle, pos for position of object and private attribute speed to set its speed.

#### features
  + is_collided(other)-> boolean

### 2. Class `aircraft.py`

Aircraft class is the child class of Mold Super class which intialize flying objects.
This class adding attributes lives and score to represent aircraft lives and its earned from destroyed enemies. 


### 3. Class `enemy.py`

This class is child class of Mold class. This class is similar to its parent class. Whose represent enemies in this program.

### 4. Class `bullets.py`

Bullets class is also child class of Mold class. Representing bullets object, with privated attributes status and pilot which use to considering firing or not and whose pilot going to be shooting the bullets.

### 5. Class `stage.py`

Class to setting up display window size and background picture.

### 6. Class `border.py`

This class are setting up the border which is playing area of this game by given attributes corner, width, height. In this class have methods to show score status, display gameover word and also show leadership scores on the screen by turtle object as a painter.

### Class `read.py`

Class Read takes the field of collect player name and score, then insert these information to the database json file to be the record of leadership score.

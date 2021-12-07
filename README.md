# RocketShootProject

Rocket Shoot Game by Python Turtle Graphic.

<img width="1292" alt="representpic" src="https://user-images.githubusercontent.com/88821578/144994155-f4585640-fcb6-4cc4-9e62-7f0e3f3809a0.png">

# Class Description

Rocket Shoot Game is created by many source code. 
Description below Here.

### 1. `Mold`

This Class is the Super class of Python turtle inherit object for the flying objects in this program.
This module requires serveral attributes which are shape to shape the turtle, color to paint the turtle, pos for position of object and private attribute speed to set its speed.

#### feature
  + is_collided(other) : To check whether objects collided or not.


### 2. `Airplane`

Aircraft class is the child class of Mold Super class which intialize flying objects.
This class adding attributes lives and score to represent aircraft lives and its earned from destroyed enemies. 

#### features
 move(), move_up(), move_down(), move_forward(), move_backward(). to control the movement of airplane object.

### 3. `Enemy`

This class is child class of Mold class. This class is similar to its parent class. Whose represent enemies in this program.

#### feature
move() to move in linear direction toward the player.

### 4. `Bullets`

Bullets class is also child class of Mold class. Representing bullets object, with privated attributes status and pilot which use to considering firing or not and whose pilot going to be shooting the bullets.

#### features
firing(), move() are cooperate to firing the bullet. The firing() will change status to firing when player activate firing by pressing spacebar if the current status is ready only. move() is move bullets to the outside screen.

### 5. `Stage`

Class to setting up display window size and background picture.

#### feature
setting up the display window.

### 6. `Border`

This class are setting up the border which is playing area of this game by given attributes corner, width, height. In this class have methods to show score status, display gameover word and also show leadership scores on the screen by turtle object as a painter.

#### features
+ draw() is method to draw the border on the screen to be specify area of playing.
+ show_status show the player score and lives on the left-top of the window.
+ display_gameover() this method write the word 'GAMEOVER' and player score on the center of the screen
+ display_rank() this method writing leadership by player name and thier score on screen. Whose highest score represent at the first lines of leadership section.


### 7. `Read`

Class Read takes the field of collect player name and score, then insert these information to the database json file to be the record of leadership score.

#### features
+ insert() : insert player name and their score into the database.json file.
+ get_top() : Return list contains player name and thier score in Decsending order from database.json file.

### 8. `Vector`

This class is the Datatype class. Define Vector in 2D space.

p.s. from week10 assignment


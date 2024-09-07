import os
import random
import turtle
import pygame # type: ignore
import time

# Initialize pygame mixer
pygame.mixer.init()

d = input("Do you want instructions")
if d == "yes"or d == "ya" or d == "Yes"or d == "Ya":
      print("are yoou ready?")
      print("you have 10 lives")
      print("kill all enemys(red circles)")
      print("space to shoot,up arrow to go faster,down arrow for slower and if\nyou press it too many times its reverse,side arrows to shange direction")
      print("good luck go!!")
      time.sleep(20.61)
else:
      print("here we go!!!")
      time.sleep(2)

#setting the animation speed, backround color
turtle.speed(0)
turtle.title('Space war')
turtle.bgcolor("black")
#turtle.bgpic("starfield.gif")
#hiding the default turtle
turtle.ht()
#limiting the memory to 1
turtle.setundobuffer(1)
#speeding up the animation speed
turtle.tracer(0)
#Sprite class
class Sprite(turtle.Turtle):
#telling it that when we define the player that were putting in the shape the color and where
#the player should spawn
    def __init__(self,spriteshape,color,startx,starty):
            turtle.Turtle.__init__(self,shape = spriteshape)
            self.speed(0)
            self.penup()
            self.color(color)
            self.fd(0)
            self.goto(startx,starty)
            self.speed = 1

    def move(self):
          self.fd(self.speed)
          if self.xcor() > 290 :
                 self.rt(60)
                 self.setx(290)

          if self.xcor() < -290 :
                 self.rt(60)
                 self.setx(-290)

          if self.ycor() > 290 :
                 self.rt(60)
                 self.sety(290)

          if self.ycor() < -290 :
                 self.rt(60)
                 self.sety(-290)

class Player(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            self.shapesize(stretch_wid=1.7,stretch_len= 1.7,outline=None)
            self.speed = 4
            self.lives = 10

    def turn_left(self):
            self.lt(45)

    def turn_right(self):
            self.rt(45)

    def accelerate(self):
            self.speed += 1

    def deccelerate(self):
            self.speed -=1

    def is_collision(self,other):
           if (self.xcor() >= (other.xcor() - 20))and \
           (self.xcor() <= (other.xcor() + 20))and \
           (self.ycor() >= (other.ycor() - 20))and \
           (self.ycor() <= (other.ycor() + 20)):
              return True
           else:
              return False
              
              
class Enemy(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            self.speed = 6
            self.setheading(random.randint(0,360))
class Ally(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            self.speed = 8
            self.setheading(random.randint(0,360))
    def move(self):
          self.fd(self.speed)
          if self.xcor() > 290 :
                 self.lt(60)
                 self.setx(290)

          if self.xcor() < -290 :
                 self.lt(60)
                 self.setx(-290)

          if self.ycor() > 290 :
                 self.lt(60)
                 self.sety(290)

          if self.ycor() < -290 :
                 self.lt(60)
                 self.sety(-290)
class Missle(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            self.shapesize(stretch_wid= 0.2,stretch_len= 0.4,outline=None)
            self.speed = 20
            self.goto(1000,-1000)
            self.status = "ready"
    def fire(self):
          if self.status == "ready":
                 sound = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\lazer.mp3")
                 sound.play()
                 self.goto(player.xcor(),player.ycor())
                 self.setheading(player.heading())
                 self.status = "firing"

    def move(self):
         if self.status == "firing":
               self.fd(self.speed)
         if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or \
                self.ycor() > 290:
                self.goto(-1000,1000)
                self.status = "ready"
         if self.status == "ready":
               self.goto(-1000,1000)
    def is_collision(self,other):
           if (self.xcor() >= (other.xcor() - 20))and \
           (self.xcor() <= (other.xcor() + 20))and \
           (self.ycor() >= (other.ycor() - 20))and \
           (self.ycor() <= (other.ycor() + 20)):
              return True
           else:
              return False
class Game():
       def __init__(self):
              self.level = 1
              self.score = 0
              self.state = "playing"
              self.pen = turtle.Turtle()
              self.lives = 10
       def draw_border(self):
              self.pen.speed(0)
              self.pen.color("white")
              self.pen.pensize(3)
              self.pen.penup()
              self.pen.goto(-300,300)
              self.pen.pendown()
              for side in range(4):
                     self.pen.fd(600)
                     self.pen.rt(90)
              self.pen.penup()
              self.pen.ht()
              self.pen.pendown()
       def show_status(self):
             self.pen.undo()
             msg = "Score:%s"%(self.score)
             self.pen.penup()
             self.pen.goto(-300,300)
             self.pen.write(msg, font= ("Arial",16,"normal"))
             

class Partical(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            self.shapesize(stretch_wid= 0.1,stretch_len= 0.1,outline=None)
            self.goto(-1000,-1000)
            self.frame = 0
    def explode(self, startx, starty):
          self.goto(startx,starty)
          self.setheading(random.randint(0,360))
          self.frame = 1
    def move(self):
          if self.frame > 0:
              self.fd(10)
              self.frame += 1
          if self.frame > 15:
                self.frame = 0
                self.goto(-1000,-1000)

game = Game()
game.draw_border()
game.show_status()

# ally = Ally("square","blue",0,0)
player = Player("classic","white",0,0)
#enemy = Enemy("circle","red",-100,0)
missle = Missle("triangle","yellow",0,0)
enemies = []
allies = []
particales = []
for h in range(20):
      particales.append(Partical('circle',"orange",0,0))
for i in range(6):
      enemies.append(Enemy("circle","red",-100,0))
for j in range(6):
      allies.append(Ally("square","magenta",100,0)) 
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_left,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.deccelerate,"Down")
turtle.onkey(missle.fire,"space")
turtle.listen()

while True:
        time.sleep(0.05)
        turtle.update()
        player.move()
        missle.move()
        for enemy in enemies:
              enemy.move()
              if player.is_collision(enemy):
                     x = random.randint(-250,250)
                     y = random.randint(-250,250)
                     enemy.goto(x,y)
                     game.score -= 2
                     game.show_status()
                     game.lives -= 1
                     if game.lives < 1:
                           print('game over')
                           turtle.bye()
                     if game.lives < 1:
                           break
              if missle.is_collision(enemy):
                sound = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\explosion.mp3")
                sound.play()
                x = random.randint(-250,250)
                y = random.randint(-250,250)
                enemy.goto(x,y)
                missle.status = "ready"
                game.score += 2
                game.show_status()
                for partical in particales:
                      partical.explode(missle.xcor(),missle.ycor())
                if game.score > 9 :
                      po = []
                      for q in range(3):
                        enemies.append(Enemy("circle","red",-100,0))
                if game.score > 19 :
                      n = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 29 :
                      f = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score >  39:
                      p = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 49  :
                      l = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 59 :
                      o = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 69 :
                      k = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 79 :
                      b = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 89 :
                      e = []
                      for q in range(3):
                            enemies.append(Enemy("circle","red",-100,0))
                if game.score > 99:
                      turtle.bye
                      print("congradulations, you beat space war!!! so ")
               
                     
                          
                     
        for ally in allies:
              ally.move()
              if missle.is_collision(ally):
                x = random.randint(-250,250)
                y = random.randint(-250,250)
                ally.goto(x,y)
                missle.status = "ready"
                game.score -= 1
                game.show_status()
        for partical in particales:
              partical.move()
              
        if player.is_collision(enemy):
                x = random.randint(-250,250)
                y = random.randint(-250,250)
                enemy.goto(x,y)
                game.score -= 2
                game.show_status()
                game.lives -= 1
                if game.lives < 1:
                     
                     print('game over')
                     break
        if missle.is_collision(enemy):
                x = random.randint(-250,250)
                y = random.randint(-250,250)
                enemy.goto(x,y)
                missle.status = "ready"
                game.score += 10
                game.show_status()
        if missle.is_collision(ally):
                x = random.randint(-250,250)
                y = random.randint(-250,250)
                ally.goto(x,y)
                missle.status = "ready"
                game.score -= 1
                game.show_status()
#        if player.is_collision(ally) and player.speed > (4):
#              enemy.health = 10

       
       
#delay = input("press Enter to finish.")

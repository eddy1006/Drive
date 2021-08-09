import os
import pygame
import random 
from pygame.constants import KEYDOWN
from pygame.constants import KEYUP

pygame.init()
pygame.mixer.init()
screen_width = 600
screen_height = 600
fps = 60
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Drive")
pygame.display.update()

#defining colors for our bg
white = (255,255,255)  #(R,G,B) --> max value and min value are from 0 to 255
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
bgimg = pygame.image.load("street.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.image.load("street3.png")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()
bglis = [bgimg,bgimg2]
car = pygame.image.load("car1.png")
car = pygame.transform.scale(car, (60,120)).convert_alpha()
car2 = pygame.image.load("car2.png")
car2 = pygame.transform.scale(car2, (120,120)).convert_alpha()
car3 = pygame.image.load("car3.png")
car3 = pygame.transform.scale(car3, (60,120)).convert_alpha()
car4 = pygame.image.load("car4.png")
car4 = pygame.transform.scale(car4, (60,120)).convert_alpha()
car5 = pygame.image.load("car5.png")
car5 = pygame.transform.scale(car5, (60,120)).convert_alpha()
car6 = pygame.image.load("car6.png")
car6 = pygame.transform.scale(car6, (120,140)).convert_alpha()
car7 = pygame.image.load("car7.png")
car7 = pygame.transform.scale(car7, (120,120)).convert_alpha()
cars = [car2,car3,car4,car5,car6,car7]
explo = pygame.image.load("explosion.png")
explo = pygame.transform.scale(explo, (180,180)).convert_alpha()
font = pygame.font.SysFont("ROG FONTS", 20,True)
clock = pygame.time.Clock()

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_character(gameWindow,x,y):
    gameWindow.blit(car,(x,y))
class Cars:
    def __init__(self):
        self.x = random.randint(140,400)
        self.y = -20
        self.velocity = 5
        self.img = random.choice(cars)
    def plot_cars(self,gameWindow):
        gameWindow.blit(self.img,(self.x,self.y)) 
def opening_screen():
    exit_game = False
    i =0 
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        gameWindow.blit(bglis[i//8], (0, 0))
        i = (i+1)%16
        plot_character(gameWindow,270,440)
        text_screen("WELOCME! TO DRIVE",black,150,100)
        text_screen("PRESS ENTER! TO BEGIN",black,125,150)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()       
def gameloop():
    exit_game = False 
    game_over = False
    i=0
    pos_x = 270
    pos_y = 440
    velocity_x=0
    velocity_y =0
    score = 0
    right = False
    left = False
    up = False
    down = False
    explosion = False
    c1 = Cars()
    car_lis = [c1]
    while not exit_game:
        if game_over:
            gameWindow.blit(bgimg,(0,0))
            text_screen("Game Over!Press Enter to continue",red,12,200)
            text_screen("Your Score :"+str(score),green,200,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("Drive_music.mp3")
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = 5
                            right = True
                        if event.key == pygame.K_LEFT:
                            velocity_x = -5
                            left = True
                        if event.key == pygame.K_UP:
                            velocity_y = -5
                            up = True
                        if event.key == pygame.K_DOWN:
                            velocity_y = 5
                            down = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            velocity_x =0
                            right = False
                        if event.key == pygame.K_LEFT:
                            velocity_x = 0
                            left = False
                        if event.key == pygame.K_UP:
                            velocity_y = 0
                            up= False
                        if event.key == pygame.K_DOWN:
                            velocity_y = 0
                            down=False
            if(pos_x<400 and pos_x>140):                
                pos_x += velocity_x
            if(pos_x==400 and left == True):
                pos_x += velocity_x
            elif(pos_x==140 and right==True):
                pos_x += velocity_x
            if(pos_y<470 and pos_y>20):
                pos_y += velocity_y
            if(pos_y==470 and up==True):
                pos_y += velocity_y
            elif(pos_y==20 and down==True):
                pos_y += velocity_y
            for j in car_lis:
                j.y += j.velocity
            for k in car_lis:
                if (k.y>300 and k.y<310):
                    cc = Cars()
                    car_lis.append(cc)
                    break
            if(len(car_lis)>5):
                del(car_lis[0])
            for coll in car_lis:
                if abs(coll.x-pos_x)<40 and abs(coll.y-pos_y)<90:
                    coll_x = pos_x + (coll.x-pos_x)
                    coll_y = pos_y + (coll.y-pos_y)
                    game_over = True
                    explosion = True
                    pygame.mixer.music.load("EXPLOSION 2.mp3")
                    pygame.mixer.music.play()
                    break
            gameWindow.blit(bglis[i//8], (0, 0))
            i = (i+1)%16
            for w in car_lis:
                w.plot_cars(gameWindow)
                if w.y - pos_y == 0:
                    score += 1
            plot_character(gameWindow,pos_x,pos_y)
            text_screen("Score:"+str(score),red,225,40)
            if explosion==True:
                gameWindow.blit(explo,(coll_x,coll_y))

        pygame.display.update()   #always update your window after making changes in it
        clock.tick(fps)
    pygame.quit()
    quit()
pygame.mixer.music.load("Drive_music.mp3")
pygame.mixer.music.play()
opening_screen()
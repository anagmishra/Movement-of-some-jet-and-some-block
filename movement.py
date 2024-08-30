import random
import pgzrun
import pygame
import itertools
HEIGHT=500
WIDTH=500
block=Actor("gear")
blockpositions=[(450, 50),(450, 450),(50, 450),(50, 50)]
blockposition=itertools.cycle(blockpositions) #ALLOWING YOU TO MOVE FROM ONE POSITION TO ANOTHER
jet=Actor("jet")
def draw():
    screen.clear()
    block.draw()
    jet.draw()

def moveblock():
    animate(block, "bounce_end", duration=1, pos=next(blockposition)) #Blockposition helps to decide where the block should go next

def callname():
    print("Anag")

def movejet():
    x=random.randint(15, 485)
    y=random.randint(15, 485)
    jet.target=x, y #Gives the x and y coordinates to the taget where the jet needs to go to
    target_angle=jet.angle_to(jet.target) #We are finding the angle at which the jet should rotate and move into
    target_angle+=360*((jet.angle-target_angle+180)//360) #It is supoosed to move at the typed angle within 0.003 seconds, and the move_ship function should get activated
    animate(jet, angle=target_angle, duration=0.003, on_finished=move_ship)

def move_ship():
    animate(jet, tween="accel_decel", pos=jet.target, duration=jet.distance_to(jet.target)/1000, on_finished=movejet) #We are forming a loop between movejet and moveship. When one function's task is done, we are calling the other function to do its task

clock.schedule_interval(callname, 10) #It continuously, and forever makes the typed function perform and the typed duration after which the typed function will repeat
moveblock()
movejet()

pgzrun.go()
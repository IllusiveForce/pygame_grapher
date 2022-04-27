#Graphing calculator. Change f(x) to change equation.



import pygame as pg
from pygame.locals import *
import math,sys
pg.init()
gameDisplay=pg.display.set_mode((600,600))


scale=20
def f(i):
  f=math.tan(i/scale)
  return f

x=0
x2=0
ctr=0
gameDisplay.fill((255,255,255))
while True:
 pg.draw.rect(gameDisplay,(170,170,170),Rect(300,0,2,600))
 pg.draw.rect(gameDisplay,(170,170,170),Rect(0,300,600,2))
 
 pg.draw.rect(gameDisplay,(220,220,220),Rect(ctr*100,0,2,600))
 pg.draw.rect(gameDisplay,(220,220,220),Rect(0,ctr*100,600,2))
 for event in pg.event.get():
  if event.type==pg.QUIT:
    pg.quit()
    sys.exit()

 try:
  pg.draw.rect(gameDisplay,(200,0,0),pg.Rect(x+300,f(x)*scale*-1+300,1,1))
  pg.draw.rect(gameDisplay,(200,0,0),pg.Rect(x2+300,f(x2)*scale*-1+300,1,1))
 except:
  pg.draw.rect(gameDisplay,(200,0,0),pg.Rect(x2+300,8754,2,2))
 x+=0.01
 x2-=0.01

 ctr+=scale/100
 pg.display.update()

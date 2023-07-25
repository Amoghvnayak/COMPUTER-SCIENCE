import  pygame
from pygame.sprite import Sprite

class Bullet(sprite):
  '''class to manage bullets fired from ship'''
  def __init__(self,ai_game):
    '''create bullet at ships current pos'''
  super().__init__()
  self.screen=ai_game.screen
  self.settings=ai_game.settings
  self.color=self.settings.bulllet_color


  #creating a bullet rect at(0,0) and set correct pos
  self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
  self.rect.midtop=ai_game.ship.rect.midtop
  #store bullets location
  self.y=float(self.rect.y)

  def update(self):
    '''move bullet up the screen'''
    #update the decimal position of the bullet
    self.y -=self.settings.bullet_speed
    #update rect position
  
    self.rect.y=self.y

  def draw_bullet(self):
    '''draw bullet to the screen'''
    pygame.draw.rect(self.screen,self.color,self.rect)
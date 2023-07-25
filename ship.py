import pygame
class Ship:
  '''a class to manage the ship'''
  def __init__(self,ai_game):
    '''initialise a ship and its starting position'''
    self.screen=ai_game.screen
    self.screen_rect=ai_game.screen.get_rect()

    #load the ship image  and get its rect
    self.image=pygame.image.load('images/ship.bmp')
    self.rect=self.image.get_rect()
    #start each new ship at bottom centre of screen.
    self.rect.midbottom=self.screen_rect.midbottom

  def blitme(self):
    '''draw the ship at its current location'''
    self.screen.blit(self.image,self.rect)
    
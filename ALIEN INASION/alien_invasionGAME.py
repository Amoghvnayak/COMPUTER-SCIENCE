import sys

import pygame

from settings import Settings

from ship import Ship

class alieninvasion:
  '''overall class to manage game behaviour'''
  def __init__(self):
    '''initialise the game,and create game resources'''
    pygame.init()
    self.settings=Settings()
    

    self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
    pygame.display.set_caption("my alien game")
    self.bg_color = (230,230,230)
    

  def run_game(self):
    '''start the main loop for the game'''
    while True:
      #watch for keyboard and mouse events
      self._check_events()
      self._update_screen
      
  def _update_screen(self) :
    
      #redraw screen each pass through the loop
      self.screen.fill(self.bg_color)
      self.ship.blitme()
      
      #make the mos recent screen visible
      pygame.display.flip()

  def _check_events(self):
    '''respond to keypresses'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          sys.exit()


if __name__== '__main__':
  #make a game instance,and run the game.
  ai=alieninvasion()
  ai.run_game
    

import sys
import pygame
class AlienInvasion:
         """Overall class to manage game assets and behavior."""
def __init__(self):
  """Initialize the game, and create game resources."""
  pygame.init() 
  self.screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Alien Invasion")
def run_game(self):
 """Start the main loop for the game."""
 while True:
 # Watch for keyboard and mouse events.
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        sys.exit()
 # Make the most recently drawn screen visible.
 pygame.display.flip()
if __name__ == '__main__':
 # Make a game instance, and run the game.
 ai = AlienInvasion()
 ai.run_game()
 def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
              #--snip--
def run_game(self):
 """Start the main loop for the game."""
 while True:
 #       --snip--
  pygame.display.flip()
 self.clock.tick(60)
def __init__(self):
      #--snip--
 pygame.display.set_caption("Alien Invasion")
 # Set the background color.
 self.bg_color = (230, 230, 230)
 def run_game(self):
       # --snip--
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      sys.exit()
 # Redraw the screen during each pass through the loop.
 self.screen.fill(self.bg_color)
 # Make the most recently drawn screen visible.
 pygame.display.flip()
 self.clock.tick(60)
 # --snip--
import pygame
from setting import Settings
class AlienInvasion:
         """Overall class to manage game assets and behavior."""
def __init__(self):
  """Initialize the game, and create game resources."""
  pygame.init()
  self.clock = pygame.time.Clock()
  self.settings = Settings()
  self.screen = pygame.display.set_mode(
 (self.settings.screen_width, self.settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
def run_game(self):
 #--snip--
 # Redraw the screen during each pass through the loop.
      self.screen.fill(self.settings.bg_color):
 # Make the most recently drawn screen visible.
pygame.display.flip() self.clock.tick(60)
 #--snip--
from setting import Settings
from ship import Ship
class AlienInvasion:
 """Overall class to manage game assets and behavior."""
 def __init__(self):
#  --snip--
  pygame.display.set_caption("Alien Invasion")
  self.ship = Ship(self)
def run_game(self):
#  --snip--
 # Redraw the screen during each pass through the loop.
 self.screen.fill(self.settings.bg_color)
 self.ship.blitme()
 # Make the most recently drawn screen visible.
pygame.display.flip()
self.clock.tick(60)
#--snip--
def run_game(self):
 """Start the main loop for the game."""
 while True:
   self._check_events()
 # Redraw the screen during each pass through the loop.
    #--snip--
def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     sys.exit()
     def run_game(self):
       """Start the main loop for the game."""
 while True:
   self._check_events()
   self._update_screen()
   self.clock.tick(60)
def _check_events(self):
#   --snip--
 def _update_screen(self):
  """Update images on the screen, and flip to the new screen."""
 self.screen.fill(self.settings.bg_color)
 self.ship.blitme()
pygame.display.flip()
def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     sys.exit()
   elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
 # Move the ship to the right.
     self.ship.rect.x += 1
     def _check_events(self):
      """Respond to keypresses and mouse events."""
for event in pygame.event.get():
         #   --snip--
 if event.type == pygame.KEYDOWN:
       self.ship.moving_right = True
if event.type == pygame.KEYUP:
  if event.key == pygame.K_RIGHT:
     self.ship.moving_right = False
def run_game(self):
      """Start the main loop for the game."""
      while True:self._check_events()
      self.ship.update()
      self._update_screen()
      self.clock.tick(60)
def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
      #--snip--
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
         self.ship.moving_right = True
      elif event.key == pygame.K_LEFT:
         self.ship.moving_left = True
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
          self.ship.moving_left = False
    def _check_events(self):
      """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      sys.exit()
     elif event.type == pygame.KEYDOWN:
      self._check_keydown_events(event)
     elif event.type == pygame.KEYUP:
       self._check_keyup_events(event)
def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
         self.ship.moving_left = True
         def _check_keyup_events(self, event):
           """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
       self.ship.moving_right = False
    if event.key == pygame.K_LEFT:
        self.ship.moving_left = False
def _check_keydown_events(self, event):
          #--snip--
    if event.key == pygame.K_LEFT:

     self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    def __init__(self):
       """Initialize the game, and create game resources."""
       pygame.init()
self.settings = Settings()
self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
self.settings.screen_width = self.screen.get_rect().width
self.settings.screen_height = self.screen.get_rect().height
pygame.display.set_caption("Alien Invasion")
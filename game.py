'''
Game:
Keep track of the player, score, levels
Start and Stop game
'''
import constants
import pygame
import level
from hero import Hero
from pygame.examples.headless_no_windows_needed import screen
from pygame.examples.oldalien import SCREENRECT



class Game():
    
    block_list = None
    sprites_list = None
    
    player_score = 0
    
    game_status = True
    
    
    
    def __init__(self):
        
        self.player_score = 0
        self.game_status = True
        
        self.block_list = pygame.sprite.Group()
        self.sprites_list = pygame.sprite.Group()
        
        self.hero = Hero()
        
        
        
        #receive list of blocks per level
        self.level_list = []
        self.level_list.append(level.Level01(self.hero))
        self.level_list.append(level.Level02(self.hero))
        
        self.current_level = 0
        self.current_level = self.level_list[self.current_level]
        
        self.hero.level = self.current_level 
        
        self.hero.x = 340
        self.hero.y = 200 #constants.SCREEN_HEIGHT - self.hero.height
        
        self.sprites_list.add(self.hero)
        
    def process_events(self):
        
        for event in pygame.event.get():
            if event.Type == pygame.QUIT:
                return False
            
            # list of all events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hero.move_left()
                if event.key == pygame.K_RIGHT:
                    self.hero.move_rigth()
                if event.key == pygame.K_UP:
                    self.hero.jump()
                    
            
        return True
    
    def update_game_state(self):
        
        if self.game_status:
            
            #update sprites position
            self.sprites_list.update()
            
            self.current_level.update()
            
            # check collision
            #blocks_collided = pygame.sprite.spritecollide(self.hero, self.block_list, True)
            
        
            self.current_level.draw(screen)
            self.sprites_list.draw(screen)
            

            #check it collision
            #for block in blocks_collided:
                
                
                
           # if len(self.block_list) == 0:
     
    def display_frame(self,screen):
        self.current_level.draw(screen)
        self.sprites_list.draw(screen)
        
        pygame.display.flip()
               
def main():
    
    pygame.init()
    
    screen_dimension = [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(screen_dimension)
    
    pygame.display.set_caption("Platybus")
    pygame.mouse.set_visible(False)
    
    clock = pygame.time.Clock()
    game_loop = True
    
    game = Game()
    
    while game_loop:
        
        game_loop = game.process_events()
        
        game.update_game_state()
        
        game.display_frame(screen)
        
        clock.tick(30)
        
    pygame.QUIT
        
        
        
            
if __name__ == "__main__":
    main()
     
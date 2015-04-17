import constants
import pygame
from platform import *
from hero import *
from pygame.examples.headless_no_windows_needed import screen

class Level():

    def __init__(self,hero):
        
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        
        self.hero = hero
        
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        
    def draw_level(self,screen):
        
        screen.fill(constants.WHITE)
        
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        
class Level01(Level):
    
    def __init__(self,hero):
        
        Level.__init__(self, hero)
        
        level = [
                 [210,70,250,250],
                 [210,70,500,300],
                 [210,70,430,90]
                 ]
        
        for platform in level:
            block = Platform(platform[0],platform[1]) 
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.hero = self.hero
            self.platform_list.add(block)
            
class Level02(Level):
    
    def __init__(self,hero):
        
        Level.__init__(self, hero)
        
        level = [
                 [210,70,250,250],
                 [210,70,500,300],
                 [210,70,430,90]
                 ]
        
        for platform in level:
            block = Platform(platform[0],platform[1]) 
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.hero = self.hero
            self.platform_list.add(block)
            
            
    
    
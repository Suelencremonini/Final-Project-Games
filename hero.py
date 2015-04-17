import constants
import pygame


class Hero(pygame.sprite.Sprite):
    
    
    def __inin__(self):
        
        super(Hero,self).__init__()
    
        self.width = 50
        self.height = 50
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(constants.BLUE)
        
        self.rect = self.image.get_rect()
        
        self.x = 0
        self.y = 0
        
        self.level = None
        
    def update(self):
        
        self.apply_gravity()
        
        self.rect.x += self.x
        
        block_list_collided = pygame.sprite.spritecollideany(self, self.level.platform_list,False)
        
        for block in block_list_collided:
            
            if self.x > 0:
                self.rect.right = block.rect.left
            elif self.x < 0:
                self.rect.left = block.rect.right
                
        self.rect.y += self.y
        
        block_list_collided = pygame.sprite.spritecollideany(self, self.level.platform_list,False)
        
        for block in block_list_collided:
            
            if self.y > 0:
                self.rect.right = block.rect.top
            elif self.y < 0:
                self.rect.left = block.rect.bottom
        
            self.y = 0
            
    def apply_gravity(self):
        
        if self.y == 0:
            self.y = 1
        else:
            self.y += .40
            
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.y >= 0:
            self.y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            
    
    def jump(self):
        
        self.rect.y += 2
        platform_list_collided = pygame.sprite.spritecollide(self, self.level.platform, False)
        self.rect.y -= 2
        
        if len(platform_list_collided) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.y = -10
            
    def move_left(self):
        self.x = -6
    
    def move_right(self):
        self.x = 6
        

        
    
        
    
    
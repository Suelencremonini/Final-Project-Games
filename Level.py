import pygame

class Level(pygame.sprite.Sprite):
	def __init__(self):
		list_sprites_scenery = pygame.sprite.Group()
		list_sprites_hero = pygame.sprite.Group()

    def update(self):
    	list_sprites_hero.update()
    	list_sprites_scenery.update()

    def drawScenery(self, screen):
    	self.list_sprites_scenery.draw(screen)
    	self.list_sprites_hero.draw(screen)

    def changeScenery(self, speed):
    	self.list_sprites_scenery.remove(list_sprites_scenery[0])
    	#adlfjasldfihçoadfugads@@@@@@@ fuuuuuuuuuu!


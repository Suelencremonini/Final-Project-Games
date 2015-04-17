import pygame

class Sprites():
	def __init__ (self, file):										#get the file
		self.file = pygame.image.load(file)
    	file.convert()

    def getImage(self, x, y, width, height, color):					#get the images from the file
    	image = pygame.Surface(ẃidth, height)						#create a new image object and cleared it to black
    	image.convert()
    	image.blit(self.file, (0, 0), (x, y, width, height))		#copy a portion (x, y, width, heigth) of file into the position (0,0) of image
    	image.set_colorkey(Colors.color)							#when drawing this image, the bits with color 'color' will be considered transparent
    	return image	

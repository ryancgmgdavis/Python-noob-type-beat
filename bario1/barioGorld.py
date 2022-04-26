import pygame
from pygame.locals import *
from barioLevels import *
from barioTac import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


#define game variables
tile_size = 50

#load images

class Player():
	def __init__(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'images/player{num}.png')
			img_right = pygame.transform.scale(img_right, (P_WIDTH, P_HEIGHT))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0

	def update(self):
		dx = 0
		dy = 0
		walk_cooldown = 1

		#get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_UP] and self.jumped == False:
			self.vel_y = -P_SPEED * 3
			self.jumped = True
		if key[pygame.K_UP] == False:
			self.jumped = False
		if key[pygame.K_LEFT]:
			dx -= P_SPEED
			self.counter += 1
			self.direction = -1
		if key[pygame.K_RIGHT]:
			dx += P_SPEED
			self.counter += 1
			self.direction = 1
		if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
			self.counter = 0
			self.index = 0
			if self.direction == 1:
				self.image = self.images_right[self.index]
			if self.direction == -1:
				self.image = self.images_left[self.index]


		#handle animation
		if self.counter > walk_cooldown:
			self.counter = 0	
			self.index += 1
			if self.index >= len(self.images_right):
				self.index = 0
			if self.direction == 1:
				self.image = self.images_right[self.index]
			if self.direction == -1:
				self.image = self.images_left[self.index]


		#add gravity
		self.vel_y += 1
		if self.vel_y > P_SPEED * 2:
			self.vel_y = P_SPEED * 2
		dy += self.vel_y

		#check for collision
		for tile in world.tile_list:
			#check for collision in x direction
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			#check for collision in y direction
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below the ground i.e. jumping
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
				#check if above the ground i.e. falling
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0




		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
			dy = 0

		#draw player onto screen
		screen.blit(self.image, self.rect)




class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		grass_img = pygame.image.load('images/block.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					blockRect = BLOCK.get_rect()
					blockRect.x = col_count * TILESIZE
					blockRect.y = row_count * TILESIZE
					tile = (BLOCK, blockRect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])




player = Player(TILESIZE * 2, HEIGHT - P_HEIGHT - TILESIZE)
world = World(level1)

run = True
while run:
	clock.tick(FPS)
	screen.blit(BGIMG, (0, 0))
	world.draw()
	player.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()
pygame.quit()
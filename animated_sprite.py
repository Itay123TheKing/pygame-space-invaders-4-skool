import pygame

class AnimatedSprite(pygame.sprite.Sprite):
	def __init__(self, sprite_sheet, colourkey, width, height, frame_count, fps, scale = 1, *groups):
		super().__init__(*groups)
		
		self.frame_count = frame_count
		self.current_frame = 0
		self.frames = [pygame.Surface((width, height)).convert_alpha() for i in range(frame_count)]
		for i in range(frame_count):
			self.frames[i].blit(sprite_sheet, (0, 0), (i * width, 0, width, height)) 

		if scale != 1:
			self.frames = [pygame.transform.scale(frame, (width * scale, height * scale)) 
				for frame in self.frames]

		for frame in self.frames:
			frame.set_colorkey(colourkey)
		
		self.image = self.frames[self.current_frame]
		self.rect = self.image.get_rect()
		self.fps = fps
		self.last_tick = pygame.time.get_ticks()

	def next_frame(self):
		self.current_frame += 1
		if self.current_frame >= self.frame_count:
			self.current_frame = 0
		self.image = self.frames[self.current_frame]

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_tick > 1000 / self.fps:
			self.next_frame()
			self.last_tick = now
	
	def draw(self, surface, x, y):
		surface.blit(self.image, (x, y))
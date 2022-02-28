from ctypes import Union
from typing import Literal, List
import pygame
import colorsys

class AlphaLayer:
	def __init__(self, output: pygame.Surface) -> None:
		self.output = output
		self.screen = pygame.Surface(output.get_size(), pygame.SRCALPHA)
		self.binded: List[self._Binded] = []

	def render(self, surface: pygame.Surface, pos: Tuple[int, int], solidColour: Union[pygame._common._ColorValue, Literal[False]] = (0, 0, 0)) -> None:
		if solidColour:
			self.screen.blit(pygame.mask.from_surface(surface).to_surface(setcolor=solidColour), (x, y))
		else:
			self.screen.blit(b.img(), b.pos())

	 
	def render_all_binded(self):
		self.screen.fill((255, 255, 255, 220), special_flags=pygame.BLEND_RGBA_MULT)
		for b in self.binded:
			if b.rotateHue:


	
	@staticmethod
	def __hue_to_rgb(h):
		return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h / 255, 1, 1))

	class __Binded:
		def __init__(self, obj: any, colour: pygame._common._ColorValue, rotateHue: bool = False, useOriginalColour: bool = False) -> None:
			self.obj = obj
			self.colour = colour
			self.rotateHue = rotateHue
			self.useOriginalColour = useOriginalColour
			self.hue, self.saturation, self.value = colorsys.rgb_to_hsv(*(i / 255 for i in self.colour))
		
		def pos(self):
			return self.rect.topleft
		
		def img(self):
			return self.obj.image

		def update_hue(self):
			self.hue += 1
			if self.hue > 255:
				self.hue = 0
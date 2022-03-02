from typing import Literal, Tuple, Union, List
from enum import Enum
from numpy import isin
import pygame
import colorsys

class flags(Enum):
	NONE            = 0
	NO_SOLID_COLOUR = 1 << 0
	HUE_SHIFT       = 1 << 1

class AlphaLayer:
	def __init__(self, output: pygame.Surface) -> None:
		self.output = output
		self.screen = pygame.Surface(output.get_size(), pygame.SRCALPHA)
		self.binded: List[self.__Binded] = []

	def render(self, surface: pygame.Surface, pos: Tuple[int, int], solid_colour) -> None:
		if solid_colour:
			solid = pygame.mask.from_surface(surface).to_surface(setcolor=solid_colour)
			solid.convert_alpha()
			solid.set_colorkey((0, 0, 0))
			self.screen.blit(solid, pos)
		else:
			self.screen.blit(surface, pos)
	 
	def render_all_binded(self) -> None:
		for b in self.binded:
			if b.hue_shift:
				b.update_hue()
			if b.no_solid_colour:
				self.render(b.img(), b.pos(), False)
			else:
				self.render(b.img(), b.pos(), b.colour)
			
		self.screen.fill((255, 255, 255, 220), special_flags=pygame.BLEND_RGBA_MULT)

	def draw(self) -> None:
		self.output.blit(self.screen, (0, 0))

	def bind(self, spr: Union[pygame.sprite.Sprite, pygame.sprite.Group], colour, special_flags: flags = flags.NONE) -> None:
		if isinstance(spr, pygame.sprite.Sprite):
			if special_flags.value & flags.NO_SOLID_COLOUR.value:
				self.binded.append(self.__Binded(spr, colour, False, True))
			elif special_flags.value & flags.HUE_SHIFT.value:
				self.binded.append(self.__Binded(spr, colour, True, False))
			else:
				self.binded.append(self.__Binded(spr, colour, False, False))
		elif isinstance(spr, pygame.sprite.Group):
			for s in spr:
				if special_flags.value & flags.NO_SOLID_COLOUR.value:
					self.binded.append(self.__Binded(s, colour, False, True))
				elif special_flags.value & flags.HUE_SHIFT.value:
					self.binded.append(self.__Binded(s, colour, True, False))
				else:
					self.binded.append(self.__Binded(s, colour, False, False))
		else:
			raise TypeError("spr must be a pygame.sprite.Sprite or pygame.sprite.Group")

	class __Binded:
		def __init__(self, spr: pygame.sprite.Sprite, colour, hue_shift: bool = False, no_solid_colour: bool = False) -> None:
			self.spr = spr
			self.colour = colour
			self.hue_shift = hue_shift
			self.no_solid_colour = no_solid_colour
			self.hue, self.saturation, self.value = colorsys.rgb_to_hsv(*(i / 255 for i in self.colour))
			self.hue = (self.hue * 255) // 1 
			
		def pos(self) -> None:
			return self.spr.rect.topleft
		
		def img(self) -> None:
			return self.spr.image

		def update_hue(self) -> None:
			if self.hue_shift:
				self.hue += 1
				if self.hue > 255:
					self.hue = 0
				self.colour = (i * 255 for i in colorsys.hsv_to_rgb(self.hue / 255, self.saturation, self.value))
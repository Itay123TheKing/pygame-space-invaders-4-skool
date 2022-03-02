import json
import os
from typing import Dict, List
from constants import *
from pygame import font, time

from player import Player

class Scores:
	def __init__(self, path: str, player: Player, clock: time.Clock) -> None:
		self.path = path
		self.score_list: List[Dict] = []
		self.highscore: int = 0
		self.player = player
		self.clock = clock
		self.text_font = font.Font("assets/font/prstart.ttf", 16)
		self.time_passed = 0

	def load(self) -> None:
		fix_JSON = lambda: json.dump({"scores": []}, open(self.path, "w"), indent="\t")

		if os.path.exists(self.path):
			with open(self.path, "r") as file:
				try:
					json_object: dict = json.load(file)
					if json_object.get('scores'):
						self.score_list = json_object['scores']
					else:
						# If scores isn't in the json, fix the file
						fix_JSON()
				except json.JSONDecodeError:
					# If file is empty for some reason, fix the file
					fix_JSON()
		else:
			# if file does not exist, create it and write empty scores
			fix_JSON()

		# Sort the scores
		self.score_list.sort(key=lambda n: n['score'], reverse=True)
		self.highscore = self.score_list[0]['score']

	
	def save(self) -> None:
		with open(self.path, "w") as file:
			json.dump({"scores": self.score_list}, file, indent="\t")

	def add(self, name: str, score: int) -> None:
		self.score_list.append({
			"name": name,
			"score": score
		})

	def update(self, dt: float) -> None:
		if self.player.score > self.highscore:
			self.highscore = self.player.score

		if time_passed > 1: # 1 second
			self.player.addScore(1)
			time_passed = 0

		time_passed += dt		

		

	def draw(self, screen: pygame.Surface) -> None:
		score_text = self.text_font.render(f"SCORE", True, (255, 255, 255))
		score_value = self.text_font.render(f"{self.player.score:04}", True, (255, 255, 255))

		highscore_text = self.text_font.render(f"HI-SCORE", True, (255, 255, 255))
		highscore_value = self.text_font.render(f"{self.highscore:04}", True, (255, 255, 255))

		screen.blit(score_text, (10, 10))
		screen.blit(score_value, (10, 20 + score_text.get_rect().bottom))

		screen.blit(highscore_text, (SCREEN_WIDTH - highscore_text.get_rect().width - 10, 10))
		screen.blit(highscore_value, (SCREEN_WIDTH - highscore_value.get_rect().width - 10, 20 + highscore_text.get_rect().bottom))

		screen.blit(self.text_font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255)), (10, screen.get_height() - 25))

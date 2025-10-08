import os
import sys
import time
from typing import List

import numpy as np
import pygame

from src.models.entities.screen_stimuli import ScreenStimuli
from src.views.stimuli import Image, Sound, Text

os.environ["SDL_VIDEO_CENTERED"] = "1"


class ScreenView:
    def __init__(self):
        # configuração de abertura do pygame
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.x, self.y = self.screen.get_size()
        self.size = self.width, self.height = np.array([(self.x - 100), (self.y - 100)])

        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("PyMTS")

        # configuração da tela
        self.screen_color = None
        self.screen_type = None
        self.images_pos = None
        self.images_size = None
        self.images = None
        self.is_clickable = None
        self.sounds = None
        self.texts = None
        self.time_right = None
        self.time_wrong = None

    def _images(self, images) -> List[Image]:

        if not images[0] == "":
            imgs = [
                Image(
                    self.screen,
                    images[i],
                    self.images_size,
                    self.images_pos[i],
                    self.is_clickable[i],
                )
                for i in range(len(images))
            ]
            return imgs
        else:
            return False

    def update_info(self, screen_stimuli: ScreenStimuli, time):
        self.screen_color = screen_stimuli.screen_color
        self.screen_type = screen_stimuli.screen_type
        self.is_clickable = screen_stimuli.clickable
        self.images_pos = screen_stimuli.images_pos
        self.images_size = screen_stimuli.images_size
        self.images = self._images(screen_stimuli.images)
        self.sounds = screen_stimuli.sounds  # TODO
        self.texts = screen_stimuli.texts  # TODO
        self.time = time

    def get_time(self, start_time):
        return time.time() - start_time

    def run(self):
        self.screen.fill(self.screen_color)
        start_time = time.time()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.images:
                    for image in self.images:

                        if image.mouse_click(event) and image.mouse_hover():
                            return image.name, self.get_time(start_time)

                        elif self.time:
                            if self.get_time(start_time) >= self.time:
                                return image.name, self.get_time(start_time)
                else:
                    return None, None
            if self.images:
                for image in self.images:
                    image.update()
            pygame.display.update()

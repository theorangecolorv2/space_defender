import pygame

pygame.init()
ARIAL_50 = pygame.font.SysFont("Arial", 50)


class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
        self.image = pygame.image.load('graphics/menu.jpg')
        self.white = (255, 255, 255)
        self.black = (181,184,177)

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        if (0 <= self._current_option_index <= 1 and direction > 0) or (
                1 <= self._current_option_index <= 2 and direction < 0):
            self._current_option_index = max(0, min(self._current_option_index + direction,
                                                    len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, (0, 0, 120), option_rect)
            else:
                pygame.draw.rect(surf, (0, 0, 0), option_rect)
            surf.blit(option, option_rect)


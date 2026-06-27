import pygame
from settings import *

pygame.font.init()

font = pygame.font.SysFont("consolas", 22)

class HUD:

    def __init__(self):
        self.total_passed = 0

    def update(self, vehicles):
        self.total_passed += len([v for v in vehicles if v.cleared])

    def draw(self, screen, fps, phase, vehicles):

        horizontal = len([v for v in vehicles if v.direction in ("E", "W")])
        vertical = len([v for v in vehicles if v.direction in ("N", "S")])

        avg_wait = 0
        if vehicles:
            avg_wait = sum(v.wait_time for v in vehicles) / len(vehicles)

        pygame.draw.rect(screen, (20, 20, 20), (10, 10, 320, 200))
        pygame.draw.rect(screen, WHITE, (10, 10, 320, 200), 2)

        texts = [
            f"FPS: {int(fps)}",
            f"Signal: {phase}",
            f"Horizontal Queue: {horizontal}",
            f"Vertical Queue: {vertical}",
            f"Vehicles: {len(vehicles)}",
            f"Passed: {self.total_passed}",
            f"Average Wait: {avg_wait:.1f}"
        ]

        y = 20
        for text in texts:
            img = font.render(text, True, WHITE)
            screen.blit(img, (20, y))
            y += 25
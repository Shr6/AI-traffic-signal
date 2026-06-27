import pygame
import random

from settings import *


class Vehicle:

    def __init__(self, direction, vehicle_type="CAR"):

        self.direction = direction
        self.vehicle_type = vehicle_type

        # ---------------- Vehicle Properties ----------------

        if vehicle_type == "CAR":
            self.length = CAR_LENGTH
            self.width = CAR_WIDTH
            self.speed = CAR_SPEED

        elif vehicle_type == "BUS":
            self.length = BUS_LENGTH
            self.width = BUS_WIDTH
            self.speed = BUS_SPEED

        else:
            self.length = TRUCK_LENGTH
            self.width = TRUCK_WIDTH
            self.speed = TRUCK_SPEED

        self.color = random.choice(VEHICLE_COLORS)

        self.wait_time = 0
        self.cleared = False

        # Once a vehicle crosses the stop line,
        # it ignores future signal changes until it exits.
        self.crossed_stop_line = False

        self.turn = random.choice(["STRAIGHT", "LEFT", "RIGHT"])

        # ---------------- Spawn Position ----------------

        if direction == "E":

            self.rect = pygame.Rect(
                -self.length,
                CENTER_Y + 25,
                self.length,
                self.width
            )

        elif direction == "W":

            self.rect = pygame.Rect(
                WIDTH + self.length,
                CENTER_Y - 55,
                self.length,
                self.width
            )

        elif direction == "N":

            self.rect = pygame.Rect(
                CENTER_X - 55,
                -self.length,
                self.width,
                self.length
            )

        else:   # South

            self.rect = pygame.Rect(
                CENTER_X + 25,
                HEIGHT + self.length,
                self.width,
                self.length
            )

    # ----------------------------------------------------

    def can_move(self, vehicles):

        nearest_gap = 999999

        for car in vehicles:

            if car == self:
                continue

            if car.direction != self.direction:
                continue

            if car.cleared:
                continue

            if self.direction == "E":

                gap = car.rect.left - self.rect.right

            elif self.direction == "W":

                gap = self.rect.left - car.rect.right

            elif self.direction == "N":

                gap = car.rect.top - self.rect.bottom

            else:

                gap = self.rect.top - car.rect.bottom

            if gap >= 0:
                nearest_gap = min(nearest_gap, gap)

        return nearest_gap >= SAFE_DISTANCE

    # ----------------------------------------------------

    def obey_signal(self, phase):

        # Already entered junction
        if self.crossed_stop_line:
            return True

        stop_left = CENTER_X - ROAD_WIDTH // 2 - STOP_DISTANCE
        stop_right = CENTER_X + ROAD_WIDTH // 2 + STOP_DISTANCE

        stop_top = CENTER_Y - ROAD_WIDTH // 2 - STOP_DISTANCE
        stop_bottom = CENTER_Y + ROAD_WIDTH // 2 + STOP_DISTANCE

        # ---------------- EAST ----------------

        if self.direction == "E":

            if self.rect.right + self.speed >= stop_left:

                if phase != "H_GREEN":
                    return False

                self.crossed_stop_line = True

        # ---------------- WEST ----------------

        elif self.direction == "W":

            if self.rect.left - self.speed <= stop_right:

                if phase != "H_GREEN":
                    return False

                self.crossed_stop_line = True

        # ---------------- NORTH ----------------

        elif self.direction == "N":

            if self.rect.bottom + self.speed >= stop_top:

                if phase != "V_GREEN":
                    return False

                self.crossed_stop_line = True

        # ---------------- SOUTH ----------------

        else:

            if self.rect.top - self.speed <= stop_bottom:

                if phase != "V_GREEN":
                    return False

                self.crossed_stop_line = True

        return True

    # ----------------------------------------------------

    def move(self):

        if self.direction == "E":

            self.rect.x += self.speed

        elif self.direction == "W":

            self.rect.x -= self.speed

        elif self.direction == "N":

            self.rect.y += self.speed

        else:

            self.rect.y -= self.speed

    # ----------------------------------------------------

    def update(self, vehicles, phase):

        if self.cleared:
            return

        if self.can_move(vehicles):

            if self.obey_signal(phase):

                self.move()

            else:

                self.wait_time += 1

        else:

            self.wait_time += 1

        # ---------------- Remove ----------------

        if self.direction == "E":

            if self.rect.left > WIDTH:
                self.cleared = True

        elif self.direction == "W":

            if self.rect.right < 0:
                self.cleared = True

        elif self.direction == "N":

            if self.rect.top > HEIGHT:
                self.cleared = True

        else:

            if self.rect.bottom < 0:
                self.cleared = True

    # ----------------------------------------------------

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=5
        )

        pygame.draw.rect(
            screen,
            BLACK,
            self.rect,
            2,
            border_radius=5
        )

        # Windshield

        if self.direction in ("E", "W"):

            pygame.draw.rect(
                screen,
                (180, 220, 255),
                (
                    self.rect.x + 6,
                    self.rect.y + 3,
                    self.rect.width - 12,
                    self.rect.height - 6,
                ),
            )

        else:

            pygame.draw.rect(
                screen,
                (180, 220, 255),
                (
                    self.rect.x + 3,
                    self.rect.y + 6,
                    self.rect.width - 6,
                    self.rect.height - 12,
                ),
            )
import random
from vehicle import Vehicle

VEHICLE_TYPES = [
    "CAR",
    "CAR",
    "CAR",
    "CAR",
    "BUS",
    "TRUCK"
]

DIRECTIONS = [
    "N",
    "S",
    "E",
    "W"
]


class VehicleSpawner:

    def __init__(self):

        self.spawn_probability = 0.025

    def update(self, vehicles):

        if random.random() > self.spawn_probability:
            return

        direction = random.choice(DIRECTIONS)

        vehicle_type = random.choice(VEHICLE_TYPES)

        # Prevent spawning if another vehicle is too close
        for vehicle in vehicles:

            if vehicle.direction != direction:
                continue

            if direction == "E" and vehicle.rect.x < 120:
                return

            elif direction == "W" and vehicle.rect.right > 1080:
                return

            elif direction == "N" and vehicle.rect.y < 120:
                return

            elif direction == "S" and vehicle.rect.bottom > 680:
                return

        vehicles.append(
            Vehicle(direction, vehicle_type)
        )
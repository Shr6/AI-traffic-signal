import pygame
import sys

from settings import *
from vehicle import Vehicle
from controller import AdaptiveController
from traffic_light import TrafficLight
from road import draw_roads
from junction import draw_junction
from spawner import VehicleSpawner
from hud import HUD


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Traffic Simulator")

clock = pygame.time.Clock()

# -----------------------
# Objects
# -----------------------

controller = AdaptiveController()

spawner = VehicleSpawner()

hud = HUD()

cars = []

lights = [

    # Light 1 – West approach (vehicles travelling East)
    TrafficLight(
        CENTER_X - ROAD_WIDTH//2 - 60,
        CENTER_Y - ROAD_WIDTH//2 - 110,
        light_id=1,
        lane="E"
    ),

    # Light 2 – East approach (vehicles travelling West)
    TrafficLight(
        CENTER_X + ROAD_WIDTH//2 + 25,
        CENTER_Y + ROAD_WIDTH//2 + 20,
        light_id=2,
        lane="W"
    ),

    # Light 3 – South lane
    TrafficLight(
        CENTER_X + ROAD_WIDTH//2 + 25,
        CENTER_Y - ROAD_WIDTH//2 - 110,
        light_id=3,
        lane="N"
    ),

    # Light 4 – South lane
    TrafficLight(
        CENTER_X - ROAD_WIDTH//2 - 60,
        CENTER_Y + ROAD_WIDTH//2 + 20,
        light_id=4,
        lane="S"
    ),

]

running = True

# -----------------------
# Main Loop
# -----------------------

while running:

    clock.tick(FPS)

    # -----------------------
    # Events
    # -----------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # -----------------------
    # Spawn Vehicles
    # -----------------------

    spawner.update(cars)

    # -----------------------
    # Calculate Queues
    # -----------------------

    horizontal = [

        v

        for v in cars

        if v.direction in ("E","W")

    ]

    vertical = [

        v

        for v in cars

        if v.direction in ("N","S")

    ]

    phase = controller.update(

        len(horizontal),

        [v.wait_time for v in horizontal],

        len(vertical),

        [v.wait_time for v in vertical]

    )

    # -----------------------
    # Update Vehicles
    # -----------------------

    for vehicle in cars:

        vehicle.update(

            cars,

            phase

        )

    # -----------------------
    # Statistics
    # -----------------------

    hud.update(cars)

    cars = [

        c

        for c in cars

        if not c.cleared

    ]

    # -----------------------
    # Draw World
    # -----------------------

    draw_roads(screen)

    draw_junction(screen)

    for light in lights:

        light.draw(

            screen,

            phase

        )

    for vehicle in cars:

        vehicle.draw(screen)

    hud.draw(

        screen,

        clock.get_fps(),

        phase,

        cars

    )

    pygame.display.flip()

pygame.quit()

sys.exit()
import pygame
from settings import *

# --------------------------
# Draw Dashed Lane
# --------------------------

def draw_dashed_line(screen, start, end, vertical=False):

    dash = 25
    gap = 15

    if vertical:

        y = start

        while y < end:

            pygame.draw.rect(
                screen,
                WHITE,
                (
                    CENTER_X-2,
                    y,
                    4,
                    dash
                )
            )

            y += dash + gap

    else:

        x = start

        while x < end:

            pygame.draw.rect(
                screen,
                WHITE,
                (
                    x,
                    CENTER_Y-2,
                    dash,
                    4
                )
            )

            x += dash + gap


# --------------------------
# Zebra Crossing
# --------------------------

def zebra_horizontal(screen, y):

    x = CENTER_X - ROAD_WIDTH//2

    for i in range(12):

        pygame.draw.rect(

            screen,

            WHITE,

            (
                x+i*15,
                y,
                10,
                40
            )

        )


def zebra_vertical(screen, x):

    y = CENTER_Y - ROAD_WIDTH//2

    for i in range(12):

        pygame.draw.rect(

            screen,

            WHITE,

            (
                x,
                y+i*15,
                40,
                10
            )

        )


# --------------------------
# Stop Lines
# --------------------------

def stop_lines(screen):

    pygame.draw.line(
        screen,
        WHITE,
        (
            CENTER_X-ROAD_WIDTH//2-5,
            CENTER_Y-ROAD_WIDTH//2
        ),
        (
            CENTER_X-ROAD_WIDTH//2-5,
            CENTER_Y+ROAD_WIDTH//2
        ),
        5
    )

    pygame.draw.line(
        screen,
        WHITE,
        (
            CENTER_X+ROAD_WIDTH//2+5,
            CENTER_Y-ROAD_WIDTH//2
        ),
        (
            CENTER_X+ROAD_WIDTH//2+5,
            CENTER_Y+ROAD_WIDTH//2
        ),
        5
    )

    pygame.draw.line(
        screen,
        WHITE,
        (
            CENTER_X-ROAD_WIDTH//2,
            CENTER_Y-ROAD_WIDTH//2-5
        ),
        (
            CENTER_X+ROAD_WIDTH//2,
            CENTER_Y-ROAD_WIDTH//2-5
        ),
        5
    )

    pygame.draw.line(
        screen,
        WHITE,
        (
            CENTER_X-ROAD_WIDTH//2,
            CENTER_Y+ROAD_WIDTH//2+5
        ),
        (
            CENTER_X+ROAD_WIDTH//2,
            CENTER_Y+ROAD_WIDTH//2+5
        ),
        5
    )


# --------------------------
# Roads
# --------------------------

def draw_roads(screen):

    screen.fill(GRASS)

    pygame.draw.rect(

        screen,

        ROAD,

        (
            0,
            CENTER_Y-ROAD_WIDTH//2,
            WIDTH,
            ROAD_WIDTH
        )

    )

    pygame.draw.rect(

        screen,

        ROAD,

        (
            CENTER_X-ROAD_WIDTH//2,
            0,
            ROAD_WIDTH,
            HEIGHT
        )

    )

    draw_dashed_line(
        screen,
        0,
        WIDTH,
        False
    )

    draw_dashed_line(
        screen,
        0,
        HEIGHT,
        True
    )

    zebra_horizontal(
        screen,
        CENTER_Y-ROAD_WIDTH//2-45
    )

    zebra_horizontal(
        screen,
        CENTER_Y+ROAD_WIDTH//2+5
    )

    zebra_vertical(
        screen,
        CENTER_X-ROAD_WIDTH//2-45
    )

    zebra_vertical(
        screen,
        CENTER_X+ROAD_WIDTH//2+5
    )

    stop_lines(screen)
import pygame
from settings import *

# -------------------------
# Junction Decoration
# -------------------------

def draw_junction(screen):

    # Central Box

    pygame.draw.rect(

        screen,

        (70,70,70),

        (

            CENTER_X-ROAD_WIDTH//2,

            CENTER_Y-ROAD_WIDTH//2,

            ROAD_WIDTH,

            ROAD_WIDTH

        )

    )

    # Border

    pygame.draw.rect(

        screen,

        LIGHT_GRAY,

        (

            CENTER_X-ROAD_WIDTH//2,

            CENTER_Y-ROAD_WIDTH//2,

            ROAD_WIDTH,

            ROAD_WIDTH

        ),

        3

    )

    # Yellow Grid

    gap = 20

    for i in range(0, ROAD_WIDTH, gap):

        pygame.draw.line(

            screen,

            YELLOW,

            (

                CENTER_X-ROAD_WIDTH//2+i,

                CENTER_Y-ROAD_WIDTH//2

            ),

            (

                CENTER_X-ROAD_WIDTH//2,

                CENTER_Y-ROAD_WIDTH//2+i

            ),

            2

        )

    for i in range(0, ROAD_WIDTH, gap):

        pygame.draw.line(

            screen,

            YELLOW,

            (

                CENTER_X+ROAD_WIDTH//2-i,

                CENTER_Y+ROAD_WIDTH//2

            ),

            (

                CENTER_X+ROAD_WIDTH//2,

                CENTER_Y+ROAD_WIDTH//2-i

            ),

            2

        )

    # Direction Arrows

    pygame.draw.polygon(

        screen,

        WHITE,

        [

            (CENTER_X-180,CENTER_Y-25),

            (CENTER_X-150,CENTER_Y),

            (CENTER_X-180,CENTER_Y+25)

        ]

    )

    pygame.draw.polygon(

        screen,

        WHITE,

        [

            (CENTER_X+180,CENTER_Y-25),

            (CENTER_X+210,CENTER_Y),

            (CENTER_X+180,CENTER_Y+25)

        ]

    )

    pygame.draw.polygon(

        screen,

        WHITE,

        [

            (CENTER_X-25,CENTER_Y-180),

            (CENTER_X,CENTER_Y-210),

            (CENTER_X+25,CENTER_Y-180)

        ]

    )

    pygame.draw.polygon(

        screen,

        WHITE,

        [

            (CENTER_X-25,CENTER_Y+180),

            (CENTER_X,CENTER_Y+210),

            (CENTER_X+25,CENTER_Y+180)

        ]

    )
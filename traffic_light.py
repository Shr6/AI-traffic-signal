import pygame

# Colors
RED    = (255, 0, 0)
YELLOW = (255, 215, 0)
GREEN  = (0, 255, 0)
OFF    = (60, 60, 60)
BLACK  = (30, 30, 30)
WHITE  = (255, 255, 255)

pygame.font.init()
_label_font = pygame.font.SysFont("consolas", 11, bold=True)


class TrafficLight:
    """
    A traffic light with an ID number and an assigned lane direction.

    Parameters
    ----------
    x, y        : top-left position on screen
    light_id    : integer label shown on the tag (1, 2, 3, 4 ...)
    lane        : the lane this light controls - one of "E", "W", "N", "S"
    """

    def __init__(self, x, y, light_id, lane):
        self.x        = x
        self.y        = y
        self.light_id = light_id
        self.lane     = lane

    # ------------------------------------------------------------------

    def draw(self, screen, phase):

        # Resolve phase -> per-direction colour for this light's lane
        states      = get_light_states(phase)
        light_state = states[self.lane]

        # Housing
        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, 34, 100),
            border_radius=6
        )

        red    = OFF
        yellow = OFF
        green  = OFF

        if light_state == "RED":
            red = RED
        elif light_state == "YELLOW":
            yellow = YELLOW
        elif light_state == "GREEN":
            green = GREEN

        cx = self.x + 17
        pygame.draw.circle(screen, red,    (cx, self.y + 16), 11)
        pygame.draw.circle(screen, yellow, (cx, self.y + 50), 11)
        pygame.draw.circle(screen, green,  (cx, self.y + 84), 11)

        # Pill tag below housing: e.g. "#1 S"
        label    = f"#{self.light_id} {self.lane}"
        tag_surf = _label_font.render(label, True, WHITE)
        tag_w    = tag_surf.get_width() + 10
        tag_h    = tag_surf.get_height() + 6
        tag_x    = self.x + (34 - tag_w) // 2
        tag_y    = self.y + 105

        pygame.draw.rect(screen, (40, 40, 40),    (tag_x, tag_y, tag_w, tag_h), border_radius=4)
        pygame.draw.rect(screen, (130, 130, 130), (tag_x, tag_y, tag_w, tag_h), 1, border_radius=4)
        screen.blit(tag_surf, (tag_x + 5, tag_y + 3))


# -----------------------------------------------------------------------

def get_light_states(phase):
    """Return the signal colour for every lane direction."""

    if phase == "H_GREEN":
        return {"E": "GREEN",  "W": "GREEN",  "N": "RED",    "S": "RED"}

    elif phase == "H_YELLOW":
        return {"E": "YELLOW", "W": "YELLOW", "N": "RED",    "S": "RED"}

    elif phase == "V_GREEN":
        return {"E": "RED",    "W": "RED",    "N": "GREEN",  "S": "GREEN"}

    elif phase == "V_YELLOW":
        return {"E": "RED",    "W": "RED",    "N": "YELLOW", "S": "YELLOW"}

    return {"E": "RED", "W": "RED", "N": "RED", "S": "RED"}
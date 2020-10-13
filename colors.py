from enum import Enum


class ColorRGB(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    LIME = (0, 255, 0)
    GRAY = (128, 128, 128)
    PURPLE = (128, 0, 128)
    BLUE = (0, 0, 255)
    MAGENTA = (255, 0, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 140, 0)

    def from_rgb(self):
        return "#%02x%02x%02x" % self.value

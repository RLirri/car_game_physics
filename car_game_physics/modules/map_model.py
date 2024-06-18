from pygame.math import Vector2
from modules.constants import *

""" Author: Ruixin """
""" Description: Map Class for Car Simulation """
class Map:
    def __init__(self, x, y):
        """Initialize the map with position, dimensions, and border size."""
        self.pos = Vector2(x, y)  # Position of the map
        self.dim = Vector2(MAP_WIDTH, MAP_HEIGHT)  # Dimensions of the map
        self.border = BORDER  # Border size around the map

    def update(self, dt, pos):
        """Update the position of the map based on the car's position."""
        self.pos.x = pos.x
        self.pos.y = pos.y
        # print("Map position:",self.pos)  # Debugging: Print the current position of the map

    def check_boundary(self, pos_valid, x, y, car):
        """Check if the car is within the boundaries of the map."""
        if x >= car["pos"].x + self.get_dim().x - car["length"] - self.get_border():
            pos_valid[0] = False
        if x <= car["pos"].x + self.get_border():
            pos_valid[0] = False

        # TODO: Change length and width parameters based on car orientation
        if y >= car["pos"].y + self.get_dim().y - car["length"] - self.get_border():
            pos_valid[1] = False
        if y <= car["pos"].y + self.get_border():
            pos_valid[1] = False

        return pos_valid

    @staticmethod
    def check_terrain(x, y, position):
        """Check the terrain type (road or grass) at the given position."""
        terrain = 0
        # print("x=",x," y=",y)  # Debugging: Print the x and y coordinates
        # print(position.x+(192*SCALE))  # Debugging: Print the scaled positions
        # print(position.x+(61*SCALE))
        # print(position.x+(191*SCALE))
        # print(position.x+(55*SCALE))

        # Check if the position is in the middle grass area
        if ((x <= position.x + (192 * SCALE)) and
                (x >= position.x + (61 * SCALE)) and
                (y <= position.y + (191 * SCALE)) and
                (y >= position.y + (55 * SCALE))):
            terrain = 1
        # Check if the position is in the top grass area
        elif ((x <= position.x + (250 * SCALE)) and
              (x >= position.x + (4 * SCALE)) and
              (y <= position.y + (17 * SCALE)) and
              (y >= position.y + (4 * SCALE))):
            terrain = 1
        # Check if the position is in the right grass area
        elif ((x <= position.x + (250 * SCALE)) and
              (x >= position.x + (231 * SCALE)) and
              (y <= position.y + (250 * SCALE)) and
              (y >= position.y + (4 * SCALE))):
            terrain = 1
        # Check if the position is in the bottom grass area
        elif ((x <= position.x + (250 * SCALE)) and
              (x >= position.x + (4 * SCALE)) and
              (y <= position.y + (250 * SCALE)) and
              (y >= position.y + (235 * SCALE))):
            terrain = 1
        # Check if the position is in the left grass area
        elif ((x <= position.x + (20 * SCALE)) and
              (x >= position.x + (4 * SCALE)) and
              (y <= position.y + (235 * SCALE)) and
              (y >= position.y + (4 * SCALE))):
            terrain = 1
        else:
            terrain = 0

        # print("terrain=",terrain)  # Debugging: Print the terrain type
        return terrain

    def get_pos(self):
        """Return the current position of the map."""
        return self.pos

    def get_dim(self):
        """Return the dimensions of the map."""
        return self.dim

    def get_border(self):
        """Return the border size of the map."""
        return self.border

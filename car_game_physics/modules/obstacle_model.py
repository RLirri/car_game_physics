from pygame.math import Vector2
from modules.constants import *

""" Author: Ruixin """
""" Description: Obstacle Class for Car Simulation """
class Obstacle:
    def __init__(self, x, y, angle=90.0, width=30, height=30, max_speed=5, max_accel=0):
        """Initialize the obstacle with position, dimensions, and motion parameters."""
        self.position = Vector2(0.0, 0.0)  # Absolute position of the obstacle
        self.pos_rel_map = Vector2(x, y)  # Position relative to the map
        self.velocity = Vector2(0.0, 0.0)  # Velocity of the obstacle
        self.dim = Vector2(OBSTACLE_LENGTH, OBSTACLE_WIDTH)  # Dimensions of the obstacle
        self.accel = 0.0  # Acceleration of the obstacle
        self.angle = angle  # Orientation angle of the obstacle
        self.speed = 0.0  # Speed of the obstacle

        # Constants
        self.width = width  # Width of the obstacle
        self.height = height  # Height of the obstacle

        # Thresholds for input
        self.max_accel = max_accel  # Maximum acceleration
        self.max_speed = max_speed  # Maximum speed

    def update(self, pos):
        """Update the absolute position of the obstacle based on the map's position."""
        self.position.x = pos.x + self.pos_rel_map.x
        self.position.y = pos.y + self.pos_rel_map.y

    def check_boundary(self, pos_valid, x, y, car):
        """Check if the car is colliding with the obstacle and update the boundary validity."""
        # print("X: ",x," and Y: ",y)  # Debugging: Print the x and y coordinates
        # print("length of car:",car["length"])  # Debugging: Print the length of the car
        # print("boundaryX:",car["pos"].x+self.getDim().x+self.pos_rel_map.x)  # Debugging: Print the boundary x
        # print("boundaryX2:",car["pos"].x+self.pos_rel_map.x-car["length"])  # Debugging: Print the boundary x2
        # print("boundaryY:",car["pos"].y+self.getDim().y+self.pos_rel_map.y)  # Debugging: Print the boundary y
        # print("boundaryY2:",car["pos"].y+self.pos_rel_map.y-car["length"])  # Debugging: Print the boundary y2

        if ((x <= car["pos"].x + self.pos_rel_map.x + self.get_dim().x - 20) and
                (x >= car["pos"].x + self.pos_rel_map.x - car["length"] + 20) and
                (y <= car["pos"].y + self.pos_rel_map.y + self.get_dim().y - 20) and
                (y >= car["pos"].y + self.pos_rel_map.y - car["length"] + 20)):
            pos_valid[0] = False
            pos_valid[1] = False

        return pos_valid

    def get_position(self):
        """Return the current position of the obstacle."""
        return self.position

    def get_dim(self):
        """Return the dimensions of the obstacle."""
        return self.dim

from math import cos, pi, sin
from pygame.math import Vector2

""" Author: Ruixin """
""" Description: Sensor Class for Car Simulation """
class Sensor:
    def __init__(self, x=0.0, y=0.0, orient=0.0):
        """Initialize the sensor with position, orientation, and dimensions."""
        self.position = Vector2(x, y)  # Position of the sensor
        self.orient = orient  # Orientation angle of the sensor
        self.length = 0  # Length of the sensor beam (updated later)
        self.width = 5  # Width of the sensor beam

    def update(self, position, orient):
        """Update the sensor's position and orientation."""
        self.position.x = position.x  # Update x-coordinate
        self.position.y = position.y  # Update y-coordinate
        self.orient = orient  # Update orientation

    def check_sensor(self, env, distance=100, num_intervals=10):
        """Check if the sensor detects any terrain within a specified distance."""
        self.length = distance  # Set the sensor beam length

        detected = False  # Flag to indicate if terrain is detected

        heading = Vector2(cos(self.orient * pi / 180.0), sin(-self.orient * pi / 180.0))  # Direction of the sensor beam
        steps = int(distance / num_intervals)  # Distance between each interval
        for i in range(0, num_intervals + 1):  # Iterate over each interval
            sensor_pos = Vector2(self.position.x + (heading.x * i * steps), self.position.y + (heading.y * i * steps))  # Calculate sensor beam position
            terrain = env.check_terrain(self.position.x, self.position.y, sensor_pos)  # Check if terrain is detected
            if terrain:
                detected = True  # Set detected flag to True if terrain is found
                continue

        return detected  # Return detection status

    def get_position(self):
        """Return the current position of the sensor."""
        return self.position

    def get_length(self):
        """Return the length of the sensor beam."""
        return self.length

    def get_width(self):
        """Return the width of the sensor beam."""
        return self.width

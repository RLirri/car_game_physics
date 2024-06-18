from math import cos, pi, sin, sqrt
from random import randint

from pygame.math import Vector2

from modules import sensor
from modules.constants import *

""" Author: Ruixin and Hilkia """
""" Description: Car Class for Car Simulation """

# max_speed = max_speeds_vehicle[len(selected)-1]
# max_accel = max_accels_vehicle[len(selected)-1]

class Car:
    def __init__(self, x, y, orient=180, max_steer=0):
        """Initialize the Car object with position, orientation, and various parameters."""
        
        self.pos = Vector2(x, y)
        self.vel = Vector2(0.0, 0.0)
        self.accel = Vector2(0.0, 0.0)
        self.engine_force = 0.0
        self.steer_angle = 0.0
        self.orient = orient
        self.brake_b = 0
        self.gear = 1  # 0:park, 1:drive, 2:reverse
        self.prev_pos = Vector2(0, 0)
        self.pos_buf = Vector2(0, 0)
        self.terrain = 0
        rdrag = C_DRAG_ROAD[selected[len(selected)-1]]
        self.drag = rdrag
        self.RR = 30 * self.drag  # Rolling resistance
        self.ang_vel = 0

        # Initialize the front sensor for the car
        self.front_sensor = sensor.Sensor(x, y)

        # Threshold Constants
        self.max_steer = max_steer
        self.max_speed = max_speeds_vehicle[selected[len(selected)-1]]
        self.max_accel = max_accels_vehicle[selected[len(selected)-1]]

    def calculate(self, dt):
        """Calculate the vehicle's new position and velocity."""
        pos_local = Vector2(0.0, 0.0)
        vel_local = Vector2(0.0, 0.0)
        speed = sqrt(self.vel.x * self.vel.x + self.vel.y * self.vel.y)  # Calculate current speed

        # Adjust steer angle slightly if the car is on rough terrain
        if self.terrain == 1:
            self.steer_angle += randint(-2, 2)

        self.ang_vel = 0

        # Calculate angular velocity if there is a steer angle
        if self.steer_angle:
            circ_radius = VEHICLE_LENGTH / sin(self.steer_angle)
            ang_vel = speed / circ_radius
            self.ang_vel = ang_vel
            self.orient = (self.orient + ang_vel) % 360  # Update orientation based on angular velocity

        # Calculate heading vector based on orientation
        heading = Vector2(cos(self.orient * pi / 180.0), sin(-self.orient * pi / 180.0))

        # Calculate traction force
        f_tract = self.engine_force * heading

        # Adjust traction force based on braking and gear conditions
        if (((self.vel.x >= 0 and heading.x >= 0) or (self.vel.x <= 0 and heading.x <= 0)) and \
                ((self.vel.y >= 0 and heading.y >= 0) or (self.vel.y <= 0 and heading.y <= 0)) and \
                self.brake_b and (self.gear == 1)):
            f_tract = -heading * C_BRAKE[selected[len(selected)-1]]
        if (((self.vel.x <= 0 <= heading.x) or (self.vel.x >= 0 >= heading.x)) and \
                ((self.vel.y <= 0 <= heading.y) or (self.vel.y >= 0 >= heading.y)) and \
                self.brake_b and (self.gear == 2)):
            f_tract = heading * C_BRAKE[selected[len(selected)-1]]

        # Calculate drag force
        f_drag = -self.drag * self.vel
        self.RR = 30 * self.drag
        # Calculate rolling resistance force
        f_rr = -self.RR * self.vel  # Rolling Resistance C_rr ~= 30*C_drag
        # Calculate the total longitudinal force
        f_long = f_tract + f_drag + f_rr

        # Calculate acceleration based on the total force
        masses = vehicle_masses[selected[len(selected)-1]]
        accel = f_long / masses
        # Update velocity based on acceleration
        vel_local.x = self.vel.x + (accel.x * dt)
        vel_local.y = self.vel.y + (accel.y * dt)
        # Update position based on velocity
        pos_local.x = self.pos.x + (vel_local.x * dt)
        pos_local.y = self.pos.y + (vel_local.y * dt)

        # Get the car's dimensions
        length = self.get_length()
        width = self.get_width()

        # Create a dictionary to store car info
        info = {
            "pos": pos_local, "vel": vel_local,
            "length": length, "width": width
        }

        return info

    def update(self, dt, car_info, pos_valid):
        """Update the vehicle's position and velocity based on calculated values and validation flags."""
        if pos_valid[0]:  # Check if the x position is valid
            self.pos.x = car_info["pos"].x
            self.vel.x = car_info["vel"].x
        else:
            self.vel.x = 0
        if pos_valid[1]:  # Check if the y position is valid
            self.pos.y = car_info["pos"].y
            self.vel.y = car_info["vel"].y
        else:
            self.vel.y = 0

    def set_gear(self, gear):
        """Set the car's gear."""
        self.gear = gear

    def set_engine_force(self, f):
        """Set the engine force applied to the car."""
        self.engine_force = f

    def set_steer_angle(self, a):
        """Set the car's steering angle."""
        self.steer_angle = a

    def set_braking(self, b):
        """Set the car's braking state."""
        self.brake_b = b

    @staticmethod
    def get_length():
        """Get the car's length."""
        return VEHICLE_LENGTH

    @staticmethod
    def get_width():
        """Get the car's width."""
        return VEHICLE_WIDTH

    def get_position(self):
        """Get the car's current position."""
        return self.pos

    def get_vel(self):
        """Get the car's current velocity."""
        return self.vel

    def get_prev_pos(self):
        """Get the car's previous position."""
        return self.prev_pos

    def get_accel(self):
        """Get the car's current acceleration."""
        return self.accel

    def get_orientation(self):
        """Get the car's current orientation."""
        return self.orient

    def get_ang_vel(self):
        """Get the car's current angular velocity."""
        return self.ang_vel

    def set_terrain(self, terrain):
        """Set the terrain type and update the drag coefficient accordingly."""
        self.terrain = terrain
        if terrain == 0:
            rdrag = C_DRAG_ROAD[selected[len(selected)-1]]
            self.drag = rdrag
        if terrain == 1:
            gdrag = C_DRAG_GRASS[selected[len(selected)-1]]
            self.drag = gdrag

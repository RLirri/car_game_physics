import os
from random import randint

import pygame
from pygame.locals import *
from pygame.math import Vector2

from modules import car_model, map_model, obstacle_model
from modules.constants import *
from modules.restart import restart
"""Author: Ruixin and Hilkia"""
"""Description: Game Class for Car Simulation"""

# Load images for the car, background, rock, and sensor from assets folder
# print(f"selected {selected}")
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(current_dir, "../assets/")
img_path = os.path.join(current_dir, "../assets/img/")
# pygame.image.load(assets_path + "car.png")
background_image = pygame.image.load(assets_path + "mario_circuit_one.png")
rock_image = pygame.image.load(assets_path + "rock.png")
sensor_image = pygame.image.load(assets_path + "sensor_beam.png")

# Initialize sound effects
pygame.mixer.init()
car_crash_sound = pygame.mixer.Sound(assets_path + "sounds/crash.wav")
car_driving_sound = pygame.mixer.Sound(assets_path + "sounds/car_driving_3.wav")
car_snow_sound = pygame.mixer.Sound(assets_path + "sounds/car_snow.wav")
car_skid_sound = pygame.mixer.Sound(assets_path + "sounds/tire_skid.wav")

class Game:
    def __init__(self):
        """Initialize the game, set up the screen, clock, car, map, and obstacles."""
        pygame.init()
        pygame.display.set_caption("Drive-Simulation")

        # Set the starting position of the car and map
        car_pos_x = (SCREEN_WIDTH / 2) - 100
        car_pos_y = (SCREEN_HEIGHT / 2) - 100
        map_pos_x = car_pos_x
        map_pos_y = car_pos_y

        # Initialize screen, clock, game ticks, exit flag, and terrain type
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.ticks = GAME_TICKS
        self.exit = False
        self.terrain = 0  # 0=road, 1=grass

        # Initialize car, map, and obstacles
        self.car = car_model.Car(car_pos_x, car_pos_y)
        self.map = map_model.Map(map_pos_x, map_pos_y)
        self.obstacles = []
        for i in range(NUM_OBSTACLES):
            x_pos = randint(100, 800)
            y_pos = randint(100, 800)
            rock = obstacle_model.Obstacle(map_pos_x + x_pos, map_pos_y + y_pos)
            self.obstacles.append(rock)

    @staticmethod
    def check_boundary(car_info, env, obstacles):
        """Check if the car or obstacles are within the boundary."""
        # Get middle of the screen
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2

        # Initialize position validity flags
        pos_valid = [True, True]
        for ob in obstacles:
            pos_valid = ob.check_boundary(pos_valid, x, y, car_info)
        pos_valid = env.check_boundary(pos_valid, x, y, car_info)

        return pos_valid

    def check_terrain(self, car, env):
        """Check the terrain type at the car's current position."""
        # Get middle of the screen
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2

        self.terrain = env.check_terrain(x, y, car.get_position())
        return self.terrain

    """Defines the controls of the car"""

    @staticmethod
    def controls(car, dt, pressed):
        """Handle car controls based on user input."""
        if pressed[pygame.K_LEFT]:
            car.set_steer_angle(-10)
        elif pressed[pygame.K_RIGHT]:
            car.set_steer_angle(10)
        else:
            car.set_steer_angle(0)
        if pressed[pygame.K_UP]:
            car.set_engine_force(500000)
            car.set_gear(1)
        elif pressed[pygame.K_DOWN]:
            car.set_engine_force(-200000)
            car.set_gear(2)
        elif pressed[pygame.K_b]:
            car.set_braking(1)
        else:
            car.set_engine_force(0)
            car.set_braking(0)

    def draw(self, car, env, obstacles):
        """Draw the screen, car, map, and obstacles."""
        # Draw background
        map_width = int(env.get_dim().x)
        map_height = int(env.get_dim().y)
        background_scaled = pygame.transform.scale(background_image, (map_width, map_height))
        self.screen.blit(background_scaled, env.get_pos())

        # Draw car
        id = len(selected)-1
        ids = selected[id]
        car_image = pygame.image.load(img_path + chosen[ids])
        car_scaled = pygame.transform.scale(car_image, (int(car.get_length()), int(car.get_width())))
        car_rotated = pygame.transform.rotate(car_scaled, car.get_orientation())
        self.screen.blit(car_rotated, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Draw obstacles
        for ob in obstacles:
            rock_scaled = pygame.transform.scale(rock_image, (int(ob.get_dim().x), int(ob.get_dim().y)))
            self.screen.blit(rock_scaled, ob.get_position())

        # Draw sensors
        fs_obj = car.front_sensor
        fs_scaled = pygame.transform.scale(sensor_image, (int(fs_obj.get_length()), int(fs_obj.get_width())))
        fs_rotated = pygame.transform.rotate(fs_scaled, car.get_orientation())
        front_sensor_position = Vector2((SCREEN_WIDTH // 2) + car.get_length(),
                                        (SCREEN_HEIGHT // 2) + (car.get_width() // 2))
        self.screen.blit(fs_rotated, front_sensor_position)

        pygame.display.flip()

    def run(self):
        """Run the game loop to process the simulation."""
        while not self.exit:
            # Local save of parameters
            prev_terrain = self.terrain

            # Convert time from milliseconds to seconds
            dt = self.clock.get_time() / 1000

            # Event queue processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                elif event.type == VIDEORESIZE:
                    pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)

            # User input handling
            pressed = pygame.key.get_pressed()
            self.controls(self.car, dt, pressed)

            # Update sensor information
            self.car.front_sensor.update(self.car.get_position(), self.car.get_orientation())
            detected = self.car.front_sensor.check_sensor(self.map, 100, 1)
            # print(detected)

            # Game logic updates
            self.terrain = self.check_terrain(self.car, self.map)
            self.car.set_terrain(self.terrain)
            car_info = self.car.calculate(dt)
            pos_valid = self.check_boundary(car_info, self.map, self.obstacles)
            self.car.update(dt, car_info, pos_valid)
            self.map.update(dt, self.car.get_position())
            for ob in self.obstacles:
                ob.update(self.map.get_pos())

            # Drawing updates
            self.screen.fill((0, 0, 0))
            self.draw(self.car, self.map, self.obstacles)

            # Handle sound effects
            if SOUND_ON:
                if not pos_valid[0] or not pos_valid[1]:  # The car crashed
                    car_crash_sound.play()
                drive_sound = False
                if abs(car_info["vel"].x) > 50 or abs(car_info["vel"].y) > 50:  # Car speed > 50
                    drive_sound = True
                if not pygame.mixer.Channel(0).get_busy():  # Prevent sound overlap
                    if drive_sound:
                        if prev_terrain != self.terrain:
                            car_snow_sound.stop()
                            car_driving_sound.stop()
                        if self.terrain == 0:
                            car_driving_sound.play()
                        if self.terrain == 1:
                            car_snow_sound.play()
                    else:
                        car_snow_sound.stop()
                        car_driving_sound.stop()
                else:
                    if not drive_sound:
                        car_snow_sound.stop()
                        car_driving_sound.stop()
                if abs(self.car.get_ang_vel()) > 3.0:
                    car_skid_sound.play()
                else:
                    car_skid_sound.stop()

            # Update the clock (called once per frame)
            self.clock.tick(self.ticks)
            #exits or rewind
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:  # Check if 'x' key is pressed
                        self.exit = True
                    elif event.key == pygame.K_z:  # Check if 'z' key is pressed
                        pygame.quit()
                        restart()
        # End of while not self.exit

        pygame.quit()

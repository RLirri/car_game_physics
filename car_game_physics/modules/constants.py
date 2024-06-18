""" Global Parameters """
""" Author: Ruixin and Hilkia """
""" Date: 2024.05.04 """
""" Description: Constants Class for Car Simulation """

# Scale factor for various game elements
SCALE = 4

# Screen Parameters
SCREEN_WIDTH = 256 * SCALE  # Width of the screen, default = 128
SCREEN_HEIGHT = 256 * SCALE  # Height of the screen, default = 128
GAME_TICKS = 60  # Number of game ticks per second

# Game Parameters
NUM_OBSTACLES = 1  # Number of obstacles in the game, default = 0

# Map Parameters
MAP_WIDTH = 500 * SCALE  # Width of the map, default = 254
MAP_HEIGHT = 500 * SCALE  # Height of the map, default = 254
BORDER = 4 * SCALE  # Width of the border around the map

# Vehicle Parameters
VEHICLE_LENGTH = 11 * SCALE  # Length of the vehicle, scaled (0.1m per unit)
VEHICLE_WIDTH = 5.5 * SCALE  # Width of the vehicle, scaled (0.1m per unit)
MASS = [1025, 970, 1285, 1815, 600, 766]  # Mass of the vehicle in kg, scaled [1025, 970, 1285, 1815, 100, 266]
scaled_masses = [mass / SCALE for mass in MASS]
vehicle_masses = scaled_masses
# C_DRAG_ROAD = [33, 31, 29, 27, 7, 56]# Drag coefficient on road
# C_DRAG_GRASS = [45, 45, 375, 375, 85, 675]  # Drag coefficient on grass
# C_BRAKE = [7.848, 7.848, 7.848, 7.848, 8.829, 9.81]  # Braking coefficient
# POS_BUFFER_LENGTH = 60  # Length of the position buffer
# max_speeds_vehicle = [44.44, 38.89, 52.78, 41.67, 25.00, 83.06]
# max_accels_vehicle = [3.17, 3.38, 6.28, 5.32, 2.27, 30.74]
C_DRAG_ROAD = [33, 31, 29, 27, 27, 26]# Drag coefficient on road
C_DRAG_GRASS = [45, 45, 75, 75, 85, 75]  # Drag coefficient on grass
C_BRAKE = [7.848, 7.848, 7.848, 7.848, 8.829, 9.81]  # Braking coefficient
POS_BUFFER_LENGTH = 60  # Length of the position buffer
max_speeds_vehicle = [44.44, 38.89, 42.78, 41.67, 25.00, 53.06]
max_accels_vehicle = [3.17, 3.38, 6.28, 5.32, 2.27, 12.74]


# Obstacle Parameters
OBSTACLE_LENGTH = 20 * SCALE  # Length of an obstacle, scaled
OBSTACLE_WIDTH = 10 * SCALE  # Width of an obstacle, scaled

# Sound Parameters
SOUND_ON = True  # Flag to turn sound on or off, default = False

# car image
selected = [0]

chosen = [
    'daihatsu_sigra6.png',
    'honda_brio6.png',
    'volkswagen_lavida6.png',
    'BYD6.png',
    'honda_super6.png',
    'suzuki_hayabusa6.png'
]

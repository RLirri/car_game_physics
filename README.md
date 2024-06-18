# Physics Car Game: Terrain Effects on Car Movement

### Computational Physics

## Abstract
This project simulates the impact of various terrains on car movement using principles of computational physics. It explores how friction, traction, and momentum affect vehicle performance, employing algorithms and numerical methods for accurate simulations. The goal is to demonstrate the practical applications of computational physics in automotive engineering.

## Introduction
### Background
Vehicles are integral to everyday life, and understanding their underlying physics is crucial, especially in testing and maintenance. This simulation provides a virtual environment for testing vehicles under different conditions, reducing prototype costs and enhancing quality.

### Objectives
To create a functional simulation using Python and Pygame, demonstrating the physics of vehicles on different terrains. The simulation uses a simplified map, Mario Circuit 1, and includes realistic vehicle parameters for a comprehensive analysis.

### Scope
The project includes six vehicle presets commonly used in Indonesia and China. It models different environmental changes like grass and road drag, providing a scaled-down version of real-life vehicular physics.

## Methodology
### Framework
The simulation uses Python and Pygame, with core components divided into classes: Game, Start, Car, Map, Obstacles, and Sensor. Each class has specific responsibilities, from initializing the start menu to modeling vehicle dynamics.

### Vehicle Dynamics
The simulation incorporates various physics principles:

- **Traction Force**: Propels the car forward or backward.
- **Drag Force**: Simulates air resistance.
- **Speed Calculation**: Determines car speed from velocity components.
- **Rolling Resistance**: Simulates tire-road friction.
- **Longitudinal Forces**: Sum of traction, drag, and rolling resistance.
- **Acceleration**: Follows Newton's second law.
- **Position and Velocity Updates**: Based on time increments and forces.
- **Braking Force**: Simulates deceleration.
- **Weight Transfer**: Adjusts weight during acceleration/deceleration.
- **Engine Force**: Converts engine torque to drive force.
- **Maximum Traction Force**: Prevents tire slip.
- **Cornering and Centripetal Forces**: Ensure realistic turning dynamics.
- **Angular Acceleration**: Determines rate of rotation change.
- **Euler Method**: Updates angular velocity.


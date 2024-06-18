import pygame
import sys
# from modules.constants import selected
from modules.game import Game  # Import the Game class from the modules.game module

""" Author: Hilkia """
""" Description: Sart class for selection menu"""

class Start:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen dimensions and create the screen object
        self.screen_width = 700
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Start Page")

        # Load background image
        self.background_image = pygame.transform.scale(pygame.image.load('assets/img/bg.jpg'),(700,700))

        # Load button images
        self.button_images = [
            pygame.transform.scale(pygame.image.load('assets/img/daihatsu_sigra.jpg'), (150, 100)),
            pygame.transform.scale(pygame.image.load('assets/img/honda_brio.jpg'), (150, 100)),
            pygame.transform.scale(pygame.image.load('assets/img/volkswagen_lavida.jpg'), (150, 100)),
            pygame.transform.scale(pygame.image.load('assets/img/BYD1.jpg'), (150, 100)),
            pygame.transform.scale(pygame.image.load('assets/img/honda_super.jpg'), (150, 100)),
            pygame.transform.scale(pygame.image.load('assets/img/suzuki_hayabusa.jpg'), (150, 100))
        ]

        # Define Colors
        self.black = (0, 0, 0)
        self.light_brown = (181, 101, 29)
        self.blue = (0, 0, 255)

        # Button settings
        self.button_width = 150
        self.button_height = 150  # Increase height to accommodate images and text
        self.button_margin = 20

        # Calculate the top-left corner positions for each button in a 2x3 grid
        self.button_positions = [
            ((self.screen_width // 2) - self.button_width - self.button_margin, (self.screen_height // 2) - self.button_height - self.button_margin),
            ((self.screen_width // 2) + self.button_margin, (self.screen_height // 2) - self.button_height - self.button_margin),
            ((self.screen_width // 2) - self.button_width - self.button_margin, (self.screen_height // 2)),
            ((self.screen_width // 2) + self.button_margin, (self.screen_height // 2)),
            ((self.screen_width // 2) - self.button_width - self.button_margin, (self.screen_height // 2) + self.button_height + self.button_margin),
            ((self.screen_width // 2) + self.button_margin, (self.screen_height // 2) + self.button_height + self.button_margin)
        ]

        # Set up font
        self.font = pygame.font.SysFont(None, 24)  # Decreased font size to fit longer text
        self.title_font = pygame.font.SysFont(None, 48)

    def draw_buttons(self):
        self.screen.blit(self.background_image, (0, 0))
        title = self.title_font.render("Choose Your Vehicle", True, self.black)
        self.screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 50))

        vehicle_names = [
            "Daihatsu Sigra",
            "Honda Brio",
            "Volkswagen Lavida",
            "BYD Qin Plus",
            "Honda Super Cub",
            "Suzuki Hayabusa"
        ]

        for idx, position in enumerate(self.button_positions):
            pygame.draw.rect(self.screen, self.light_brown, (position[0], position[1], self.button_width, self.button_height))
            # Draw image on button
            image = self.button_images[idx]
            image_rect = image.get_rect(center=(position[0] + self.button_width // 2, position[1] + self.button_height // 3))
            self.screen.blit(image, image_rect)
            # Draw label below image
            label = self.font.render(vehicle_names[idx], True, self.black)
            self.screen.blit(label, (position[0] + (self.button_width - label.get_width()) // 2, position[1] + self.button_height - label.get_height() - 10))

    def start_game(self):
        # pygame.quit()  # Quit Pygame
        game = Game()  # Create an instance of the Game class
        game.run()  # Call the run method to start the game
    

    def run(self):
        from modules.constants import selected
        running = True
        start_game_flag = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for idx, position in enumerate(self.button_positions):
                        button_rect = pygame.Rect(position[0], position[1], self.button_width, self.button_height)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            print(f"Button {idx + 1} clicked")
                            selected.append(idx) # Save the selected id
                            print(f"selected {selected}")
                            start_game_flag = True
                            running = False  # Exit the loop to close the Pygame window

            self.draw_buttons()
            pygame.display.flip()

        pygame.quit()  # Quit Pygame after the loop ends
        if start_game_flag:
            print(f"selected {selected}")
            self.start_game()  # Start the game if a button was clicked
            print(f"selected {selected}")
        sys.exit()  # Exit the program


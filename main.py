import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    # Print some startup info for debugging
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame and create the game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0  # Time in seconds between frames (delta time)

    # Create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        # Log the current game state each frame
        log_state()

        # Handle window events (like closing the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen to black
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        player.update(dt)

        # Swap the back buffer to the screen
        pygame.display.flip()

        # Cap the frame rate at 60 FPS and get delta time
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
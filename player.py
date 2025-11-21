import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS , LINE_WIDTH

class Player(CircleShape):
  # Represents the player's spaceship on screen
  def __init__(self, x, y):
    # Initialize the circle hitbox at (x, y) with the player radius
    super().__init__(x, y, PLAYER_RADIUS)
    # Rotation in degrees, 0 points "up"
    self.rotation = 0

  def triangle(self):
      # Direction the ship is facing
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      # Perpendicular direction to get the triangle's side points
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

      # Tip of the ship
      a = self.position + forward * self.radius
      # Back-left and back-right corners
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]

  def draw(self, screen):
      # Draw the ship as a white triangle outline
      pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), LINE_WIDTH)
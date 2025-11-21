import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS , LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

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

  def rotate(self, dt):
     self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        self.rotate(-dt)
    if keys[pygame.K_d]:
        self.rotate(dt)
    if keys[pygame.K_w]:
        self.move(dt)
    if keys[pygame.K_s]:
        self.move(-dt)

  def move(self, dt):
    unit_vector = pygame.Vector2(0, 1)
    rotated_vector = unit_vector.rotate(self.rotation)
    rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
    self.position += rotated_with_speed_vector
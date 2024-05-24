import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 3

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y

class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10

class Game:
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.display_final_score = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                self.display_final_score = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_END:
                    self.game_over = True
                    self.display_final_score = True

    def update(self):
        if not self.game_over:
            self.ball.move()
            self.ball.check_collision()
            if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
                if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                    self.ball.y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                    self.ball.speed_y = -self.ball.speed_y
                    self.score += 1
                    # Increase speed after collision with the paddle
                    self.ball.speed_x *= 1.1  # Increase horizontal speed by 10%
                    self.ball.speed_y *= 1.1  # Increase vertical speed by 10%
                else:
                    self.game_over = True
                    self.display_final_score = True

    def draw(self, screen):
        screen.fill(BLACK)
        if not self.display_final_score:
            pygame.draw.circle(screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
            pygame.draw.rect(screen, WHITE, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
        if self.display_final_score:
            game_over_text = self.font.render(f"Game Over! Final Score: {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over_text, game_over_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    game = Game()
    font = pygame.font.Font(None, 74)  # Larger font for countdown

    # Countdown before the game starts
    countdown = 3
    while countdown > 0:
        screen.fill(BLACK)
        countdown_text = font.render(str(countdown), True, WHITE)
        countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.flip()
        pygame.time.delay(1000)  # Wait for 1 second
        countdown -= 1

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.paddle.move("left")
        if keys[pygame.K_RIGHT]:
            game.paddle.move("right")

        game.handle_events()
        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

        if game.game_over:
            # Delay after game over to show the final score
            pygame.time.delay(5000)  # Display for 2000 milliseconds (2 seconds)
            running = False

    pygame.quit()

main()

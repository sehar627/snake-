import pygame, random

# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = 600
SNAKE_SIZE = 20
FPS = 15
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake Game")

# Colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize variables
clock = pygame.time.Clock()
score = 0
snake = [(WINDOW_SIZE // 2, WINDOW_SIZE // 2)]
direction = (0, 0)
apple = (random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
         random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, SNAKE_SIZE):
                direction = (0, -SNAKE_SIZE)
            if event.key == pygame.K_DOWN and direction != (0, -SNAKE_SIZE):
                direction = (0, SNAKE_SIZE)
            if event.key == pygame.K_LEFT and direction != (SNAKE_SIZE, 0):
                direction = (-SNAKE_SIZE, 0)
            if event.key == pygame.K_RIGHT and direction != (-SNAKE_SIZE, 0):
                direction = (SNAKE_SIZE, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # Check for apple collision
    if head == apple:
        score += 1
        apple = (random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                 random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
    else:
        snake.pop()

    # Check for collisions
    if (head[0] < 0 or head[0] >= WINDOW_SIZE or
        head[1] < 0 or head[1] >= WINDOW_SIZE or
        head in snake[1:]):
        running = False

    # Draw everything
    display.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(display, DARKGREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(display, RED, (apple[0], apple[1], SNAKE_SIZE, SNAKE_SIZE))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

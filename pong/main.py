# Import library
import pygame
import random as rd

# Initialize pygame
pygame.init()

# Colors
background_color = (10, 10, 10)
player_color = (255, 255, 255)
ball_color = (255, 255, 255)
line_color = (255, 255, 255)

# Size players
players_width = 15
players_height = 90

# Player 1 coordinates
player_1_x = 50
player_1_y = 250 
player_1_y_speed = 0

# Player 2 coordinates
player_2_x = 725
player_2_y = 250
player_2_y_speed = 0

# Ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20
ball_x_speed = 0.5
ball_y_speed = 0.5


#window size
screen_height = 800
screen_width = 600

# Size variable
size = (screen_height, screen_width)

# Display the window
screen = pygame.display.set_mode( size )

# Icon
icon = pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption("Ping-Pong Classic PC Edition")

# Score variables
player_1_score = 0
player_2_score = 0

# Score font
score_font = pygame.font.Font("texto.ttf", 32)

# Win font
win_font = pygame.font.Font("texto.ttf", 64) 

# Score position in the screen - Player 1
player_1_score_x = 30
player_1_score_y = 10

# Score position in the screen - Player 2
player_2_score_x = 730
player_2_score_y = 10

# Win text position
win_x = 250
win_y = 250

# Player 1 score function
def show_score_1(x, y):
    score1 =  score_font.render(" " + str(player_1_score), True, (255, 255, 255))
    screen.blit( score1, (x, y))

# Player 2 score function
def show_score_2(x, y):
    score2 =  score_font.render(" " + str(player_2_score), True, (255, 255, 255))
    screen.blit( score2, (x, y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player key controls

        # Cheks for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            
            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -1

            if event.key == pygame.K_s:
                player_1_y_speed = 1

            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -1

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 1
        
        if event.type == pygame.KEYUP:

            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = 0

            if event.key == pygame.K_s:
                player_1_y_speed = 0

            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = 0

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0
            


    # Players movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed

    # Players boundaries

    # Player 1
    if player_1_y <= 0:
        player_1_y = 0
    if player_1_y >= 510:
        player_1_y = 510

    # Player 2
    if player_2_y <= 0:
        player_2_y = 0
    if player_2_y >= 510:
        player_2_y = 510

    # Ball movement
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Ball boundaries: top or buttom
    if ball_y > (screen_width - ball_radius) or ball_y < ball_radius:
        ball_y_speed *= -1

    # Ball boundaries (right or left) and score update
    if ball_x > screen_height:

        player_1_score += 1

        ball_x = screen_height/2
        ball_y = screen_width/2
        ball_x_speed *= rd.choice([-1, 1])

    elif ball_x < 0:

        player_2_score += 1

        ball_x = screen_height/2
        ball_y = screen_width/2
        ball_x_speed *= rd.choice([-1, 1])


    # Fill the screen with colorss
    screen.fill( background_color )

    # Drawing area

    # Define the player 1 -left: rectangle
    player_1 = pygame.draw.rect( screen, player_color, (player_1_x, player_1_y, players_width, players_height))
 
    # Define the player 2 -left: rectangle
    player_2 = pygame.draw.rect( screen, player_color, (player_2_x, player_2_y, players_width, players_height))

    # Draw the ball
    ball = pygame.draw.circle( screen, ball_color, (ball_x, ball_y), ball_radius)

    # Collitions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_x_speed *= -1

    # Players win
    if player_1_score == 25:
        player_1_y_speed = 0
        player_2_y_speed = 0
        ball_y = 2000
        ball_x_speed = 0
        ball_y_speed = 0
        win_text = win_font.render("Player 1 win!", True, (255, 255, 255))
        screen.blit(win_text, (win_x, win_y))
        
    elif player_2_score == 25:
        player_1_y_speed = 0
        player_2_y_speed = 0
        ball_y = 2000 
        ball_x_speed = 0
        ball_y_speed = 0
        win_text = win_font.render("Player 2 win!", True, (255, 255, 255))
        screen.blit(win_text, (win_x, win_y))

    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/1.5,0),(screen_width/1.5, screen_height)  )

    # Call the show_score_1 function
    show_score_1(player_1_score_x, player_1_score_y)

    # Call the show_score_1 function
    show_score_2(player_2_score_x, player_2_score_y)

    # Refresh the window
    pygame.display.flip()
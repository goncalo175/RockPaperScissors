import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Rock, Paper, Scissors - Deluxe")

# Set up clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define font
fontTitle = pygame.font.Font(None, 74)  # None uses default font, 74 is the font size
fontSmall = pygame.font.Font(None, 34)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)



def main_menu():
    while True:
        screen.fill(BLUE)  # Fill the background color
        # Draw menu options
        draw_text('Welcome to Rock, Paper Scissors - Deluxe', fontTitle, WHITE, screen, screen.get_width() // 2, 100)
        draw_text('Press 1 to Start', fontSmall, WHITE, screen, screen.get_width() // 2, 250)
        draw_text('Press 2 for Instructions', fontSmall, WHITE, screen, screen.get_width() // 2, 350)
        draw_text('Press ESC to Quit', fontSmall, WHITE, screen, screen.get_width() // 2, 450)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Start game option
                    return 'start'
                if event.key == pygame.K_2:  # Instructions option
                    return 'instructions'
                if event.key == pygame.K_ESCAPE:  # Quit option
                    pygame.quit()
                    sys.exit()

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)


def game_loop():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text('Game Running... Press ESC to return to Menu', fontSmall, WHITE, screen, 400, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'  # Return to the menu

        pygame.display.flip()
        clock.tick(60)


def instructions_screen():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text("Instructions:", fontTitle, WHITE, screen, screen.get_width() // 2, 100 )
        draw_text("In Rock, Paper, Scissors, each player simultaneously chooses one of three options:",
                  fontSmall, WHITE, screen, screen.get_width() // 2, 250)
        draw_text("Rock, Paper, or Scissors. Rock crushes Scissors, Scissors cut Paper, and Paper covers Rock.",
                  fontSmall, WHITE, screen, screen.get_width() // 2, 300)
        draw_text("If one player's choice beats the other's, that player wins the round; if both players choose the "
                  "same", fontSmall, WHITE, screen, screen.get_width() // 2, 330)
        draw_text("option, it's a draw. Continue playing until a player wins or you decide to stop.",
                  fontSmall, WHITE, screen, screen.get_width() // 2, 360)

        draw_text('Press ESC to return to Menu', fontSmall, WHITE, screen, screen.get_width() // 2, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'  # Return to the menu

        pygame.display.flip()
        clock.tick(60)


# Rock, Paper, Scissors simple game logic
def game():
    p1 = input('Player 1 Turn, please enter "Rock", "Paper" or "Scissors"')
    p2 = input('Player 2 Turn, please enter "Rock", "Paper" or "Scissors"')
    if p1 == p2:
        print("Match ended up as a draw!")
        return
    if (p1 == "Paper" and p2 == "Rock") or (p1 == "Rock" and p2 == "Scissors") or (
            p1 == "Scissors" and p2 == "Paper"):
        print("Player 1 won using " + p1 + "!")
        return
    else:
        print("Player 2 won using " + p2 + "!")
        return


while True:
    choice = main_menu()

    if choice == 'start':
        game_loop()
    elif choice == 'instructions':
        instructions_screen()




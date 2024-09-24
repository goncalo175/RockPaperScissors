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
SKYBLUE = (135, 206, 250)
TEAL = (0, 128, 128)
LIGHTGRAY = (211, 211, 211)

# Define font
fontGameTitle = pygame.font.Font(None, 74)  # None uses default font, 74 is the font size
fontMenuItems = pygame.font.Font(None, 34)


# Define actions for buttons
def start_game():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text('Game Running... Press ESC to return to Menu', fontMenuItems, WHITE, screen, 400, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'  # Return to the menu

        pygame.display.flip()
        clock.tick(60)


def show_instructions():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text("Instructions:", fontGameTitle, WHITE, screen, screen.get_width() // 2, 100)
        draw_text("In Rock, Paper, Scissors, each player simultaneously chooses one of three options:",
                  fontMenuItems, WHITE, screen, screen.get_width() // 2, 250)
        draw_text("Rock, Paper, or Scissors. Rock crushes Scissors, Scissors cut Paper, and Paper covers Rock.",
                  fontMenuItems, WHITE, screen, screen.get_width() // 2, 300)
        draw_text("If one player's choice beats the other's, that player wins the round; if both players choose the "
                  "same", fontMenuItems, WHITE, screen, screen.get_width() // 2, 330)
        draw_text("option, it's a draw. Continue playing until a player wins or you decide to stop.",
                  fontMenuItems, WHITE, screen, screen.get_width() // 2, 360)

        draw_text('Press ESC to return to Menu', fontMenuItems, WHITE, screen, screen.get_width() // 2, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'  # Return to the menu

        pygame.display.flip()
        clock.tick(60)


def exit_game():
    pygame.quit()
    exit()

# Define main screen button properties
button_color = TEAL # color
hover_color = LIGHTGRAY  # Red when hovered
# (screen_width - rect_width) // 2   == formula to get rect in the middle of the screen (X axis)
buttons = [
    {"rect": pygame.Rect((screen.get_width() - 200) // 2, 250, 200, 60), "text": "Start!", "action": start_game},
    {"rect": pygame.Rect((screen.get_width() - 200) // 2, 350, 200, 60), "text": "Instructions", "action": show_instructions},
    {"rect": pygame.Rect((screen.get_width() - 200) // 2, 450, 200, 60), "text": "Exit", "action": exit_game}
]

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


def draw_button(surface, button_color, rect, text):
    pygame.draw.rect(screen, button_color, rect)  # Draw button
    text_surface = fontMenuItems.render(text, True, (255, 255, 255))  # Button label
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)



def main_menu():
    while True:
        screen.fill(BLUE)  # Fill the background color
        mouse_pos = pygame.mouse.get_pos()  # Get current mouse position
        mouse_pressed = pygame.mouse.get_pressed()  # Get mouse button press status

        # Draw menu options
        draw_text('Welcome to Rock, Paper Scissors - Deluxe', fontGameTitle, WHITE, screen, screen.get_width() // 2, 100)

        # Iterate through buttons and handle drawing and interaction
        for button in buttons:
            rect = button["rect"]
            text = button["text"]
            action = button["action"]
            if rect.collidepoint(mouse_pos):
                draw_button(screen, hover_color, rect, text)
                if mouse_pressed[0]:  # Left mouse button is pressed
                    action()

            else:
                draw_button(screen, button_color, rect, text)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_2:  # Instructions option
                    return 'instructions'
                if event.key == pygame.K_ESCAPE:  # Quit option
                    pygame.quit()
                    sys.exit()

        # Update display
        pygame.display.flip()

        # Cap frame rate
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
        start_game()
    elif choice == 'instructions':
        show_instructions()




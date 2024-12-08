import pygame
<<<<<<< HEAD
=======
import sys
>>>>>>> 3b83eb328e66b97704fd18ccc592e52cf460b198

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.Font(None, 36)
        
    def draw(self, screen):
        if self.is_hovered: 
            color = self.hover_color
        else:
            color = self.color

        # Draw the button with rounded corners
        pygame.draw.rect(screen, color, self.rect, border_radius = 18)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        button_text = text_surface.get_rect(center = self.rect.center)  # Center the text
        screen.blit(text_surface, button_text)
        
    def handle_event(self, event):
        # Check for hover and click events
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False


class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.background = pygame.image.load('Graphics/map1.png')
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.title_text = self.font.render("Welcome to Tic-Tac-Tactics", True, (189, 0, 255))
        self.center_title = self.title_text.get_rect(center=(screen.get_width() // 2, 200))

        button_width = 200
        button_height = 50
        button_x = (screen.get_width() - button_width) // 2

<<<<<<< HEAD
        self.start_button = Button(button_x, 300, button_width, button_height, "START", (46, 204, 113), (2, 113, 72))
        self.exit_button = Button(button_x, 400, button_width, button_height, "EXIT", (255, 0, 0), (139, 0, 0))
        self.restart_button = Button(button_x, 500, button_width, button_height, "RESTART", (255, 223, 0), (186, 142, 35))
=======
        self.start_button = Button(button_x, 300, button_width, button_height, "START", (46, 204, 113), (39, 174, 96))
        self.exit_button = Button(button_x, 400, button_width, button_height, "EXIT", (255, 0, 0), (139, 0, 0))
        self.restart_button = Button(button_x, 500, button_width, button_height, "RESTART", (255, 223, 0), (218, 190, 0))
>>>>>>> 3b83eb328e66b97704fd18ccc592e52cf460b198

    def display_menu(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_text, self.center_title)
        self.start_button.draw(self.screen)
        self.exit_button.draw(self.screen)
        self.restart_button.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        if self.start_button.handle_event(event):
            return "start"
        if self.exit_button.handle_event(event):
            return "exit"
        if self.restart_button.handle_event(event):
            return "restart"
        return None
<<<<<<< HEAD

=======
>>>>>>> 3b83eb328e66b97704fd18ccc592e52cf460b198

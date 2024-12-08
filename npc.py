import pygame

pygame.init()

class NPC():
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dialogue = "Well, well, look who thinks they can challenge me. Let’s see how well you hack your way out of this."
        self.font = pygame.font.Font(None, 32)  # You can choose a specific font and size
        self.screen = screen

    def draw(self, camera_offset):
        # Adjust NPC's position by subtracting the camera offset
        adjusted_x = self.x - camera_offset.x
        adjusted_y = self.y - camera_offset.y
        adjusted_rect = pygame.Rect(adjusted_x, adjusted_y, self.width, self.height)

        # Draw the NPC
        pygame.draw.rect(self.screen, (0, 255, 0), adjusted_rect)
    
    def draw_dialogue_box(self):
        # Draw the dialogue box
        box_width = 400
        box_height = 100
        box_x = (self.screen.get_width() - box_width) // 2
        box_y = self.screen.get_height() - box_height - 20  # 20 pixels from the bottom

        # Draw the box
        pygame.draw.rect(self.screen, (0, 0, 0), (box_x, box_y, box_width, box_height))  # Black box
        pygame.draw.rect(self.screen, (255, 255, 255), (box_x + 5, box_y + 5, box_width - 10, box_height - 10))  # White inner box

        # Split the dialogue into lines
        words = self.dialogue.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + ' '
            if self.font.size(test_line)[0] <= box_width - 10:  # 10 pixels padding
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)

        # Draw each line centered within the box with proper spacing
        total_height = len(lines) * self.font.get_height()  # Total height of all lines
        start_y = box_y + (box_height - total_height) // 2  # Center the text vertically

        for line in lines:
            line_surface = self.font.render(line, True, (255, 0, 0))  # Red text
            line_rect = line_surface.get_rect(center=(box_x + box_width // 2, start_y))
            self.screen.blit(line_surface, line_rect)
            start_y += self.font.get_height()  # Move down for the next line
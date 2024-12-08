import pygame
#from handle_movements import Handle

pygame.init()

# class Player():
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#         #self.handle = Handle(x, y)

#     def move(self):
#         key = pygame.key.get_pressed()
#         if key[pygame.K_RIGHT]:
#             self.rect.x += 5
#         elif key[pygame.K_LEFT]:
#             self.rect.x -= 5
#         elif key[pygame.K_UP]:
#             self.rect.y -= 5
#         elif key[pygame.K_DOWN]:
#             self.rect.y += 5
#     def npc_talk(self):
#         font = pygame.font.Font(None, 32)
#         text = font.render("Hello, player!", True, (0,0,0))
#         screen.blit(text, (npc.x, npc.y - 35))

#     def npc_hit(self):
#         return self.rect.colliderect(npc.rect)

#     def draw(self):
#         pygame.draw.rect(screen, (255, 0, 0), self.rect)

#     def update(self):
#         self.draw()
#         self.move()
#         if self.npc_hit():
#             self.npc_talk()

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


# width = 1280
# height = 720
# screen = pygame.display.set_mode((width, height))
# clock = pygame.time.Clock()

# player = Player(100, 100, 50, 50)
# npc = NPC(200, 200, 100, 100)

# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     screen.fill((255, 255, 255))
#     npc.draw()
#     player.update()
    
#     if player.npc_hit():
#         npc.draw_dialogue_box()  # Draw the dialogue box when colliding with NPC
    
#     #self.handle.handle_mov(event)

#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()

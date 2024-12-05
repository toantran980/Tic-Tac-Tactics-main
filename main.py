import pygame, sys
from handle_movements import Handle
from tic_tac_toe import Battle
from tiles import Tile
from pytmx.util_pygame import load_pygame
from menu import GameMenu

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.sprite_group = pygame.sprite.Group()
        self.camera_offset = pygame.Vector2(0, 0)  # Camera offset to adjust view

        # Load the map
        tmx_data = load_pygame('Graphics/map1.tmx')
        self.map_width = tmx_data.width * 128  # Map width in pixels
        self.map_height = tmx_data.height * 128  # Map height in pixels

        # Cycle through all layers and create tiles
        for layer in tmx_data.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 128, y * 128)
                    surf = pygame.transform.scale(surf, (128, 128))
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)

        self.clock = pygame.time.Clock()
        self.handle = Handle(500, 650)
        self.BOARD = pygame.image.load("Graphics/Board.png")
        self.X_IMG = pygame.image.load("Graphics/X.png")
        self.O_IMG = pygame.image.load("Graphics/O.png")
        self.FONT = pygame.font.Font("Font/Pixeltype.ttf")

    def update_camera(self):
        """Update the camera's position based on the character's position."""
        screen_center = pygame.Vector2(self.screen.get_width() // 2, self.screen.get_height() // 2)
        
        # Calculate the target camera offset
        target_offset_x = self.handle.rect.centerx - screen_center.x
        target_offset_y = self.handle.rect.centery - screen_center.y
        
        # Clamp the camera offset to the map boundaries
        self.camera_offset.x = max(0, min(target_offset_x, self.map_width - self.screen.get_width()))
        self.camera_offset.y = max(0, min(target_offset_y, self.map_height - self.screen.get_height()))


    def run(self) -> None:
        menu = GameMenu(self.screen)
        in_menu = True  # Track if we're in the menu

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.K_q:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        is_running = False
                    if event.key == pygame.K_b:
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "threebythree")
                    if event.key == pygame.K_v:
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "")

                if in_menu:
                    menu.display_menu()
                    action = menu.handle_event(event)
                    if action == "start":
                        print("Game starting...")
                        in_menu = False
                    elif action == "exit":
                        print("Exiting game...")
                        pygame.quit()
                        sys.exit()
                    elif action == "restart":
                        print("Restarting game...")
                        in_menu = False  # Restart is treated like start here

            self.handle.handle_mov(event)

            if not in_menu:
                self.update_camera()  # Update camera position
                self.screen.fill((0, 0, 0))

                for sprite in self.sprite_group:
                    offset_pos = sprite.rect.topleft - self.camera_offset
                    self.screen.blit(sprite.image, offset_pos)

                # Render the player at its adjusted position
                character_pos = self.handle.rect.topleft - self.camera_offset
                if 0 <= self.handle.curr_image < len(self.handle.images):
                    self.screen.blit(self.handle.images[self.handle.curr_image], character_pos)
                else:
                    print(f"Error: curr_image index {self.handle.curr_image} is out of range. Total images: {len(self.handle.images)}")

                pygame.display.flip()
                self.clock.tick(60)



if __name__ == '__main__':
    game = Game()
    game.run()
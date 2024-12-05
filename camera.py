import pygame

class Camera:
    def __init__(self, width, height, map_width, map_height):
        self.camera = pygame.Rect(0, 0, width, height)  # Camera viewport
        self.width = width
        self.height = height
        self.map_width = map_width  # Total map size
        self.map_height = map_height
        self.camera_speed = 5  # Optional: Can be used to limit how fast the camera follows the player

    def apply(self, entity):
        """
        Apply the camera offset to an entity's rect.
        This method can be used for both the player and tiles.
        """
        # For tiles (or other objects), we apply the camera offset by adjusting the entity's position
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """
        Update the camera to follow the target (player).
        Target should be an object with x and y attributes (like the player).
        """
        x = -target.x_axis + int(self.width / 2)  # Center camera on player
        y = -target.y_axis + int(self.height / 2)

        # Keep the camera within bounds of the map
        x = min(0, x)  # Camera can't move past the left side of the map
        y = min(0, y)  # Camera can't move past the top side of the map
        x = max(-(self.map_width - self.width), x)  # Camera can't move past the right side of the map
        y = max(-(self.map_height - self.height), y)  # Camera can't move past the bottom side of the map

        # Apply the updated camera position
        self.camera = pygame.Rect(x, y, self.width, self.height)

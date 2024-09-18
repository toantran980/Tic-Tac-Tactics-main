import pygame
import sys

# basic movements left/right/up/down, have not fixed the diagonal movements issue yet...
def handle_mov(event) -> None:

    flags = {
        'move_left': False,
        'move_right': False,
        'move_up': False,
        'move_down': False
    }

    key_mov = {
        pygame.K_LEFT: 'move_left',
        pygame.K_RIGHT: 'move_right',
        pygame.K_UP: 'move_up',
        pygame.K_DOWN: 'move_down'
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            flags[key_mov[event.key]] = True
        else:
            flags[key_mov[event.key]] = False

    # 5 units each time
    if flags['move_left']:
        x_axis -= 5
    elif flags['move_right']:
        x_axis += 5
    elif flags['move_down']:
        y_axis -= 5
    else:
        y_axis += 5
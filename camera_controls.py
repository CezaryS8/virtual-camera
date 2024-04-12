import pygame
from pygame.locals import *

ZOOM_SPEED = 0.1

def handle_controls(camera):
    key_state = pygame.key.get_pressed()

    if key_state[K_w]:
        camera.translate(0, 0, 1)
    if key_state[K_s]:
        camera.translate(0, 0, -1)
    if key_state[K_a]:
        camera.translate(-1, 0, 0)
    if key_state[K_d]:
        camera.translate(1, 0, 0)
    if key_state[K_z]:
        camera.translate(0, 1, 0)
    if key_state[K_c]:
        camera.translate(0, -1, 0)
    
    if key_state[K_UP]:
        camera.rotate(0, 0, 0.01)
    if key_state[K_DOWN]:
        camera.rotate(0, 0, -0.01)
    if key_state[K_LEFT]:
        camera.rotate(0.0, 0.01, 0)
    if key_state[K_RIGHT]:
        camera.rotate(0, -0.01, 0)
    if key_state[K_q]:
        camera.rotate(0.01, 0, 0)
    if key_state[K_e]:
        camera.rotate(-0.01, 0, 0)

    if key_state[K_EQUALS] or key_state[K_PLUS]:
        camera.zoom_in()
    if key_state[K_MINUS]:
        camera.zoom_out()

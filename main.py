import pygame
from data_loader import load_data_from_file
from graphics_renderer import Renderer
from camera import Camera
from camera_controls import handle_controls

def main():
    lines = load_data_from_file('3d_data.txt')
    renderer = Renderer(800, 600)
    camera = Camera()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_controls(camera) 
        
        transformed_lines = []
        for line in lines:
            start = line[0]
            end = line[1]
            transformed_lines.append((start, end))

        renderer.render_scene(transformed_lines, camera)

    pygame.quit()

if __name__ == "__main__":
    main()

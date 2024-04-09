import pygame
import numpy as np

class Renderer:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Virtual Camera")
        self.width = width
        self.height = height

    def render_scene(self, lines, camera):
        self.screen.fill((255, 255, 255))

        for line in lines:
            start = self.project(line[0], camera)
            end = self.project(line[1], camera)
            if start is not None and end is not None:
                pygame.draw.line(self.screen, (0, 0, 0), start, end)

        pygame.display.flip()

    def project(self, point, camera):
        x, y, z = point.x - camera.pos[0], point.y - camera.pos[1], point.z - camera.pos[2]

        rot_matrix = self.get_rotation_matrix(camera.rot)
        transformed = np.dot(rot_matrix, np.array([x, y, z]))

        x, y, z = transformed[0], transformed[1], transformed[2]

        if z > 0:
            scale = 1 / z
            x_screen = int(x * scale * self.width / 2 + self.width / 2)
            y_screen = int(-y * scale * self.height / 2 + self.height / 2)
            return x_screen, y_screen
        else:
            return None

    def get_rotation_matrix(self, rot):
        yaw, pitch, roll = rot
        rotation_matrix = np.array([
            [np.cos(yaw) * np.cos(pitch), np.cos(yaw) * np.sin(pitch) * np.sin(roll) - np.sin(yaw) * np.cos(roll), np.cos(yaw) * np.sin(pitch) * np.cos(roll) + np.sin(yaw) * np.sin(roll)],
            [np.sin(yaw) * np.cos(pitch), np.sin(yaw) * np.sin(pitch) * np.sin(roll) + np.cos(yaw) * np.cos(roll), np.sin(yaw) * np.sin(pitch) * np.cos(roll) - np.cos(yaw) * np.sin(roll)],
            [-np.sin(pitch), np.cos(pitch) * np.sin(roll), np.cos(pitch) * np.cos(roll)]
        ])
        return rotation_matrix

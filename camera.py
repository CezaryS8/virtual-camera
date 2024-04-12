import numpy as np

class Camera:
    def __init__(self):
        self.pos = np.array([0, 0, 0])
        self.rot = np.array([0.0, 0.0, 0.0])
        self.zoom = 1.0  # Initial zoom level

    def translate(self, dx, dy, dz):
        translation_matrix = np.array([[1, 0, 0, dx],
                                       [0, 1, 0, dy],
                                       [0, 0, 1, dz],
                                       [0, 0, 0, 1]])
        self.pos = np.dot(translation_matrix, np.append(self.pos, 1))[:3]

    def rotate(self, yaw, pitch, roll):
        self.rot[0] += yaw
        self.rot[1] += pitch
        self.rot[2] += roll

    def zoom_in(self):
        self.zoom *= 1.03  # Increase zoom level

    def zoom_out(self):
        self.zoom /= 1.03  # Decrease zoom level

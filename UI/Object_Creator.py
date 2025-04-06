"""from glass_engine import *
from glass import Vertex"""
from pyglm import glm
import math
import random


"""class Cuboid(Mesh):
    def __init__(self, base_vertex: glm.vec3, width: float, height: float, depth: float):
        Mesh.__init__(self)
        self.base_vertex = base_vertex
        self.width = width
        self.height = height
        self.depth = depth
        self.start_building()
        self.material = Material()
        self.material.diffuse = random_color()

    def build(self):
        x, y, z = self.base_vertex.x, self.base_vertex.y, self.base_vertex.z

        # Define 8 vertices of the cuboid
        vertices = [
            glm.vec3(x, y, z),  # 0: Bottom-front-left
            glm.vec3(x + self.width, y, z),  # 1: Bottom-front-right
            glm.vec3(x + self.width, y + self.height, z),  # 2: Top-front-right
            glm.vec3(x, y + self.height, z),  # 3: Top-front-left
            glm.vec3(x, y, z + self.depth),  # 4: Bottom-back-left
            glm.vec3(x + self.width, y, z + self.depth),  # 5: Bottom-back-right
            glm.vec3(x + self.width, y + self.height, z + self.depth),  # 6: Top-back-right
            glm.vec3(x, y + self.height, z + self.depth)  # 7: Top-back-left
        ]

        for v in vertices:
            self.vertices.append(Vertex(position=v))

        # Define 12 triangles (2 per face)
        faces = [
            (0, 1, 2), (0, 2, 3),  # Front face
            (1, 5, 6), (1, 6, 2),  # Right face
            (5, 4, 7), (5, 7, 6),  # Back face
            (4, 0, 3), (4, 3, 7),  # Left face
            (3, 2, 6), (3, 6, 7),  # Top face
            (4, 5, 1), (4, 1, 0)  # Bottom face
        ]

        for f in faces:
            self.indices.append(glm.uvec3(f[0], f[1], f[2]))


class OpenCuboid(Mesh):
    def __init__(self, position: glm.vec3, width: float, height: float, depth: float, open_face: str = None):
        Mesh.__init__(self)
        self.position = position
        self.width = width
        self.height = height
        self.depth = depth
        self.open_face = open_face  # Face to leave open
        self.start_building()
        self.material = Material()
        self.material.diffuse = random_color()

    def build(self):
        x, y, z = self.position
        w, h, d = self.width, self.height, self.depth

        # Define 8 vertices
        vertices = [
            glm.vec3(x, y, z),  # 0: Front-bottom-left
            glm.vec3(x + w, y, z),  # 1: Front-bottom-right
            glm.vec3(x + w, y + h, z),  # 2: Front-top-right
            glm.vec3(x, y + h, z),  # 3: Front-top-left
            glm.vec3(x, y, z - d),  # 4: Back-bottom-left
            glm.vec3(x + w, y, z - d),  # 5: Back-bottom-right
            glm.vec3(x + w, y + h, z - d),  # 6: Back-top-right
            glm.vec3(x, y + h, z - d)  # 7: Back-top-left
        ]

        # Add vertices to mesh
        for v in vertices:
            self.vertices.append(Vertex(position=v))

        # Define faces using triangle indices
        faces = {
            "front": [(0, 1, 2), (0, 2, 3)],
            "right": [(1, 5, 6), (1, 6, 2)],
            "back": [(5, 4, 7), (5, 7, 6)],
            "left": [(4, 0, 3), (4, 3, 7)],
            "top": [(3, 2, 6), (3, 6, 7)],
            "bottom": [(4, 5, 1), (4, 1, 0)]
        }

        # Add all faces except the open one
        for face, triangles in faces.items():
            if face != self.open_face:
                for f in triangles:
                    self.indices.append(glm.uvec3(*f))


def random_color():
    return glm.vec3(random.random(), random.random(), random.random())

def compute_centroid(position, width, height, depth):
    x, y, z = position
    centroid = glm.vec3(
        x + width / 2,
        y + height / 2,
        z - depth / 2  # Adjust based on your coordinate system
    )
    return centroid
"""

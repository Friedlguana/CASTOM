import math
import numpy as np

from collections import defaultdict
MAX_WORKERS = 8
MIN_CELL_SIZE = 100  # Reduced from 250mm for better collision detection


import math
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Item:
    def __init__(self, item_id, name, width, depth, height, mass, priority, expiry, uses, pref_zone,fixed_position=False):
        # Convert cm to mm
        self.original_width = int(width * 10)
        self.original_depth = int(depth * 10)
        self.original_height = int(height * 10)

        self.item_id = item_id
        self.name = name
        self.mass = mass
        self.priority = priority
        self.expiry = expiry
        self.uses = uses
        self.pref_zone = pref_zone
        self.rotation = 0
        self.x = self.y = self.z = None
        self.placed = False
        self.placed_cont = None
        self.apply_rotation()
        self.fixed_position = fixed_position

    def apply_rotation(self):
        rotations = self.get_rotation_states()
        self.width, self.depth, self.height = rotations[self.rotation % 6]
        self.volume = self.width * self.depth * self.height

    def get_rotation_states(self):
        return [
            (self.original_width, self.original_depth, self.original_height),
            (self.original_width, self.original_height, self.original_depth),
            (self.original_depth, self.original_width, self.original_height),
            (self.original_depth, self.original_height, self.original_width),
            (self.original_height, self.original_width, self.original_depth),
            (self.original_height, self.original_depth, self.original_width)
        ]
    def is_colliding(self, obj):

        def centroid(obj):
            xc = float(obj.x) + obj.original_width / 2
            yc = float(obj.y) + obj.original_depth / 2
            zc = float(obj.z) + obj.original_height / 2

            return xc, yc, zc

        xsc, ysc, zsc = centroid(self)
        xc, yc, zc = centroid(obj)

        b_self = self.original_width
        b_obj = obj.original_width
        d_self = self.original_depth
        d_obj = obj.original_depth
        h_self = self.original_height
        h_obj = obj.original_height

        def colliding_xy(xsc, xc, b_self, b_obj):

            dist_cent = abs(xsc - xc)

            if dist_cent < b_self / 2 + b_obj / 2:
                return True

        def colliding_yz(ysc, yc, d_self, d_obj):

            dist_cent = abs(ysc - yc)

            if dist_cent < d_self / 2 + d_obj / 2:
                return True

        def colliding_xz(zsc, zc, h_self, h_obj):

            dist_cent = abs(zsc - zc)

            if dist_cent < h_self / 2 + h_obj / 2:
                return True

        #Optimise !!

        if colliding_xz(zsc, zc, h_self, h_obj):
            if colliding_yz(ysc, yc, d_self, d_obj):
                if colliding_xy(xsc, xc, b_self, b_obj):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def sort_priority(self):
        return self.z

    def Use_Item(self,no_of_uses):

        self.uses -= no_of_uses



class Container:
    def __init__(self, container_id, width, depth, height, zone):
        self.container_id = container_id
        self.original_width = int(width * 10)
        self.original_depth = int(depth * 10)
        self.original_height = int(height * 10)
        self.zone = zone
        self.grid = {}
        self.cell_size = MIN_CELL_SIZE

    def get_grid_cells(self, item):
        x = int(item.x)
        y = int(item.y)
        z = int(item.z)
        width = int(item.width)
        depth = int(item.depth)
        height = int(item.height)
        x_start = x // self.cell_size
        x_end = (x+width) // self.cell_size
        y_start = y // self.cell_size
        y_end = (y + depth) // self.cell_size
        z_start = z // self.cell_size
        z_end = (z + height) // self.cell_size

        return [
            (x, y, z)
            for x in range(x_start, x_end + 1)
            for y in range(y_start, y_end + 1)
            for z in range(z_start, z_end + 1)
        ]

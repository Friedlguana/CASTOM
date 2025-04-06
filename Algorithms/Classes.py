import math
import numpy as np
class Item:

    def __init__(self, item_id, name, width, depth, height, mass, priority, expiry, uses, pref_zone, x=None, y=None,
                 z=None, placed_cont=None, placed =False,status = None):
        self.item_id = item_id
        self.name = name
        self.original_width = int(math.ceil(10*width))
        self.original_depth = int(math.ceil(10*depth))
        self.original_height = int(math.ceil(10*height))
        self.rotation = 0

        self.apply_rotation()

        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.placed_cont = placed_cont
        self.pref_zone = pref_zone
        self.priority = int(priority)
        self.expiry = expiry
        self.uses = uses
        self.status = status
        self.volume = self.original_width * self.original_depth * self.original_height
        self.fixed_position = all([x is not None, y is not None, z is not None])
        self.placed = placed or self.fixed_position
        if any(d < 0 for d in (self.width, self.depth, self.height)):
            raise ValueError(f"Invalid dimensions for item {item_id}")

    def apply_rotation(self):
        """Update dimensions based on rotation state using 3D permutations"""
        rotations = [
            (self.original_width, self.original_depth, self.original_height),
            (self.original_width, self.original_height, self.original_depth),
            (self.original_depth, self.original_width, self.original_height),
            (self.original_depth, self.original_height, self.original_width),
            (self.original_height, self.original_width, self.original_depth),
            (self.original_height, self.original_depth, self.original_width)
        ]
        self.width, self.depth, self.height = rotations[self.rotation % 6]

    def get_rotation_states(self):
        """Return all possible dimension permutations for rotation detection"""
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
    def update_status(self,status):
        self.status = status


class Container:
    def __init__(self, zone, container_id, width, depth, height):
        self.zone = zone
        self.container_id = container_id
        self.original_width = int(math.floor(10*width))
        self.original_depth = int(math.floor(10*depth))
        self.original_height = int(math.floor(10*height))
        self.zone = zone


        if any(d <= 0 for d in (self.original_width, self.original_depth, self.original_height)):
            raise ValueError(f"Invalid dimensions for container {container_id}")

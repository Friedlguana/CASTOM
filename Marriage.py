import math
import numpy as np
import csv
from itertools import permutations
class Item:
    def __init__(self, item_id, name, width, depth, height, mass, priority, expiry, uses, pref_zone,x=None,y=None,z=None,placed_cont=None,placed=False):
        self.item_id = item_id
        self.name = name
        self.width = math.ceil(width)
        self.depth = math.ceil(depth)
        self.height = math.ceil(height)
        self.mass=mass
        self.x=x
        self.y=y
        self.z=z
        self.placed_cont=placed_cont
        self.pref_zone=pref_zone
        self.priority = priority
        self.expiry=expiry
        self.uses=uses
        self.volume = self.width * self.depth * self.height
        self.placed = placed


class Container:
    def __init__(self, zone, container_id, width, depth, height):
        self.zone=zone
        self.container_id = container_id
        self.width = math.floor(width)
        self.depth = math.floor(depth)
        self.height = math.floor(height)
        self.remaining_space = np.zeros((self.width, self.depth, self.height), dtype=np.uint8)


def sort_items(items):
    return sorted(items, key=lambda x: (-x.priority, -x.volume))


def best_fit(items, container):

    def get_valid_rotations(item):
        rotations = set(permutations([item.width, item.depth, item.height]))
        return [(w, d, h) for w, d, h in rotations
                if w <= container.width
                and d <= container.depth
                and h <= container.height]

    def find_best_position(rotations):
        best_score = float('inf')
        best_pos = None
        best_rot = None

        for width, depth, height in rotations:
            # Quick dimension check
            if width > container.width or depth > container.depth or height > container.height:
                continue

            # Search space reduced using numpy slicing
            max_w = container.width - width
            max_d = container.depth - depth
            max_h = container.height - height

            if max_w < 0 or max_d < 0 or max_h < 0:
                continue

            # Vectorized search for first valid position
            for h in range(max_h + 1):
                for d in range(max_d + 1):
                    window = container.remaining_space[:max_w + 1, d:d + depth, h:h + height]
                    valid_columns = np.where(
                        (window.sum(axis=(1, 2)) == 0) &
                        (np.arange(window.shape[0]) + width <= container.width)
                    )[0]

                    if valid_columns.size > 0:
                        w = valid_columns[0]
                        score = h * 1000 + d * 1000000 + w  # Prioritize low height/depth
                        if score < best_score:
                            best_score = score
                            best_pos = (w, d, h)
                            best_rot = (width, depth, height)
                            break  # Take first valid in best rotation
                if best_pos:
                    break
            if best_pos:
                break

        return best_pos, best_rot

    for item in items:
        if item.placed:
            continue

        rotations = sorted(get_valid_rotations(item),
                           key=lambda r: (-r[0] * r[1] * r[2], -min(r)))  # Prefer larger volumes first

        if not rotations:
            continue

        best_pos, best_rot = find_best_position(rotations)

        if best_pos:
            w, d, h = best_pos
            width, depth, height = best_rot

            # Mark space as occupied
            container.remaining_space[w:w + width, d:d + depth, h:h + height] = 1
            item.placed = True
            item.placed_cont=container.container_id
            item.x=int(w)
            item.y=int(h)
            item.z=int(d)
            item.width=int(width)
            item.height=int(height)
            item.depth=int(depth)



def start_BFD():
    for container in containers:#Placing things in the right container if possible
        items = []
        for i in Overall_List:
            if i.placed == False and i.pref_zone==container.zone:
                items.append(i)
        sorted_items = sort_items(items)
        best_fit(sorted_items, container)
    for container in containers:#Placing the unplaced if possible
        items = []
        for i in Overall_List:
            if i.placed == False:
                items.append(i)
        sorted_items = sort_items(items)
        best_fit(sorted_items, container)
    for item in Overall_List:
        print("Item id:",item.item_id," Start Cords::",item.x,item.y,item.z," Dimensions:",item.width,item.height,item.depth," Container:",item.placed_cont,"  Pref zone:",item.pref_zone," Priority:",item.priority)

def remove_items():
    for item_id in To_Remove_List:
        for item in Overall_List:
            if item.item_id==item_id:
                for container in containers:
                    if container.container_id==item.placed_cont:
                        w=item.x
                        h=item.y
                        d=item.z
                        container.remaining_space[w:w + item.width, d:d + item.depth, h:h + item.height] = 0
                        item.placed = False
                        item.placed_cont = None
                        item.x = None
                        item.y = None
                        item.z = None
                        break
def add_items():
    Overall_List.extend(To_Add_list)
    initialise()
def initialise():
    for item in Overall_List:
        if item.placed:
            for container in containers:
                if container.container_id == item.placed_cont:
                    w = item.x
                    h = item.y
                    d = item.z
                    container.remaining_space[w:w + item.width, d:d + item.depth, h:h + item.height] = 1
                    break
# Overall list is the list containing all items.
Overall_List =[]
itemobj=open('items.csv','r',newline='')
csvreader=csv.reader(itemobj)
head=next(csvreader)
for row in csvreader:
    Overall_List.append(Item(row[0],row[1],float(row[2]),float(row[3]),float(row[4]),float(row[5]),int(row[6]),row[7],int(row[8]),row[9]))
itemobj.close()

#you input the item id to remove that object from placement
'''To_Remove_List = ["001","002","003","040"]'''
#you give me the item object that needs to be added
'''To_Add_list=[Item("041", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True)]'''

containers=[]
containerobj=open('containers.csv','r',newline='')
csvreader=csv.reader(containerobj)
head=next(csvreader)
for row in csvreader:
    containers.append(Container(row[0],row[1],int(row[2]),int(row[3]),int(row[4])))
containerobj.close()
initialise()
while True:
    choice=int(input("Enter Choice:"))
    if choice==1:
        start_BFD()
    elif choice==2:
        remove_items()
    elif choice==3:
        add_items()
    else :
        break

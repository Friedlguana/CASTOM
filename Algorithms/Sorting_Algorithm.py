import math
import csv
import pickle


from .Classes import *
from py3dbp import Packer, Bin as PyBin, Item as PyItem

def sort_items(items):
     return sorted(items, key=lambda x: (-x.priority, -x.volume))


def pack_container(container, items):
    """Pack items into a single container using py3dbp's logic"""
    packer = Packer()
    packer.add_bin(PyBin(
        container.container_id,
        container.original_width,
        container.original_depth,
        container.original_height,
        max_weight=1_000_000
    ))

    for item in items:
        if not item.placed and not item.fixed_position:
            packer.add_item(PyItem(
                item.item_id,
                item.original_width,
                item.original_depth,
                item.original_height,
                0
            ))

    packer.pack(bigger_first=True)
    return packer.bins[0] if packer.bins else None


def determine_rotation(original_item, packed_dims):
    """Calculate rotation based on packed dimensions"""
    try:
        return original_item.get_rotation_states().index(packed_dims)
    except ValueError:
        return 0


def start_BFD(zone_map):
    # First pass: preferred zones
    for container in containers:
        preferred_items = [i for i in Overall_List
                           if not i.placed
                           and not i.fixed_position
                           and i.pref_zone == container.zone]

        if not preferred_items:
            continue

        sorted_items = sort_items(preferred_items)
        py3dbp_bin = pack_container(container, sorted_items)

        if py3dbp_bin:
            update_container_placements(container, py3dbp_bin)

    # Second pass: remaining items
    remaining = [i for i in Overall_List if not i.placed and not i.fixed_position]
    for container in containers:
        if not remaining:
            break

        sorted_items = sort_items(remaining)
        py3dbp_bin = pack_container(container, sorted_items)

        if py3dbp_bin:
            update_container_placements(container, py3dbp_bin)
            remaining = [i for i in Overall_List if not i.placed and not i.fixed_position]
    # Second pass: remaining items
    remaining = [i for i in Overall_List if not i.placed and not i.fixed_position]
    for container in containers:
        if not remaining:
            break

        sorted_items = sort_items(remaining)
        py3dbp_bin = pack_container(container, sorted_items)

        if py3dbp_bin:
            for packed_item in py3dbp_bin.items:
                original_item = next(i for i in Overall_List if i.item_id == packed_item.name)

                packed_dims = (packed_item.width, packed_item.depth, packed_item.height)
                original_item.rotation = determine_rotation(original_item, packed_dims)
                original_item.apply_rotation()
                original_item.placed = True
                original_item.placed_cont = container.container_id
                original_item.x = packed_item.position[0]
                original_item.y = packed_item.position[2]
                original_item.z = packed_item.position[1]

    # Print results
    print("\nPlacement Results:")
    for item in Overall_List:
        item_dict.update({item.item_id : item})
        status = "Fixed item in" if item.fixed_position else "Placed in" if item.placed else "Unplaced item"
        print(f"Item {item.item_id}: {status} {item.placed_cont or 'with'} "
              f"Position: ({item.x}, {item.y}, {item.z})"
              f"Dimensions: {item.original_width} {item.original_depth} {item.original_height} "
              )
    with open("item_data.bin", "ab") as file:
        pickle.dump(item_dict, file)


def update_container_placements(container, py3dbp_bin):
    for packed_item in py3dbp_bin.items:
        original_item = next(i for i in Overall_List if i.item_id == packed_item.name)
        original_item.x, original_item.y, original_item.z = packed_item.position
        original_item.rotation = determine_rotation(
            original_item,
            (packed_item.width, packed_item.depth, packed_item.height)
        )
        original_item.apply_rotation()

        if validate_placement(original_item, container):
            original_item.placed = True
            original_item.placed_cont = container.container_id
        else:
            original_item.placed = False
            original_item.x = original_item.y = original_item.z = None


def load_containers(file_path):
    containers = []
    containerobj = open(file_path, 'r', newline='')
    csvreader = csv.reader(containerobj)
    headCont = next(csvreader)

    for row in csvreader:
        containers.append(Container(row[0], row[1], float(row[2]), float(row[3]), float(row[4])))

        cont_dict.update({row[1]: Container(row[0], row[1], float(row[2]), float(row[3]), float(row[4]))})

    with open("container_data.bin", "ab") as file:
        pickle.dump(cont_dict, file)

    containerobj.close()
    return containers


def load_items(file_path):
    items = []
    itemobj = open(file_path, 'r', newline='')
    csvreader = csv.reader(itemobj)
    headItem = next(csvreader)
    for row in csvreader:
        Overall_List.append(
            Item(int(row[0]), row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), int(row[6]), row[7],
                 int(row[8].split()[0]), row[9]))
    itemobj.close()
    return items

def print_results():
    print("\nPlacement Results:")
    for item in Overall_List:
        status = "Fixed" if item.fixed_position else "Placed" if item.placed else "Unplaced"
        print(f"Item {item.item_id}: {status} in {item.placed_cont or 'N/A'} "
              f"(Preferred: {item.pref_zone}) "
              f"Position: ({item.x}, {item.y}, {item.z}) "
              f"Dimensions: {item.width} {item.depth} {item.height}")


def remove_items(remove_list):
    for item_id in remove_list:
        for item in Overall_List:
            if item.item_id == item_id and not item.fixed_position:
                item.placed = False
                item.placed_cont = None
                item.x = item.y = item.z = None


def add_items(new_items):
    Overall_List.extend(new_items)
    initialise()


def initialise():
    for item in Overall_List:
        if not item.fixed_position:
            item.placed = False
            item.placed_cont = None
            item.x = item.y = item.z = None


Overall_List =[]
def OpenFileSort(item_fname,cont_fname):

    load_items(item_fname)
    load_containers(cont_fname)

    initialise()

    zone_map = {}
    for c in containers:
        if c.zone not in zone_map:
            zone_map[c.zone] = []
        zone_map[c.zone].append(c)

    return start_BFD(zone_map) , "container_data.bin"




#you input the item id to remove that object from placement
To_Remove_List = []
#you give me the item object that needs to be added
To_Add_list=[]

item_dict = {}
cont_dict = {}

containers=[]


initialise()






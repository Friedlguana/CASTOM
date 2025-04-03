import math
import csv
import pickle


from .Classes import *
from py3dbp import Packer, Bin as PyBin, Item as PyItem

def sort_items(items):
    return sorted(items, key=lambda x: (-x.priority, -x.volume))


def pack_container(container, items):
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
                item.width,
                item.depth,
                item.height,
                0
            ))

    packer.pack(bigger_first=True)
    return packer.bins[0] if packer.bins else None


def determine_rotation(original_item, packed_dims):
    try:
        return [
            (original_item.original_width, original_item.original_depth, original_item.original_height),
            (original_item.original_width, original_item.original_height, original_item.original_depth),
            (original_item.original_depth, original_item.original_width, original_item.original_height),
            (original_item.original_depth, original_item.original_height, original_item.original_width),
            (original_item.original_height, original_item.original_width, original_item.original_depth),
            (original_item.original_height, original_item.original_depth, original_item.original_width)
        ].index(packed_dims)
    except ValueError:
        return 0


def validate_placement(item, container):
    return (item.x + item.width <= container.original_width and
            item.y + item.depth <= container.original_depth and
            item.z + item.height <= container.original_height)


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

    for item in Overall_List:
        item_dict.update({item.item_id : item})

    with open("item_data.bin", "wb") as file:
        pickle.dump(item_dict, file)
    return "item_data.bin"


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
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            containers.append(Container(
                container_id=row['container_id'],
                width=float(row['width_cm']),
                depth=float(row['depth_cm']),
                height=float(row['height_cm']),
                zone=row['zone']
            ))
    return containers


def load_items(file_path):
    items = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(Item(
                item_id=row['item_id'],
                name=row['name'],
                width=float(row['width_cm']),
                depth=float(row['depth_cm']),
                height=float(row['height_cm']),
                mass= float(row["mass_kg"]),
                priority=int(row['priority']),
                expiry=str(row["expiry_date"]),
                uses=int(row['usage_limit']),
                pref_zone=row['preferred_zone']
            ))
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


def OpenFileSort(item_fname,cont_fname):
    global Overall_List
    Overall_List =load_items(item_fname)
    global containers
    containers = load_containers(cont_fname)

    initialise()

    zone_map = {}
    for c in containers:
        if c.zone not in zone_map:
            zone_map[c.zone] = []
        zone_map[c.zone].append(c)

    path = start_BFD(zone_map)
    print_results()
    return (item_fname,cont_fname)




#you input the item id to remove that object from placement
To_Remove_List = []
#you give me the item object that needs to be added
To_Add_list=[]

item_dict = {}
cont_dict = {}












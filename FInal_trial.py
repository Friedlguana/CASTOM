import math
import csv
from py3dbp import Packer, Bin as PyBin, Item as PyItem


class Item:
    def __init__(self, item_id, name, width, depth, height, priority, pref_zone,
                 x=None, y=None, z=None, placed_cont=None, placed=False):
        self.item_id = item_id
        self.name = name

        # Original dimensions and rotation tracking
        self.original_width = int(math.ceil(width))
        self.original_depth = int(math.ceil(depth))
        self.original_height = int(math.ceil(height))
        self.rotation = 0  # 0-5 rotation state

        # Apply initial rotation
        self.apply_rotation()

        # Position and placement info
        self.x = x
        self.y = y
        self.z = z
        self.placed_cont = placed_cont
        self.pref_zone = pref_zone
        self.priority = int(priority)
        self.volume = self.width * self.depth * self.height
        self.fixed_position = all([x is not None, y is not None, z is not None])
        self.placed = placed or self.fixed_position

    def apply_rotation(self):
        """Update dimensions based on rotation state"""
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
        """Return all possible dimension permutations"""
        return [
            (self.original_width, self.original_depth, self.original_height),
            (self.original_width, self.original_height, self.original_depth),
            (self.original_depth, self.original_width, self.original_height),
            (self.original_depth, self.original_height, self.original_width),
            (self.original_height, self.original_width, self.original_depth),
            (self.original_height, self.original_depth, self.original_width)
        ]


class Container:
    def __init__(self, container_id, width, depth, height, zone):
        self.container_id = container_id
        self.width = int(math.floor(width))
        self.depth = int(math.floor(depth))
        self.height = int(math.floor(height))
        self.zone = zone


def sort_items(items):
    return sorted(items, key=lambda x: (-x.priority, -x.volume))


def pack_container(container, items):
    """Attempt to pack items into a single container"""
    packer = Packer()
    packer.add_bin(PyBin(
        container.container_id,
        container.width,
        container.depth,
        container.height,
        max_weight=1_000_000
    ))

    for item in items:
        if not item.placed and not item.fixed_position:
            packer.add_item(PyItem(
                item.item_id,
                item.width,
                item.depth,
                item.height,
                0  # Weight not used
            ))

    packer.pack(bigger_first=True)
    return packer.bins[0] if packer.bins else None


def determine_rotation(original_item, packed_dims):
    """Match packed dimensions to rotation state"""
    try:
        return original_item.get_rotation_states().index(packed_dims)
    except ValueError:
        return 0


def start_BFD(zone_map):
    # First pass: preferred zones
    for container in containers:
        items_to_pack = [i for i in Overall_List
                         if not i.placed
                         and not i.fixed_position
                         and i.pref_zone == container.zone]

        if not items_to_pack:
            continue

        sorted_items = sort_items(items_to_pack)
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


def update_container_placements(container, py3dbp_bin):
    """Update positions for all items in a container"""
    for packed_item in py3dbp_bin.items:
        original_item = next(i for i in Overall_List if i.item_id == packed_item.name)

        # Update dimensions and rotation first
        packed_dims = (packed_item.width, packed_item.depth, packed_item.height)
        original_item.rotation = determine_rotation(original_item, packed_dims)
        original_item.apply_rotation()

        # Update position if valid
        if packed_item.position != [0, 0, 0]:
            original_item.x = packed_item.position[0]
            original_item.y = packed_item.position[1]
            original_item.z = packed_item.position[2]
            original_item.placed = True
            original_item.placed_cont = container.container_id


def try_pack_item(item, container):
    """Attempt to pack a single item into a container"""
    temp_bin = pack_container(container, [item])
    if temp_bin and temp_bin.items:
        packed_item = temp_bin.items[0]

        # Update item properties
        item.rotation = determine_rotation(item,
                                           (packed_item.width,
                                            packed_item.depth,
                                            packed_item.height))

        item.apply_rotation()
        item.placed = True
        item.placed_cont = container.container_id
        item.x = packed_item.position[0]
        item.y = packed_item.position[1]  # y and z swapped for py3dbp's coordinate system
        item.z = packed_item.position[2]
        return True
    return False


def load_containers():
    containers = []
    with open(r"C:\Users\Saket Ramchandra\Downloads\containers.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                containers.append(Container(
                    container_id=row['container_id'],
                    width=float(row['width_cm']),
                    depth=float(row['depth_cm']),
                    height=float(row['height_cm']),
                    zone=row['zone']
                ))
            except Exception as e:
                print(f"Error loading container {row['container_id']}: {str(e)}")
    return containers


def load_items():
    items = []
    with open(r"C:\Users\Saket Ramchandra\Downloads\input_items.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                items.append(Item(
                    item_id=row['item_id'],
                    name=row['name'],
                    width=float(row['width_cm']),
                    depth=float(row['depth_cm']),
                    height=float(row['height_cm']),
                    priority=int(row['priority']),
                    pref_zone=row['preferred_zone']
                ))
            except Exception as e:
                print(f"Error loading item {row['item_id']}: {str(e)}")
    return items


def print_results():
    print("\nPlacement Results:")
    for item in Overall_List:
        status = "Fixed" if item.fixed_position else "Placed" if item.placed else "Unplaced"
        print(f"Item {item.item_id}: {status} in {item.placed_cont or 'N/A'} "
              f"(Zone: {item.pref_zone}) "
              f"Dimensions: {item.width} {item.depth} {item.height} "
              f"Position: ({item.x}, {item.y}, {item.z})")


def remove_items(remove_list):
    for item_id in remove_list:
        for item in Overall_List:
            if item.item_id == item_id and not item.fixed_position:
                item.placed = False
                item.placed_cont = None
                item.x = item.y = item.z = None
                item.rotation = 0
                item.apply_rotation()


def add_items(new_items):
    for new_item in new_items:
        if not any(i.item_id == new_item.item_id for i in Overall_List):
            Overall_List.append(new_item)
    initialise()


def initialise():
    for item in Overall_List:
        if not item.fixed_position:
            item.placed = False
            item.placed_cont = None
            item.x = item.y = item.z = None
            item.rotation = 0
            item.apply_rotation()


# Initialize data from CSVs
containers = load_containers()
Overall_List = load_items()

# Create zone mapping
zone_map = {}
for container in containers:
    if container.zone not in zone_map:
        zone_map[container.zone] = []
    zone_map[container.zone].append(container)

# Main menu
while True:
    print("\n1. Run BFD Placement")
    print("2. Remove Items")
    print("3. Add Items")
    print("4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == '1':
        initialise()
        start_BFD(zone_map)
        print_results()
    elif choice == '2':
        remove_ids = input("Enter item IDs to remove (comma-separated): ").split(',')
        remove_items([id.strip() for id in remove_ids])
        print("Items removed successfully")
    elif choice == '3':
        new_items = load_items(input("Enter CSV path for new items: "))
        add_items(new_items)
        print("Items added successfully")
    elif choice == '4':
        break
    else:
        print("Invalid choice")

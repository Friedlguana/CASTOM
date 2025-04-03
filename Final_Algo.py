import math
from py3dbp import Packer, Bin as PyBin, Item as PyItem


class Item:
    def __init__(self, item_id, name, width, depth, height, priority, pref_cont,
                 x=None, y=None, z=None, placed_cont=None, placed=False):
        self.item_id = item_id
        self.name = name

        # Store original dimensions and rotation state
        self.original_width = int(math.ceil(width))
        self.original_depth = int(math.ceil(depth))
        self.original_height = int(math.ceil(height))
        self.rotation = 0  # Rotation state (0-5)

        # Apply initial rotation
        self.apply_rotation()

        # Position and placement tracking
        self.x = x
        self.y = y
        self.z = z
        self.placed_cont = placed_cont
        self.pref_cont = pref_cont
        self.priority = int(priority)  # Ensure priority is integer
        self.volume = self.width * self.depth * self.height
        self.fixed_position = all([x is not None, y is not None, z is not None])
        self.placed = placed or self.fixed_position

        # Validate dimensions
        if any(d <= 0 for d in (self.width, self.depth, self.height)):
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


class Container:
    def __init__(self, container_id, width, depth, height):
        self.container_id = container_id
        self.width = int(math.floor(width))
        self.depth = int(math.floor(depth))
        self.height = int(math.floor(height))

        if any(d <= 0 for d in (self.width, self.depth, self.height)):
            raise ValueError(f"Invalid dimensions for container {container_id}")


def sort_items(items):
    return sorted(items, key=lambda x: (-x.priority, -x.volume))


def pack_container(container, items):
    """Pack items into a single container using py3dbp's logic"""
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


def start_BFD():
    # First pass: preferred containers
    for container in containers:
        preferred_items = [i for i in Overall_List
                           if not i.fixed_position
                           and not i.placed
                           and i.pref_cont == container.container_id]

        sorted_items = sort_items(preferred_items)
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
        status = "Fixed item in" if item.fixed_position else "Placed in" if item.placed else "Unplaced item"
        print(f"Item {item.item_id}: {status} {item.placed_cont or 'with'} "
              f"Position: ({item.x}, {item.y}, {item.z})"
              f"Dimensions: {item.width} {item.depth} {item.height} "
              )


def remove_items():
    for item_id in To_Remove_List:
        for item in Overall_List:
            if item.item_id == item_id and not item.fixed_position:
                item.placed = False
                item.placed_cont = None
                item.x = item.y = item.z = None
                item.rotation = 0
                item.apply_rotation()
        for item in Overall_List:
            status = "Fixed item in" if item.fixed_position else "Placed in" if item.placed else "Unplaced item"
            print(f"Item {item.item_id}: {status} {item.placed_cont or 'with'} "
                  f"Position: ({item.x}, {item.y}, {item.z})"
                  f"Dimensions: {item.width} {item.depth} {item.height} "
                  )


def add_items():
    for new_item in To_Add_list:
        if not any(i.item_id == new_item.item_id for i in Overall_List):
            if any(d <= 0 for d in (new_item.width, new_item.depth, new_item.height)):
                print(f"Skipping invalid item {new_item.item_id}")
                continue
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


# Data initialization
Overall_List = [
    Item("001", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True),
    Item("002", "Rotatable Box", 10.5, 20.2, 30.8, 10, "contB"),
    Item("003", "Rotatable Box", 10.5, 20.2, 30.8, 99, "contB"),
    Item("004", "Rotatable Box", 10.5, 2.2, 0.8, 80, "contA"),
    Item("005", "Rotatable Box", 15.5, 20.2, 31.8, 15, "contB"),
    Item("006", "Rotatable Box", 1.5, 20.2, 30.8, 10, "contA"),
    Item("007", "Rotatable Box", 27.5, 28.2, 30.8, 12, "contB"),
    Item("008", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True),
    Item("009", "Rotatable Box", 10.5, 20.2, 30.8, 10, "contB"),
    Item("010", "Rotatable Box", 10.5, 20.2, 30.8, 99, "contB"),
    Item("011", "Rotatable Box", 10.5, 2.2, 0.8, 80, "contA"),
    Item("012", "Rotatable Box", 15.5, 20.2, 31.8, 15, "contB"),
    Item("013", "Rotatable Box", 1.5, 20.2, 30.8, 10, "contA"),
    Item("014", "Rotatable Box", 27.5, 28.2, 30.8, 12, "contB"),
    Item("015", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True),
    Item("016", "Rotatable Box", 10.5, 20.2, 30.8, 10, "contB"),
    Item("017", "Rotatable Box", 10.5, 20.2, 30.8, 99, "contB"),
    Item("018", "Rotatable Box", 10.5, 2.2, 0.8, 80, "contA"),
    Item("019", "Rotatable Box", 15.5, 20.2, 31.8, 15, "contB"),
    Item("020", "Rotatable Box", 1.5, 20.2, 30.8, 10, "contA"),
    Item("021", "Rotatable Box", 27.5, 28.2, 30.8, 12, "contB"),
    Item("022", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True),
    Item("023", "Rotatable Box", 10.5, 20.2, 30.8, 10, "contB"),
    Item("024", "Rotatable Box", 10.5, 20.2, 30.8, 99, "contB"),
    Item("025", "Rotatable Box", 10.5, 2.2, 0.8, 80, "contA"),
    Item("026", "Rotatable Box", 15.5, 20.2, 31.8, 15, "contB"),
    Item("027", "Rotatable Box", 1.5, 20.2, 30.8, 10, "contA"),
    Item("028", "Rotatable Box", 27.5, 28.2, 30.8, 12, "contB"),
    Item("029", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True),
    Item("030", "Rotatable Box", 10.5, 20.2, 30.8, 10, "contB"),
    Item("031", "Rotatable Box", 10.5, 20.2, 30.8, 99, "contB"),
    Item("032", "Rotatable Box", 10.5, 2.2, 0.8, 80, "contA"),
    Item("033", "Rotatable Box", 15.5, 20.2, 31.8, 15, "contB"),
    Item("034", "Rotatable Box", 1.5, 20.2, 30.8, 10, "contA"),
    Item("035", "Rotatable Box", 27.5, 28.2, 30.8, 12, "contB"),
    Item("036", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True),
    Item("037", "Rotatable Box", 10.5, 20.2, 30.8, 10, "contB"),
    Item("038", "Rotatable Box", 10.5, 20.2, 30.8, 99, "contB"),
    Item("039", "Rotatable Box", 10.5, 2.2, 0.8, 80, "contA"),
    Item("040", "Rotatable Box", 15.5, 20.2, 31.8, 15, "contB"),
    Item("041", "Rotatable Box", 1.5, 20.2, 30.8, 10, "contA"),
    Item("042", "Rotatable Box", 27.5, 28.2, 30.8, 12, "contB"),




]

To_Remove_List = ["002"]

To_Add_list=[Item("043", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True)]

containers = [Container("contA", width=10  , depth=100 , height=100),
              Container("contB", width=10  , depth=100 , height=100)]
initialise()
while True:
    print("\n1. Run BFD Placement")
    print("2. Remove Items")
    print("3. Add Items")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice==1:
        start_BFD()
    elif choice==2:
        remove_items()
    elif choice==3:
        add_items()
    else :
        break





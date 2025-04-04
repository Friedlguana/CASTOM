from .Classes import *
import pickle


def steps_for_retrieval(obj, cont, visited=None):

    Item_ID_in_cont = [attribute.item_id for attribute in item_dict.values() if attribute.placed_cont == cont]

    if visited is None:
        visited = set()

    if obj.item_id in visited:
        return {}  # Avoid redundant processing

    visited.add(obj.item_id)
    # Create a collision object
    colobj = Item(None,"colobj", obj.original_width, obj.z, obj.original_height, None, 0, None, None, None, obj.x, obj.y, obj.z)
    wo_target_items = [item for item in Item_ID_in_cont if item != obj.item_id]

    # Find blocking items
    raw_steps = [item_dict[item] for item in wo_target_items if colobj.is_colliding(item_dict[item])]

    # Sort blocking items by original_height (z-axis priority)
    flagged = sorted(raw_steps, key=lambda x: x.sort_priority())

    # Base case: No blocking items
    dependencies = []
    for i in flagged:
        dependencies.append(steps_for_retrieval(i, cont, visited))  # Track dependencies first

    return {obj.item_id: dependencies}

def unpack_output(op, target):
    unpacked = op[target]
    temp_fifo = []
    for entry in unpacked:
        for k, v in entry.items():
            temp_fifo.extend(unpack_output(entry, k))  # Process dependencies first
            if k not in temp_fifo:
                temp_fifo.append(k)  # Append after processing dependencies

    temp_fifo.append(target)
    return temp_fifo

def global_searcher(target,targ_cont = False):

    paths = {}
    lengths = {}
    if targ_cont:

        lengths[container_dict[targ_cont]] = (unpack_output(steps_for_retrieval(item_dict[target], targ_cont), target))
        paths = {}
        min_val = min([len(item) for item in lengths.values()])

        for k, v in lengths.items():
            if len(v) <= min_val:
                paths[k.container_id] = v


    else:
        container_ID = [attribute.container_id for attribute in container_dict.values()]
        for i in container_ID:

            lengths[container_dict[i]] = (unpack_output(steps_for_retrieval(item_dict[target],i),target))
            paths = {}
            min_val = min([len(item) for item in lengths.values()])
            for k,v in lengths.items():
                if len(v) == min_val:
                    paths[k.container_id] = v

    return paths


def SetupRetrieval(item, cont):
    global Item_ID
    global container_ID
    global container_dict
    global item_dict

    with open("item_data.bin", "rb") as file:
        item_dict = pickle.load(file)



    with open("container_data.bin", "rb") as file:
        container_dict = pickle.load(file)

    Item_ID = [attribute.item_id for attribute in item_dict.values()]
    container_ID = [attribute.container_id for attribute in container_dict.values()]
    if item in Item_ID:

        return global_searcher(item,cont),True

    else:
        return None, False

item_dict  = {}
container_dict = {}

Item_ID = []
container_ID = []



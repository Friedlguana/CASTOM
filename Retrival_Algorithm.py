
class Container():

    def __init__(self,name,dim,items):

        self.name = name
        self.b = dim[0]
        self.h = dim[1]
        self.d = dim[2]
        self.items = items

    def __str__(self):
        return (f"{self.name} of size {self.b}X{self.h}X{self.d}")

class Item():

    def __init__(self, name, dim, coords,cont):
        # dimensions are passed post rotation so make sure to pass it in the correct order
        self.name = name
        self.b = dim[0]
        self.h = dim[1]
        self.d = dim[2]
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.cont = cont

        # ALL THESE CALCULATIONS TAKE THE BOTTOM LEFT CORNER AS THE LOCAL ORIGIN/// consider all three axes of orientation: to do
        #to do for moving anchor point(local origin) - Arthur

        #axis is a list of form [a,b,c] where a, b and c assume value of 0 or 1. 1 implies anti clockwise rotation in that axis and 0 implies the lack thereof.

        # if self.dim[0] == 1:
        #     self.z=self.z-self.h
        # if self.dim[1] == 1:
        #     self.x=self.x-self.d
        # if self.dim[2] == 1:
        #     self.y=self.y-self.b

    def __str__(self):
        return (f"{self.name} of size {self.b}X{self.h}X{self.d} and location {(self.x, self.y, self.z)}")

    def is_colliding(self,obj):

        def centroid(obj):

            xc = obj.x + obj.b/2
            yc = obj.y + obj.h/2
            zc = obj.z + obj.d/2

            return xc,yc,zc

        xsc,ysc,zsc = centroid(self)
        xc,yc,zc = centroid(obj)

        b_self =self.b
        b_obj = obj.b
        h_self = self.h
        h_obj = obj.h
        d_self = self.d
        d_obj = obj.d

        def colliding_xy(xsc,xc,b_self,b_obj):

            dist_cent = abs(xsc - xc)

            if dist_cent < b_self/2 + b_obj/2:
                return True

        def colliding_yz(ysc, yc, h_self, h_obj):

            dist_cent = abs(ysc - yc)

            if dist_cent < h_self / 2 + h_obj / 2:
                return True

        def colliding_xz(zsc, zc, d_self,d_obj):

            dist_cent = abs(zsc - zc)

            if dist_cent < d_self / 2 + d_obj / 2:
                return True

        #Optimise !!

        if colliding_xz(zsc,zc,d_self,d_obj):
             if colliding_yz(ysc,yc,h_self,h_obj):
                 if colliding_xy(xsc,xc,b_self,b_obj):
                     return True
                 else:
                    return False
             else:
                return False
        else:
            return False


    def sort_priority(self):
        return self.z


def steps_for_retrieval(obj, cont, visited=None):
    if visited is None:
        visited = set()

    if obj.name in visited:
        return {}  # Avoid redundant processing

    visited.add(obj.name)

    # Create a collision object
    colobj = Item("colobj", (obj.b, obj.h, obj.z), (obj.x, obj.y, 0),cont)
    wo_target_items = [item for item in items_names if item != obj.name]

    # Find blocking items
    raw_steps = [item_dict[item] for item in wo_target_items if colobj.is_colliding(item_dict[item])]

    # Sort blocking items by height (z-axis priority)
    flagged = sorted(raw_steps, key=lambda x: x.sort_priority())

    # Base case: No blocking items
    dependencies = []
    for i in flagged:
        dependencies.append(steps_for_retrieval(i, cont, visited))  # Track dependencies first

    return {obj.name: dependencies}

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

    lengths = {}
    if targ_cont:

        lengths[container_dict[targ_cont]] = (unpack_output(steps_for_retrieval(item_dict[target], targ_cont), target))
        paths = {}
        max_val = max([len(item) for item in lengths.values()])
        for k, v in lengths.items():
            if len(v) == max_val:
                paths[k.name] = v


    else:
        for i in container_names:
            lengths[container_dict[i]] = (unpack_output(steps_for_retrieval(item_dict[target],i),target))
            paths = {}
            max_val = max([len(item) for item in lengths.values()])
            for k,v in lengths.items():
                if len(v) == max_val:
                    paths[k.name] = v


    return paths






"""
Final Output
subdict = [{1: 
            [{A: [1,2]},
           2:
            {B: [2,4]},
           3:
            [{C:{$: [2,3]}},{D: [0]}]]
           }]

Convert to FIFO

steps = (1,2,3,4,5)

"""

#Creating all the objects

tempdict_objs = {"MedKit": ([10, 6, 5], [0, 0, 10], "Medbay"),
            "Water": ([5,5,10],[0,0,0],"Medbay"),
            "Pills": ([5,9,10],[5,0,0],"Medbay"),
            "Drugs": ([5,5,5],[0,0,15],"Medbay")}


items_names = [items[0] for items in tempdict_objs.items()]
item_dict = {}
for i in range(len(items_names)):
    exec(f'I{i} = Item("{items_names[i]}",tempdict_objs["{items_names[i]}"][0],tempdict_objs["{items_names[i]}"][1],tempdict_objs["{items_names[i]}"][2])')
    exec(f'item_dict["{items_names[i]}"] = I{i} ')



tempdict_conts = {"MedBay": [(20,40,60), [items_names]],
                  "Kitchen": [(20,40,60), [items_names]]}

container_names = [items[0] for items in tempdict_conts.items()]
container_dict = {}
for i in range(len(container_names)):
    exec(f'C{i} = Container("{container_names[i]}",tempdict_conts["{container_names[i]}"][0],tempdict_conts["{container_names[i]}"][1])')
    exec(f'container_dict["{container_names[i]}"] = C{i} ')


print(global_searcher('Drugs',None))










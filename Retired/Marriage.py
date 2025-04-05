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
    def is_colliding(self,obj):

        def centroid(obj):
            xc = obj.x + obj.width/2
            yc = obj.y + obj.depth/2
            zc = obj.z + obj.height/2

            return xc,yc,zc

        xsc,ysc,zsc = centroid(self)
        xc,yc,zc = centroid(obj)

        b_self =self.width
        b_obj = obj.width
        d_self = self.depth
        d_obj = obj.depth
        h_self = self.height
        h_obj = obj.height

        def colliding_xy(xsc,xc,b_self,b_obj):

            dist_cent = abs(xsc - xc)

            if dist_cent < b_self/2 + b_obj/2:
                return True

        def colliding_yz(ysc, yc, d_self, d_obj):

            dist_cent = abs(ysc - yc)

            if dist_cent < d_self / 2 + d_obj / 2:
                return True

        def colliding_xz(zsc, zc, h_self,h_obj):

            dist_cent = abs(zsc - zc)

            if dist_cent < h_self / 2 + h_obj / 2:
                return True

        #Optimise !!

        if colliding_xz(zsc,zc,h_self,h_obj):
             if colliding_yz(ysc,yc,d_self,d_obj):
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

'''def steps_for_retrieval(obj, cont, visited=None):
    if visited is None:
        visited = set()

    if obj.name in visited:
        return {}  # Avoid redundant processing

    visited.add(obj.name)

    # Create a collision object
    colobj = Item(None,"colobj", obj.width, obj.depth, obj.z, None, None, None, None, None, x=obj.x, y=obj.y, z=0,placed_cont=cont, placed=True)
    wo_target_items = [item for item in Overall_List if (item.placed_cont==cont and item.item_id != obj.item_id )]

    # Find blocking items
    raw_steps = [item for item in wo_target_items if colobj.is_colliding(item)]

    # Sort blocking items by height (z-axis priority)
    flagged = sorted(raw_steps, key=lambda x: x.sort_priority())

    # Base case: No blocking items
    dependencies = []
    for i in flagged:
        dependencies.append(steps_for_retrieval(i, cont, visited))  # Track dependencies first

    print({obj:dependencies})
    return {obj: dependencies}



def unpack_output(op, target):
    unpacked = op[target]
    temp_fifo = []
    for entry in unpacked:
        for k, v in entry.items():

            temp_fifo.extend(unpack_output(entry, k))  # Process dependencies first
            if k not in temp_fifo:
                temp_fifo.append(k)  # Append after processing dependencies

    temp_fifo.append(target)
    print(temp_fifo)
    return temp_fifo


def global_searcher(target,targ_cont = False):

    lengths = {}
    paths = {}
    if targ_cont:

        lengths[targ_cont] = (unpack_output(steps_for_retrieval(target, targ_cont), target))
        paths = {}
        min_val = min([len(item) for item in lengths.values()])
        for k, v in lengths.items():
            if len(v) == min_val:
                paths[k.container_id] = v


    else:
        for i in containers:
            lengths[i] = (unpack_output(steps_for_retrieval(target,i),target))     
        min_val = min([len(item) for item in lengths.values()])
        for k,v in lengths.items():
            if len(v) == min_val:
                paths[k.container_id] = v


    return paths'''
def steps_for_retrieval(obj, cont, visited=None):
    if visited is None:
        visited = set()

    if obj.item_id in visited:
        return {}  # Avoid redundant processing

    visited.add(obj.item_id)
    # Create a collision object
    colobj = Item(None,"colobj",obj.width,obj.z,obj.height,None,None,None,None,None,obj.x,obj.y,obj.z)
    wo_target_items = [item for item in Item_ID if item != obj.item_id]

    # Find blocking items
    raw_steps = [item_dict[item] for item in wo_target_items if colobj.is_colliding(item_dict[item])]

    # Sort blocking items by height (z-axis priority)
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
    
    lengths = {}
    if targ_cont:

        lengths[container_dict[targ_cont]] = (unpack_output(steps_for_retrieval(item_dict[int(target.item_id)], targ_cont), target))
        paths = {}
        min_val = min([len(item) for item in lengths.values()])
        for k, v in lengths.items():
            if len(v) == min_val:
                paths[k.item_id] = v
    else:
        for i in container_ID:
            lengths[container_dict[i]] = (unpack_output(steps_for_retrieval(item_dict[target],i),target))
            paths = {}
            min_val = min([len(item) for item in lengths.values()])
            for k,v in lengths.items():
                if len(v) == min_val:
                    paths[k.container_id] = v


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

#I0 = Item(1,"Medkit",5,3,2,10,100,None,30,"Medbay",0,0,10,"ContA")
#Creating all the objects

'''tempdict_objs = {1: (1,"Medkit",5,3,2,10,100,None,30,"Medbay",0,0,10,"ContA"),
            2: (2,"Medkit",5,3,2,10,100,None,30,"Medbay",0,0,10,"ContA"),
            3: (3,"Medkit",5,3,2,10,100,None,30,"Medbay",0,0,10,"ContA"),
            4: (3,"Medkit",5,3,2,10,100,None,30,"Medbay",0,0,10,"ContA")}'''

#Retire this once youre done importing from csv or bin
#Item_ID = [attribute[0] for attribute in tempdict_objs.values()]

'''item_dict = {}
for i in range(len(Item_ID)):
    exec(f'I{i} = Item(tempdict_objs[{Item_ID[i]}][0],'
         f'tempdict_objs[{Item_ID[i]}][1],'
         f'tempdict_objs[{Item_ID[i]}][2],'
         f'tempdict_objs[{Item_ID[i]}][3],'
         f'tempdict_objs[{Item_ID[i]}][4],'
         f'tempdict_objs[{Item_ID[i]}][5],'
         f'tempdict_objs[{Item_ID[i]}][6],'
         f'tempdict_objs[{Item_ID[i]}][7],'
         f'tempdict_objs[{Item_ID[i]}][8],'
         f'tempdict_objs[{Item_ID[i]}][9],'
         f'tempdict_objs[{Item_ID[i]}][10],'
         f'tempdict_objs[{Item_ID[i]}][11],'
         f'tempdict_objs[{Item_ID[i]}][12],'
         f'tempdict_objs[{Item_ID[i]}][13])')

    exec(f'item_dict[{Item_ID[i]}] = I{i} ')

tempdict_conts = {"ContA": ["MedBay","ContA",200,10,200],
                  "ContB": ["MedBay","ContA",200,10,200]}


container_ID = [attribute[1] for attribute in tempdict_conts.values()]

container_dict = {}
for i in range(len(container_ID)):
    exec(f'C{i} = Container(tempdict_conts["{container_ID[i]}"][0]'
         f',tempdict_conts["{container_ID[i]}"][1]'
         f',tempdict_conts["{container_ID[i]}"][2]'
         f',tempdict_conts["{container_ID[i]}"][3]'
         f',tempdict_conts["{container_ID[i]}"][4])')
    exec(f'container_dict["{container_ID[i]}"] = C{i} ')'''


#print(global_searcher(1,None))




# Overall list is the list containing all items.
Overall_List =[]
itemobj=open('items.csv','r',newline='')
csvreader=csv.reader(itemobj)
headItem=next(csvreader)
for row in csvreader:
    Overall_List.append(Item(int(row[0]),row[1],float(row[2]),float(row[3]),float(row[4]),float(row[5]),int(row[6]),row[7],int(row[8].split()[0]),row[9]))
itemobj.close()

#you input the item id to remove that object from placement
'''To_Remove_List = ["001","002","003","040"]'''
#you give me the item object that needs to be added
'''To_Add_list=[Item("041", "Large Box", 21.2, 18.8, 19.6, 10,"contB",0,0,0,"contA",True)]'''

containers=[]
containerobj=open('containers.csv','r',newline='')
csvreader=csv.reader(containerobj)
headCont=next(csvreader)
for row in csvreader:
    containers.append(Container(row[0],row[1],int(row[2]),int(row[3]),int(row[4])))
containerobj.close()
initialise()
while True:
    choice=int(input("Enter Choice:"))
    if choice==1:
        start_BFD()
        itemobj=open('itemFile.csv','w',newline='')
        csvwriter=csv.writer(itemobj)
        csvwriter.writerow(["item_id", "name", "width", "depth", "height", "mass", "priority", "expiry", "uses", "pref_zone","x","y","z","placed_cont","placed Status"])
        for item in Overall_List:
            csvwriter.writerow([item.item_id, item.name, item.width, item.depth, item.height, item.mass, item.priority, item.expiry, item.uses, item.pref_zone,item.x,item.y,item.z,item.placed_cont,item.placed])
        itemobj.close()
    elif choice==2:
         #modify for item name input
        Overall_List = [
            Item(1,"MedKit",float(10),float(6),float(5),float(100),int(100),"01-05-2005",int(5),"medbay",x=0,y=0,z=10,placed_cont="contA",placed=True),
            Item(2,"Water",float(5),float(5),float(10),float(100),int(100),"01-05-2005",int(5),"medbay",x=0,y=0,z=0,placed_cont="contA",placed=True),
            Item(3,"Pills",float(5),float(9),float(10),float(100),int(100),"01-05-2005",int(5),"medbay",x=5,y=0,z=0,placed_cont="contA",placed=True),
            Item(4,"Drugs",float(5),float(5),float(5),float(100),int(100),"01-05-2005",int(5),"medbay",x=0,y=0,z=15,placed_cont="contA",placed=True)
            ]
        tempdict_objs = {
            1:[1,"MedKit",float(10),float(6),float(5),float(100),int(100),"01-05-2005",int(5),"medbay",0,0,10,"contA",True],
            2:[2,"Water",float(5),float(5),float(10),float(100),int(100),"01-05-2005",int(5),"medbay",0,0,0,"contA",True],
            3:[3,"Pills",float(5),float(9),float(10),float(100),int(100),"01-05-2005",int(5),"medbay",5,0,0,"contA",True],
            4:[4,"Drugs",float(5),float(5),float(5),float(100),int(100),"01-05-2005",int(5),"medbay",0,0,15,"contA",True]
            }        
        
        containers=[Container("medbay","contA",20,40,60)]
        tempdict_conts={"contA":["medbay","contA",20,40,60]}
        for item in Overall_List:
            print(item.item_id, item.name, item.width, item.depth, item.height, item.mass, item.priority, item.expiry, item.uses, item.pref_zone,item.x,item.y,item.z,item.placed_cont,item.placed)
        Item_ID = [item.item_id for item in Overall_List]
        
        item_dict = {}
        for i in range(len(Item_ID)):
            exec(f'I{i} = Item(tempdict_objs[{Item_ID[i]}][0],'
                 f'tempdict_objs[{Item_ID[i]}][1],'
                 f'tempdict_objs[{Item_ID[i]}][2],'
                 f'tempdict_objs[{Item_ID[i]}][3],'
                 f'tempdict_objs[{Item_ID[i]}][4],'
                 f'tempdict_objs[{Item_ID[i]}][5],'
                 f'tempdict_objs[{Item_ID[i]}][6],'
                 f'tempdict_objs[{Item_ID[i]}][7],'
                 f'tempdict_objs[{Item_ID[i]}][8],'
                 f'tempdict_objs[{Item_ID[i]}][9],'
                 f'tempdict_objs[{Item_ID[i]}][10],'
                 f'tempdict_objs[{Item_ID[i]}][11],'
                 f'tempdict_objs[{Item_ID[i]}][12],'
                 f'tempdict_objs[{Item_ID[i]}][13])')
        
            exec(f'item_dict[{Item_ID[i]}] = I{i} ')
                
        container_ID = [container.container_id for container in containers]
        
        container_dict = {}
        for i in range(len(container_ID)):
            exec(f'C{i} = Container(tempdict_conts["{container_ID[i]}"][0]'
                 f',tempdict_conts["{container_ID[i]}"][1]'
                 f',tempdict_conts["{container_ID[i]}"][2]'
                 f',tempdict_conts["{container_ID[i]}"][3]'
                 f',tempdict_conts["{container_ID[i]}"][4])')
            exec(f'container_dict["{container_ID[i]}"] = C{i} ')        
    
                        
        '''itemobj=open('itemFile.csv','r',newline='')
        csvreader=csv.reader(itemobj)
        head=next(csvreader)
        for row in csvreader:
            Overall_List.append(Item(row[0],row[1],float(row[2]),float(row[3]),float(row[4]),float(row[5]),int(row[6]),row[7],int(row[8].split()[0]),row[9]))
        print(Overall_List)
        containerobj=open('containers.csv','r',newline='')
        csvreader=csv.reader(containerobj)
        headCont=next(csvreader)
        for row in csvreader:
            containers.append(Container(row[0],row[1],int(row[2]),int(row[3]),int(row[4])))
        containerobj.close()'''
        target_id=int(input("Enter item id to be retrieved"))
        '''for item in Overall_List:
            if item.item_id==target_id:
                target=item
                targetContID=item.placed_cont
        for container in containers:
            if container.container_id==targetContID:
                targetCont=container'''
        #To_Remove_List=list(global_searcher(target,targetCont).values())
        #print(global_searcher("Drugs"))
        print(global_searcher(target_id,None))
        #remove_items()
    elif choice==3:
        add_items()
    else :
        break

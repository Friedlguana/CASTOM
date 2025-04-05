import datetime

from .Classes import *
from .utils.file_loader import *
from config import *

def GarbageCollector():

    garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
    item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)

    item_id = [int(item) for item in item_dict.keys]
    for item in item_id:

        if item_dict[item].status != None:
            garbage_dict.update({item : item_dict[item_id] })


    save_dict_to_file(garbage_dict,WASTE_DATA_PATH)

def IdentifyWaste():
    garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
    return garbage_dict

def ReturnPlan(udc,date,maxweight):
    garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)



def Complete_Undocking(udc,jet_time):
    undockingCont = udc
    garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
    garbage_ids = [int(item) for item in garbage_dict.keys]

    return sum(garbage_ids),jet_time










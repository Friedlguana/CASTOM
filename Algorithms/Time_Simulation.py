import csv
import datetime
import pickle
import os
from .Classes import *
from config import *
from .utils.file_loader import *


def loader(daiy_use):
    global dater
    global item_dict
    item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
    dater = {}  # k,v pairs of item id, [expiry date, uses, waste status]


    Item_ID = [int(attribute.item_id) for attribute in item_dict.values()]
    for item in daiy_use:
        if item["itemId"]:
            iid =  item_dict[item["itemId"]].expiry if item_dict[item["itemId"]].expiry != "N/A" else "no expiry"
            dater.update({item["itemId"]: [iid, item_dict[item["itemId"]].uses , item_dict[item["itemId"]].status]})

        elif item["name"]:
            items_by_id = [item for item in Item_ID == item["name"]]
            for i in items_by_id:
                dater.update({i: [item_dict[i].expiry if item_dict["itemId"].expiry != "N/A" else "no expiry",item_dict[i].uses,item_dict[i].status]})


def shiftCurrentDate(dailyUseList, n=1):
    global item_dict

    Item_ID = [int(attribute.item_id) for attribute in item_dict.values()]
    global currDate, dater, expiredlist, usedlist

    currDateOriginal = currDate
    currDate = currDate + datetime.timedelta(days=n)
    updated_item_dict = {}
    def useItem(itemID, n):

        global item_dict
        item_dict[itemID].Use_Item(n)

    for items in dailyUseList:
        if items['itemId']:
            item_id = items['itemId']
            useItem(item_id, n)

            item = item_dict[item_id]
            if item.expiry == "N/A":
                if item.uses <= 0:
                    item.update_status("Out of Uses")

                    usedlist.append(item_id)

            else:
                expiry_date = datetime.datetime.strptime(item.expiry, "%Y-%m-%d")
                if expiry_date.date() <= currDate and item.uses <= 0:

                    days_to_expiry = (expiry_date - datetime.datetime.now()).days

                    if days_to_expiry<item.uses:
                        item.update_status("Expired")

                        expiredlist.append(item_id)


                    elif days_to_expiry>item.uses:
                        item.update_status("Out of Uses")

                        usedlist.append(item_id)


                elif expiry_date.date() <= currDate :
                    item.update_status("Expired")
                    expiredlist.append(item_id)


                elif item.uses <= 0:
                    item.update_status("Out of Uses")
                    usedlist.append(item_id)


        elif items['name']:
            name = items['name']
            ids_to_check = [id for id in Item_ID if item_dict[id].name == name]
            for item_id in ids_to_check:
                useItem(item_id, n)
                item = item_dict[item_id]
                if item.expiry == "N/A":
                    if item.uses <= 0:
                        item.update_status("Out of Uses")
                        usedlist.append(item_id)
                else:
                    expiry_date = datetime.datetime.strptime(item.expiry, "%Y-%m-%d")
                    if expiry_date < currDate:
                        item.update_status("Expired")
                        expiredlist.append(item_id)

    save_dict_to_file(item_dict,ITEM_DATA_PATH)
    return currDate




def SetupSimulation(days_to_sim,daily_use,simulation_date):
    global expiredlist
    global usedlist
    global currDate
    expiredlist = []
    usedlist = []

    currDate = simulation_date
    loader(daily_use)
    new_date = shiftCurrentDate(daily_use,days_to_sim)

    for i in usedlist:
        print({item_dict[i].status:item_dict[i].uses})
        print({item_dict[i].status: item_dict[i].expiry})

    return new_date,expiredlist,usedlist

item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
expiredlist = []
usedlist = []
dater = {}
currDate = None









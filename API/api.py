from fastapi import (FastAPI, Query, UploadFile, File, HTTPException)
from pydantic import BaseModel


from typing import List, Optional, Literal,Union
from datetime import datetime

import csv

import Algorithms.Algo_Picker
from Algorithms.Algo_Picker import ScreenFunctions
from Algorithms.Algo_Picker import SetupSimulation
from Algorithms.Classes import *
import pickle
from Algorithms.utils.file_loader import *
from config import *

from Algorithms.Retrival_Algorithm import SetupRetrieval

app = FastAPI()
boolean = True
number = 0
csvFile = "file download"
simulated_date = datetime.today().date()
disposed_items = []
first_run = True






#-----------------------------------------------------------------------------------------

#1 Placement Recommendations
#'Request' structure definition
class Item(BaseModel):
    itemId: str
    name: str
    width: float
    depth: float
    height: float
    priority: int
    expiryDate: str
    usageLimit: int
    preferredZone: str
class Container(BaseModel):
    containerId: str
    zone: str
    width: float
    depth: float
    height: float
class placementRequest(BaseModel):
    items: List[Item]
    containers: List[Container]

@app.post("/api/placement")
async def placementRecommendations(request: placementRequest):


    number = None
    ## Example usage
    # container_ids = [container.containerId for container in request.containers]
    itemobj=open('itemFile.csv','w',newline='')
    containerobj = open('containerFile.csv','w',newline='')
    itemCsvWriter=csv.writer(itemobj)
    containerCsvWriter=csv.writer(containerobj)

    itemCsvWriter.writerow(["item_id", "name", "width_cm", "depth_cm", "height_cm", "mass_kg", "priority", "expiry_date", "usage_limit",
                            "preferred_zone","x","y","z","placed_cont","placed Status"])
    containerCsvWriter.writerow(["container_id", "width_cm", "depth_cm", "height_cm", "zone"])

    for item in request.items:
        itemCsvWriter.writerow([item.itemId, item.name, item.width, item.depth, item.height, 0, item.priority, item.expiryDate, item.usageLimit, item.preferredZone])
    itemobj.close()
    for container in request.containers:
        containerCsvWriter.writerow([container.containerId, container.width, container.depth, container.height, container.zone])
    containerobj.close()
    obj = ScreenFunctions.SortingScreen("itemFile.csv", "containerFile.csv")

    global first_run
    if first_run:
        first_run = False
        log_dict = {
            "logs": [

            ]
        }


        binItems, binContainers = obj.BeginSort()
        itemData = load_or_initialize_item_dict(ITEM_DATA_PATH)

        item_ids = [ item for item in itemData.keys()]
        placement_result_json = []
        for ID in item_ids:

            log_template = {
                "timestamp": simulated_date,
                "userId": "string",
                "actionType": "string",
                "itemId": "string",
                "details": {
                    "fromContainer": "string",
                    "toContainer": "string",
                    "reason": "string"
                }
            }


            placements_template = {
                "itemId": "string",
                "containerId": "string",
                "position": {
                    "startCoordinates": {
                        "width": number,
                        "depth": number,
                        "height": number
                    },
                    "endCoordinates": {
                        "width": number,
                        "depth": number,
                        "height": number
                    }
                }
            }
            placements_template['itemId'] = itemData[ID].item_id
            placements_template['containerId'] = itemData[ID].placed_cont
            placements_template["position"]["startCoordinates"]["width"] = float(itemData[ID].x)
            placements_template["position"]["startCoordinates"]["depth"] = float(itemData[ID].y)
            placements_template["position"]["startCoordinates"]["height"] = float(itemData[ID].z)
            placements_template["position"]["endCoordinates"]["width"] = itemData[ID].width + float(itemData[ID].x)
            placements_template["position"]["endCoordinates"]["depth"] = itemData[ID].depth + float(itemData[ID].y)
            placements_template["position"]["endCoordinates"]["height"] = itemData[ID].height + float(itemData[ID].z)
            placement_result_json.append(placements_template)

        return {
            "success": boolean,
            "placements": [placement_result_json
            ],
            "rearrangements": [

            ]
        }

    #THIS IS FOR IF WE NEED REARRAGNMENTS TBD
    else:

        item_dict=load_or_initialize_item_dict(ITEM_DATA_PATH)
        container_dict=load_or_initialize_container_dict(CONTAINER_DATA_PATH)


        itemobj=open('itemFile.csv','w',newline='')
        containerobj = open('containerFile.csv','w',newline='')
        itemCsvWriter=csv.writer(itemobj)
        containerCsvWriter=csv.writer(containerobj)

        itemCsvWriter.writerow(["item_id", "name", "width_cm", "depth_cm", "height_cm", "mass_kg", "priority", "expiry_date", "usage_limit",
                                "preferred_zone","x","y","z","placed_cont","placed Status"])
        containerCsvWriter.writerow(["container_id", "width_cm", "depth_cm", "height_cm", "zone"])

        for item in item_dict.values():
            itemCsvWriter.writerow([item.item_id, item.name, item.width, item.depth, item.height, item.mass, item.priority, item.expiry, item.uses, item.pref_zone])
        itemobj.close()
        for container in container_dict.values():
            containerCsvWriter.writerow([container.container_id, container.original_width, container.original_depth, container.original_height, container.zone])
        containerobj.close()
        obj = ScreenFunctions.SortingScreen("itemFile.csv", "containerFile.csv")
        binItems, binContainers = obj.BeginSort()

        itemData = load_or_initialize_item_dict(ITEM_DATA_PATH)

        item_ids = [item for item in itemData.keys()]
        rearrangements_result_json = []
        for ID in item_ids:
            rearrangements_template = {
                "step": number,
                "action": "string",
                "itemId": "string",
                "fromContainer": "string",
                "fromPosition": {
                    "startCoordinates": {
                        "width": number,
                        "depth": number,
                        "height": number
                    },
                    "endCoordinates": {
                        "width": number,
                        "depth": number,
                        "height": number
                    }
                },
                "toContainer": "string",
                "toPosition": {
                    "startCoordinates": {
                        "width": number,
                        "depth": number,
                        "height": number
                    },
                    "endCoordinates": {
                        "width": number,
                        "depth": number,
                        "height": number
                    }
                }
            }
            rearrangements_template['itemId'] = itemData[ID].item_id
            rearrangements_template["fromContainer"] = item_dict[ID].placed_cont
            rearrangements_template["fromPosition"]["startCoordinates"]["width"] = float(item_dict[ID].x)
            rearrangements_template["fromPosition"]["startCoordinates"]["depth"] = float(item_dict[ID].y)
            rearrangements_template["fromPosition"]["startCoordinates"]["height"] = float(item_dict[ID].z)
            rearrangements_template["fromPosition"]["endCoordinates"]["width"] = float(item_dict[ID].width) + float(item_dict[ID].x)
            rearrangements_template["fromPosition"]["endCoordinates"]["depth"] = float(item_dict[ID].depth) + float(item_dict[ID].y)
            rearrangements_template["fromPosition"]["endCoordinates"]["height"] = float(item_dict[ID].height) + float(item_dict[ID].z)
            rearrangements_template["toContainer"] = itemData[ID].placed_cont
            rearrangements_template["toPosition"]["startCoordinates"]["width"] = float(itemData[ID].x)
            rearrangements_template["toPosition"]["startCoordinates"]["depth"] = float(itemData[ID].y)
            rearrangements_template["toPosition"]["startCoordinates"]["height"] = float(itemData[ID].z)
            rearrangements_template["toPosition"]["endCoordinates"]["width"] = float(itemData[ID].width) + float(itemData[ID].x)
            rearrangements_template["toPosition"]["endCoordinates"]["depth"] = float(itemData[ID].depth) + float(itemData[ID].y)
            rearrangements_template["toPosition"]["endCoordinates"]["height"] = float(itemData[ID].height) + float(itemData[ID].z)
            if item_dict[ID].placed_cont==itemData[ID].placed_cont:
                rearrangements_template['step']=0
                rearrangements_template['action']="move"
            else:
                rearrangements_template['step']=0
                rearrangements_template['action']="remove"
                rearrangements_result_json.append(rearrangements_template)
                rearrangements_template['step']=1
                rearrangements_template['action']="place"

            rearrangements_result_json.append(rearrangements_template)

            # rearrangements_template = {
            #     "step": number,
            #     "action": "string",
            #     "itemId": "string",
            #     "fromContainer": "string",
            #     "fromPosition": {
            #         "startCoordinates": {
            #             "width": number,
            #             "depth": number,
            #             "height": number
            #         },
            #         "endCoordinates": {
            #             "width": number,
            #             "depth": number,
            #             "height": number
            #         }
            #     },
            #     "toContainer": "string",
            #     "toPosition": {
            #         "startCoordinates": {
            #             "width": number,
            #             "depth": number,
            #             "height": number
            #         },
            #         "endCoordinates": {
            #             "width": number,
            #             "depth": number,
            #             "height": number
            #         }
            #     }
            # }


        return {
            "success": boolean,
            "placements": [
                           ],
            "rearrangements": [rearrangements_result_json
            ]
        }


#-----------------------------------------------------------------------------------------

#2 Item Search and Retrieval
#2.a Item Search Request
@app.get("/api/search")
async def searchItem(
    itemId: int = Query(None, description="itemID"),
    itemName: str = Query(None, description="itemName"),
    userId: str = Query(None, description="userID")
):

    number = None


    itemData = load_or_initialize_item_dict(ITEM_DATA_PATH)
    containerData = load_or_initialize_container_dict(CONTAINER_DATA_PATH)


    item_ids = [item for item in itemData.keys()]
    # container_ids = [cont for cont in containerData.keys()]

    success = True
    # try:

    route = ScreenFunctions.RetrivalScreen(itemId, itemName,userId, itemData[itemId].placed_cont)
    path, found = route.BeginRetrieval()
    steps = path

    # except Exception:
    #     success = Exception
    #     found = 0
    #     steps = {}

    itemId = list(steps.values())[0][-1]

    result_json = {
        "success": boolean,
        "found": boolean,
        "item": {
            "itemId": itemId,
            "name": itemData[itemId].name,
            "containerId": "string",
            "zone": "string",
            "position": {
                "startCoordinates": {
                    "width": number,
                    "depth": number,
                    "height": number
                },
                "endCoordinates": {
                    "width": number,
                    "depth": number,
                    "height": number
                }
            }
        },
        "retrievalSteps": [
        ]
    }

    result_json["success"] = success
    result_json["found"] = found
    result_json["item"]["containerId"] = itemData[itemId].placed_cont
    result_json["item"]["zone"] = containerData[itemData[itemId].placed_cont].zone
    result_json["item"]["position"]["startCoordinates"]["width"] = itemData[itemId].width
    result_json["item"]["position"]["startCoordinates"]["depth"] = itemData[itemId].depth
    result_json["item"]["position"]["startCoordinates"]["height"] = itemData[itemId].height
    result_json["item"]["position"]["endCoordinates"]["width"] = itemData[itemId].width + float(itemData[itemId].x)
    result_json["item"]["position"]["endCoordinates"]["depth"] = itemData[itemId].depth + float(itemData[itemId].y)
    result_json["item"]["position"]["endCoordinates"]["height"] = itemData[itemId].height + float(itemData[itemId].z)

    remove_buffer = list(steps.values())[0][::-1]
    placeback_buffer = []
    step = 0
    for j in range(len(remove_buffer) -1):
        removed_item = remove_buffer.pop()
        placeback_buffer.append(removed_item)
        template = {
                "step": step,
                "action": "remove",  # Possible values: "remove", "retrieve", "placeBack"
                "itemId": removed_item,
                "itemName": itemData[removed_item].name
            }
        result_json["retrievalSteps"].append(template)
        step += 1

    template = {
        "step": step,
        "action": "retrieve",  # Possible values: "remove", "retrieve", "placeBack"
        "itemId": remove_buffer.pop(),
        "itemName": itemData[itemId].name
    }
    step += 1
    result_json["retrievalSteps"].append(template)

    for j in range(len(placeback_buffer)):
        placed_item = placeback_buffer.pop()
        template = {
            "step": step,
            "action": "placeBack",  # Possible values: "remove", "retrieve", "placeBack"
            "itemId": placed_item,
            "itemName": itemData[placed_item].name
        }

        result_json["retrievalSteps"].append(template)
        step +=1

    # response
    return result_json


#2.b Item Retrieval Request
#'Request' structure definition
class retrieveRequest(BaseModel):
    itemId: str
    userId: str
    timestamp: str

@app.post("/api/retrieve")
async def retrieveItem(request: retrieveRequest):

    #logging
    logdict = {"itemId" : request.itemId,
               "userId": request.userId,
               "timestamp":request.timestamp,
               "actionType":"retrieval",
               }
    save_logdict_to_file(logdict,LOG_DATA_PATH)

    return {
            "success": True,
        }

class place_params(BaseModel):
    itemId: str
    userId: str
    timestamp: str  # ISO
    containerId: str
    width: Union[int, float]
    depth: Union[int, float]
    height: Union[int, float]

@app.post("/api/place")
async def place_item(request: place_params):

    logdict = {"itemId": request.itemId,
               "userId": request.userId,
               "timestamp": request.timestamp,
               "action":"placement"}
    save_logdict_to_file(logdict, LOG_DATA_PATH)

    item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)

    item2place = Algorithms.Algo_Picker.ScreenFunctions.RetrivalScreen(int(request.itemId), item_dict[int(request.itemId)],request.userId,request.containerId)
    val = item2place.PlaceItem(request.itemId,request.containerId,(request.width,request.depth,request.height))

    return {
        "success" : val
    }


#-----------------------------------------------------------------------------------------

#3 Waste Management
#3.a identify waste
@app.get("/api/waste/identify")
async def wasteIdentify():

    ident = Algorithms.Algo_Picker.ScreenFunctions.UndockingScreen()
    waste = ident.IdentifyWaste().keys()
    result = []
    for i in waste:
        tempres = {
                    "itemId": i.item_id,
                    "name": i.name,
                    "reason": i.status,  # "Expired", "Out of Uses"
                    "containerId": i.placed_cont,
                    "position": {
                        "startCoordinates": {
                            "width": i.x,
                            "depth": i.y,
                            "height": i.z
                        },
                        "endCoordinates": {
                            "width": i.width + i.x,
                            "depth": i.depth + i.y,
                            "height": i.height + i.z
                        }
                    }
                }

        result.append(tempres)



    if waste:
        found = True

    #response
    return {
        "success": True,
        "wasteItems": result
    }

#3.b waste return plan
class wasteReturnPlanRequest(BaseModel):
    undockingContainerId: str
    undockingDate: str
    maxWeight: float
@app.post("/api/waste/return-plan")
async def wasteReturnPlan(request: wasteReturnPlanRequest):
    waste = Algorithms.Algo_Picker.ScreenFunctions.UndockingScreen()
    path_to_items,slated_return,maxweight,volume = waste.ReturnPlan(request.undockingContainerId,request.undockingDate,request.maxWeight)

    cont_ids = [id.keys()[0] for id in path_to_items]

    returnplan = []
    step = 0
    for i in slated_return:

        temp = {
            "step": step,
            "itemId": waste[i].item_id,
            "itemName": waste[i].name,
            "fromContainer": waste[i].placed_cont,
            "toContainer": request.undockingContainerId
        }

        returnplan.append(temp)
        step+=1

    returnsteps = []
    for i in path_to_items:
        remove_buffer = list(i.values())[0][::-1]
        placeback_buffer = []

        step = 0
        for j in range(len(remove_buffer) -1):
            removed_item = remove_buffer.pop()
            placeback_buffer.append(removed_item)
            template = {
                    "step": step,
                    "action": "remove",  # Possible values: "remove", "retrieve", "placeBack"
                    "itemId": removed_item,
                    "itemName": itemData[removed_item].name
                }
            returnsteps.append(template)
            step += 1

        template = {
            "step": step,
            "action": "retrieve",  # Possible values: "remove", "retrieve", "placeBack"
            "itemId": remove_buffer.pop(),
            "itemName": itemData[itemId].name
        }
        returnsteps.append(template)
        step += 1


        for j in range(len(placeback_buffer)):
            placed_item = placeback_buffer.pop()
            template = {
                "step": step,
                "action": "placeBack",  # Possible values: "remove", "retrieve", "placeBack"
                "itemId": placed_item,
                "itemName": itemData[placed_item].name
            }

            returnsteps.append(template)
            step +=1

    returnItems = []
    for i in slated_return:
        temp ={
            "itemId": waste[i].item_id,
            "name": waste[i].name,
            "reason": waste[i].status
          }
        returnItems.append(temp)


    #response
    return {
        "success": boolean,
        "returnPlan": returnplan,
        "retrievalSteps": returnsteps,
        "returnManifest": {
            "undockingContainerId": request.undockingContainerId,
            "undockingDate": request.undockingDate,
            "returnItems": returnItems,
            "totalVolume": volume,
            "totalWeight": maxweight
        }
    }

#3.c Complete Undocking (Item Removal)
class wasteCompleteUndockingRequest(BaseModel):
    undockingContainerId: str
    timestamp: str #iso
@app.post("/api/waste/complete-undocking")
async def completeUndocking(request: wasteCompleteUndockingRequest):

    itemData = load_or_initialize_item_dict(ITEM_DATA_PATH)
    containerData = load_or_initialize_container_dict(CONTAINER_DATA_PATH)

    threshold = datetime.strptime(wasteCompleteUndockingRequest.timestamp, "%Y-%m-%d")
    number = 0

    for item in itemData.values():
        expiry = item.expiry

        if expiry != "N/A":
            expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
            if expiry_date <= threshold:
                number += 1

    return {
        "success": true,
        "itemsRemoved": number
    }

#-----------------------------------------------------------------------------------------

#4 Time simulation
class ItemToUse(BaseModel):
    itemId: str
    name: Optional[str] = None

class SimulationRequest(BaseModel):
    numOfDays: Optional[int] = None
    toTimestamp: Optional[str] = None
    itemsToBeUsedPerDay: List[ItemToUse] = []

class itemUsed(BaseModel):
    itemId: str
    name: str
    remainingUses: int

class itemExpired(BaseModel):
    itemId: str
    name: str

class simulationChanges(BaseModel):
    itemsUsed: List[itemUsed]
    itemsExpired: List[itemExpired]
    itemsDepletedToday: List[itemExpired]

class simulationResponse(BaseModel):
    success: bool
    newDate: str
    changes: simulationChanges

@app.post("/api/simulate/day")
async def simulateDay(request: SimulationRequest):
    try:
        # Validate input - either numOfDays or toTimestamp must be provided
        if request.numOfDays is None and request.toTimestamp is None:
            raise HTTPException(status_code=400, detail="Either numOfDays or toTimestamp must be provided")

        # Convert itemsToBeUsedPerDay to the format expected by TimeSimScreen
        items_to_use = [{"itemId": item.itemId, "name": item.name} for item in request.itemsToBeUsedPerDay]

        # Parse timestamp if provided
        sim_date = None
        if request.toTimestamp:
            try:
                sim_date = datetime.fromisoformat(request.toTimestamp)
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid ISO format for toTimestamp")

        # Create TimeSimScreen instance and begin simulation
        time_sim_screen = ScreenFunctions.TimeSimScreen(
            no_of_days=request.numOfDays,
            usage_list=items_to_use,
            sim_date=sim_date
        )

        # Call BeginSimulation which returns new_date, expired_list, used_list
        new_date, expired_list, used_list = time_sim_screen.BeginSimulation()

        # Identify items that are depleted (have 0 remaining uses)
        items_depleted = [
            {"itemId": item["itemId"], "name": item["name"]}
            for item in used_list if item.get("remainingUses", 0) == 0
        ]

        # Format response according to expected structure
        response = {
            "success": True,
            "newDate": new_date.isoformat() if isinstance(new_date, datetime) else str(new_date),
            "changes": {
                "itemsUsed": used_list,
                "itemsExpired": expired_list,
                "itemsDepletedToday": items_depleted
            }
        }

        return response

    except Exception as e:
        # Handle any exceptions
        return {
            "success": False,
            "error": str(e)
        }

#-----------------------------------------------------------------------------------------

#5 Import/Export
#5.a Import Items (CSV Upload)
@app.post("/api/import/items")
async def import_items(file: UploadFile = File(...)):
    # Process the uploaded CSV file here
    # Example: Read CSV and count imported items, handle errors, etc.
    with open(f"items.csv", "wb") as f:
        f.write(await file.read())  # Write the file content to disk

    return {
        "success": boolean,
        "itemsImported": number,
        "errors": [
            {
                "row": number,
                "message": "string"
            }
        ]
    }


# 5.b Import Containers (CSV Upload)
@app.post("/api/import/containers")
async def import_containers(file: UploadFile = File(...)):
    # Process the uploaded CSV file here
    # Example: Read CSV and count imported items, handle errors, etc.
    with open(f"containers.csv", "wb") as f:
        f.write(await file.read())  # Write the file content to disk

    return {
        "success": boolean,
        "containersImported": number,
        "errors": [
            {
                "row": number,
                "message": "string"
            }
        ]
    }


# 5.c Export Arrangement (CSV Download)
@app.get("/api/export/arrangement")
async def export_arrangement():
    csv_content = "Item ID,Container ID,Coordinates (W1,D1,H1),(W2,D2,H2)\n"

    csv_content += "001,contA,(0,0,0),(10,10,20)\n"
    csv_content += "002,contB,(0,0,0),(15,15,50)\n"

    return csv_content  # Ideally, return as a downloadable CSV file

class log_params(BaseModel):
    startDate : str #iso
    endDate: str
    itemId: str
    userId: str
    actionType: str #optional
@app.post("/api/logs")
async def returnlogs(request: log_params):



    return {
        "logs": [
            {
                "timestamp": "string",
                "userId": "string",
                "actionType": "string",
                "itemId": "string",
                "details": {
                    "fromContainer": "string",
                    "toContainer": "string",
                    "reason": "string"
                }
            }
        ]
    }




#-----------------------------------------------------------------------------------------
#END
#to run this api server first install fastapi and uvicorn and then run:
##python3 -m uvicorn API.api:app --host 0.0.0.0 --port 8000 --reload



# from Algorithms.Algo_Picker import ScreenFunctions
# import pickle

# obj = ScreenFunctions.SortingScreen("items.csv", "containers.csv")

# binItems, binContainers = obj.BeginSort()
# with poen(binItems, "rb") as f:
#     f.load()

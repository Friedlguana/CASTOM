from fastapi import FastAPI, Query, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional, Literal
import csv
from Algorithms.Algo_Picker import ScreenFunctions
from Algorithms.Classes import *
import pickle
from Algorithms.utils.file_loader import *
from config import *

from Algorithms.Retrival_Algorithm import SetupRetrieval

app = FastAPI()
boolean = True
number = 0
csvFile = "file download"

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

    binItems, binContainers = obj.BeginSort()
    itemData = load_or_initialize_item_dict(ITEM_DATA_PATH)
    item_ids = [ item for item in itemData.keys()]
    placement_result_json = []
    for ID in item_ids:
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
        placements_template["position"]["startCoordinates"]["width"] = itemData[ID].x
        placements_template["position"]["startCoordinates"]["depth"] = itemData[ID].y
        placements_template["position"]["startCoordinates"]["height"] = itemData[ID].z
        placements_template["position"]["endCoordinates"]["width"] = itemData[ID].width + itemData[ID].x
        placements_template["position"]["endCoordinates"]["depth"] = itemData[ID].depth + itemData[ID].y
        placements_template["position"]["endCoordinates"]["height"] = itemData[ID].height + itemData[ID].z
        placement_result_json.append(placements_template)



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
    return {
        "success": boolean,
        "placements": [placement_result_json
        ],
        "rearrangements": [

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
    try:

        route = ScreenFunctions.RetrivalScreen(itemId, itemName,itemData[itemId].placed_cont, userId)
        path,found = route.BeginRetrieval()
        steps = path

    except Exception:
        success = Exception
        found = 0
        steps = {}



    result_json = {
        "success": boolean,
        "found": boolean,
        "item": {
            "itemId": itemId,
            "name": itemName,
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
    result_json["item"]["position"]["endCoordinates"]["width"] = itemData[itemId].width + itemData[itemId].x
    result_json["item"]["position"]["endCoordinates"]["depth"] = itemData[itemId].depth + itemData[itemId].y
    result_json["item"]["position"]["endCoordinates"]["height"] = itemData[itemId].height + itemData[itemId].z

    remove_buffer = list(steps[0].values())[0][::-1]
    placeback_buffer = []
    for i in range(len(list(steps[0].values())[0])*2 - 1):
        step = 0
        while remove_buffer != [itemId]:
            removed_item = remove_buffer.pop()
            placeback_buffer.append(remove_buffer.pop())
            template = {
                    "step": step,
                    "action": "remove",  # Possible values: "remove", "retrieve", "placeBack"
                    "itemId": removed_item,
                    "itemName": itemData[removed_item].name
                }
            step+=1
            result_json["retrievalSteps"].append(template)

        template = {
            "step": step,
            "action": "retrieve",  # Possible values: "remove", "retrieve", "placeBack"
            "itemId": itemId,
            "itemName": itemName
        }
        step += 1
        result_json["retrievalSteps"].append(template)
        while placeback_buffer != []:
            placed_item = placeback_buffer.pop()
            template = {
                "step": step,
                "action": "placeBack",  # Possible values: "remove", "retrieve", "placeBack"
                "itemId": placed_item,
                "itemName": itemData[placed_item].name
            }
            step += 1
            result_json["retrievalSteps"].append(template)

    # response
    return {
        result_json
    }

#2.b Item Retrieval Request
#'Request' structure definition
class retrieveRequest(BaseModel):
    itemId: str
    userId: str
    timestamp: str

@app.post("/api/retrieve")
async def retrieveItem(request: retrieveRequest):
    try:
        # Load data
        item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
        container_dict = load_or_initialize_container_dict(CONTAINER_DATA_PATH)

        # Validate input
        item_id = int(request.itemId)
        if item_id not in item_dict:
            return {"success": False, "message": "Item not found"}

        # Get target container from item data
        target_container = item_dict[item_id].placed_cont

        # Find retrieval path
        paths, found = SetupRetrieval(item_id, target_container)
        if not found:
            return {"success": False, "message": "No retrieval path found"}

        # Generate steps
        retrieval_steps = []
        step_counter = 0

        # Use the first available path (algorithm returns shortest path)
        container_id, item_sequence = next(iter(paths.items()))

        # Remove phase
        for item in item_sequence[:-1]:  # Last item is the target
            retrieval_steps.append({
                "step": step_counter,
                "action": "remove",
                "itemId": str(item),
                "itemName": item_dict[item].name
            })
            step_counter += 1

        # Retrieve phase
        retrieval_steps.append({
            "step": step_counter,
            "action": "retrieve",
            "itemId": request.itemId,
            "itemName": item_dict[item_id].name
        })
        step_counter += 1

        # Placeback phase (reverse order)
        for item in reversed(item_sequence[:-1]):
            retrieval_steps.append({
                "step": step_counter,
                "action": "placeBack",
                "itemId": str(item),
                "itemName": item_dict[item].name
            })
            step_counter += 1

        return {
            "success": True,
        }

    except Exception as e:
        return {"success": False, "message": str(e)}

#-----------------------------------------------------------------------------------------

#3 Waste Management
#3.a identify waste
@app.get("/api/waste/identify")
async def wasteIdentify():

    #response
    return {
        "success": boolean,
        "wasteItems": [
            {
                "itemId": "string",
                "name": "string",
                "reason": "string",  # "Expired", "Out of Uses"
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
        ]
    }

#3.b waste return plan
class wasteReturnPlanRequest(BaseModel):
    undockingContainerId: str
    undockingDate: str
    maxWeight: float
@app.post("/api/waste/return-plan")
async def wasteReturnPlan(request: wasteReturnPlanRequest):
    #response
    return {
        "success": boolean,
        "returnPlan": [
            {
                "step": number,
                "itemId": "string",
                "itemName": "string",
                "fromContainer": "string",
                "toContainer": "string"
            }
        ],
        "retrievalSteps": [
            {
                "step": number,
                "action": "string",  # "remove", "setAside", "retrieve", "placeBack"
                "itemId": "string",
                "itemName": "string"
            }
        ],
        "returnManifest": {
            "undockingContainerId": "string",
            "undockingDate": "string",
            "returnItems": [
                {
                    "itemId": "string",
                    "name": "string",
                    "reason": "string"
                }
            ],
            "totalVolume": number,
            "totalWeight": number
        }
    }

#3.c Complete Undocking (Item Removal)
class wasteCompleteUndockingRequest(BaseModel):
    undockingContainerId: str
    timestamp: str #iso
@app.post("/api/waste/complete-undocking")
async def completeUndocking(request: wasteCompleteUndockingRequest):
    #response
    return {
        "success": boolean,
        "itemsRemoved": number
    }

#-----------------------------------------------------------------------------------------

#4 Time simulation
class itemUsage(BaseModel):
    itemId: str
    name: Optional[str] = None

class simulationRequest(BaseModel):
    numOfDays: Optional[int] = None
    toTimestamp: Optional[str] = None
    itemsToBeUsedPerDay: List[itemUsage] = []

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
async def simulateDay(request: simulationRequest):
    return {
        "success": boolean,
        "newDate": "string",  # ISO format
        "changes": {
            "itemsUsed": [
                {
                    "itemId": "string",
                    "name": "string",
                    "remainingUses": number
                }
            ],
            "itemsExpired": [
                {
                    "itemId": "string",
                    "name": "string"
                }
            ],
            "itemsDepletedToday": [
                {
                    "itemId": "string",
                    "name": "string"
                }
            ]
        }
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

#-----------------------------------------------------------------------------------------
#END
#to run this api server first install fastapi and uvicorn and then run:
#python3 -m uvicorn API.api:app --reload



# from Algorithms.Algo_Picker import ScreenFunctions
# import pickle

# obj = ScreenFunctions.SortingScreen("items.csv", "containers.csv")

# binItems, binContainers = obj.BeginSort()
# with poen(binItems, "rb") as f:
#     f.load()

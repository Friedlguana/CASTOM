from fastapi import FastAPI, Query, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional, Literal
import csv
from Algorithms.Algo_Picker import ScreenFunctions
from Algorithms.Classes import *
import pickle



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

    itemCsvWriter.writerow(["item_id", "name", "width", "depth", "height", "mass", "priority", "expiry", "uses",
                            "pref_zone","x","y","z","placed_cont","placed Status"])
    itemCsvWriter.writerow(["zone", "container_id", "width", "depth", "height"])


    for item in request.items:
        itemCsvWriter.writerow([item.itemId, item.name, item.width, item.depth, item.height, 0, item.priority, item.expiryDate, item.usageLimit, item.preferredZone])
    itemobj.close()
    for container in request.containers:
        itemCsvWriter.writerow([container.zone, container.containerId, container.width, container.depth, container.height])
    containerobj.close()
    obj = ScreenFunctions.SortingScreen("itemFile.csv", "containerFile.csv")

    binItems, binContainers = obj.BeginSort()
    with open(binItems, "rb") as f:
        itemData = f.load()
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
        placements_template['itemId'] = itemData[ID].itemId
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
    itemId: str = Query(None, description="itemID"),
    itemName: str = Query(None, description="itemName"),
    userId: str = Query(None, description="userID")
):

    number = None


    with open(r"Algorithms/item_data.bin", "rb") as f:
        itemData = f.load()
    with open(r"Algorithms/container_data.bin", "rb") as f:
        containerData = f.load()


    item_ids = [item for item in itemData.keys]
    container_ids = [cont for cont in containerData.keys]

    success = True
    try:

        route = ScreenFunctions.RetrivalScreen(itemId, itemName,itemData[itemId].placed_cont, userId)
        steps,found = route.BeginRetrieval()

    except Exception:
        success = Exception



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
    result_json["found"] = bool
    result_json["item"]["containerId"] = itemData[itemId].placed_cont
    result_json["item"]["zone"] = list(steps[0].keys())[0]
    result_json["item"]["position"]["startCoordinates"]["width"] = itemData[itemId].width
    result_json["item"]["position"]["startCoordinates"]["depth"] = itemData[itemId].depth
    result_json["item"]["position"]["startCoordinates"]["height"] = itemData[itemId].height
    result_json["item"]["position"]["endCoordinates"]["width"] = itemData[itemId].width + itemData[ID].x
    result_json["item"]["position"]["endCoordinates"]["depth"] = itemData[itemId].depth + itemData[ID].y
    result_json["item"]["position"]["endCoordinates"]["height"] = itemData[itemId].height + itemData[ID].z

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

    #can call the client request data as follows:
    # itemId = request.itemId
    # userId = request.userId
    # timestamp = request.timestamp

    #respone
    #Call code to retrieve item and return a boolean value for "success"
    return {"success": boolean}

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
#python -m uvicorn api:app --reload



# from Algorithms.Algo_Picker import ScreenFunctions
# import pickle

# obj = ScreenFunctions.SortingScreen("items.csv", "containers.csv")

# binItems, binContainers = obj.BeginSort()
# with poen(binItems, "rb") as f:
#     f.load()
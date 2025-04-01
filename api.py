from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional, Literal

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

@app.post("api/placement")
async def placementRecommendations(request: placementRequest):
    ## Example usage
    # item_ids = [item.itemId for item in request.items]
    # container_ids = [container.containerId for container in request.containers]

    return {
        "success": boolean,
        "placements": [
            {
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
        ],
        "rearrangements": [
            {
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
    #response
    return {
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
            {
                "step": number,  
                "action": "string",  # Possible values: "remove", "setAside", "retrieve", "placeBack"
                "itemId": "string",
                "itemName": "string"
            }
        ]
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
@app.post("/api/waste/return-plan")
class wasteReturnPlanRequest(BaseModel):
    undockingContainerId: str
    undockingDate: str
    maxWeight: float
async def wasteReturnPlan():
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
@app.post("/api/waste/complete-undocking")
class wasteCompleteUndockingRequest(BaseModel):
    undockingContainerId: str
    timestamp: str #iso
async def completeUndocking():
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
#5.a Import items
class importItemsResponse(BaseModel):
    #Form data with CSV File upload
    pass
@app.post("/api/import/items")
async def importItems(request: importItemsResponse):
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

#5.b Import containers
class importContainersResponse(BaseModel):
    #Form data with CSV File upload
    pass
@app.post("/api/import/containers")
async def importContainers(request: importContainersResponse):
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

#5.c Export Arrangement
@app.get("/api/export/arrangement")
async def exportArrangement():
    #respone is a csv file download with the following arrangement in format
    #Item ID,Container ID,Coordinates (W1,D1,H1),(W2,D2,H2) 001,contA,(0,0,0),(10,10,20) 002,contB,(0,0,0),(15,15,50)
    return csvFile

#-----------------------------------------------------------------------------------------

#6 Logging API

@app.get("/api/logs")
def get_logs(
    startDate: str,
    endDate: str,
    itemId: Optional[str] = None,
    userId: Optional[str] = None,
    actionType: Optional[Literal["placement", "retrieval", "rearrangement", "disposal"]] = None
):
    return{
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
#python -m uvicorn api:app --reload
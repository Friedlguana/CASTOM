# CASTOM- Cargo Stowage And Management System

## What does it do?

### This software acts as a stowage advisor to astronauts, assisting in the following ways:
1) Sorting for ideal placement of items into containers.
2) Shows the most efficient path for the retrieval of items.
3) In case of a space shortage, the program will suggest the rearrangement of items in order to optimise space usage.
4) Simulates how items may be used up or expire through the course of a given number of days.
5) When items are no longer usable, they are categorised as waste. The program suggests which container this waste should be moved into for undocking.
6) Before a resupply module undocks, the system provides a clear plan for waste return and space reclamation.
7) Logs all activities performed by the astronauts.

## Getting Started:
### Required packages:
1) PySide6
2) fastapi
3) uvicorn
4) pydantic
5) py3dbp
6) python-dateutil
7) numpy
8) python-multipart

### Usage:
In order to run the program, you must first download all the py files in _main_ and download all the packages mentioned above (If not installed already).
1) API Support: The program supports the usage of API to create endpoints and perform automated testing of the code. (port 8000). The api.py program is located in the API folder
2) User Interface: The user interface is run by executing UI_Constructor.py. This file is located in the UI directory.

HOME SCREEN:
![image](https://github.com/user-attachments/assets/aebdd861-dd32-4981-ac95-5e2adf53ab03)

ITEM SORTING PAGE:
![image](https://github.com/user-attachments/assets/c9f14bba-4b7a-4e11-99d7-6d172fba6d2e)

ITEM SEARCH AND RETRIEVAL PAGE:
![image](https://github.com/user-attachments/assets/9156332f-1e25-4bbe-8f79-44cdf199ad80)

UNDOCKING PAGE:
![image](https://github.com/user-attachments/assets/1a7eeac4-aef3-4f1d-b281-60914d6334be)

TIME SIMULATION PAGE:
![image](https://github.com/user-attachments/assets/88e3cb2e-a53a-4969-bdc2-c62be4601316)

   


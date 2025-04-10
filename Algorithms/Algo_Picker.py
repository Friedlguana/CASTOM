import datetime

from .Sorting_Algorithm import OpenFileSort
from .Retrival_Algorithm import SetupRetrieval
from .Time_Simulation import SetupSimulation
from .Classes import *
from datetime import *
from dateutil.relativedelta import relativedelta
import pickle
from config import *
from .utils.file_loader import *
class ScreenFunctions():

    class SortingScreen:
        def __init__(self,fname_items,fname_cont):
            self.f_itemspath = fname_items
            self.f_contpath = fname_cont
            self.sortedfpath = None

        def BeginSort(self):
            self.sortedfpath = OpenFileSort(self.f_itemspath,self.f_contpath)

            return self.sortedfpath



        def ResetSort(self):
            self.sortedfpath = None
            self.f_itemspath = None
            self.f_contpath = None

    class RetrivalScreen():

        def __init__(self,item_id,item_name,astro_id,container = None):
            self.searchitem_name = item_name
            self.searchitem_id = item_id
            self.searchcont_id = container
            self.astro_id = astro_id
            self.item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
            self.container_dict = load_or_initialize_container_dict(CONTAINER_DATA_PATH)



        def BeginRetrieval(self):
            best_route = {}
            scores = []
            if self.searchitem_id:
                if self.searchitem_id in self.item_dict:
                    route,bool = SetupRetrieval(self.searchitem_id, self.searchcont_id if self.searchcont_id else self.item_dict[self.searchitem_id].placed_cont)
                    return route,bool
                else:
                    return None,False

            elif self.searchitem_name:

                # min_date = (datetime.today() + timedelta(weeks=2)).strftime("%d-%m-%Y")
                id_to_search = [id for id in self.item_dict.keys() if self.searchitem_name == self.item_dict[id].name]


                for i in id_to_search:
                    output_dict,bool = SetupRetrieval(i, self.item_dict[i].placed_cont)
                    if bool:
                        route =  [item for item in output_dict.values()]
                        expiry_date = datetime.strptime(self.item_dict[i].expiry, '%d-%m-%Y') if not "N/A" else datetime.now()
                        days_to_expiry = (expiry_date - datetime.now()).days
                        score =  len(route) * 100 + days_to_expiry * 150 + self.item_dict[i].uses * 50
                        scores.append(score)
                        best_route.update({score : route})
                        return {self.item_dict[best_route[min(scores)][0][-1]].placed_cont: best_route[min(scores)][
                            0]}, bool
                    else:
                        return output_dict,bool

        def PlaceItem(self,item,new_cont,coords):
            x = coords[0]
            y = coords[1]
            z = coords[2]


            item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)

            item = item_dict[self.searchitem_id]
            item.x,item.y,item.z = x,y,z

            save_dict_to_file(item_dict,ITEM_DATA_PATH)

            return True




        def logger(self,timestamp,loc_start,loc_end):
            self.searchitem_name
            self.searchitem_id = item_id
            self.searchcont_id = container
            self.astro_id = astro_id
            self.timestamp = timestamp



    class TimeSimScreen():
        def __init__(self,no_of_days,usage_list,sim_date):
            self.daysToSim = int(no_of_days)
            self.itemsToUse = usage_list
            self.sim_date = sim_date

        def BeginSimulation(self):

            new_date,item_dict,expiredlist,usedlist = SetupSimulation(self.daysToSim,self.itemsToUse,self.sim_date)
            return new_date,item_dict,expiredlist,usedlist

    class UndockingScreen():

        def __init__(self,udc = None,date =None,maxweight = None):
            self.undockingcontainerID = udc
            self.date = date
            self.weight = maxweight
        def GarbageCollector(self):

            garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
            item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
            item_id = [item for item in item_dict.keys()]
            for item in item_id:
                if item_dict[item].status != None and item not in garbage_dict.keys():
                    garbage_dict.update({item: item_dict[item].status})


            save_dict_to_file(garbage_dict, WASTE_DATA_PATH)

        def IdentifyWaste(self):
            garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
            return garbage_dict

        def ReturnPlan(self,udc, date, maxweight):
            item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
            garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)

            depleted_items = [item_dict[item] for item in garbage_dict.keys()]

            weighted = sorted(depleted_items, key = lambda item : item.mass )

            slated_return = []
            mass_sum = 0
            totvol = 0
            while mass_sum < maxweight:
                try:
                    temp_obj = weighted.pop()
                except IndexError:
                    break
                slated_return.append(temp_obj)
                mass_sum += temp_obj.mass
                totvol += temp_obj.volume
            if slated_return:
                extra = slated_return.pop()
            path_to_items = []
            for i in slated_return:
                route = ScreenFunctions.RetrivalScreen(i.item_id, i.name,None, i.placed_cont)
                path, found = route.BeginRetrieval()
                path_to_items.append(path)

            #print(path_to_items,slated_return,slated_return)
            return path_to_items,slated_return,maxweight,totvol


        def Complete_Undocking(self,udc, jet_time):
            undockingCont = udc
            garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
            garbage_ids = [int(item) for item in garbage_dict.keys()]

            return sum(garbage_ids), jet_time


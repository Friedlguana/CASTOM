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



        def logger(self):
            pass

    class TimeSimScreen():
        def __init__(self,no_of_days,usage_list,sim_date):
            self.daysToSim = no_of_days
            self.itemsToUse = usage_list
            self.sim_date = sim_date

        def BeginSimulation(self):

            new_date,expiredlist,usedlist = SetupSimulation(self.daysToSim,self.itemsToUse,self.sim_date)
            return new_date,expiredlist,usedlist










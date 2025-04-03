from .Sorting_Algorithm import OpenFileSort
from .Retrival_Algorithm import SetupRetrivel
from .Classes import *
from datetime import *
import pickle
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
            self.itemsdict = "item_data.bin"
            self.contdict = "container_data.bin"
            self.astro_id = astro_id

            with open("item_data.bin", "rb") as file:
                self.item_dict = pickle.load(file)

            with open("container_data.bin", "rb") as file:
                self.cont_dict = pickle.load(file)



        def BeginRetrieval(self):
            best_route = {}
            scores = []
            if self.searchitem_id:
                route = SetupRetrivel(self.searchitem_id, self.searchcont_id)
                print("search",route)
                return route

            elif self.searchitem_name:

                min_date = datetime.strptime(datetime.date.today(),"%d-%m+2-%Y")
                id_to_search = [id for id in self.item_dict.keys() if self.searchitem_name in self.item_dict.values().name]


                for i in id_to_search:
                    route =  [item for item in SetupRetrivel(i).values()]
                    expiry_date = datetime.strptime(obj['expiry_date'], '%d-%m-%Y')
                    days_to_expiry = (expiry_date - datetime.now()).days
                    score =  len(route) * 100  + days_to_expiry * 75 + i.uses * 50
                    scores.append(score)
                    best_route = {score : route}


                return best_route[min(scores)]

        def logger(self):
            pass










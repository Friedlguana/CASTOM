import sys
import os
import platform
import csv
import datetime
import PySide6.QtCore
import matplotlib
from PySide6 import QtWidgets as qtw
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
matplotlib.use('QtAgg')  # Set backend before other matplotlib imports
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from datetime import datetime

"""from glass_engine import *
from glass_engine.Geometries import *
from glass_engine.Lights import *"""
#from pyglm import glm
import time
import pickle

iteration=0
rearrage_factor = 0

import Algorithms.Algo_Picker
from main import Ui_MainWindow
#from Object_Creator import *
from Algorithms import *

from Algorithms.utils.file_loader import (
    load_or_initialize_item_dict,
    load_or_initialize_container_dict,
)
from config import *

# os.environ["QT_FONT_DPI"] = "180"
Window_Size = 0
GLOBAL_STATE = False


class Settings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET ="""
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        color: rgb(255, 255, 255);"""
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(5, 5), dpi=100)
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Set background colors
        dark_gray_rgb = (44 / 255, 49 / 255, 58 / 255)
        self.fig.patch.set_facecolor(dark_gray_rgb)  # Set figure background
        self.ax.set_facecolor(dark_gray_rgb)         # Set axes background

        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.updateGeometry()


widgets = None


"""class GlassEngineWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.node = None
        # Initialize Glass Engine
        self.scene, self.camera, self.light, self.floor = SceneRoam()
        self.floor.hide()

        # Camera orbit parameters
        self.orbit_radius = 5.0  # Distance from object
        self.orbit_height = 2.0  # Vertical offset
        self.current_angle = 0.0
        self.camera.far = 100000

        # Add camera screen to layout
        self.layout.addWidget(self.camera.screen)

        # # Disable manual camera controls
        # self.camera.mouse_sensitivity = 0
        # self.camera.key_speed = 0
        # self.camera.screen.setFocusPolicy(Qt.NoFocus)

        # # Setup timer for continuous updates (~60 FPS)
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_orbit)
        # self.timer.start(16)  # Refresh every ~16ms (60 FPS)

    def update_orbit(self):
        pass

    def Create_Digi_Twin(self, cont_obj, item_dict):
        self.node = SceneNode()
        self.scene.add(self.node)
        self.container = OpenCuboid(glm.vec3(0, 0, 0), cont_obj.original_width / 10, cont_obj.original_depth / 10,
                                    -1 * cont_obj.original_height / 10, "bottom")
        self.node.add_child(self.container)

        def Generate_Children():
            print("Cooking")

            for objs in item_dict.values():
                if objs.placed_cont == cont_obj.container_id:
                    computed_position = glm.vec3(objs.x / 10, objs.y / 10,
                                                 objs.z / 10)  # Switched axes as per your definition
                    self.item = Cuboid(computed_position, objs.width / 10, objs.height / 10, objs.depth / 10)
                    self.container.add_child(self.item)  # Attach to container, not node

        Generate_Children()

    def Clear_Scene(self):
        if self.node:
            children = self.node.children_names
            self.node.remove_child(children)
            self.scene.remove(self.node)"""


class MainWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global widgets
        widgets = self
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Make the window frameless
        self.clickPosition = QPoint()
        self.setAttribute(Qt.WA_TranslucentBackground)
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        title = "CASTOM"
        description = "CASTOM - Cargo Stowage Management System."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)

        widgets.Table_SimResults.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #Widget Connections
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_sorting.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_undocking.clicked.connect(self.buttonClick)
        widgets.btn_time_simulation.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        # Initialize Matplotlib canvas
        self.mpl_canvas = MplCanvas(self.sort_visualiser)
        self.search_canvas = MplCanvas(self.search_visualiser)

        # Create layout for visualizer widget
        layout = QVBoxLayout(self.sort_visualiser)
        layout2 = QVBoxLayout(self.search_visualiser)

        layout.setContentsMargins(0, 0, 0, 0)
        layout2.setContentsMargins(0, 0, 0, 0)
        # Add navigation toolbar
        self.sort_toolbar = NavigationToolbar(self.mpl_canvas, self)


        # Add widgets in consistent order
        layout.addWidget(self.sort_toolbar)
        layout.addWidget(self.mpl_canvas)


        layout2.addWidget(self.search_canvas)



        # Clock Logic

        def update_time():
            current_time =QTime.currentTime()
            self.timeEdit.setTime(current_time)

        self.timer = QTimer(self)
        self.timer.timeout.connect(update_time)
        self.timer.start(10)

        #Date logic

        self.current_date = date.today() #.strftime("%d-%m-%Y")

        self.simulated_date = datetime.datetime.today()
        self.dateEdit.setDisplayFormat("dd MMM yyyy")
        self.dateEdit.setDate(QDate.currentDate())

        self.datetimer = QTimer(self)
        self.datetimer.timeout.connect(self.update_date)
        self.datetimer.start(60000)  # 60,000 ms = 1 minute


        self.garbagetimer = QTimer(self)
        self.garbagetimer.timeout.connect(self.GarbageTrigger)
        self.garbagetimer.start(60000)


        ##Sorting Page Definitions
        self.sort_fname = None
        self.cont_dict = {}

        self.label = self.findChild(QLabel, "sortingpath_label")
        self.file_dropper_item.clicked.connect(self.add_path_item)
        self.file_dropper_cont.clicked.connect( self.add_path_cont)
        self.btn_sorting_sort.clicked.connect( self.sort_btn_function)
        self.resetSim.clicked.connect(self.reset_btn_function)

        self.sorting_cont_comboBox.currentTextChanged.connect(lambda cont_id: self.create_plot(1,container_needed=cont_id))

        ###Retrieval Page Definitions################################################3
        self.btn_search_search.clicked.connect(self.Search_Trigger)
        self.btn_search_next.clicked.connect(self.Next_Item)
        self.btn_search_prevstep.clicked.connect(self.Prev_Item)
        self.btn_search_retrieve.clicked.connect( self.Retrieval_Trigger)



        ##################Time Sim Definitions######################################
        self.daystosim = 1
        self.sim_items = {}
        self.btn_next.clicked.connect(self.TimeSimTrigger)
        self.file_dropper_timesim.clicked.connect(self.add_path_sim)

        ########################################################################

        ##########################Garbage sim def#############################
        self.btn_load_waste.clicked.connect(self.button_Identify)
        self.btn_waste_manifest.clicked.connect(self.button_generate_manifest)
        self.btn_undocking_confirm.clicked.connect(self.button_complete_dock)
        ######################################################################3
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        #widgets.togglesettings.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        self.titleRightInfo.installEventFilter(self)

        # Glass Engine Driver Code
        #self.glass_engine_widget = GlassEngineWidget(parent=self.sort_visualiser)

        # Add the Glass Engine widget to `sort_visualiser`
        '''if not self.sort_visualiser.layout():
            layout = QVBoxLayout(self.sort_visualiser)  # Create a layout if none exists
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            #layout.addWidget(self.glass_engine_widget)
        else:
            layout = self.sort_visualiser.layout()  # Use existing layout
            #layout.addWidget(self.glass_engine_widget)'''

        self.stackedWidget.setCurrentWidget(self.sorting)

        self.show()

        # useCustomTheme = True
        # themeFile = r"themes\py_dracula_light.qss"
        #
        # # SET THEME AND HACKS
        # if useCustomTheme:
        #     # LOAD AND APPLY STYLE
        #     UIFunctions.theme(self, themeFile, True)
        #
        #     # SET HACKS
        #     AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_viewport)
        # self.timer.start(16)  # Approximately 60 FPS (1000ms / 60 ≈ 16ms)

    def set_custom_start_date(self, year, month, day):
        self.simulated_date = date(year, month, day)
        self.update_date()

    def update_date(self):
        if self.simulated_date:
            self.simulated_date += timedelta(days=1)
            qdate = QDate(self.simulated_date.year, self.simulated_date.month, self.simulated_date.day)
        else:
            qdate = QDate.currentDate()

        #print("Warping: Date is now", qdate )

        self.dateEdit.setDate(qdate)
    # def update_viewport(self):
    #     self.repaint()  # Force a redraw of the widget

    ## Sorting Page Functions###################################################################################################################

    def add_path_item(self):
        items_fname, _ = QFileDialog.getOpenFileName(self, "Open item file for sorting", "", "CSV Files (*.csv)")
        self.sort_fname_items = items_fname
        if items_fname:
            self.label.setText(str(items_fname))

    def add_path_cont(self):
        cont_fname, _ = QFileDialog.getOpenFileName(self, "Open container file", "", "CSV Files (*.csv)")
        self.sort_fname_cont = cont_fname
        if cont_fname:
            self.label.setText(str(cont_fname))

    def sort_btn_function(self):
        global rearrage_factor
        rearrage_factor = 0
        self.sorting_cont_comboBox.clear()
        #GlassEngineWidget.Clear_Scene(self.glass_engine_widget)
        sorter = Algorithms.Algo_Picker.ScreenFunctions.SortingScreen(self.sort_fname_items,
                                                                      self.sort_fname_cont)  # pass this through the sorting algo // should return the sorted file at the end
        self.sorted_fname = sorter.BeginSort()  ##Create the Item Objects and store them in a binary file.

        item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
        container_dict = load_or_initialize_container_dict(CONTAINER_DATA_PATH)

        ##Create Container Objects
        # for container in containers:
        #     ##Add the references to the correct containers ( which container each item is in)
        #    exec("cont = Container(1, 'Medkit', [4, 2, 5], [I0, I1])")
        #Use csv to get values of the container object.
        self.item_dict = item_dict
        self.cont_dict = cont_dict
        for k in self.cont_dict.keys():
            self.sorting_cont_comboBox.addItem(k)

    first = True

    def create_plot(self, type, container_needed=None, item_needed=None,retrieval=None):
        # ======== Container Data ========
        CONTAINERS = {}
        cont = []
        item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)

        if type !=1:

            container_needed = item_dict[str(item_needed)].placed_cont

        # Filter items for the container
        for item in item_dict:
            if item_dict[item].placed_cont == container_needed:
                itemer = {
                    "Position": (float(item_dict[item].x), float(item_dict[item].y), float(item_dict[item].z)),
                    "Dimensions": (
                    float(item_dict[item].width), float(item_dict[item].depth), float(item_dict[item].height)),
                    "ID": item_dict[item].item_id
                }
                cont.append(itemer)

        CONTAINERS[container_needed] = cont
        # ======== Visualization Functions ========
        def plot_cuboid(ax, position, dimensions, color):

            """Plot a 3D cuboid with specified position and dimensions"""
            x, y, z = position
            dx, dy, dz = dimensions

            # Define cuboid vertices
            vertices = [
                [x, y, z],
                [x + dx, y, z],
                [x + dx, y + dy, z],
                [x, y + dy, z],
                [x, y, z + dz],
                [x + dx, y, z + dz],
                [x + dx, y + dy, z + dz],
                [x, y + dy, z + dz],
            ]

            # Define cube faces
            faces = [
                [vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom
                [vertices[2], vertices[3], vertices[7], vertices[6]],  # Top
                [vertices[0], vertices[3], vertices[2], vertices[1]],  # Front
                [vertices[4], vertices[5], vertices[6], vertices[7]],  # Back
                [vertices[0], vertices[4], vertices[7], vertices[3]],  # Left
                [vertices[1], vertices[5], vertices[6], vertices[2]],  # Right
            ]

            ax.add_collection3d(Poly3DCollection(faces, facecolors=color,
                                                 edgecolors='black', alpha=0.8))

        def visualize_container(container_name):
            """Visualize a single container inside the sort_visualiser widget"""

            if type == 1:
                canvas = self.mpl_canvas  # sort_visualizer
            else:
                canvas = self.search_canvas  # search_visualizer
            # Clear previous plot from canvas
            canvas.ax.clear()

            # Set background colors to match the dark theme
            dark_gray_rgb = (44 / 255, 49 / 255, 58 / 255)  # Convert RGB values to normalized format (0-1)
            canvas.fig.patch.set_facecolor(dark_gray_rgb)  # Figure background
            canvas.ax.set_facecolor(dark_gray_rgb)  # Axes background

            # Customize gridlines and labels for better visibility
            canvas.ax.grid(color='gray', linestyle='--', linewidth=0.5)

            # Change axis labels and ticks to white for visibility
            canvas.ax.xaxis.label.set_color('white')  # X-axis label color
            canvas.ax.yaxis.label.set_color('white')  # Y-axis label color
            canvas.ax.zaxis.label.set_color('white')  # Z-axis label color

            canvas.ax.tick_params(axis='x', colors='white')
            canvas.ax.tick_params(axis='y', colors='white')
            canvas.ax.tick_params(axis='z', colors='white')

            # Set title with white text color
            canvas.ax.set_title(f"Container {container_name}", fontweight='bold', color='white')

            canvas.ax.set_xlabel("X-axis", color='white')  # X-axis label text color
            canvas.ax.set_ylabel("Y-axis", color='white')  # Y-axis label text color
            canvas.ax.set_zlabel("Z-axis", color='white')  # Z-axis label text color
            if type==1:
                items = CONTAINERS.get(container_name)
                if not items:
                    print(f"No items found in container {container_name}")
                    return

                # Plot each item with random color
                for item in items:
                    color = (random.random(), random.random(), random.random())
                    plot_cuboid(self.mpl_canvas.ax, item["Position"], item["Dimensions"], color)

                self.mpl_canvas.ax.set_box_aspect([1, 1, 1])

                self.mpl_canvas.draw()
            elif type==2:
                items = CONTAINERS.get(container_name)
                if not items:
                    print(f"No items found in container {container_name}")
                    return

                # Plot each item with random color
                for item in items:
                    if str(item["ID"])==str(item_needed):
                        color = ("red","red","red")
                    else:
                        color=("white","white","white")
                    plot_cuboid(canvas.ax, item["Position"], item["Dimensions"], color)
                    self.search_canvas.ax.set_box_aspect([1, 1, 1])
                    self.search_canvas.draw()
            elif type==3:
                items = CONTAINERS.get(container_name)
                if not items:
                    print(f"No items found in container {container_name}")
                    return

                # Plot each item with random color
                for item in items:
                    if item["ID"] == int(item_needed):
                        color = ("red", "red", "red")
                    elif item["ID"] in retrieval:
                        color = ("yellow", "yellow", "yellow")
                    else:
                        color=("white","white","white")
                    plot_cuboid(canvas.ax, item["Position"], item["Dimensions"], color)
                    self.search_canvas.ax.set_box_aspect([1, 1, 1])
                    self.search_canvas.draw()
            else:
                global iteration
                if type==5:
                    iteration -= 1
                ahead=retrieval[iteration:]
                behind=retrieval[:iteration]
                items = CONTAINERS.get(container_name)
                if not items:
                    print(f"No items found in container {container_name}")
                    return

                # Plot each item with random color
                for item in items:
                    if item["ID"] == int(item_needed):
                        color = ("red", "red", "red")
                    elif item["ID"]==int(ahead[0]):
                        color = ("yellow", "yellow", "yellow")
                    elif item["ID"] in ahead:
                        color = ("orange", "orange", "orange")
                    else:
                        color = ("white", "white", "white")
                    if (item["ID"]) not in behind:
                        plot_cuboid(canvas.ax, item["Position"], item["Dimensions"], color)
                        self.search_canvas.ax.set_box_aspect([1, 1, 1])
                        self.search_canvas.draw()
                if type==4:
                    iteration+=1







        # ======== Run Visualization ========
        visualize_container(container_needed)

        # Call the function with the desired container ID
    def reset_btn_function(self):
        self.sorting_cont_comboBox.clear()
        #GlassEngineWidget.Clear_Scene(self.glass_engine_widget)

    ####################################################################################3####################################################################

    ########################################Retriveal Functions###########################################################################3

    def Search_Trigger(self):
        self.searchitem_id = self.le_item_id.text() if self.le_item_id.text() else None
        self.searchitem_name = self.le_item_name.text()
        self.searchcont_id = self.le_cont_id.text() if self.le_cont_id.text() else None
        self.astro_id = self.le_astro_id.text()

        route = Algorithms.Algo_Picker.ScreenFunctions.RetrivalScreen(self.searchitem_id, self.searchitem_name,
                                                                      self.searchcont_id, self.astro_id)
        self.create_plot(2,item_needed=self.searchitem_id)
        self.steps, self.bool = route.BeginRetrieval()
        print(self.steps)
        global iteration
        iteration=0

    def Retrieval_Trigger(self):
        global rearrage_factor
        rearrage_factor += 1
        self.searchitem_id = self.le_item_id.text()
        self.searchitem_name = self.le_item_name.text()
        self.searchcont_id = self.le_cont_id.text() if self.le_cont_id.text() else None
        self.astro_id = self.le_astro_id.text()
        self.create_plot(3, item_needed=self.searchitem_id, retrieval=list(self.steps.values())[0])
        item_dict[self.searchitem_id].Use_Item(1)

        # remove_buffer = list(self.steps[0].values())[0][::-1]
        # placeback_buffer = []
        # for i in range(len(list(self.steps[0].values())[0]) * 2 - 1):
        #     step = 0
        #     while remove_buffer != [itemId]:
        #         removed_item = remove_buffer.pop()
        #         placeback_buffer.append(remove_buffer.pop())
        #         #########Visualisation Code Goes Here#########################
        #         step += 1
        #
        #     #MARK TARGET
        #     #target.colour = red
        #     step += 1
        #     while placeback_buffer != []:
        #         placed_item = placeback_buffer.pop()
        #         #########Visualisation Code Goes Here#########################
        #         step += 1
    def Next_Item(self):
        global iteration
        steper = list(self.steps.values())[0]
        if iteration<len(steper):
            self.create_plot(4,item_needed=self.searchitem_id,retrieval=steper)




    def Prev_Item(self):
        global iteration
        steper = list(self.steps.values())[0]
        if iteration > 0:
            self.create_plot(5, item_needed=self.searchitem_id, retrieval=steper)

    ################################################################################################################################3######

    ##################################################TIMESIMULATION#########################################################3######

    def add_path_sim(self):

        sim_items_csv, _ = items_fname, _ = QFileDialog.getOpenFileName(self, "Open items to be used daily", "",
                                                                        "CSV Files (*.csv)")

        itemObj = open(sim_items_csv, 'r', newline="")
        csvreader = csv.reader(itemObj)
        head = next(csvreader)
        self.item_consumption_list = []
        for row in csvreader:
            self.item_consumption_list.append({"itemId": str(int(row[0])),"name": None})
        itemObj.close()

    def TimeSimTrigger(self):
        self.daystosim = 1 if self.le_days.text() == "" else int(self.le_days.text())
        # item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)

        sim = Algorithms.Algo_Picker.ScreenFunctions.TimeSimScreen(self.daystosim,self.item_consumption_list,self.current_date)
        new_date,item_dict, expiredlist, usedlist = sim.BeginSimulation()
        self.simulated_date = new_date
        self.set_custom_start_date(self.simulated_date.year,self.simulated_date.month,self.simulated_date.day)

        wastelist = set(expiredlist + usedlist)

        data = []
        for i in wastelist:
            temp_data = [i,item_dict[i].name,item_dict[i].status]

            data.append(temp_data)

        self.Table_SimResults.setRowCount(len(data))
        self.Table_SimResults.setColumnCount(len(data[0]) if len(data[0]) else 0)

        for row_idx,row_data in enumerate(data):
            for col_idx,value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.Table_SimResults.setItem(row_idx,col_idx,item)

    ################################################################################################################################3######

    ###################################################GARBAGE COLLECTOR####################################################3######


    def GarbageTrigger(self):
        garbage = Algorithms.Algo_Picker.ScreenFunctions.UndockingScreen()
        garbage.GarbageCollector()

    def button_Identify(self):

        self.undockingcontname = self.le_udc_name
        if not self.undockingcontname:
            self.le_udc_name.setText("Enter Valid Container Name")
            return

        self.max_weight = self.le_dc_maxweight
        if not self.max_weight:
            self.le_dc_maxweight.setText("Enter Valid Maximum Weight")
            return

        garbage = Algorithms.Algo_Picker.ScreenFunctions.UndockingScreen()
        garbage_dict = garbage.IdentifyWaste()
        garbage_id = [item for item in garbage_dict.keys()]

        data = []
        for i in garbage_id:
            temp_data = [i,item_dict[i].name,item_dict[i].status,item_dict[i].mass]
            data.append(temp_data)

        self.onship_table.setRowCount(len(data))
        try:
            col = len(data[0])
        except IndexError:
            col = 0

        self.onship_table.setColumnCount(col)

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.onship_table.setItem(row_idx, col_idx, item)

        return garbage_dict

    def button_generate_manifest(self):

        self.undockingcontname = self.le_udc_name.text()
        if not self.undockingcontname:
            self.le_udc_name.setText("Enter Valid Container Name")
            return

        self.max_weight = int(self.le_dc_maxweight.text())
        if not self.max_weight:
            self.le_dc_maxweight.setText("Enter Valid Maximum Weight")
            return

        garbage = Algorithms.Algo_Picker.ScreenFunctions.UndockingScreen()
        item_paths,items_to_return,max_weight,tot_vol = garbage.ReturnPlan(self.undockingcontname, 32, self.max_weight)
        garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)
        garbage_id = [id for id in garbage_dict.keys()]

        data = []
        for i in items_to_return:
            temp_data = [i.item_id, i.name, i.status, i.mass]
            data.append(temp_data)

        self.slated4return.setRowCount(len(data))
        self.slated4return.setColumnCount(len(data[0]) if len(data[0]) else 0)

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.slated4return.setItem(row_idx, col_idx, item)


    def button_complete_dock(self):

        item_dict = load_or_initialize_item_dict(ITEM_DATA_PATH)
        garbage_dict = load_or_initialize_waste_dict(WASTE_DATA_PATH)

        garb_id = [id for id in garbage_dict.keys()]
        for id in garb_id:
            item_dict.pop(id,None)
            garbage_dict.pop(id,None)

        save_dict_to_file(item_dict,ITEM_DATA_PATH)
        save_dict_to_file(garbage_dict,WASTE_DATA_PATH)

        self.undockingcontname = self.le_udc_name
        if not self.undockingcontname:
            self.le_udc_name.setText("Enter Valid Container Name")
            return

        garbage = Algorithms.Algo_Picker.ScreenFunctions.UndockingScreen()
        num,date = garbage.Complete_Undocking(self.undockingcontname,self.simulated_date)

        self.slated4return.clear()
        self.onship_table.clear()
        return num,date
        print(num,date)


    ################################################################################################################################3######
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW sorting
        if btnName == "btn_sorting":
            widgets.stackedWidget.setCurrentWidget(widgets.sorting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW Search
        if btnName == "btn_search":
            widgets.stackedWidget.setCurrentWidget(widgets.retrieval)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_undocking":
            widgets.stackedWidget.setCurrentWidget(widgets.undocking)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_time_simulation":
            widgets.stackedWidget.setCurrentWidget(widgets.time_simulation)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def restore_or_maximize_window(self):
        global Window_Size
        win_status = Window_Size

        if win_status == 0:
            Window_Size = 1
            self.maximizeRestoreAppBtn.setIcon(QIcon(r"images/icons/cil-clone.png"))
            self.showMaximized()

        else:
            Window_Size = 0
            self.maximizeRestoreAppBtn.setIcon(QIcon(r"images/icons/icon_maximize.png"))
            self.showNormal()

    def eventFilter(self, obj, event):
        global Window_Size
        """Ensures dragging only happens when clicking the main_header."""
        if obj == self.titleRightInfo:
            if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                if self.isMaximized():  # If window is maximized
                    # Get mouse position relative to header before restoring
                    cursor_pos = event.globalPosition().toPoint()

                    # Restore window to normal state and set a reasonable default size
                    self.showNormal()
                    self.resize(1280, 720)
                    Window_Size = 0
                    self.restorebut.setIcon(QIcon(r"images/icons/icon_maximize.png"))

                    # Adjust window position so cursor stays in the same place relative to the header
                    new_x = cursor_pos.x() - (self.width() // 2)  # Center horizontally
                    new_y = 0  # Keep the window at the top
                    self.move(new_x, new_y)

                    # Adjust click position to prevent jump
                    self.clickPosition = QPoint(cursor_pos.x() - self.x(), cursor_pos.y() - self.y())
                else:
                    self.clickPosition = event.globalPosition().toPoint() - self.pos()

                event.accept()
                return True

            if event.type() == QEvent.Type.MouseMove and event.buttons() == Qt.MouseButton.LeftButton:
                self.move(event.globalPosition().toPoint() - self.clickPosition)
                event.accept()
                return True

        '''if obj == self.glass_engine_widget.camera.screen:
            if event.type() in [QEvent.MouseButtonPress, QEvent.MouseMove, QEvent.MouseButtonRelease]:
                self.glass_engine_widget.camera.screen.event(event)
                return True'''

        return super().eventFilter(obj, event)

    class Settings():
        # APP SETTINGS
        # ///////////////////////////////////////////////////////////////
        ENABLE_CUSTOM_TITLE_BAR = True
        MENU_WIDTH = 240
        LEFT_BOX_WIDTH = 240
        RIGHT_BOX_WIDTH = 240
        TIME_ANIMATION = 500

        # BTNS LEFT AND RIGHT BOX COLORS
        BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
        BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

        # MENU SELECTED STYLESHEET
        MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        """

    GLOBAL_STATE = False
    GLOBAL_TITLE_BAR = True


class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.maximizeRestoreAppBtn.setToolTip("Restore")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.appMargins.setContentsMargins(10, 10, 10, 10)
            self.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):

        if enable:
            if not hasattr(self, "leftMenuBg"):
                print("leftMenuBg is missing!")
                return

            width = self.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            widthExtended = maxExtend if width == 60 else standard

            self.animation = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()



    # # TOGGLE LEFT BOX
    # # ///////////////////////////////////////////////////////////////
    # def toggleLeftBox(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         original_width = self.extraLeftBox.original_width()
    #         widthLeftMenu = self.leftMenuFrame.original_width()
    #         #widthRightBox = self.extraRightBox.original_width()
    #         maxExtend = Settings.LEFT_BOX_WIDTH
    #         color = Settings.BTN_LEFT_BOX_COLOR
    #         standard = 0
    #
    #         # GET BTN STYLE
    #         style = self.toggleLeftBox.styleSheet()
    #
    #         # SET MAX WIDTH
    #         if original_width == 0:
    #             widthExtended = maxExtend
    #             # SELECT BTN
    #             self.toggleLeftBox.setStyleSheet(style + color)
    #             if widthLeftMenu != 0:
    #                 style = self.settingsTopBtn.styleSheet()
    #                 self.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
    #         else:
    #             widthExtended = standard
    #             # RESET BTN
    #             self.toggleLeftBox.setStyleSheet(style.replace(color, ''))
    #
    #     UIFunctions.start_box_animation(self, original_width, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    # def toggleRightBox(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         original_width = self.leftMenuFrame.original_width()
    #         widthLeftBox = self.extraLeftBox.original_width()
    #         maxExtend = Settings.RIGHT_BOX_WIDTH
    #         color = Settings.BTN_RIGHT_BOX_COLOR
    #         standard = 0
    #
    #         # GET BTN STYLE
    #         style = self.settingsTopBtn.styleSheet()
    #
    #         # SET MAX WIDTH
    #         if original_width == 0:
    #             widthExtended = maxExtend
    #             # SELECT BTN
    #             self.settingsTopBtn.setStyleSheet(style + color)
    #             if widthLeftBox != 0:
    #                 style = self.toggleLeftBox.styleSheet()
    #                 self.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
    #         else:
    #             widthExtended = standard
    #             # RESET BTN
    #             self.settingsTopBtn.setStyleSheet(style.replace(color, ''))
    #
    #         UIFunctions.start_box_animation(self, widthLeftBox, original_width, "right")

    def start_box_animation(self, left_box_width, direction):
        left_width = 0

        if left_box_width == 0 and direction == "left":
            left_width = Settings.LEFT_BOX_WIDTH
        else:
            left_width = 0

        # Animate Left Box Only
        self.left_box = QPropertyAnimation(self.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        self.left_box.start()

    # ANIMATION RIGHT BOX
    # self.leftMenuFrame = QPropertyAnimation(self.leftMenuFrame, b"minimumWidth")
    # self.leftMenuFrame.setDuration(Settings.TIME_ANIMATION)
    # self.leftMenuFrame.setStartValue(left_menu_width)
    # self.leftMenuFrame.setEndValue(right_width)
    # self.leftMenuFrame.setEasingCurve(QEasingCurve.InOutQuart)
    #
    # # GROUP ANIMATION
    # self.group = QParallelAnimationGroup()
    # self.group.addAnimation(self.left_box)
    # self.group.addAnimation(self.leftMenuFrame)
    # self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        self.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            self.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.minimizeAppBtn.hide()
            self.maximizeRestoreAppBtn.hide()
            self.closeAppBtn.hide()
            self.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("original_width: 20px; original_height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.btn_exit.clicked.connect(lambda: self.close())
        self.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)


class CustomGrip(QWidget):
    def __init__(self, parent, position, disable_color=False):

        # SETUP UI
        QWidget.__init__(self)
        self.parent = parent
        self.setParent(parent)
        self.wi = Widgets()

        # SHOW TOP GRIP
        if position == Qt.TopEdge:
            self.wi.top(self)
            self.setGeometry(0, 0, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # GRIPS
            top_left = QSizeGrip(self.wi.top_left)
            top_right = QSizeGrip(self.wi.top_right)

            # RESIZE TOP
            def resize_top(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
                geo = self.parent.geometry()
                geo.setTop(geo.bottom() - height)
                self.parent.setGeometry(geo)
                event.accept()

            self.wi.top.mouseMoveEvent = resize_top

            # ENABLE COLOR
            if disable_color:
                self.wi.top_left.setStyleSheet("background: transparent")
                self.wi.top_right.setStyleSheet("background: transparent")
                self.wi.top.setStyleSheet("background: transparent")

        # SHOW BOTTOM GRIP
        elif position == Qt.BottomEdge:
            self.wi.bottom(self)
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # GRIPS
            self.bottom_left = QSizeGrip(self.wi.bottom_left)
            self.bottom_right = QSizeGrip(self.wi.bottom_right)

            # RESIZE BOTTOM
            def resize_bottom(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
                self.parent.resize(self.parent.width(), height)
                event.accept()

            self.wi.bottom.mouseMoveEvent = resize_bottom

            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_left.setStyleSheet("background: transparent")
                self.wi.bottom_right.setStyleSheet("background: transparent")
                self.wi.bottom.setStyleSheet("background: transparent")

        # SHOW LEFT GRIP
        elif position == Qt.LeftEdge:
            self.wi.left(self)
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # RESIZE LEFT
            def resize_left(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
                geo = self.parent.geometry()
                geo.setLeft(geo.right() - width)
                self.parent.setGeometry(geo)
                event.accept()

            self.wi.leftgrip.mouseMoveEvent = resize_left

            # ENABLE COLOR
            if disable_color:
                self.wi.leftgrip.setStyleSheet("background: transparent")

        # RESIZE RIGHT
        elif position == Qt.RightEdge:
            self.wi.right(self)
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            def resize_right(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
                self.parent.resize(width, self.parent.height())
                event.accept()

            self.wi.rightgrip.mouseMoveEvent = resize_right

            # ENABLE COLOR
            if disable_color:
                self.wi.rightgrip.setStyleSheet("background: transparent")

    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def resizeEvent(self, event):
        if hasattr(self.wi, 'container_top'):
            self.wi.container_top.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'container_bottom'):
            self.wi.container_bottom.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'leftgrip'):
            self.wi.leftgrip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'rightgrip'):
            self.wi.rightgrip.setGeometry(0, 0, 10, self.height() - 20)


class Widgets(object):
    def top(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_top = QFrame(Form)
        self.container_top.setObjectName(u"container_top")
        self.container_top.setGeometry(QRect(0, 0, 500, 10))
        self.container_top.setMinimumSize(QSize(0, 10))
        self.container_top.setMaximumSize(QSize(16777215, 10))
        self.container_top.setFrameShape(QFrame.NoFrame)
        self.container_top.setFrameShadow(QFrame.Raised)
        self.top_layout = QHBoxLayout(self.container_top)
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_left = QFrame(self.container_top)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(10, 10))
        self.top_left.setMaximumSize(QSize(10, 10))
        self.top_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.top_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_left.setFrameShape(QFrame.NoFrame)
        self.top_left.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_left)
        self.top = QFrame(self.container_top)
        self.top.setObjectName(u"top")
        self.top.setCursor(QCursor(Qt.SizeVerCursor))
        self.top.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top)
        self.top_right = QFrame(self.container_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(10, 10))
        self.top_right.setMaximumSize(QSize(10, 10))
        self.top_right.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.top_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_right.setFrameShape(QFrame.NoFrame)
        self.top_right.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_right)

    def bottom(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, 10))
        self.container_bottom.setMinimumSize(QSize(0, 10))
        self.container_bottom.setMaximumSize(QSize(16777215, 10))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_left = QFrame(self.container_bottom)
        self.bottom_left.setObjectName(u"bottom_left")
        self.bottom_left.setMinimumSize(QSize(10, 10))
        self.bottom_left.setMaximumSize(QSize(10, 10))
        self.bottom_left.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.bottom_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_left.setFrameShape(QFrame.NoFrame)
        self.bottom_left.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_left)
        self.bottom = QFrame(self.container_bottom)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom)
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(10, 10))
        self.bottom_right.setMaximumSize(QSize(10, 10))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

    def left(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.leftgrip = QFrame(Form)
        self.leftgrip.setObjectName(u"left")
        self.leftgrip.setGeometry(QRect(0, 10, 10, 480))
        self.leftgrip.setMinimumSize(QSize(10, 0))
        self.leftgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.leftgrip.setStyleSheet(u"background-color: rgb(255, 121, 198);")
        self.leftgrip.setFrameShape(QFrame.NoFrame)
        self.leftgrip.setFrameShadow(QFrame.Raised)

    def right(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        self.rightgrip = QFrame(Form)
        self.rightgrip.setObjectName(u"right")
        self.rightgrip.setGeometry(QRect(0, 0, 10, 500))
        self.rightgrip.setMinimumSize(QSize(10, 0))
        self.rightgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.rightgrip.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.rightgrip.setFrameShape(QFrame.NoFrame)
        self.rightgrip.setFrameShadow(QFrame.Raised)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = MainWindow()

    sys.exit(app.exec())

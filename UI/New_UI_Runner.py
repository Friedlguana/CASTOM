import sys
import os
import platform

import PySide6.QtCore
from PySide6 import QtWidgets as qtw
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from main import Ui_MainWindow
os.environ["QT_FONT_DPI"] = "96"
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
    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        """

widgets = None

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global widgets
        widgets = self
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Make the window frameless
        self.clickPosition = QPoint()
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.titleRightInfo.installEventFilter(self)

        # self.minimizeAppBtn.clicked.connect(self.showMinimized)
        # self.maximizeRestoreAppBtn.clicked.connect(self.restore_or_maximize_window)
        # self.closeAppBtn.clicked.connect(self.close)
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "CASTOM"
        description = "CASTOM - Cargo Stowage Management System."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)

        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_sorting.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_undocking.clicked.connect(self.buttonClick)
        widgets.btn_time_simulation.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.togglesettings.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX



        self.show()
        useCustomTheme = False
        themeFile = r"themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))



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
            widgets.stackedWidget.setCurrentWidget(widgets.retrieval) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

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



class AppFunctions(MainWindow):
        def setThemeHack(self):
            Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
            Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
            Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
            border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
            background-color: #566388;
            """

            # SET MANUAL STYLES
            self.lineEdit.setStyleSheet("background-color: #6272a4;")
            self.pushButton.setStyleSheet("background-color: #6272a4;")
            self.plainTextEdit.setStyleSheet("background-color: #6272a4;")
            self.tableWidget.setStyleSheet(
                "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
            self.scrollArea.setStyleSheet(
                "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
            self.comboBox.setStyleSheet("background-color: #6272a4;")
            self.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
            self.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
            self.commandLinkButton.setStyleSheet("color: #ff79c6;")

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
                # GET WIDTH
                width = self.leftMenuBg.width()
                maxExtend = Settings.MENU_WIDTH
                standard = 60

                # SET MAX WIDTH
                if width == 60:
                    widthExtended = maxExtend
                else:
                    widthExtended = standard

                # ANIMATION
                self.animation = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
                self.animation.setDuration(Settings.TIME_ANIMATION)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QEasingCurve.InOutQuart)
                self.animation.start()

        # TOGGLE LEFT BOX
        # ///////////////////////////////////////////////////////////////
        def toggleLeftBox(self, enable):
            if enable:
                # GET WIDTH
                width = self.extraLeftBox.width()
                widthRightBox = self.extraRightBox.width()
                maxExtend = Settings.LEFT_BOX_WIDTH
                color = Settings.BTN_LEFT_BOX_COLOR
                standard = 0

                # GET BTN STYLE
                style = self.toggleLeftBox.styleSheet()

                # SET MAX WIDTH
                if width == 0:
                    widthExtended = maxExtend
                    # SELECT BTN
                    self.toggleLeftBox.setStyleSheet(style + color)
                    if widthRightBox != 0:
                        style = self.settingsTopBtn.styleSheet()
                        self.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
                else:
                    widthExtended = standard
                    # RESET BTN
                    self.toggleLeftBox.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, width, widthRightBox, "left")

        # TOGGLE RIGHT BOX
        # ///////////////////////////////////////////////////////////////
        def toggleRightBox(self, enable):
            if enable:
                # GET WIDTH
                width = self.extraRightBox.width()
                widthLeftBox = self.extraLeftBox.width()
                maxExtend = Settings.RIGHT_BOX_WIDTH
                color = Settings.BTN_RIGHT_BOX_COLOR
                standard = 0

                # GET BTN STYLE
                style = self.settingsTopBtn.styleSheet()

                # SET MAX WIDTH
                if width == 0:
                    widthExtended = maxExtend
                    # SELECT BTN
                    self.settingsTopBtn.setStyleSheet(style + color)
                    if widthLeftBox != 0:
                        style = self.toggleLeftBox.styleSheet()
                        self.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
                else:
                    widthExtended = standard
                    # RESET BTN
                    self.settingsTopBtn.setStyleSheet(style.replace(color, ''))

                UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

        def start_box_animation(self, left_box_width, right_box_width, direction):
            right_width = 0
            left_width = 0

            # Check values
            if left_box_width == 0 and direction == "left":
                left_width = 240
            else:
                left_width = 0
            # Check values
            if right_box_width == 0 and direction == "right":
                right_width = 240
            else:
                right_width = 0

                # ANIMATION LEFT BOX
            self.left_box = QPropertyAnimation(self.extraLeftBox, b"minimumWidth")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(left_box_width)
            self.left_box.setEndValue(left_width)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

            # ANIMATION RIGHT BOX
            self.right_box = QPropertyAnimation(self.extraRightBox, b"minimumWidth")
            self.right_box.setDuration(Settings.TIME_ANIMATION)
            self.right_box.setStartValue(right_box_width)
            self.right_box.setEndValue(right_width)
            self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

            # GROUP ANIMATION
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.addAnimation(self.right_box)
            self.group.start()

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
            self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

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
    def __init__(self, parent, position, disable_color = False):

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

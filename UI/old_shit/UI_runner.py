import sys
import os

from PySide6 import QtWidgets as qtw
from PySide6.QtCore import *
from PySide6.QtGui import *
from UI.old_shit.main import Ui_MainWindow
os.environ["QT_FONT_DPI"] = "96"

Window_Size = 0

class DemoFrom(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Make the window frameless
        self.clickPosition = QPoint()
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.main_header.installEventFilter(self)

        self.minimizebut.clicked.connect(self.showMinimized)
        self.restorebut.clicked.connect(self.restore_or_maximize_window)
        self.closebut.clicked.connect(self.close)

        self.show()

    def restore_or_maximize_window(self):
        global Window_Size
        win_status = Window_Size

        if win_status == 0:
            Window_Size = 1
            self.restorebut.setIcon(QIcon(r"../images/icons/cil-clone.png"))
            self.showMaximized()

        else:
            Window_Size = 0
            self.restorebut.setIcon(QIcon(r"../images/icons/icon_maximize.png"))
            self.showNormal()

    def eventFilter(self, obj, event):
        global Window_Size
        """Ensures dragging only happens when clicking the main_header."""
        if obj == self.main_header:
            if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                if self.isMaximized():  # If window is maximized
                    # Get mouse position relative to header before restoring
                    cursor_pos = event.globalPosition().toPoint()

                    # Restore window to normal state and set a reasonable default size
                    self.showNormal()
                    self.resize(1280, 720)
                    Window_Size = 0
                    self.restorebut.setIcon(QIcon(r"../images/icons/icon_maximize.png"))

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


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = DemoFrom()

    sys.exit(app.exec())

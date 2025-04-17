# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1166,687)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);}\n"
"\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
""
                        "}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/"
                        "icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147,"
                        " 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right:"
                        " 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-c"
                        "olor: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: non"
                        "e;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScroll"
                        "Bar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background"
                        ": none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked "
                        "{\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding"
                        ": 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, "
                        "76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QP"
                        "ushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"image: url(:/images/images/images/PyDracula.png);")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)

        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setGeometry(QRect(0, 3, 60, 45))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setGeometry(QRect(0, 50, 60, 261))
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_sorting = QPushButton(self.topMenu)
        self.btn_sorting.setObjectName(u"btn_sorting")
        sizePolicy.setHeightForWidth(self.btn_sorting.sizePolicy().hasHeightForWidth())
        self.btn_sorting.setSizePolicy(sizePolicy)
        self.btn_sorting.setMinimumSize(QSize(0, 45))
        self.btn_sorting.setFont(font)
        self.btn_sorting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sorting.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_sorting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-quilt.png);")

        self.verticalLayout_8.addWidget(self.btn_sorting)

        self.btn_search = QPushButton(self.topMenu)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QSize(0, 45))
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_search.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_search)

        self.btn_undocking = QPushButton(self.topMenu)
        self.btn_undocking.setObjectName(u"btn_undocking")
        sizePolicy.setHeightForWidth(self.btn_undocking.sizePolicy().hasHeightForWidth())
        self.btn_undocking.setSizePolicy(sizePolicy)
        self.btn_undocking.setMinimumSize(QSize(0, 45))
        self.btn_undocking.setFont(font)
        self.btn_undocking.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_undocking.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_undocking.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-truck.png);")

        self.verticalLayout_8.addWidget(self.btn_undocking)

        self.btn_time_simulation = QPushButton(self.topMenu)
        self.btn_time_simulation.setObjectName(u"btn_time_simulation")
        sizePolicy.setHeightForWidth(self.btn_time_simulation.sizePolicy().hasHeightForWidth())
        self.btn_time_simulation.setSizePolicy(sizePolicy)
        self.btn_time_simulation.setMinimumSize(QSize(0, 45))
        self.btn_time_simulation.setFont(font)
        self.btn_time_simulation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_time_simulation.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_time_simulation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clock.png);")

        self.verticalLayout_8.addWidget(self.btn_time_simulation)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setGeometry(QRect(0, 603, 60, 45))
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.resetSim = QPushButton(self.bottomMenu)
        self.resetSim.setObjectName(u"resetSim")
        sizePolicy.setHeightForWidth(self.resetSim.sizePolicy().hasHeightForWidth())
        self.resetSim.setSizePolicy(sizePolicy)
        self.resetSim.setMinimumSize(QSize(0, 45))
        self.resetSim.setFont(font)
        self.resetSim.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resetSim.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.resetSim.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);")

        self.verticalLayout_9.addWidget(self.resetSim, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_credits = QPushButton(self.extraTopMenu)
        self.btn_credits.setObjectName(u"btn_credits")
        sizePolicy.setHeightForWidth(self.btn_credits.sizePolicy().hasHeightForWidth())
        self.btn_credits.setSizePolicy(sizePolicy)
        self.btn_credits.setMinimumSize(QSize(0, 45))
        self.btn_credits.setFont(font)
        self.btn_credits.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_credits.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_credits.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_credits)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QStackedWidget{\n"
"\n"
"background: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:None;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.missiontime_frame = QFrame(self.frame)
        self.missiontime_frame.setObjectName(u"missiontime_frame")
        self.missiontime_frame.setStyleSheet(u"border:None;")
        self.missiontime_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.missiontime_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.missiontime_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_mission_time = QLabel(self.missiontime_frame)
        self.label_mission_time.setObjectName(u"label_mission_time")

        self.gridLayout_4.addWidget(self.label_mission_time, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.missiontime_frame)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border:None;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.timeEdit = QTimeEdit(self.frame_5)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setStyleSheet(u"QTimeEdit {\n"
"    border: none;\n"
"    background: transparent;\n"
"    font: 54px \"Segoe UI\"; /* Digital-style font */\n"
"    qproperty-alignment: AlignCenter; /* Centers the text */\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    width: 0px; /* Hides the dropdown button */\n"
"    border: none;\n"
"}\n"
"\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    width: 0px; /* Hides the spin buttons */\n"
"    height: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QTimeEdit::down-arrow {\n"
"    image: url(/images/down-arrow.png); /* Optional, use a simple icon */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.timeEdit.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.timeEdit)

        self.dateEdit = QDateEdit(self.frame_5)
        self.dateEdit.setObjectName(u"dateEdit")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.dateEdit.setFont(font4)
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    border: none;\n"
"    background: transparent;\n"
"    font: 30px \"Segoe UI\"; /* Digital-style font */\n"
"    qproperty-alignment: AlignCenter; /* Centers the text */\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    width: 0px; /* Hides the dropdown button */\n"
"    border: none;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"    width: 0px; /* Hides the spin buttons */\n"
"    height: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(/images/down-arrow.png); /* Optional, use a simple icon */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.dateEdit.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.dateEdit)


        self.horizontalLayout_6.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:None;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_reccomendations = QLabel(self.frame_2)
        self.label_reccomendations.setObjectName(u"label_reccomendations")
        self.label_reccomendations.setMinimumSize(QSize(0, 400))
        self.label_reccomendations.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_reccomendations)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.home)
        self.sorting = QWidget()
        self.sorting.setObjectName(u"sorting")
        self.verticalLayout_20 = QVBoxLayout(self.sorting)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_6 = QFrame(self.sorting)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.header = QFrame(self.frame_6)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"border:None;")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.header)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_8 = QFrame(self.header)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setSpacing(1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.file_dropper_item = QPushButton(self.frame_8)
        self.file_dropper_item.setObjectName(u"file_dropper_item")
        self.file_dropper_item.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_dropper_item.setIcon(icon3)

        self.horizontalLayout_15.addWidget(self.file_dropper_item)

        self.file_dropper_cont = QPushButton(self.frame_8)
        self.file_dropper_cont.setObjectName(u"file_dropper_cont")
        self.file_dropper_cont.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.file_dropper_cont)

        self.sortingpath_label = QLabel(self.frame_8)
        self.sortingpath_label.setObjectName(u"sortingpath_label")
        self.sortingpath_label.setStyleSheet(u"padding: 5px;\n"
"font: 9pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_15.addWidget(self.sortingpath_label)


        self.horizontalLayout_13.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_9 = QFrame(self.header)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_sorting_sort = QPushButton(self.frame_9)
        self.btn_sorting_sort.setObjectName(u"btn_sorting_sort")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_sorting_sort.sizePolicy().hasHeightForWidth())
        self.btn_sorting_sort.setSizePolicy(sizePolicy3)
        self.btn_sorting_sort.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sorting_sort.setIcon(icon4)

        self.horizontalLayout_16.addWidget(self.btn_sorting_sort)


        self.horizontalLayout_13.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignRight)

        self.sorting_cont_comboBox = QComboBox(self.header)
        self.sorting_cont_comboBox.setObjectName(u"sorting_cont_comboBox")

        self.horizontalLayout_13.addWidget(self.sorting_cont_comboBox)


        self.horizontalLayout_14.addWidget(self.header)


        self.verticalLayout_20.addWidget(self.frame_6)

        self.sort_frame = QFrame(self.sorting)
        self.sort_frame.setObjectName(u"sort_frame")
        sizePolicy2.setHeightForWidth(self.sort_frame.sizePolicy().hasHeightForWidth())
        self.sort_frame.setSizePolicy(sizePolicy2)
        self.sort_frame.setStyleSheet(u"border:None;")
        self.sort_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sort_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.sort_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sort_visualiser = QWidget(self.sort_frame)
        self.sort_visualiser.setObjectName(u"sort_visualiser")

        self.gridLayout_3.addWidget(self.sort_visualiser, 0, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.sort_frame)

        self.footer = QFrame(self.sorting)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_20.addWidget(self.footer)

        self.stackedWidget.addWidget(self.sorting)
        self.retrieval = QWidget()
        self.retrieval.setObjectName(u"retrieval")
        self.verticalLayout_17 = QVBoxLayout(self.retrieval)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.search_frame = QFrame(self.retrieval)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.le_item_id = QLineEdit(self.search_frame)
        self.le_item_id.setObjectName(u"le_item_id")
        self.le_item_id.setStyleSheet(u"\n"
"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.le_item_id)

        self.le_item_name = QLineEdit(self.search_frame)
        self.le_item_name.setObjectName(u"le_item_name")

        self.horizontalLayout_9.addWidget(self.le_item_name)

        self.le_cont_id = QLineEdit(self.search_frame)
        self.le_cont_id.setObjectName(u"le_cont_id")

        self.horizontalLayout_9.addWidget(self.le_cont_id)

        self.le_astro_id = QLineEdit(self.search_frame)
        self.le_astro_id.setObjectName(u"le_astro_id")

        self.horizontalLayout_9.addWidget(self.le_astro_id)

        self.btn_search_search = QPushButton(self.search_frame)
        self.btn_search_search.setObjectName(u"btn_search_search")
        self.btn_search_search.setStyleSheet(u"padding: 6px 15px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.btn_search_search)

        self.btn_search_retrieve = QPushButton(self.search_frame)
        self.btn_search_retrieve.setObjectName(u"btn_search_retrieve")
        self.btn_search_retrieve.setStyleSheet(u"padding: 6px 12px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.btn_search_retrieve)


        self.verticalLayout_17.addWidget(self.search_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.retriveal_frame = QFrame(self.retrieval)
        self.retriveal_frame.setObjectName(u"retriveal_frame")
        sizePolicy2.setHeightForWidth(self.retriveal_frame.sizePolicy().hasHeightForWidth())
        self.retriveal_frame.setSizePolicy(sizePolicy2)
        self.retriveal_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.retriveal_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.retriveal_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.search_visualiser = QWidget(self.retriveal_frame)
        self.search_visualiser.setObjectName(u"search_visualiser")
        self.gridLayout_5 = QGridLayout(self.search_visualiser)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)

        self.horizontalLayout_10.addWidget(self.search_visualiser)


        self.verticalLayout_17.addWidget(self.retriveal_frame)

        self.frame_11 = QFrame(self.retrieval)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_search_prevstep = QPushButton(self.frame_11)
        self.btn_search_prevstep.setObjectName(u"btn_search_prevstep")
        self.btn_search_prevstep.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-media-skip-backward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search_prevstep.setIcon(icon5)

        self.horizontalLayout_18.addWidget(self.btn_search_prevstep, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_search_next = QPushButton(self.frame_11)
        self.btn_search_next.setObjectName(u"btn_search_next")
        self.btn_search_next.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_search_next.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-media-skip-forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search_next.setIcon(icon6)

        self.horizontalLayout_18.addWidget(self.btn_search_next, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.logging_frame = QFrame(self.retrieval)
        self.logging_frame.setObjectName(u"logging_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.logging_frame.sizePolicy().hasHeightForWidth())
        self.logging_frame.setSizePolicy(sizePolicy4)
        self.logging_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.logging_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.logging_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit = QLineEdit(self.logging_frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.lineEdit_3 = QLineEdit(self.logging_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_11.addWidget(self.lineEdit_3)

        self.btn_search_log = QPushButton(self.logging_frame)
        self.btn_search_log.setObjectName(u"btn_search_log")
        self.btn_search_log.setMinimumSize(QSize(75, 25))
        self.btn_search_log.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.btn_search_log)


        self.verticalLayout_17.addWidget(self.logging_frame)

        self.stackedWidget.addWidget(self.retrieval)
        self.undocking = QWidget()
        self.undocking.setObjectName(u"undocking")
        self.undocking.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.undocking)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_13 = QFrame(self.undocking)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:transparent")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_load_waste = QPushButton(self.frame_12)
        self.btn_load_waste.setObjectName(u"btn_load_waste")
        self.btn_load_waste.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.btn_load_waste, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_20.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.le_udc_name = QLineEdit(self.frame_13)
        self.le_udc_name.setObjectName(u"le_udc_name")

        self.horizontalLayout_20.addWidget(self.le_udc_name)

        self.le_dc_maxweight = QLineEdit(self.frame_13)
        self.le_dc_maxweight.setObjectName(u"le_dc_maxweight")

        self.horizontalLayout_20.addWidget(self.le_dc_maxweight)


        self.verticalLayout.addWidget(self.frame_13)

        self.frame_10 = QFrame(self.undocking)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.waste_label = QLabel(self.frame_10)
        self.waste_label.setObjectName(u"waste_label")

        self.horizontalLayout_17.addWidget(self.waste_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.return_label = QLabel(self.frame_10)
        self.return_label.setObjectName(u"return_label")

        self.horizontalLayout_17.addWidget(self.return_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_10)

        self.tables_btns_frame = QFrame(self.undocking)
        self.tables_btns_frame.setObjectName(u"tables_btns_frame")
        self.tables_btns_frame.setMinimumSize(QSize(0, 150))
        self.tables_btns_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tables_btns_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.tables_btns_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.onship_table = QTableWidget(self.tables_btns_frame)
        if (self.onship_table.columnCount() < 4):
            self.onship_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.onship_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.onship_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.onship_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.onship_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.onship_table.setObjectName(u"onship_table")
        self.onship_table.setStyleSheet(u"border-radius:0;")
        self.onship_table.setCornerButtonEnabled(True)
        self.onship_table.horizontalHeader().setVisible(True)
        self.onship_table.horizontalHeader().setCascadingSectionResizes(False)
        self.onship_table.horizontalHeader().setDefaultSectionSize(124)
        self.onship_table.horizontalHeader().setHighlightSections(True)
        self.onship_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.onship_table.horizontalHeader().setStretchLastSection(True)
        self.onship_table.verticalHeader().setVisible(True)
        self.onship_table.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_12.addWidget(self.onship_table)

        self.slated4return = QTableWidget(self.tables_btns_frame)
        if (self.slated4return.columnCount() < 4):
            self.slated4return.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.slated4return.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.slated4return.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.slated4return.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.slated4return.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.slated4return.setObjectName(u"slated4return")
        self.slated4return.setStyleSheet(u"")
        self.slated4return.horizontalHeader().setDefaultSectionSize(123)
        self.slated4return.horizontalHeader().setStretchLastSection(True)
        self.slated4return.verticalHeader().setVisible(True)

        self.horizontalLayout_12.addWidget(self.slated4return)


        self.verticalLayout.addWidget(self.tables_btns_frame)

        self.frame_14 = QFrame(self.undocking)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border:transparent")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_waste_manifest = QPushButton(self.frame_15)
        self.btn_waste_manifest.setObjectName(u"btn_waste_manifest")
        self.btn_waste_manifest.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.btn_waste_manifest)

        self.btn_undocking_confirm = QPushButton(self.frame_15)
        self.btn_undocking_confirm.setObjectName(u"btn_undocking_confirm")
        self.btn_undocking_confirm.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.btn_undocking_confirm)


        self.horizontalLayout_21.addWidget(self.frame_15, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.undocking)
        self.time_simulation = QWidget()
        self.time_simulation.setObjectName(u"time_simulation")
        self.gridLayout = QGridLayout(self.time_simulation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.time_simulation)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Table_SimResults = QTableWidget(self.frame_7)
        if (self.Table_SimResults.columnCount() < 3):
            self.Table_SimResults.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Table_SimResults.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Table_SimResults.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Table_SimResults.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.Table_SimResults.setObjectName(u"Table_SimResults")

        self.gridLayout_2.addWidget(self.Table_SimResults, 3, 0, 1, 1)

        self.open_file_frame = QFrame(self.frame_7)
        self.open_file_frame.setObjectName(u"open_file_frame")
        self.open_file_frame.setStyleSheet(u"border:None")
        self.open_file_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.open_file_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.open_file_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.file_dropper_timesim = QPushButton(self.open_file_frame)
        self.file_dropper_timesim.setObjectName(u"file_dropper_timesim")
        self.file_dropper_timesim.setMinimumSize(QSize(75, 35))
        self.file_dropper_timesim.setStyleSheet(u"padding: 8px 25px;\n"
"font: bold 9pt \"Segoe UI\";")
        self.file_dropper_timesim.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.file_dropper_timesim, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_timesim_reset = QPushButton(self.open_file_frame)
        self.btn_timesim_reset.setObjectName(u"btn_timesim_reset")
        self.btn_timesim_reset.setStyleSheet(u"padding: 8px 25px;\n"
"font: bold 9pt \"Segoe UI\";")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_timesim_reset.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.btn_timesim_reset)

        self.path_display = QLabel(self.open_file_frame)
        self.path_display.setObjectName(u"path_display")

        self.horizontalLayout_8.addWidget(self.path_display)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.le_days = QLineEdit(self.open_file_frame)
        self.le_days.setObjectName(u"le_days")
        self.le_days.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_8.addWidget(self.le_days, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_next = QPushButton(self.open_file_frame)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(0, 35))
        self.btn_next.setStyleSheet(u"padding: 6px 20px;\n"
"font: bold 9pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.btn_next)


        self.gridLayout_2.addWidget(self.open_file_frame, 1, 0, 1, 1)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_7)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.time_simulation)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"CASTOM", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Stowage Assistant ", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_sorting.setText(QCoreApplication.translate("MainWindow", u"Sorting", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_undocking.setText(QCoreApplication.translate("MainWindow", u"Undocking", None))
        self.btn_time_simulation.setText(QCoreApplication.translate("MainWindow", u"Time Simulation", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.resetSim.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_credits.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_mission_time.setText("")
        self.label_reccomendations.setText("")
        self.file_dropper_item.setText(QCoreApplication.translate("MainWindow", u"Open Item FIle", None))
        self.file_dropper_cont.setText(QCoreApplication.translate("MainWindow", u"Open Container FIle", None))
        self.sortingpath_label.setText(QCoreApplication.translate("MainWindow", u"- upload a csv file to sort", None))
        self.btn_sorting_sort.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.sorting_cont_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a container after sorting", None))
        self.le_item_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the item ID", None))
        self.le_item_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"or enter the item name", None))
        self.le_cont_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optional: Enter container name", None))
        self.le_astro_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter astronaut ID", None))
        self.btn_search_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_search_retrieve.setText(QCoreApplication.translate("MainWindow", u"Retrieve", None))
        self.btn_search_prevstep.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.btn_search_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter container in which item was placed", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter coordinates as [0,0,0]", None))
        self.btn_search_log.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btn_load_waste.setText(QCoreApplication.translate("MainWindow", u"Load Waste", None))
        self.le_udc_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Undocking Container Name", None))
        self.le_dc_maxweight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Maximum Weight", None))
        self.waste_label.setText(QCoreApplication.translate("MainWindow", u"Waste and Expired Items", None))
        self.return_label.setText(QCoreApplication.translate("MainWindow", u"Slated For Return", None))
        ___qtablewidgetitem = self.onship_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.onship_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u" Name", None));
        ___qtablewidgetitem2 = self.onship_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.onship_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem4 = self.slated4return.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.slated4return.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem6 = self.slated4return.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem7 = self.slated4return.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        self.btn_waste_manifest.setText(QCoreApplication.translate("MainWindow", u"Generate Manifest", None))
        self.btn_undocking_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        ___qtablewidgetitem8 = self.Table_SimResults.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Item ID", None));
        ___qtablewidgetitem9 = self.Table_SimResults.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem10 = self.Table_SimResults.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.file_dropper_timesim.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.btn_timesim_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.path_display.setText(QCoreApplication.translate("MainWindow", u"- Upload a CSV with items that are used daily", None))
        self.le_days.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Number of days", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi


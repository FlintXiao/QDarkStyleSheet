# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_containers_tabs.ui'
#
# Created: Thu Mar  8 10:07:40 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(578, 515)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)
        self.tabWidgetNorth = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetNorth.setDocumentMode(False)
        self.tabWidgetNorth.setTabsClosable(True)
        self.tabWidgetNorth.setObjectName("tabWidgetNorth")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_52 = QtGui.QLabel(self.tab_7)
        self.label_52.setObjectName("label_52")
        self.gridLayout_8.addWidget(self.label_52, 0, 0, 1, 1)
        self.tabWidgetNorth.addTab(self.tab_7, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_48 = QtGui.QLabel(self.tab_8)
        self.label_48.setObjectName("label_48")
        self.gridLayout_4.addWidget(self.label_48, 0, 0, 1, 1)
        self.tabWidgetNorth.addTab(self.tab_8, "")
        self.gridLayout_5.addWidget(self.tabWidgetNorth, 1, 0, 1, 1)
        self.tabWidgetNorth_2 = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetNorth_2.setEnabled(False)
        self.tabWidgetNorth_2.setDocumentMode(False)
        self.tabWidgetNorth_2.setTabsClosable(True)
        self.tabWidgetNorth_2.setObjectName("tabWidgetNorth_2")
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_53 = QtGui.QLabel(self.tab_9)
        self.label_53.setObjectName("label_53")
        self.gridLayout_10.addWidget(self.label_53, 0, 0, 1, 1)
        self.tabWidgetNorth_2.addTab(self.tab_9, "")
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_19 = QtGui.QGridLayout(self.tab_10)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_49 = QtGui.QLabel(self.tab_10)
        self.label_49.setObjectName("label_49")
        self.gridLayout_19.addWidget(self.label_49, 0, 0, 1, 1)
        self.tabWidgetNorth_2.addTab(self.tab_10, "")
        self.gridLayout_5.addWidget(self.tabWidgetNorth_2, 1, 1, 1, 1)
        self.tabWidgetWest = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetWest.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidgetWest.setObjectName("tabWidgetWest")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_39 = QtGui.QLabel(self.tab_5)
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 0, 0, 1, 1)
        self.tabWidgetWest.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_54 = QtGui.QLabel(self.tab_6)
        self.label_54.setObjectName("label_54")
        self.gridLayout_9.addWidget(self.label_54, 0, 0, 1, 1)
        self.tabWidgetWest.addTab(self.tab_6, "")
        self.gridLayout_5.addWidget(self.tabWidgetWest, 2, 0, 1, 1)
        self.tabWidgetWest_2 = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetWest_2.setEnabled(False)
        self.tabWidgetWest_2.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidgetWest_2.setObjectName("tabWidgetWest_2")
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_11)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_50 = QtGui.QLabel(self.tab_11)
        self.label_50.setObjectName("label_50")
        self.gridLayout_20.addWidget(self.label_50, 0, 0, 1, 1)
        self.tabWidgetWest_2.addTab(self.tab_11, "")
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_21 = QtGui.QGridLayout(self.tab_12)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_72 = QtGui.QLabel(self.tab_12)
        self.label_72.setObjectName("label_72")
        self.gridLayout_21.addWidget(self.label_72, 0, 0, 1, 1)
        self.tabWidgetWest_2.addTab(self.tab_12, "")
        self.gridLayout_5.addWidget(self.tabWidgetWest_2, 2, 1, 1, 1)
        self.tabWidgetEast = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetEast.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidgetEast.setObjectName("tabWidgetEast")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_38 = QtGui.QLabel(self.tab_3)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 0, 0, 1, 1)
        self.tabWidgetEast.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_55 = QtGui.QLabel(self.tab_4)
        self.label_55.setObjectName("label_55")
        self.gridLayout_11.addWidget(self.label_55, 0, 0, 1, 1)
        self.tabWidgetEast.addTab(self.tab_4, "")
        self.gridLayout_5.addWidget(self.tabWidgetEast, 3, 0, 1, 1)
        self.tabWidgetEast_2 = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetEast_2.setEnabled(False)
        self.tabWidgetEast_2.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidgetEast_2.setObjectName("tabWidgetEast_2")
        self.tab_13 = QtGui.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_22 = QtGui.QGridLayout(self.tab_13)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_51 = QtGui.QLabel(self.tab_13)
        self.label_51.setObjectName("label_51")
        self.gridLayout_22.addWidget(self.label_51, 0, 0, 1, 1)
        self.tabWidgetEast_2.addTab(self.tab_13, "")
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_30 = QtGui.QGridLayout(self.tab_14)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.label_73 = QtGui.QLabel(self.tab_14)
        self.label_73.setObjectName("label_73")
        self.gridLayout_30.addWidget(self.label_73, 0, 0, 1, 1)
        self.tabWidgetEast_2.addTab(self.tab_14, "")
        self.gridLayout_5.addWidget(self.tabWidgetEast_2, 3, 1, 1, 1)
        self.tabWidgetSouth = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetSouth.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidgetSouth.setTabsClosable(True)
        self.tabWidgetSouth.setObjectName("tabWidgetSouth")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_34 = QtGui.QLabel(self.tab)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 1)
        self.tabWidgetSouth.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_18 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_62 = QtGui.QLabel(self.tab_2)
        self.label_62.setObjectName("label_62")
        self.gridLayout_18.addWidget(self.label_62, 0, 0, 1, 1)
        self.tabWidgetSouth.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidgetSouth, 4, 0, 1, 1)
        self.tabWidgetSouth_2 = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetSouth_2.setEnabled(False)
        self.tabWidgetSouth_2.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidgetSouth_2.setTabsClosable(True)
        self.tabWidgetSouth_2.setObjectName("tabWidgetSouth_2")
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_31 = QtGui.QGridLayout(self.tab_15)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.label_35 = QtGui.QLabel(self.tab_15)
        self.label_35.setObjectName("label_35")
        self.gridLayout_31.addWidget(self.label_35, 0, 0, 1, 1)
        self.tabWidgetSouth_2.addTab(self.tab_15, "")
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_32 = QtGui.QGridLayout(self.tab_16)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.label_74 = QtGui.QLabel(self.tab_16)
        self.label_74.setObjectName("label_74")
        self.gridLayout_32.addWidget(self.label_74, 0, 0, 1, 1)
        self.tabWidgetSouth_2.addTab(self.tab_16, "")
        self.gridLayout_5.addWidget(self.tabWidgetSouth_2, 4, 1, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.tabWidgetNorth.setCurrentIndex(0)
        self.tabWidgetNorth_2.setCurrentIndex(1)
        self.tabWidgetWest.setCurrentIndex(0)
        self.tabWidgetWest_2.setCurrentIndex(0)
        self.tabWidgetEast.setCurrentIndex(0)
        self.tabWidgetEast_2.setCurrentIndex(0)
        self.tabWidgetSouth.setCurrentIndex(0)
        self.tabWidgetSouth_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "Containers - Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DockWidget", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DockWidget", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget North Closable Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetNorth.setTabText(self.tabWidgetNorth.indexOf(self.tab_7), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget North Closable Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetNorth.setTabText(self.tabWidgetNorth.indexOf(self.tab_8), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget North Closable Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetNorth_2.setTabText(self.tabWidgetNorth_2.indexOf(self.tab_9), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_49.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget North Closable Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetNorth_2.setTabText(self.tabWidgetNorth_2.indexOf(self.tab_10), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget West Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetWest.setTabText(self.tabWidgetWest.indexOf(self.tab_5), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget West Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetWest.setTabText(self.tabWidgetWest.indexOf(self.tab_6), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget West Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetWest_2.setTabText(self.tabWidgetWest_2.indexOf(self.tab_11), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_72.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget West Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetWest_2.setTabText(self.tabWidgetWest_2.indexOf(self.tab_12), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget East Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetEast.setTabText(self.tabWidgetEast.indexOf(self.tab_3), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget East Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetEast.setTabText(self.tabWidgetEast.indexOf(self.tab_4), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_51.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget East Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetEast_2.setTabText(self.tabWidgetEast_2.indexOf(self.tab_13), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_73.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget East Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetEast_2.setTabText(self.tabWidgetEast_2.indexOf(self.tab_14), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget South Closable Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetSouth.setTabText(self.tabWidgetSouth.indexOf(self.tab), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget South Closable Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetSouth.setTabText(self.tabWidgetSouth.indexOf(self.tab_2), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget South Closable Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetSouth_2.setTabText(self.tabWidgetSouth_2.indexOf(self.tab_15), QtGui.QApplication.translate("DockWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_74.setText(QtGui.QApplication.translate("DockWidget", "Inside TabWidget South Closable Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetSouth_2.setTabText(self.tabWidgetSouth_2.indexOf(self.tab_16), QtGui.QApplication.translate("DockWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))


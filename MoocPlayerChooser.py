# coding: utf-8
################################################
#
#  MoocPlayerChooser.py
#
#  Copyright 2018 Jonathan Wiedemann <contact at freecad-france dot com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
################################################

__title__="MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"

# import pyside2 module for ui
from PySide2 import QtCore, QtGui, QtWidgets

# for handling paths
import os, moocwb_locator

# import freecad and its gui
import FreeCAD as app
import FreeCADGui as gui



class Ui_MoocPlayerChooser(QtWidgets.QDialog):
    '''The FreeCAD Player chooser interface'''
    def setupUi(self, MoocPlayerChooser):
        MoocPlayerChooser.setObjectName("MoocPlayerChooser")
        MoocPlayerChooser.resize(324, 339)
        self.verticalLayout = QtWidgets.QVBoxLayout(MoocPlayerChooser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_welcome = QtWidgets.QLabel(MoocPlayerChooser)
        self.label_welcome.setObjectName("label_welcome")
        self.verticalLayout.addWidget(self.label_welcome)
        self.listWidget_trainings = QtWidgets.QListWidget(MoocPlayerChooser)
        self.listWidget_trainings.setObjectName("listWidget_trainings")
        QtWidgets.QListWidgetItem(self.listWidget_trainings)
        QtWidgets.QListWidgetItem(self.listWidget_trainings)
        QtWidgets.QListWidgetItem(self.listWidget_trainings)
        QtWidgets.QListWidgetItem(self.listWidget_trainings)
        self.verticalLayout.addWidget(self.listWidget_trainings)
        self.label_description = QtWidgets.QLabel(MoocPlayerChooser)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.buttonBox = QtWidgets.QDialogButtonBox(MoocPlayerChooser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MoocPlayerChooser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MoocPlayerChooser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MoocPlayerChooser.reject)
        QtCore.QObject.connect(self.listWidget_trainings, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), MoocPlayerChooser.launch_mooc)
        QtCore.QObject.connect(self.listWidget_trainings, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), MoocPlayerChooser.get_description)
        QtCore.QMetaObject.connectSlotsByName(MoocPlayerChooser)

        self.show()

    def retranslateUi(self, MoocPlayerChooser):
        MoocPlayerChooser.setWindowTitle(QtWidgets.QApplication.translate("MoocPlayerChooser", "Choisir la leçon", None, -1))
        self.label_welcome.setText(QtWidgets.QApplication.translate("MoocPlayerChooser", u"Quelle leçon souhaitez vous étudier aujourd'hui ?", None, -1))
        __sortingEnabled = self.listWidget_trainings.isSortingEnabled()
        self.listWidget_trainings.setSortingEnabled(False)
        self.listWidget_trainings.item(0).setText(QtWidgets.QApplication.translate("MoocPlayerChooser", "FUN Mooc Modélisation 3D Semaine 1", None, -1))
        self.listWidget_trainings.item(1).setText(QtWidgets.QApplication.translate("MoocPlayerChooser", "FUN Mooc Modélisation 3D Semaine 2", None, -1))
        self.listWidget_trainings.item(2).setText(QtWidgets.QApplication.translate("MoocPlayerChooser", "FUN Mooc Modélisation 3D Semaine 3", None, -1))
        self.listWidget_trainings.item(3).setText(QtWidgets.QApplication.translate("MoocPlayerChooser", "FUN Mooc Modélisation 3D Semaine 4", None, -1))
        self.listWidget_trainings.setSortingEnabled(__sortingEnabled)
        self.label_description.setText(QtWidgets.QApplication.translate("MoocPlayerChooser", "Cliquer sur un éléments de la liste pour obtenir la description de la leçon.", None, -1))

    def accept(self):
        self.launch_mooc(self.listWidget_trainings.currentItem())

    def get_description(self, item):
        row = self.listWidget_trainings.row(item)
        if row==0:
            self.label_description.setText(QtWidgets.QApplication.translate("MoocPlayerChooser",
             "Tutoriel de la semaine 1 du mooc, modélisation 3D", None, -1))
        if row==1:
            self.label_description.setText(QtWidgets.QApplication.translate("MoocPlayerChooser",
             "Tutoriel de la semaine 2 du mooc, modélisation 3D", None, -1))
        if row==2:
            self.label_description.setText(QtWidgets.QApplication.translate("MoocPlayerChooser",
             "Tutoriel de la semaine 3 du mooc, modélisation 3D", None, -1))
        if row==3:
            self.label_description.setText(QtWidgets.QApplication.translate("MoocPlayerChooser",
             "Tutoriel de la semaine 4 du mooc, modélisation 3D", None, -1))

    def launch_mooc(self, item):
        row = self.listWidget_trainings.row(item)
        self.close()
        # import MoocPlayer
        import MoocPlayer
        # make sure MoocChecker is reloaded
        try :
            reload(MoocPlayer)
        except NameError:
            import importlib
            importlib.reload(MoocPlayer)

        if row == 0:
            command = MoocPlayer.FCPlayer1()
        elif row == 1:
            command = MoocPlayer.FCPlayer2()
        elif row == 2:
            command = MoocPlayer.FCPlayer3()
        elif row == 3:
            command = MoocPlayer.FCPlayer4()
        command.Activated()


class MoocChooser():
        "class to choose the lesson"
        def GetResources(self):
            moocWBpath = os.path.dirname(moocwb_locator.__file__)
            moocWBpath_medias = os.path.join(moocWBpath, 'medias')
            moocWB_icons_path = os.path.join( moocWBpath_medias, 'icons')
            return {'Pixmap'  : os.path.join( moocWB_icons_path , 'mooc-workbench.svg'),
                    'MenuText': QtCore.QT_TRANSLATE_NOOP(u"Mooc","Choisir la leçon."),
                    'ToolTip': QtCore.QT_TRANSLATE_NOOP(u"Mooc","Choisir la leçon.")}

        def IsActive(self):
            return True

        def Activated(self):
            form = Ui_MoocPlayerChooser()
            form.setupUi(form)
            form.exec_()


if app.GuiUp:
    gui.addCommand('Mooc_Player', MoocChooser())

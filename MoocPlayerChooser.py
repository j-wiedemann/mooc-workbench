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


from os import listdir
from os.path import isfile, join
import importlib.util


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
        self.verticalLayout.addWidget(self.listWidget_trainings)
        self.label_description = QtWidgets.QLabel(MoocPlayerChooser)
        self.label_description.setObjectName("label_description")
        self.label_description.setWordWrap(True)
        self.verticalLayout.addWidget(self.label_description)
        self.buttonBox = QtWidgets.QDialogButtonBox(MoocPlayerChooser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.get_lessons_title_list()

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
        self.label_description.setText(QtWidgets.QApplication.translate("MoocPlayerChooser", "Cliquer sur un éléments de la liste pour obtenir la description de la leçon.", None, -1))

    def accept(self):
        self.launch_mooc(self.listWidget_trainings.currentItem())

    def get_lessons_title_list(self):
        self.lessons_infos_list = []
        moocWBpath = os.path.dirname(moocwb_locator.__file__)
        moocWBpath_lessons = os.path.join(moocWBpath, 'lessons')
        onlyfiles = [f for f in listdir(moocWBpath_lessons) if isfile(join(moocWBpath_lessons, f))]
        #print(onlyfiles)

        for lesson in onlyfiles:
            name = lesson.split('.')[0]
            path = os.path.join(moocWBpath_lessons, lesson)
            spec = importlib.util.spec_from_file_location(name, path)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            self.lessons_infos_list.append([foo.get_title(),foo.get_description(),name])
            '''print(foo.get_title())
            print(foo.get_description())
            print(foo.__title__)'''

            self.listWidget_trainings.addItem(foo.get_title())

    def get_description(self, item):
        # get the row number from item
        row = self.listWidget_trainings.row(item)
        # display descritpion in label from lessons list
        self.label_description.setText(self.lessons_infos_list[row][1])

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
            return {'Pixmap'  : os.path.join( moocWB_icons_path , 'mooc-player.svg'),
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

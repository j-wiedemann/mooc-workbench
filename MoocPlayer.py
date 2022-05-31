# coding: utf-8
################################################
#
#  MoocPlayer.py
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

__title__ = "MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "https://freecad-france.com"

# to make gui
from PySide import QtCore, QtGui

# to handle resources paths
import os
import sys
import moocwb_locator

# to load module from path
from os import listdir
from os.path import isfile, join

if sys.version_info > (3, 0):  # py3
    import importlib
else:  # py2
    import imp

# import freecad and its gui
import FreeCAD as app
import FreeCADGui as gui

# import webbrowser to play video inside default web Browser
import webbrowser

# import MoocChecker
import MoocChecker
import MoocCheckerSpreadsheet
import MoocCheckerPart


# to DEBUG purpose
DEBUG = False

# if DEBUG make sure MoocChecker is reloaded
if DEBUG:
    try:
        reload(MoocChecker)
        reload(MoocCheckerSpreadsheet)
        reload(MoocCheckerPart)
    except NameError:
        importlib.reload(MoocChecker)
        importlib.reload(MoocCheckerSpreadsheet)
        importlib.reload(MoocCheckerPart)


def debug():
    if DEBUG:
        print("DEBUG:ping TIMER")


# set global timer
TIMER = QtCore.QTimer()
if DEBUG:
    TIMER.timeout.connect(debug)

moocWB_path = os.path.dirname(moocwb_locator.__file__)
moocWB_medias_path = os.path.join(moocWB_path, "medias")
moocWB_icons_path = os.path.join(moocWB_medias_path, "icons")

QtWidgets = QtGui


class Ui_MoocPlayer(QtWidgets.QDialog):
    """The FreeCAD Player interface"""

    def __init__(self, parent=gui.getMainWindow()):
        super(Ui_MoocPlayer, self).__init__(parent)
        self.setObjectName("MoocPlayer")
        self.resize(400, 640)
        mw_size = parent.size()
        mw_pos = parent.pos()
        move_x = mw_pos.x() + mw_size.width() - self.size().width()
        move_y = mw_pos.y() + mw_size.height() / 2 - self.size().height() / 2
        self.move(move_x, move_y)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.verticalLayout_left = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        self.label_resume = QtWidgets.QLabel(self)
        self.label_resume.setObjectName("label_resume")
        self.verticalLayout_left.addWidget(self.label_resume)
        self.text_resume = QtWidgets.QTextBrowser(self)
        self.text_resume.setAcceptRichText(True)
        self.text_resume.setObjectName("text_resume")
        self.verticalLayout_left.addWidget(self.text_resume)
        self.horizontalLayout_play = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_play.setObjectName("horizontalLayout_play")
        self.btn_play = QtWidgets.QPushButton(self)
        self.btn_play.setObjectName("btn_play")
        self.btn_play.setIcon(
            QtGui.QIcon(os.path.join(moocWB_icons_path, "media-playback-start.svg"))
        )
        self.horizontalLayout_play.addWidget(self.btn_play)
        self.btn_help = QtWidgets.QPushButton(self)
        self.btn_help.setObjectName("btn_help")
        self.btn_help.setIcon(
            QtGui.QIcon(os.path.join(moocWB_icons_path, "help-contents.svg"))
        )
        self.horizontalLayout_play.addWidget(self.btn_help)
        self.verticalLayout_left.addLayout(self.horizontalLayout_play)
        self.label_objectifs = QtWidgets.QLabel(self)
        self.label_objectifs.setObjectName("label_objectifs")
        self.verticalLayout_left.addWidget(self.label_objectifs)
        self.listWidget_objectifs = QtWidgets.QListWidget(self)
        self.listWidget_objectifs.setObjectName("listWidget_objectifs")
        self.listWidget_objectifs.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection
        )
        self.verticalLayout_left.addWidget(self.listWidget_objectifs)
        self.horizontalLayout_change_step = QtWidgets.QHBoxLayout()
        self.horizontalLayout_change_step.setObjectName("horizontalLayout_change_step")
        self.btn_previous_step = QtWidgets.QPushButton(self)
        self.btn_previous_step.setObjectName("btn_previous_step")
        self.btn_previous_step.setIcon(
            QtGui.QIcon(os.path.join(moocWB_icons_path, "go-previous.svg"))
        )
        self.horizontalLayout_change_step.addWidget(self.btn_previous_step)
        self.label_step = QtWidgets.QLabel(self)
        self.label_step.setAlignment(QtCore.Qt.AlignCenter)
        self.label_step.setObjectName("label_step")
        self.horizontalLayout_change_step.addWidget(self.label_step)
        self.btn_next_step = QtWidgets.QPushButton(self)
        self.btn_next_step.setObjectName("btn_next_step")
        self.btn_next_step.setIcon(
            QtGui.QIcon(os.path.join(moocWB_icons_path, "go-next.svg"))
        )
        self.horizontalLayout_change_step.addWidget(self.btn_next_step)
        self.verticalLayout_left.addLayout(self.horizontalLayout_change_step)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(app.Qt.translate("MOOC", "Tutoriels FreeCAD"))
        self.label_resume.setText(app.Qt.translate("MOOC", "Résumé de la leçon"))
        self.label_objectifs.setText(app.Qt.translate("MOOC", "Objectifs à réaliser"))
        self.btn_help.setText(app.Qt.translate("MOOC", "Aide"))
        self.btn_previous_step.setText(app.Qt.translate("MOOC", "Précédent"))
        self.label_step.setText(app.Qt.translate("MOOC", "Étape X / X"))
        self.btn_next_step.setText(app.Qt.translate("MOOC", "Suivant"))
        self.btn_play.setText(app.Qt.translate("MOOC", "Voir la vidéo"))

    def closeEvent(self, event):
        TIMER.stop()
        if DEBUG:
            print("Closing Mooc Player")


class Manager_MoocPlayer:
    """functions to control and update the dialog"""

    def __init__(self, lesson):
        self.form = Ui_MoocPlayer()
        self.lesson = lesson
        self.form.setWindowTitle(self.lesson.get_title())
        self.current_step_id = 0
        self.total_step = self.lesson.get_lesson_len()
        self.fill_data()

        self.form.btn_play.clicked.connect(self.play_video)
        self.form.btn_next_step.clicked.connect(self.forward_step)
        self.form.btn_previous_step.clicked.connect(self.backward_step)
        if DEBUG:
            print(self.lesson.get_title())
            print(self.get_label_step())

        TIMER.start(200)
        TIMER.timeout.connect(self.update)

        self.form.exec_()

    def get_label_step(self):
        label = app.Qt.translate("MOOC", "Étape") + " " + str(self.current_step_id + 1) + " / " + str(self.total_step)
        return label

    def forward_step(self):
        if self.current_step_id + 1 < self.total_step:
            self.current_step_id += 1
            if DEBUG:
                print(self.get_label_step())
            self.fill_data()
        else:
            if DEBUG:
                print("This is the end !")
            pass

    def backward_step(self):
        if self.current_step_id > 0:
            self.current_step_id -= 1
            if DEBUG:
                print(self.get_label_step())
            self.fill_data()
        else:
            if DEBUG:
                print("This is the beginning !")
            pass

    def fill_data(self):
        self.form.label_step.setText(self.get_label_step())
        step_data = self.lesson.get_data_step(self.current_step_id)
        self.form.text_resume.setHtml(step_data["description"])
        self.form.listWidget_objectifs.clear()
        for obj in step_data["objectives"]:
            self.form.listWidget_objectifs.addItem(obj)
        self.form.listWidget_objectifs.setFixedHeight(
            (self.form.listWidget_objectifs.sizeHintForRow(0) + 10)
            * self.form.listWidget_objectifs.count()
            + 10 * self.form.listWidget_objectifs.frameWidth()
            + 8
        )

    def play_video(self):
        step_data = self.lesson.get_data_step(self.current_step_id)
        link_url = step_data["video"]
        webbrowser.open(link_url, new=2)

    def get_results(self):
        step_data = self.lesson.get_data_step(self.current_step_id)
        results = []
        for func in step_data["checks"]:
            results.append(eval(func))
        if len(results) > 0:
            return results
        else:
            return [0]

    def update(self):
        if DEBUG:
            print("Manager_MoocPlayer.update")
        results = self.get_results()
        brush_green = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush_green.setStyle(QtCore.Qt.NoBrush)
        brush_red = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush_red.setStyle(QtCore.Qt.NoBrush)

        idx = 0
        if results:
            for x in results:
                if x == 0:
                    self.form.listWidget_objectifs.item(idx).setForeground(brush_red)
                    self.form.listWidget_objectifs.item(idx).setIcon(
                        QtGui.QIcon(os.path.join(moocWB_icons_path, "window-close.svg"))
                    )
                elif x == 1:
                    self.form.listWidget_objectifs.item(idx).setForeground(brush_green)
                    self.form.listWidget_objectifs.item(idx).setIcon(
                        QtGui.QIcon(os.path.join(moocWB_icons_path, "dialog-apply.svg"))
                    )
                idx += 1


class Ui_MoocChooser(QtWidgets.QDialog):
    """The FreeCAD Player chooser interface"""

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
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.get_lessons_title_list()

        self.retranslateUi(MoocPlayerChooser)
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("accepted()"), MoocPlayerChooser.accept
        )
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("rejected()"), MoocPlayerChooser.reject
        )
        QtCore.QObject.connect(
            self.listWidget_trainings,
            QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"),
            MoocPlayerChooser.launch_mooc,
        )
        QtCore.QObject.connect(
            self.listWidget_trainings,
            QtCore.SIGNAL("itemClicked(QListWidgetItem *)"),
            MoocPlayerChooser.display_lesson_description,
        )
        QtCore.QMetaObject.connectSlotsByName(MoocPlayerChooser)

        self.show()

    def retranslateUi(self, MoocPlayerChooser):
        MoocPlayerChooser.setWindowTitle(app.Qt.translate("MOOC", "Choisir la leçon"))
        self.label_welcome.setText(app.Qt.translate("MOOC", "Quelle leçon souhaitez vous étudier aujourd'hui ?"))
        self.label_description.setText(
            app.Qt.translate("MOOC", "Cliquer sur un éléments de la liste pour obtenir la description de la leçon."
        ))

    def accept(self):
        self.launch_mooc(self.listWidget_trainings.currentItem())

    def get_lessons_list(self):
        moocWB_path = os.path.dirname(moocwb_locator.__file__)
        moocWB_path_lessons = os.path.join(moocWB_path, "lessons")
        dirlist = [d for d in listdir(moocWB_path_lessons)]
        lesson_fileslist = []
        for dir in dirlist:
            l = []
            lesson_path = os.path.join(moocWB_path_lessons, dir)
            for file in listdir(lesson_path):
                if isfile(join(lesson_path, file)):
                    if os.path.splitext(file)[-1] == ".py":
                        l.append(file)
                        l.append(dir)
                        lesson_fileslist.append(l)
        lesson_fileslist.sort()
        if DEBUG:
            print(dirlist)
            print(lesson_fileslist)
        self.lessons_list = []
        for lesson in lesson_fileslist:
            name, ext = os.path.splitext(lesson[0])
            path = os.path.join(moocWB_path_lessons, lesson[1], lesson[0])
            if sys.version_info > (3, 0):
                spec = importlib.util.spec_from_file_location(name, path)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
            else:
                foo = imp.load_source(name, path)
            self.lessons_list.append(foo.lesson())

    def get_lessons_title_list(self):
        self.get_lessons_list()
        for lesson in self.lessons_list:
            self.listWidget_trainings.addItem(lesson.get_title())

    def display_lesson_description(self, item):
        # get the row number from item
        row = self.listWidget_trainings.row(item)
        # description is
        desc = self.lessons_list[row].get_description()
        # display description in label_description
        self.label_description.setText(desc)

    def launch_mooc(self, item):
        row = self.listWidget_trainings.row(item)
        lesson = self.lessons_list[row]
        self.close()
        Manager_MoocPlayer(lesson)


class Command_MoocChooser:
    "class to choose the lesson"

    def GetResources(self):
        # moocWB_path = os.path.dirname(moocwb_locator.__file__)
        # moocWB_medias_path = os.path.join(moocWB_path, 'medias')
        # moocWB_icons_path = os.path.join(moocWB_medias_path, 'icons')
        return {
            "Pixmap": os.path.join(moocWB_icons_path, "mooc-player.svg"),
            "MenuText": app.Qt.translate("MOOC", "Voir un tutoriel."),
            "ToolTip": app.Qt.translate(
                "MOOC", "Permet de choisir et voir un tutoriel interactif."
            ),
        }

    def IsActive(self):
        return True

    def Activated(self):
        form = Ui_MoocChooser()
        form.setupUi(form)
        form.exec_()


if app.GuiUp:
    gui.addCommand("Mooc_Player", Command_MoocChooser())

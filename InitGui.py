# coding: utf-8
################################################
#
#  InitGui.py
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
__url__ = "http://www.freecadweb.org"

# for handling paths
import os
import moocwb_locator

# import freecad and its gui
import FreeCAD
import FreeCADGui


global MOOC_VERSION
MOOC_VERSION = "V1.3.0"

moocWB_path = os.path.dirname(moocwb_locator.__file__)
moocWB_medias_path = os.path.join(moocWB_path, "medias")
moocWB_translation_path = os.path.join(moocWB_path, "translations")
moocWB_icons_path = os.path.join(moocWB_medias_path, "icons")
FreeCADGui.addLanguagePath(moocWB_translation_path)
FreeCADGui.updateLocale()

global main_moocWB_Icon
main_moocWB_Icon = os.path.join(moocWB_icons_path, "mooc-workbench.svg")


class MoocWorkbench(Gui.Workbench):
    """The MOOC Workbench."""
    from PySide.QtCore import QT_TRANSLATE_NOOP
    global main_moocWB_Icon

    MenuText = "MOOC"
    ToolTip = FreeCAD.Qt.translate("MOOC", "Apprenez FreeCAD")
    Icon = main_moocWB_Icon

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import MoocPlayer
        import MoocGrader

        self.appendToolbar("MOOC", ["Mooc_Player", "Mooc_Grader"])
        self.appendMenu("MOOC", ["Mooc_Player", "Mooc_Grader"])
        print("Initialize MOOC module... done.")

    def Activated(self):
        "This function is executed when the workbench is activated"
        print("Activated MoocWorkbench... done")
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(MoocWorkbench())

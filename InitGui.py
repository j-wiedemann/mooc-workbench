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

__title__="MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"

# for handling paths
import os, moocwb_locator

# import freecad and its gui
import FreeCAD as app
import FreeCADGui as gui

global MOOC_VERSION
MOOC_VERSION = 'V0.1.3'

moocWBpath = os.path.dirname(moocwb_locator.__file__)
moocWBpath_medias = os.path.join(moocWBpath, 'medias')
moocWB_icons_path = os.path.join(moocWBpath_medias, 'icons')

global main_moocWB_Icon
main_moocWB_Icon = os.path.join(moocWB_icons_path , 'mooc-workbench.svg')

class MoocWorkbench ( Workbench ):

    global main_moocWB_Icon

    MenuText = "MOOC"
    ToolTip = "Learn FreeCAD"
    Icon = main_moocWB_Icon

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        import MoocPlayer,  MoocGrader
        self.appendToolbar('MOOC',['Mooc_Player','Mooc_Grader'])
        self.appendMenu('MOOC',['Mooc_Player','Mooc_Grader'])
        print('Initialize MOOC module... done.')

    def Activated(self):
        "This function is executed when the workbench is activated"
        self.checkMoocWBVersion()
        print(u'Activated MoocWorkbench... done')
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"

    def checkMoocWBVersion(self):
        '''Check version of workbench'''
        print(u'Check workbench version...')
        import urllib.request
        webUrl  = urllib.request.urlopen('http://framagit.org/freecad-france/mooc-workbench/raw/master/InitGui.py')
        for line in webUrl:
            if 'MOOC_VERSION = ' in str(line, 'utf-8'):
                mooc_version = str(line, 'utf-8').split(' = ')
                mooc_version = mooc_version[1].split('\n')
                mooc_version = mooc_version[0][1:-1]
                print(u'MOOC last release : ' + str(mooc_version))
                print(u'MOOC current release : ' + str(MOOC_VERSION))
                if str(mooc_version) == MOOC_VERSION:
                    print(u'Mooc Workbench is up to date !')
                else:
                    print(u'Please update Mooc Workbench !')
                    from PySide2 import QtWidgets
                    reply = QtWidgets.QMessageBox.information(None, u'Mise à jour nécessaire...',
                        u'''Votre version de l'atelier MOOC est obsolète.\nMerci de le mettre à jour à l'aide de l'addon manager.''')
                # only check the first occurence
                break



gui.addWorkbench(MoocWorkbench())

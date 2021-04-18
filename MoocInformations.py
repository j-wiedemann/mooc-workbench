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

import FreeCAD

__title__ = "MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"


def checkMoocWBVersion(MOOC_VERSION):
    '''Check version of workbench'''
    print(u'Check workbench version...')
    import urllib.request
    webUrl = urllib.request.urlopen('http://framagit.org/freecad-france/mooc-workbench/raw/master/InitGui.py')
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
                import MoocInformations
                from PySide2 import QtWidgets
                reply = QtWidgets.QMessageBox.information(None, FreeCAD.Qt.translate("MOOC", 'Mise à jour nécessaire...'),
                    FreeCAD.Qt.translate("MOOC", '''Votre version de l'atelier MOOC est obsolète.\nMerci de le mettre à jour à l'aide de l'addon manager.'''))
            # only check the first occurence
            break

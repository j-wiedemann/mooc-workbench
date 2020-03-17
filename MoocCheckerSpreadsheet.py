# coding: utf-8
################################################
#
#  MoocChecker.py
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

import FreeCAD as app
import FreeCADGui as gui

import math


# for debug purposes
DEBUG = False

if DEBUG:
    print("MOOC CHECKER")


def make_result(r):
    """make_result(r) -> 0 or 1
    make final result from list of result
    to get 1 there must not be 0 in r
    r=[1,1,1,0] => result = 0
    r=[1,1,1,1] => result = 1
    """
    if DEBUG:
        print("Check.make_result(r = %s)" % r)
    if len(r) > 0:
        if 0 in r:
            result = 0
        else:
            result = 1
    else:
        result = 0
    # if DEBUG:print('result = ', result)
    # if DEBUG:print('End check')
    return result


def getSheet(sheetname=None):
    if sheetname is None:
        sheetname = "Spreadsheet"
    doc = app.ActiveDocument
    if doc:
        return app.ActiveDocument.getObject(sheetname)
    else:
        return None


def checkSheet():
    r = []
    doc = app.ActiveDocument
    if doc:
        for obj in app.ActiveDocument.Objects:
            if obj.TypeId == "Spreadsheet::Sheet":
                r.append(1)
        if len(r) < 1:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)


def checkCell(sheet="Spreadsheet", index="A1", content=""):
    r = []
    obj = getSheet(sheet)
    if obj:
        if hasattr(obj, index):
            r.append(1)
            if content:
                get = obj.get(index)
                if type(get) is str:
                    if content == get:
                        r.append(1)
                else:
                    if content == get.Value:
                        r.append(1)
    return make_result(r)


def checkAlias(sheet="Spreadsheet", index="A1", content=""):
    r = []
    obj = getSheet(sheet)
    if hasattr(obj, index):
        r.append(1)
        if content:
            if content == obj.getAlias(index):
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)
    return make_result(r)

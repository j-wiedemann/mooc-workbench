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

__title__="MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"

# import freecad and its gui
import FreeCAD as app
import FreeCADGui as gui

# for handling paths
import os, moocwb_locator


def get_title():
    title = u'[FR] MOOC Semaine 4 - Tabouret Kouign'
    return title

def get_description():
    description = u'''[FR] MOOC Semaine 4 : Tabouret Kouign'''
    return description

def get_instructions():
    filename = 'Carnet Plans Tabouret.pdf'
    return filename

def grader(doc_name):
    print("[FR] MOOC Semaine 4 - Tabouret Kouign")
    #print("importing MoocChecker")
    # import MoocChecker
    import MoocChecker
    # make sure MoocChecker is reloaded
    try :
        reload(MoocChecker)
    except NameError:
        import importlib
        importlib.reload(MoocChecker)
    # name MoocChecker
    Check = MoocChecker

    grader_dict = {"notes": [], "messages": []}

    doc = app.getDocument(doc_name)

    step_id = 0
    grader_dict["notes"].append(Check.a2p_importedPart_presence(doc, label="pied a"))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Pied A importé avec a2plus.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Pied A n'est pas importé avec a2plus.")

    step_id += 1
    grader_dict["notes"].append(Check.a2p_importedPart_presence(doc, label="pied b"))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Pied B importé avec a2plus.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Pied B n'est pas importé avec a2plus.")

    step_id += 1
    grader_dict["notes"].append(Check.a2p_importedPart_presence(doc, label="entretoise"))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Entretoise importé avec a2plus.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Entretoise n'est pas importé avec a2plus.")

    step_id += 1
    grader_dict["notes"].append(Check.a2p_importedPart_presence(doc, label="assise"))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Assise importé avec a2plus.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Assise n'est pas importé avec a2plus.")

    step_id += 1
    grader_dict["notes"].append(Check.a2p_constraint_presence(doc, type='plane'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une contrainte de plan coïncident.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il ,'y a pas contrainte de plan coïncident.")

    step_id += 1
    grader_dict["notes"].append(Check.a2p_constraint_presence(doc, type='axial'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une contrainte d'axe coïncident.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il ,'y a pas contrainte d'axe coïncident.")

    step_id += 1
    grader_dict["notes"].append(Check.a2p_constraint_presence(doc, type='planesParallel'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une contrainte de plan parallèle.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il ,'y a pas contrainte de plan parallèle.")


    return grader_dict

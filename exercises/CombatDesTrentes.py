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
    title = u'[FR] Exercice Combat des Trentes (Semaine2)'
    return title

def get_description():
    description = u'''[FR] Part Design Primitives Semaine 2 : Cette semaine nous \
allons voir comment modéliser le Korrigans de Valérian HENRY à l'aide d'esquisses \
et de fonctions d'ajout et d'enlèvement de matière.'''
    return description

def grader(doc_name):
    print("MOOC FreeCAD - Grader 02 ")
    print("importing MoocChecker")
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
    # Check for a Body presence
    grader_dict["notes"].append(Check.body_presence(doc))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a un corps de pièce.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de corps de pièce.")

    step_id += 1
    # Check for a Pad presence
    grader_dict["notes"].append(Check.pad_presence(doc, name=None, type="Length", length=18.0, midplane=True))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une protrusion de 18 mm.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de protrusion de 18 mm.")

    step_id += 1
    # Check for a Pocket presence
    grader_dict["notes"].append(Check.pocket_presence(doc, name=None, type="ThroughAll", length=None, midplane=None, reversed=None))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une cavité de type À Travers Tout.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de cavité de type À Travers Tout.")

    step_id += 1
    # Check volume
    grader_dict["notes"].append(Check.volume(doc, name=None, typeId='PartDesign::Body', target=29292.00))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Le volume correspond.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Le volume ne correspond pas.")

    step_id += 1
    # Check boundbox
    grader_dict["notes"].append(Check.boundbox_dimensions(doc, name=None, typeId='PartDesign::Body', x=40.00, y=18.00, z=65.00))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Les dimensions de la boite englobante correpsondent.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Les dimensions de la boite englobante ne correpsondent pas.")


    return grader_dict

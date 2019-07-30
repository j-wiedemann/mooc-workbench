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
    title = u'[FR] MOOC Semaine 1 - Socle Humidificateur'
    return title

def get_description():
    description = u'''[FR] Part Design Primitives Semaine 1 : Cette semaine nous \
allons voir comment modéliser le Korrigans de Steven Akoun à l'aide d'esquisses \
et de fonctions d'ajout et d'enlèvement de matière.'''
    return description

def grader(doc_name):
    print("MOOC FreeCAD - Grader 01 ")
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
    grader_dict["notes"].append(Check.primitive_presence(doc, typeId='PartDesign::AdditiveBox'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a un cube additif.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de cube additif.")

    step_id += 1
    # Check for a Pocket presence
    grader_dict["notes"].append(Check.primitive_presence(doc, typeId='PartDesign::AdditiveCylinder'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a un cylindre additif.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de cylindre additif.")

    step_id += 1
    # Check volume
    grader_dict["notes"].append(Check.primitive_presence(doc, typeId='PartDesign::SubtractiveCylinder'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a un cylindre soustractif.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de cylindre soustractif.")

    step_id += 1
    # Check boundbox
    grader_dict["notes"].append(Check.primitive_presence(doc, typeId='PartDesign::SubtractiveBox'))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a un cube soustractif.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de cube soustractif.")

    step_id += 1
    grader_dict["notes"].append(Check.boundbox_dimensions(doc, typeId='PartDesign::Body', x = 190, y = 90, z = 15))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Les dimensions extérieures correspondent avec l'objectif.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Les dimensions extérieures ne correspondent pas avec l'objectif.")

    step_id += 1
    grader_dict["notes"].append(Check.volume(doc, typeId='PartDesign::Body', target=82134))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Le volume du corps de pièce correspond avec l'objectif.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Le volume du corps de pièce ne correspond pas avec l'objectif.")

    return grader_dict

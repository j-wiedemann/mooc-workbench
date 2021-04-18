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
__url__ = "http://www.freecadweb.org"

# import freecad
import FreeCAD as app


def get_title():
    title = app.Qt.translate("MOOC", '[FR] MOOC Semaine 3 - Lampe Mercure')
    return title


def get_description():
    description = app.Qt.translate("MOOC", '''[FR] MOOC Semaine 3 : Cette semaine nous \
allons voir comment modéliser le Korrigans de Valérian HENRY à l'aide \
d'esquisses et de fonctions d'ajout et d'enlèvement de matière.''')
    return description


def get_instructions():
    filename = 'Carnet Plans Lampe.pdf'
    return filename


def grader(doc_name):
    print("MOOC FreeCAD - Grader 03 ")
    # print("importing MoocChecker")
    # import MoocChecker
    import MoocChecker
    # make sure MoocChecker is reloaded
    try:
        reload(MoocChecker)
    except NameError:
        import importlib
        importlib.reload(MoocChecker)
    # name MoocChecker
    Check = MoocChecker

    grader_dict = {"notes": [], "messages": []}

    doc = app.getDocument(doc_name)

    step_id = 0
    grader_dict["notes"].append(Check.body_presence(doc, label="Lampe"))
    if grader_dict["notes"][step_id] == 1:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il y a un corps de pièce Lampe."))
    elif grader_dict["notes"][step_id] == 0:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il n'y a pas de corps de pièce Lampe."))

    step_id += 1
    grader_dict["notes"].append(Check.body_presence(doc, label="Fil"))
    if grader_dict["notes"][step_id] == 1:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il y a un corps de pièce Fil."))
    elif grader_dict["notes"][step_id] == 0:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il n'y a pas de corps de pièce Fil."))

    step_id += 1
    grader_dict["notes"].append(Check.body_presence(doc, label="Capuchon"))
    if grader_dict["notes"][step_id] == 1:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il y a un corps de pièce Capuchon."))
    elif grader_dict["notes"][step_id] == 0:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il n'y a pas de corps de pièce Capuchon."))

    step_id += 1
    # Check for a Pocket presence
    grader_dict["notes"].append(Check.additiveloft_presence(doc))
    if grader_dict["notes"][step_id] == 1:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il y a lissage."))
    elif grader_dict["notes"][step_id] == 0:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il n'y a pas de lissage."))

    step_id += 1
    # Check volume
    grader_dict["notes"].append(Check.additivepipe_presence(doc))
    if grader_dict["notes"][step_id] == 1:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il y a un balayage."))
    elif grader_dict["notes"][step_id] == 0:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il n'y a pas de balayage."))

    step_id += 1
    # Check boundbox
    grader_dict["notes"].append(Check.revolution_presence(doc))
    if grader_dict["notes"][step_id] == 1:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il y a une révolution."))
    elif grader_dict["notes"][step_id] == 0:
        grader_dict["messages"].append(app.Qt.translate("MOOC", "Il n'y a pas de révolution."))

    return grader_dict

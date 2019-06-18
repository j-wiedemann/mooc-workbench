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


# for handling paths
import os, moocwb_locator

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

def get_title():
    title = u'[FR] MOOC Semaine 1 - Humidificateur de Steven Akoun'
    return title

def get_description():
    description = u'''[FR] Part Design Primitives Semaine 1 : Cette semaine nous \
allons voir comment modéliser l'hmidificateur de Steven avec des formes \
primitives uniquement.'''
    return description

def MakeDataTutorial():
    data_tutorial = {}
    data_tutorial['title'] = get_title()
    data_tutorial['description'] = get_description()
    data_tutorial['steps'] = []
    moocWBpath = os.path.dirname(moocwb_locator.__file__)
    moocWBpath_medias = os.path.join(moocWBpath, 'medias')
    moocWB_images_path = os.path.join(moocWBpath_medias, 'images')
    moocWB_icons_path = os.path.join(moocWBpath_medias, 'icons')

    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Document-new.svg')
    img2 = os.path.join(moocWB_icons_path, 'Workbench_PartDesign.svg')
    img3 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
    img4 = os.path.join(moocWB_images_path, 'korrigans_final.png')
    step["description"] = u'''<h3>Préparation</h3>
        <p><img src= %s width="25"/> Créer un nouveau document :
        <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Nouveau.</li>
        <li>à l'aide du raccourcis Ctrl + N</li></ul></p>
        <p><img src= %s width="25"/> Basculer dans l'atelier <b>Part Design</b> :
        <ul><li>à l'aide du sélecteur d'atelier.</li>
        <li>depuis le menu <i>Affichage</i> puis <i>Atelier</i></li></ul></p>
        <p><img src= %s width="25"/>Créer un nouveau corps de pièce :
        <ul><li>à l'aide du menu <i>Part Design</i> puis <i>Créer un corps</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li> \
        </ul></p> ''' % (img1, img2, img3)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=0m00s'
    step["objectives"] = [u"Créer un nouveau document.", u"Basculer dans l'atelier PartDesign.", u"Mode de navigation : Gesture"]
    data_tutorial['steps'].append(step)

    #step2
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
    step["description"] = u'''<h3>Corps de pièce</h3>
        <p>Pour modéliser un solide dans l'atelier Part Design nous avons
        besoin d'un corps de pièce qui contiendra toutes nos opérations.</p>
        <p><img src= %s width="25"/>Créer un nouveau corps de pièce :
        <ul><li>à l'aide du menu <i>Part Design</i> puis <i>Créer un corps</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li> \
        </ul></p>''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=1m03s'
    step["objectives"] = [u"1 Corps de piece"]
    data_tutorial['steps'].append(step)

    #step2
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Additive_Box.svg')
    step["description"] = u'''<h3>Cube additif</h3>
        <p>Nous commencerons par ajouter un cube primitif.</p>
        <p><img src= %s width="25"/> Créer un cube primitif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive additive</i> puis <i>Cube additif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Longueur = 100 mm</li>
        <li>Largeur = 80 mm</li>
        <li>Hauteur = 140 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p>On valide la tâche en cours en cliquant sur OK''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=2m23s'
    step["objectives"] = [u"1 Cube additif 100 x 80 x 140 mm"]
    data_tutorial['steps'].append(step)

    #step3
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Additive_Cylinder.svg')
    step["description"] = u'''<h3>Cylindre additif</h3> \
        <p>Ensuite nous allons ajouter des cylindres pour faire les bords arrondi de l'objet.</p>
        <p><img src= %s width="25"/> Créer un cylindre additif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive additive</i> puis <i>Cylindre additif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Rayon = 40 mm</li>
        <li>Hauteur = 140 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
        <ul><li>X = 0 mm</li>
        <li>Y = 40 mm</li>
        <li>Z = 0 mm</li></ul></p>
        <p>On valide la tâche en cours en cliquant sur OK''' % ( img1 )

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=3m32s'
    step["objectives"] = [u"1 Cylindre additif Ø40 x 140 mm"]
    data_tutorial['steps'].append(step)

    #step4
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Additive_Cylinder.svg')
    step["description"] = u'''<h3>Cylindre additif</h3> \
        <p>On recommence l'opération mais cette fois on compensera la position
        du cylindre de 100 mm en X et 40 mm en Y..</p>
        <p><img src= %s width="25"/> Créer un cylindre additif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive additive</i> puis <i>Cylindre additif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Rayon = 40 mm</li>
        <li>Hauteur = 140 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
        <ul><li>X = 100 mm</li>
        <li>Y = 40 mm</li>
        <li>Z = 0 mm</li></ul></p>
        <p>On valide la tâche en cours en cliquant sur OK''' % ( img1 )

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=4m21s'
    step["objectives"] = [u"1 Cylindre additif Ø40 x 140 mm"]
    data_tutorial['steps'].append(step)

    #step5
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Subtractive_Box.svg')
    step["description"] = u'''<h3>Cube soustractif</h3>
        <p>Pour enlever de la matière en bas de la pièce nous allons ajouter un cube soustractif.</p>
        <p><img src= %s width="25"/> Créer un cube soustractif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive soustractive</i> puis <i>Cube soustractif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Longueur = 000 mm</li>
        <li>Largeur = 80 mm</li>
        <li>Hauteur = 20 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
        <ul><li>X = 10 mm</li>
        <li>Y = 0 mm</li>
        <li>Z = 0 mm</li></ul></p>
        <p>On valide la tâche en cours en cliquant sur OK''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=4m52s'
    step["objectives"] = [u"1 Cube soustractif de 80 x 80 x 20 mm" ]
    data_tutorial['steps'].append(step)

    #step6
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Subtractive_Cylinder.svg')
    step["description"] = u'''<h3>Cube soustractif</h3>
        <p>Pour enlever de la matière en haut de la pièce nous allons ajouter un cylindre soustractif.</p>
        <p><img src= %s width="25"/> Créer un cylindre soustractif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive soustractive</i> puis <i>cylindre soustractif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Rayon = 36 mm</li>
        <li>Hauteur = 30 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
        <ul><li>X = 0 mm</li>
        <li>Y = 40 mm</li>
        <li>Z = 110 mm</li></ul></p>
        <p>On valide la tâche en cours en cliquant sur OK''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=5m38s'
    step["objectives"] = [u"1 cylindre soustractif de Ø36 x 30 mm."]
    data_tutorial['steps'].append(step)

    #step7
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Subtractive_Cylinder.svg')
    step["description"] = u'''<h3>Cube soustractif</h3>
        <p>Pour enlever de la matière en haut de la pièce nous allons ajouter un cylindre soustractif.</p>
        <p><img src= %s width="25"/> Créer un cylindre soustractif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive soustractive</i> puis <i>cylindre soustractif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Rayon = 36 mm</li>
        <li>Hauteur = 30 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
        <ul><li>X = 100 mm</li>
        <li>Y = 40 mm</li>
        <li>Z = 110 mm</li></ul></p>
        <p>On valide la tâche en cours en cliquant sur OK''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=6m20s'
    step["objectives"] = [u"1 cylindre soustractif de Ø36 x 30 mm."]
    data_tutorial['steps'].append(step)

    #step8
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Subtractive_Box.svg')
    step["description"] = u'''<h3>Cube soustractif</h3>
        <p>Pour enlever de la matière entre les deux trous cylindrique nous allons ajouter un cube soustractif.</p>
        <p><img src= %s width="25"/> Créer un cube soustractif :
        <ul><li>à l'aide du menu <i>Part Design</i> puis
        <i>Créer une primitive soustractive</i> puis <i>Cube soustractif</i>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
        <ul><li>Longueur = 100 mm</li>
        <li>Largeur = 72 mm</li>
        <li>Hauteur = 30 mm</li></ul></p>
        <p>Maintenant nous allons attacher la primitive au plan XY du corps de
        pièce en cliquant sur le plan XY dans la vue 3D.</p>
        <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
        <ul><li>X = 0 mm</li>
        <li>Y = 4 mm</li>
        <li>Z = 110 mm</li></ul></p>
        <p>On valide la tâche en cours en cliquant sur OK''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=6m51s'
    step["objectives"] = [u"1 cube soustractif de 100 x 72 x 30 mm."]
    data_tutorial['steps'].append(step)

    #step9
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Fillet.svg')
    step["description"] = u'''<h3>Faire une congé</h3> \
        <p>Pour arrondir les angles en bas de la pièce nous allons utiliser
        l'outil Congé qui créer un arrondi sur les arêtes sélectionné et selon le rayon demandé.</p>
        <p><img src= %s width="25"/> Créer un congé :
        <ul><li>Sélectionner les arêtes à arrondir.</li>
        <li>à l'aide du menu <i>Part Design</i> puis
        <i>Congé</i>.</li></ul><p>''' % (img1)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=7m47s'
    step["objectives"] = [u"1 congé de 9 mm de rayon"]
    data_tutorial['steps'].append(step)

    #step19
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Document-save.svg')
    img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')
    step["description"] = u'''<h3>Sauvegarder le document.</h3> \
        <p><img src=%s width="25"/> Sauvegader le document sous le nom <b>Humidificateur</b> : \
        <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li> \
        <li>à l'aide du raccourcis <b>Ctrl+Maj+S</b></li></lu></p> \
        <p><img src=%s width="360"/></p>''' % (img1, img2)

    step["video"] = 'https://open.tube/videos/watch/f5773731-9864-470b-a3d5-9e805c419f96?start=9m45s'
    step["objectives"] = [u"1 Sauvegardé le document sous le nom Humidificateur."]
    data_tutorial['steps'].append(step)

    return data_tutorial

def CheckResult(step_id):
    if step_id == 0:
        results = []
        results.append(Check.document_presence())
        results.append(Check.active_workbench("PartDesignWorkbench"))
        results.append(Check.navigation_style("Gui::GestureNavigationStyle"))
        return results

    # create a new body, show it's origin and relabel it
    if step_id == 1:
        results = []
        results.append(Check.body_presence())
        return results

    if step_id == 2:
        results = []
        results.append(Check.primitive_presence(label="Box", typeId='PartDesign::AdditiveBox', dimensions=[100,80,140], support="XY_Plane", offset=[0,0,0,0,0,1,0]))
        return results

    if step_id == 3:
        results = []
        results.append(Check.primitive_presence(label="Cylinder", typeId='PartDesign::AdditiveCylinder', dimensions=[40,140], support="XY_Plane", offset=[0,40,0,0,0,1,0]))
        return results

    if step_id == 4:
        results = []
        results.append(Check.primitive_presence(label="Cylinder001", typeId='PartDesign::AdditiveCylinder', dimensions=[40,140], support="XY_Plane", offset=[100,40,0,0,0,1,0]))
        return results

    if step_id == 5:
        results = []
        results.append(Check.primitive_presence(label="Box001", typeId='PartDesign::SubtractiveBox', dimensions=[80,80,20], support="XY_Plane", offset=[10.0,0.0,0.0,0.0,0.0,1.0,0.0]))
        return results

    if step_id == 6:
        results = []
        results.append(Check.primitive_presence(label="Cylinder002", typeId='PartDesign::SubtractiveCylinder', dimensions=[36,30], support="XY_Plane", offset=[0,40,110,0,0,1,0]))
        return results

    if step_id == 7:
        results = []
        results.append(Check.primitive_presence(label="Cylinder003", typeId='PartDesign::SubtractiveCylinder', dimensions=[36,30], support="XY_Plane", offset=[100,40,110,0,0,1,0]))
        return results

    if step_id == 8:
        results = []
        results.append(Check.primitive_presence(label="Box002", typeId='PartDesign::SubtractiveBox', dimensions=[100,72,30], support="XY_Plane", offset=[0,4,110,0,0,1,0]))
        return results

    if step_id == 9:
        results = []
        results.append(Check.fillet_presence(label="Fillet", radius=9))
        return results

    if step_id == 10:
        results = []
        results.append(Check.document_save('Humidificateur'))
        return results

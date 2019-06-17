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
    img2 = os.path.join(moocWB_images_path, 'Workbench_PartDesign.svg')
    img3 = os.path.join(moocWB_images_path, 'PartDesign_Body.png')
    img4 = os.path.join(moocWB_images_path, 'korrigans_final.png')
    step["description"] = u'''<h3>Préparation</h3> \
        <p><img src= %s width="25"/> Créer un nouveau document : \
        <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Nouveau.</li> \
        <li>à l'aide du raccourcis Ctrl + N</li></ul></p> \
        <p><img src= %s width="25"/> Basculer dans l'atelier <b>Part Design</b> :\
        <ul><li>à l'aide du sélecteur d'atelier.</li> \
        <li>depuis le menu <i>Affichage</i> puis <i>Atelier</i></li></ul></p> \
        <p><img src= %s width="25"/>Créer un nouveau corps de pièce : \
        <ul><li>à l'aide du menu <i>Part Design</i> puis <i>Créer un corps</i>.</li> \
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li> \
        </ul></p> ''' % (img1, img2, img3)

    step["video"] = 'https://cloud.freecad-france.com/index.php/s/AxwZyMXmAxCAzHq'
    step["objectives"] = [u"Créer un nouveau document.", u"Basculer dans l'atelier PartDesign.", u"Mode de navigation : Gesture"]
    data_tutorial['steps'].append(step)

    #step2
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Sketcher_NewSketch.svg')
    step["description"] = u'''<h3>Corps de pièce</h3> \
        <p>Pour créer la base de l'objet, on va d'abord créer une esquisse \
        sur le plan XZ du corps de pièce.</p> \
        <p><img src= %s width="25"/> Pour cela on clique sur l'icone \
        Nouvelle Esquisse et on choisit le plan XZ dans la liste visible \
        dans l'onglet Tâche de la vue combinée.</p>''' % (img1)

    step["video"] = 'https://cloud.freecad-france.com/index.php/s/AxwZyMXmAxCAzHq'
    step["objectives"] = [u"1 Corps de piece"]
    data_tutorial['steps'].append(step)

    #step2
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Sketcher_NewSketch.svg')
    step["description"] = u'''<h3>Cube additif</h3> \
        <p>Pour créer la base de l'objet, on va d'abord créer une esquisse \
        sur le plan XZ du corps de pièce.</p> \
        <p><img src= %s width="25"/> Pour cela on clique sur l'icone \
        Nouvelle Esquisse et on choisit le plan XZ dans la liste visible \
        dans l'onglet Tâche de la vue combinée.</p>''' % (img1)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 Cube additif 100 x 80 x 140 mm"]
    data_tutorial['steps'].append(step)

    #step3
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Constraint_Horizontal.svg')
    img2 = os.path.join(moocWB_images_path, 'Constraint_Vertical.svg')
    img3 = os.path.join(moocWB_images_path, 'Constraint_PointOnPoint.svg')
    step["description"] = u'''<h3>Cylindre additif</h3> \
        <p>Dessiner un contour fermé de 5 coté à l'aide de l'outil polyligne.<p> \
        <p><img src=%s width="25"/> L'outil polyligne ajoute \
        automatiquement des contrainte de coïncidence entre chaque extrémités de segment.<p>\
        <p>Faire en sorte d'avoir des contraintes verticales <img src= %s width="25"/> \
         et horizontales <img src=%s width="25"/>  sur les bons éléments.</p> \
        <p>À ce stade l'esquisse dispose de 7 degrès de liberté \
        restants.</p>''' % (img3, img1, img2)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 Cylindre additif Ø40 x 140 mm"]
    data_tutorial['steps'].append(step)

    #step4
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Constraint_EqualLength.svg')
    step["description"] =  u'''<h3>Cylindre additif</h3> \
        <p>Nous pouvons contraindre 2 segments à être égaux, dans notre cas \
        on veut que les 2 segments verticaux soient égaux entre eux et de \
        même pour les 2 segments obliques.</p> \
        <p>On sélectionne d'abord les 2 segments verticaux puis on clique \
        sur l'icône <img src=%s width="25"/>. Et on recommence pour les 2 segments obliques.<p>''' %(img1)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 Cylindre additif Ø40 x 140 mm"]
    data_tutorial['steps'].append(step)

    #step5
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Constraint_HorizontalDistance.svg')
    img2 = os.path.join(moocWB_images_path, 'Constraint_VerticalDistance.svg')
    img3 = os.path.join(moocWB_images_path, 'Constraint_InternalAngle.svg')
    step["description"] = u'''<h3>Cube soustractif</h3> \
        <p>Pour paramétrer précisement les mesures de notre esquisse,  \
        on va ajouter des contraintes de dimensions.</p> \
        <p><img src=%s width="25"/>Pour ajouter des dimensions horizontale entre 2 points ou un segment, \
        on sélectionne l'outil <i>Contrainte distance horizontale</i> : \
        <ul><li>à l'aide du raccourcis : <i>Maj + H</i></li> \
        <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte distance horizontale.</i></li></ul> \
        Puis on clique sur le segment ou 2 points dans l'esquisse. \
        Une fenêtre apparait et permet de préciser la valeur de la distance. \
        <b>Ici c'est 55 mm.</b> On clique enfin sur Ok pour valider la contrainte.</p> \
        <p><img src= %s width="25"/> Le fonctionnement est le même pour ajouter une contrainte de distance verticale : \
        <ul><li>à l'aide du raccourcis : <i>Maj + V</i></li> \
        <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte distance verticale.</i></li></ul> \
        Ici la valeur demandé <b>est de 150 mm.</b></p> \
        <p><img src= %s width="25"/>Pour ajouter un angle entre 2 segments on utilisera une <b>contrainte angulaire :</b> \
        <ul><li>à l'aide du raccourcis : A</li> \
        <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte angulaire.</i></li></ul> \
        Ensuite il faut cliquer sur 2 segments et préciser la valeur de l'angle. <b>Ici c'est 55°.</b></p>''' % ( img1, img2, img3 )

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 Cube soustractif de 80 x 80 x 20 mm" ]
    data_tutorial['steps'].append(step)

    #step6
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Constraint_Symmetric.svg')
    step["description"] = u'''<h3>cylindre soustractif</h3> \
        <p>Il nous reste 2 degrès de libertés qui sont les positions X et Y  \
        de notre contour dans l'esquisse.<p> \
        <p>Nous allons contraindre le contour de façon à ce que l'origine  \
        passe par le milieu du segment horizontal.<p> \
        <p><img src= %s width="25"/>Pour contraindre un point au milieu \
        d'un segment on utilise une contrainte de symétrie.<p>''' % (img1)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 cylindre soustractif de Ø36 x 30 mm."]
    data_tutorial['steps'].append(step)

    #step7
    step = {}
    img1 = os.path.join(moocWB_images_path, 'PartDesign_Pad.svg')
    step["description"] = u'''<h3>cylindre soustractif</h3> \
        <p>Nous allons maintenant créer une protrusion de 55 mm à partir de \
        cette esquisse afin de générer du volume.<p> \
        <p>On commence par sélectionner l'esquisse qui servira de base à la \
        protrusion, puis on clique sur l'icone <img src= %s width="25"/>.</p> \
        <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant : \
        <ul><li>Type : Dimension</li> \
        <li>Longueur : 55 mm</li> \
        <li>Symétrique au plan : coché</li> \
        <li>Inversée : décoché</li></ul></p>''' % (img1)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 cylindre soustractif de Ø36 x 30 mm."]
    data_tutorial['steps'].append(step)

    #step8
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Sketcher_External.svg')
    step["description"] = u'''<h3>Cube soustractif</h3> \
        <p>Dans cette étape nous allons créer une nouvelle esquisse sur le plan YZ \
        pour dessiner un triangle qui nous permettra d'enlever de la matière \
        pour faire les pentes du chapeau. Pour positionner abilement le triangle \
        nous utiliseront les arêtes externes.</p> \
        <p>Les arêtes externes nous permettent de projeter des arêtes du \
        volume sous jacent dans le plan de l'esquisse et ainsi y contraindre des géométries.<p> \
        <p>On va cliquer sur l'icône <img src= %s width="25"/> et ensuite \
        cliquer sur les arêtes du volume que l'on souhaite utiliser.</p>''' % (img1)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 cube soustractif de 100 x 72 x 30 mm."]
    data_tutorial['steps'].append(step)

    #step9
    step = {}
    img1 = os.path.join(moocWB_images_path, 'PartDesign_Pocket.svg')
    step["description"] = u'''<h3>Faire une congé</h3> \
        <p>Une cavité (pocket en anglais) est une fonction qui sert à enlever de la matière.</p> \
        <p>On commence par sélectionner l'esquisse qui servira de base à la \
        cavité, puis on clique sur l'icone <img src= %s width="25"/>.</p> \
        <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant : \
        <ul><li>Type : À travers tout</li> \
        <li>Symétrique au plan : coché</li> \
        <li>Inversée : décoché</li></ul></p>''' % (img1)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
    step["objectives"] = [u"1 congé de 9 mm de rayon"]
    data_tutorial['steps'].append(step)

    #step19
    step = {}
    img1 = os.path.join(moocWB_images_path, 'Document-save.svg')
    img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')
    step["description"] = u'''<h3>Sauvegarder le document.</h3> \
        <p><img src=%s width="25"/> Sauvegader le document sous le nom <b>Humidificateur</b> : \
        <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li> \
        <li>à l'aide du raccourcis <b>Ctrl+Maj+S</b></li></lu></p> \
        <p><img src=%s width="360"/></p>''' % (img1, img2)

    step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
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
        results.append(Check.primitive_presence(label="Box", type='PartDesign::AdditiveBox', dimensions=[100,80,140], support="XY_Plane", offset=[0,0,0,0,0,1,0]))
        return results

    if step_id == 3:
        results = []
        results.append(Check.primitive_presence(label="Cylinder", type='PartDesign::AdditiveCylinder', dimensions=[40,140], support="XY_Plane", offset=[0,40,0,0,0,1,0]))
        return results

    if step_id == 4:
        results = []
        results.append(Check.primitive_presence(label="Cylinder001", type='PartDesign::AdditiveCylinder', dimensions=[40,140], support="XY_Plane", offset=[100,40,0,0,0,1,0]))
        return results

    if step_id == 5:
        results = []
        results.append(Check.primitive_presence(label="Box001", type='PartDesign::SubstractiveBox', dimensions=[80,80,20], support="XY_Plane", offset=[10,0,0,0,0,1,0]))
        return results

    if step_id == 6:
        results = []
        results.append(Check.primitive_presence(label="Cylinder002", type='PartDesign::SubstractiveCylinder', dimensions=[36,30], support="XY_Plane", offset=[0,40,110,0,0,1,0]))
        return results

    if step_id == 7:
        results = []
        results.append(Check.primitive_presence(label="Cylinder003", type='PartDesign::SubstractiveCylinder', dimensions=[36,30], support="XY_Plane", offset=[100,40,110,0,0,1,0]))
        return results

    if step_id == 8:
        results = []
        results.append(Check.primitive_presence(label="Box002", type='PartDesign::SubstractiveBox', dimensions=[100,72,30], support="XY_Plane", offset=[0,4,110,0,0,1,0]))
        return results

    if step_id == 9:
        results = []
        results.append(Check.fillet_presence(label="Fillet", radius=9))
        return results

    if step_id == 10:
        results = []
        results.append(Check.document_save('Humidificateur'))
        return results

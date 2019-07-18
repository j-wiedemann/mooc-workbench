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
    title = u'[FR] MOOC Semaine 3 - Lampe Mercure de Lucie Le Guen'
    return title

def get_description():
    description = u'''[FR] MOOC Semaine 3 : Cette semaine nous allons modéliser
    la Lampe Mercure de Lucie Le Guen. Nous allons travailler dans l'atelier
    Part Design et utiliser des opérations de lissage, balayage et révolution.'''
    return description

def MakeDataTutorial():
    data_tutorial = {}
    data_tutorial['title'] = get_title()
    data_tutorial['description'] = get_description()
    data_tutorial['url_video'] = 'https://open.tube/videos/embed/a9863ee3-a0d8-4919-8b28-8920246d22e6'
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
        <p>Créer un nouveau document :
        <ul><li>en cliquant sur l'icone <img src= %s width="25"/> </li>
        <li>à l'aide du menu <i>Fichier</i> puis <i>Nouveau.</li>
        <li>à l'aide du raccourcis Ctrl + N (sur Winodws et Linux ) ou Cmd ⌘ + N (sur Mac)</li></ul></p>
        <p> Basculer dans l'atelier <b>Part Design</b> :
        <ul><li>à l'aide du sélecteur d'atelier.<img src= %s width="25"/></li>
        <li>depuis le menu <i>Affichage</i> puis <i>Atelier</i></li></ul></p>
        <p>Créer un nouveau corps de pièce :
        <ul><li>en cliquant sur l'icone <img src= %s width="25"/></li>
        <li>à l'aide du menu <b>Part Design</b> puis <b>Créer un corps</b>.</li>
        <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
        <p>Sélectionner le corps de pièce puis renommer le corps de pièce en <b>Lampe</b> :
        <ul><li>en faisant un clic droit sur l'objet dans l'arborescence puis <b>Renommer</b></li>
        <li>à l'aide du raccourcis <b>F2</b></li>
        <li>en modifiant la propriété <b>Label</b> dans l'onglet <b>Données</b> de ses paramètres</li></ul></p>''' % (img1, img2, img3)

    step["video"] = data_tutorial['url_video'] + str('?start=0m00s')
    step["objectives"] = [u"Créer un nouveau document.", u"Basculer dans l'atelier PartDesign.", u'1 corps de pièce nommé "Lampe".']
    data_tutorial['steps'].append(step)

    #step2
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Plane.svg')
    step["description"] = u'''<h3>Créer des plans de référence</h3>
        <p>Nous avons besoin de 3 plans de références pour placer nos
         profils. Ils seront coplanaire au plan YZ et décalés respectivement de
         0mm, 50mm et 100 mm selon l'axe Z.</p>
        <p>Pour créer le premier plan de référence, on commence par afficher
        l'origine du corps de pièce (barre espace sur la fonction Origin),
        ensuite on clique sur l'icône <img src= %s width="25"/>.</p>
        <p>On valide la création du premier plan en cliquant sur Ok dans
        l'onglet Tâches ou en appuyant sur la touche Entrer.</p>
        <p>Pour créer les plans suivant on reproduit la même manipulaution mais
        cette fois on va paraméter une compensation de placement dans l'onglet
        Tâches. Dans les parametres de compensation on décalera le deuxième plan
        de 50 mm selon Z et le troisième plan de 100 mm selon Z.</p>''' % (img1)

    step["video"] = data_tutorial['url_video'] + str('?start=0m45s')
    step["objectives"] = [u"1 plan de référence coplanaire à YZ et décaler de 0 mm selon Z.",
    u"1 plan de référence coplanaire à YZ et décaler de 50 mm selon Z.",
    u"1 plan de référence coplanaire à YZ et décaler de 100 mm selon Z."]
    data_tutorial['steps'].append(step)

    #step3
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Constraint_Horizontal.svg')
    img2 = os.path.join(moocWB_icons_path, 'Constraint_Vertical.svg')
    img3 = os.path.join(moocWB_icons_path, 'Constraint_PointOnPoint.svg')
    img4 = os.path.join(moocWB_icons_path, 'Sketcher_CreatePolyline.svg')
    img5 = os.path.join(moocWB_images_path, 'Lesson2Step3.png')
    step["description"] = u'''<h3>Création de la première esquisse</h3>
        <p>Dessiner un contour fermé de 5 coté à l'aide de l'outil polyligne.</p>
        <p><img src=%s width="25"/> L'outil polyligne ajoute
        automatiquement des contraintes de coïncidence <img src=%s width="25"/>
        entre chaque extrémités de segment.</p>
        <p>Faire en sorte d'avoir des contraintes verticales <img src= %s width="25"/>
         et horizontales <img src=%s width="25"/>  sur les bons éléments.</p>
        <p>À ce stade l'esquisse dispose de 7 degrès de liberté
        restants.</p><p><img src=%s/></p>''' % (img4, img3, img1, img2, img5)

    step["video"] = data_tutorial['url_video'] + str('?start=1m45s')
    step["objectives"] = [u"1 esquisse sur plan de référence.",
    u"2 hexagones régulier de ø 40 mm.",
    u"1 contrainte de rayon de 17 mm.",
    u"1 contrainte de rayon de 20 mm."]
    data_tutorial['steps'].append(step)

    #step4
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Constraint_EqualLength.svg')
    step["description"] =  u'''<h3>Deuxieme Esquisse</h3>
        <p>Nous pouvons contraindre 2 segments à être égaux, dans notre cas
        on veut que les 2 segments verticaux soient égaux entre eux et de
        même pour les 2 segments obliques.</p>
        <p>On sélectionne d'abord les 2 segments verticaux puis on clique
        sur l'icône <img src=%s width="25"/>. Et on recommence pour les 2 segments obliques.</p>''' %(img1)

    step["video"] = data_tutorial['url_video'] + str('?start=2m57s')
    step["objectives"] = [u"1 esquisse sur DatumPlane001.",
    u"2 hexagones régulier.",
    u"1 contrainte de rayon de 47 mm.",
    u"1 contrainte de rayon de 50 mm."]
    data_tutorial['steps'].append(step)

    #step5
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Constraint_HorizontalDistance.svg')
    img2 = os.path.join(moocWB_icons_path, 'Constraint_VerticalDistance.svg')
    img3 = os.path.join(moocWB_icons_path, 'Constraint_InternalAngle.svg')
    step["description"] = u'''<h3>Troisieme esquisse</h3>
        <p>Pour paramétrer précisement les mesures de notre esquisse,
        on va ajouter des contraintes de dimensions.</p>
        <p><img src=%s width="25"/>Pour ajouter des dimensions horizontale entre 2 points ou un segment,
        on sélectionne l'outil <i>Contrainte distance horizontale</i> :
        <ul><li>à l'aide du raccourcis : <i>Maj + H</i></li>
        <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte distance horizontale.</i></li></ul>
        Puis on clique sur le segment ou 2 points dans l'esquisse.
        Une fenêtre apparait et permet de préciser la valeur de la distance.
        <b>Ici c'est 55 mm.</b> On clique enfin sur Ok pour valider la contrainte.</p>
        <p><img src= %s width="25"/> Le fonctionnement est le même pour ajouter une contrainte de distance verticale :
        <ul><li>à l'aide du raccourcis : <i>Maj + V</i></li>
        <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte distance verticale.</i></li></ul>
        Ici la valeur demandé <b>est de 150 mm.</b></p>
        <p><img src= %s width="25"/>Pour ajouter un angle entre 2 segments on utilisera une <b>contrainte angulaire :</b>
        <ul><li>à l'aide du raccourcis : A</li>
        <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte angulaire.</i></li></ul>
        Ensuite il faut cliquer sur 2 segments et préciser la valeur de l'angle. <b>Ici c'est 55°.</b></p>''' % ( img1, img2, img3 )

    step["video"] = data_tutorial['url_video'] + str('?start=3m47s')
    step["objectives"] = [u"1 esquisse sur DatumPlane002.",
    u"2 cercles.",
    u"1 contrainte de rayon de 17 mm.",
    u"1 contrainte de rayon de 20 mm."]
    data_tutorial['steps'].append(step)

    #step6
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Constraint_Symmetric.svg')
    img2 = os.path.join(moocWB_images_path, 'Lesson2Step6.png')
    step["description"] = u'''<h3>Lissage additif</h3>
        <p>Il nous reste 2 degrès de libertés qui sont les positions X et Y
        de notre contour dans l'esquisse.</p>
        <p>Nous allons contraindre le contour de façon à ce que l'origine
        passe par le milieu du segment horizontal.</p>
        <p><img src= %s width="25"/>Pour contraindre un point au milieu
        d'un segment on utilise une contrainte de symétrie.</p>
        <p>Notre esquisse est entièrement contrainte, nous pouvons donc quitter
        le mode édition en cliquant sur le bouton <b>Fermer</b> dans l'onglet
        tâche de la vue combinée.</p><p><img src= %s/></p>''' % (img1, img2)

    step["video"] = data_tutorial['url_video'] + str('?start=4m25s')
    step["objectives"] = [u"1 lissage additif passant par 3 esquisse avec surface réglée."]
    data_tutorial['steps'].append(step)

    #step7
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Pad.svg')
    img2 = os.path.join(moocWB_images_path, 'Lesson2Step7-1.png')
    img3 = os.path.join(moocWB_images_path, 'Lesson2Step7-2.png')
    step["description"] = u'''<h3>Esquisse profil de révolution</h3>
        <p>Nous allons maintenant créer une protrusion de 55 mm à partir de
        cette esquisse afin de générer du volume.</p>
        <p>On commence par sélectionner l'esquisse qui servira de base à la
        protrusion, puis on clique sur l'icone <img src= %s width="25"/>.</p>
        <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant :
        <ul><li>Type : Dimension</li>
        <li>Longueur : 55 mm</li>
        <li>Symétrique au plan : coché</li>
        <li>Inversée : décoché</li></ul></p>
        <p><img src= %s/><img src= %s/></p>''' % (img1, img3, img2)

    step["video"] = data_tutorial['url_video'] + str('?start=5m20s')
    step["objectives"] = [u"1 esquisse Sketch003 sur plan XY."]
    data_tutorial['steps'].append(step)

    #step8
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Sketcher_External.svg')
    step["description"] = u'''<h3>Révolution</h3>
        <p>Dans cette étape nous allons créer une nouvelle esquisse sur le plan YZ
        pour dessiner un triangle qui nous permettra d'enlever de la matière
        pour faire les pentes du chapeau. Pour positionner abilement le triangle
        nous utiliseront les arêtes externes.</p>
        <p>Les arêtes externes nous permettent de projeter des arêtes du
        volume sous jacent dans le plan de l'esquisse et ainsi y contraindre des géométries.</p>
        <p>On va cliquer sur l'icône <img src= %s width="25"/> et ensuite
        cliquer sur les arêtes du volume que l'on souhaite utiliser.</p>''' % (img1)

    step["video"] = data_tutorial['url_video'] + str('?start=6m57s')
    step["objectives"] = [u"1 révolution de 360°."]
    data_tutorial['steps'].append(step)

    #step9
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Pocket.svg')
    step["description"] = u'''<h3>Fillet</h3>
        <p>Une cavité (pocket en anglais) est une fonction qui sert à enlever de la matière.</p>
        <p>On commence par sélectionner l'esquisse qui servira de base à la
        cavité, puis on clique sur l'icone <img src= %s width="25"/>.</p>
        <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant :
        <ul><li>Type : À travers tout</li>
        <li>Symétrique au plan : coché</li>
        <li>Inversée : décoché</li></ul></p>''' % (img1)

    step["video"] = data_tutorial['url_video'] + str('?start=7m32s')
    step["objectives"] = [u"1 fillet."]
    data_tutorial['steps'].append(step)

    #step10
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'PartDesign_Mirrored.svg')
    step["description"] = u'''<h3>Répétition</h3>
        <p>Nous n'avons fais qu'un coté du chapeau. On pourrait répéter
        l'opération (esquisse + cavité) ou alors dessiner une esquisse
        plus complexe à l'étape précédente. Mais nous avons à disposition
        des outils de répétition. Ainsi nous allons facilement répéter la
        fonction cavité par mirroir.</p>
        <p>On sélectionne en premier lieu la fonction à répéter, puis on
        clique sur l'icône <img src= %s width="25"/>.</p>
        <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant :
        <ul><li>Plan : axe d'esquisse vertical</li></ul></p>''' % (img1)

    step["video"] = data_tutorial['url_video'] + str('?start=8m56s')
    step["objectives"] = [u"1 corps de pièce Capuchon.",
    u"1 esquisse .",
    u"1 révolution."]
    data_tutorial['steps'].append(step)

    #step11
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateSlot.svg')
    step["description"] = u'''<h3>Contour oblong</h3>
        <p>Pour faire l'espace entre les jambes du Korrigan, nous allons
        enlever de la matière à l'aide d'une forme oblongue.</p>
        Nous devons donc dessiner le contour de cette forme dans une nouvelle
        esquisse sur le plan YZ. Dans cette esquisse, nous allons utiliser l'outil
        <b>Créer une rainure</b> :
        <ul><li>en cliquant sur le bouton <img src= %s width="25"/></li>
        <li>ou par le menu <i>Sketch > Géométries d'esquisse > Créer une rainure</i></li></ul></p>
        <p>Une fois l'outil actif, vous allez cliquer une première fois sur la
        position voulu du centre d'un des arc de cercle puis sur la position
        d'un des point du second cercle. L'outil ajoute automatiquement les
        contraintes géométrique.</p>''' % (img1)

    step["video"] = data_tutorial['url_video'] + str('?start=10m52s')
    step["objectives"] = [u"1 corps de pièce Fil.",
    u"1 esquisse sur le plan XY.",
    u"1 plan de référence normal à la Spline.",
    u"1 esquisse sur DatumPlane003",
    u"1 balayage."]
    data_tutorial['steps'].append(step)

    #step12
    step = {}
    img1 = os.path.join(moocWB_icons_path, 'Document-save.svg')
    img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')
    step["description"] = u'''<h3>Sauvegarder le document.</h3>
        <p><img src=%s width="25"/> Sauvegader le document sous le nom <b>Lampe Mercure</b> :
        <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li>
        <li>à l'aide du raccourcis <b>Ctrl+Maj+S</b></li></lu></p>
        <p><img src=%s width="360"/></p>''' % (img1, img2)

    step["video"] = data_tutorial['url_video'] + str('?start=14m18s')
    step["objectives"] = [u"1 Sauvegardé le document sous le nom Lampe Mercure."]
    data_tutorial['steps'].append(step)

    return data_tutorial

def CheckResult(step_id):
    if step_id == 0:
        results = []
        results.append(Check.document_presence())
        results.append(Check.active_workbench("PartDesignWorkbench"))
        results.append(Check.body_presence(label=u'Lampe'))
        return results

    # create a new body, show it's origin and relabel it
    if step_id == 1:
        results = []
        results.append(Check.datum_plane_presence(support="YZ_Plane", offset=[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]))
        results.append(Check.datum_plane_presence(support="YZ_Plane", offset=[0.0, 0.0, 50.0, 0.0, 0.0, 1.0, 0.0]))
        results.append(Check.datum_plane_presence(support="YZ_Plane", offset=[0.0, 0.0, 100.0, 0.0, 0.0, 1.0, 0.0]))
        return results

    if step_id == 2:
        results = []
        results.append(Check.sketch_presence(label="Sketch", support="DatumPlane"))
        results.append(Check.geometry_presence(sketch_label="Sketch", count=14, isclosed=True))
        results.append(Check.dimension_constraint_presence(sketch_label="Sketch", type="Radius", value=17.0))
        results.append(Check.dimension_constraint_presence(sketch_label="Sketch", type="Radius", value=20.0))
        return results

    if step_id == 3:
        results = []
        results.append(Check.sketch_presence(label="Sketch001", support="DatumPlane001"))
        results.append(Check.geometry_presence(sketch_label="Sketch001", count=14, isclosed=True))
        results.append(Check.dimension_constraint_presence(sketch_label="Sketch001", type="Radius", value=47.0))
        results.append(Check.dimension_constraint_presence(sketch_label="Sketch001", type="Radius", value=50.0))
        return results

    if step_id == 4:
        results = []
        results.append(Check.sketch_presence(label="Sketch002", support="DatumPlane002"))
        results.append(Check.geometry_presence(sketch_label="Sketch002", count=2, isclosed=True))
        results.append(Check.dimension_constraint_presence(sketch_label="Sketch002", type="Radius", value=17.0))
        results.append(Check.dimension_constraint_presence(sketch_label="Sketch002", type="Radius", value=20.0))
        return results


    if step_id == 5:
        results = []
        results.append(Check.additiveloft_presence(outlist=3, ruled=True, closed=False))
        return results


    if step_id == 6:
        results = []
        results.append(Check.sketch_presence(label="Sketch003", support="XY_Plane"))
        return results

    if step_id == 7:
        results = []
        results.append(Check.revolution_presence())
        return results

    if step_id == 8:
        results = []
        results.append(Check.fillet_presence())
        return results

    if step_id == 9:
        results = []
        results.append(Check.body_presence(label=u'Capuchon'))
        results.append(Check.sketch_presence(label="Sketch004", support="XZ_Plane001"))
        results.append(Check.revolution_presence())
        return results

    if step_id == 10:
        results = []
        results.append(Check.body_presence(label=u'Fil'))
        results.append(Check.sketch_presence(label="Sketch005", support="XY_Plane002"))
        results.append(Check.datum_plane_presence(support="Sketch005"))
        results.append(Check.sketch_presence(label="Sketch006", support="DatumPlane003"))
        results.append(Check.additivepipe_presence(outlist=2))
        return results

    if step_id == 11:
        results = []
        results.append(Check.document_save('Lampe Mercure'))
        return results

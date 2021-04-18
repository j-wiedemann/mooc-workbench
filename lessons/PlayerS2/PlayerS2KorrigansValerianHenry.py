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
import os
import moocwb_locator

import FreeCAD as app


class lesson(object):
    def __init__(self):
        moocWB_path = os.path.dirname(moocwb_locator.__file__)
        moocWB_medias_path = os.path.join(moocWB_path, "medias")
        moocWB_icons_path = os.path.join(moocWB_medias_path, "icons")
        moocWB_images_path = os.path.join(moocWB_medias_path, 'images')
        self.data_tutorial = {}
        self.data_tutorial["title"] = app.Qt.translate("MOOC", '[FR] MOOC Semaine 2 - Korrigans de Valérian Henry')
        self.data_tutorial["description"] = app.Qt.translate("MOOC", '''[FR] Part Design Primitives \
Semaine 2 :\nCette semaine nous allons voir comment modéliser le Korrigans de \
Valérian HENRY à l'aide d'esquisses et de fonctions d'ajout et d'enlèvement \
de matière.''')
        url = 'https://open.tube/videos/embed/a9863ee3-a0d8-4919-8b28-8920246d22e6'
        self.data_tutorial["steps"] = []

        # Step 1
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Document-new.svg')
        img2 = os.path.join(moocWB_icons_path, 'Workbench_PartDesign.svg')
        img3 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
        img4 = os.path.join(moocWB_images_path, 'korrigans_final.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Préparation</h3>
            <p><img src= %s width="25"/> Créer un nouveau document :
            <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Nouveau.</li>
            <li>à l'aide du raccourci Ctrl + N</li></ul></p>
            <p><img src= %s width="25"/> Basculer dans l'atelier <b>Part Design</b> :
            <ul><li>à l'aide du sélecteur d'atelier.</li>
            <li>depuis le menu <i>Affichage</i> puis <i>Atelier</i></li></ul></p>
            <p><img src= %s width="25"/>Créer un nouveau corps de pièce :
            <ul><li>à l'aide du menu <i>Part Design</i> puis <i>Créer un corps</i>.</li>
            <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li>
            </ul></p> ''') % (img1, img2, img3)

        step["video"] = str(url) + str('?start=0m00s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "Créer un nouveau document."),
            app.Qt.translate("MOOC", "Basculer dans l'atelier PartDesign."),
            app.Qt.translate("MOOC", "1 corps de pièce (Body).")]
        step["checks"] = ['MoocChecker.document_presence()',
        'MoocChecker.active_workbench("PartDesignWorkbench")',
        'MoocChecker.body_presence()',]
        self.data_tutorial["steps"].append(step)

        # Step 2
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Esquisse</h3>
            <p>Pour créer la base de l'objet, on va d'abord créer une esquisse
            sur le plan XZ du corps de pièce.</p>
            <p>Créer une nouvelle esquisse :
            <ul><li>sélectionner le corps de pièce (Body) dans l'arborescence</li>
            <li>cliquer sur l'icône <img src= %s width="25"/></li>
            <li>ou depuis le menu <i>Part Design</i> > <i>Nouvelle Esquisse</i></li>
            <li>dans l'onglet Tâche de la vue combinée, cliquer sur le plan XZ</li>\
            <li>ou cliquer sur le plan XZ dans la vue 3D</li>
            <li>Enfin cliquer sur le bonton OK</li></lu></p>''') % (img1)

        step["video"] = str(url) + str('?start=0m41s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 esquisse (Sketch) sur le plan XZ."),]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch", support="XZ_Plane")',]
        self.data_tutorial["steps"].append(step)

        # Step 3
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Constraint_Horizontal.svg')
        img2 = os.path.join(moocWB_icons_path, 'Constraint_Vertical.svg')
        img3 = os.path.join(moocWB_icons_path, 'Constraint_PointOnPoint.svg')
        img4 = os.path.join(moocWB_icons_path, 'Sketcher_CreatePolyline.svg')
        img5 = os.path.join(moocWB_images_path, 'Lesson2Step3.png')

        step["description"] = app.Qt.translate("MOOC", '''<h3>Géométries et contraintes</h3>
            <p>Dessiner un contour fermé de 5 côtés à l'aide de l'outil polyligne.</p>
            <p><img src=%s width="25"/> L'outil polyligne ajoute
            automatiquement des contraintes de coïncidence <img src=%s width="25"/>
            entre chaque extrémités de segment.</p>
            <p>Faire en sorte d'avoir des contraintes verticales <img src= %s width="25"/>
             et horizontales <img src=%s width="25"/>  sur les bons éléments.</p>
            <p>À ce stade l'esquisse dispose de 7 degrès de liberté
            restants.</p><p><img src=%s/></p>''') % (img4, img3, img1, img2, img5)

        step["video"] = str(url) + str('?start=2m23s')

        step["objectives"] = [app.Qt.translate("MOOC","1 contour fermé de 5 segments. (cliquer sur le bouton Mettre à jour dans l'onglet Tâches pour vérifier cet objectif)"),
        app.Qt.translate("MOOC", "5 contraintes de coïncidence."),
        app.Qt.translate("MOOC", "2 contraintes d'orientation verticales."),
        app.Qt.translate("MOOC", "1 contrainte d'orientation horizontale.")]

        step["checks"] = ['MoocChecker.geometry_presence(sketch_label="Sketch", count=5, isclosed=True)',
        'MoocChecker.constraint_presence(sketch_label="Sketch", count=5, type="Coincident")',
        'MoocChecker.constraint_presence(sketch_label="Sketch", count=2, type="Vertical")',
        'MoocChecker.constraint_presence(sketch_label="Sketch", count=1, type="Horizontal")',]

        self.data_tutorial["steps"].append(step)

        # Step 4
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Constraint_EqualLength.svg')
        step["description"] =  app.Qt.translate("MOOC", '''<h3>Contrainte d'égalité</h3>
            <p>Nous pouvons contraindre 2 segments à être égaux, dans notre cas
            on veut que les 2 segments verticaux soient égaux entre eux et de
            même pour les 2 segments obliques.</p>
            <p>On sélectionne d'abord les 2 segments verticaux puis on clique
            sur l'icône <img src=%s width="25"/>. Et on recommence pour les 2 segments obliques.</p>''') %(img1)

        step["video"] = str(url) + str('?start=3m32s')
        step["objectives"] = [app.Qt.translate("MOOC","2 paires de contraintes d'égalités"), ]
        step["checks"] = ['MoocChecker.constraint_presence(sketch_label="Sketch", count=2, type="Equal")',]
        self.data_tutorial["steps"].append(step)

        # Step 5
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Constraint_HorizontalDistance.svg')
        img2 = os.path.join(moocWB_icons_path, 'Constraint_VerticalDistance.svg')
        img3 = os.path.join(moocWB_icons_path, 'Constraint_InternalAngle.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Dimensions</h3>
            <p>Pour paramétrer précisement les mesures de notre esquisse,
            on va ajouter des contraintes de dimensions.</p>
            <p><img src=%s width="25"/>Pour ajouter des dimensions horizontales entre 2 points ou un segment,
            on sélectionne l'outil <i>Contrainte distance horizontale</i> :
            <ul><li>à l'aide du raccourci : <i>Maj + H</i></li>
            <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte distance horizontale.</i></li></ul>
            Puis on clique sur le segment ou 2 points dans l'esquisse.
            Une fenêtre apparaît et permet de préciser la valeur de la distance.
            <b>Ici c'est 55 mm.</b> On clique enfin sur Ok pour valider la contrainte.</p>
            <p><img src= %s width="25"/> Le fonctionnement est le même pour ajouter une contrainte de distance verticale :
            <ul><li>à l'aide du raccourci : <i>Maj + V</i></li>
            <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte distance verticale.</i></li></ul>
            Ici la valeur demandé <b>est de 150 mm.</b></p>
            <p><img src= %s width="25"/>Pour ajouter un angle entre 2 segments on utilisera une <b>contrainte angulaire :</b>
            <ul><li>à l'aide du raccourci : A</li>
            <li>depuis le menu <i>Sketch</i> > <i>Contraintes d'esquisses</i> > <i>Contrainte angulaire.</i></li></ul>
            Ensuite il faut cliquer sur 2 segments et préciser la valeur de l'angle. <b>Ici c'est 55°.</b></p>''') % ( img1, img2, img3 )

        step["video"] = str(url) + str('?start=4m00s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 contrainte de dimension verticale de 150mm."),
            app.Qt.translate("MOOC", "1 contrainte de dimension horizontale de 55 mm."),
            app.Qt.translate("MOOC", "1 contrainte de valeure angulaire de 55°.")]
        step["checks"] = ['MoocChecker.constraint_presence(sketch_label="Sketch", count=1, type="DistanceY", value=150.0 )',
        'MoocChecker.constraint_presence(sketch_label="Sketch", count=1, type="DistanceX", value=55.0 )',
        'MoocChecker.constraint_presence(sketch_label="Sketch", count=1, type="Angle", value=55.0 )',]
        self.data_tutorial["steps"].append(step)

        # Step 6
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Constraint_Symmetric.svg')
        img2 = os.path.join(moocWB_images_path, 'Lesson2Step6.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Contrainte de symétrie</h3>
            <p>Il nous reste 2 degrès de libertés qui sont les positions X et Y
            de notre contour dans l'esquisse.</p>
            <p>Nous allons contraindre le contour de façon à ce que l'origine
            passe par le milieu du segment horizontal.</p>
            <p><img src= %s width="25"/>Pour contraindre un point au milieu
            d'un segment on utilise une contrainte de symétrie.</p>
            <p>On clique d'abord sur les points qui doivent être symétrique
             puis sur le point ou l'axe de symétrie.</p>
            <p>Notre esquisse est entièrement contrainte, nous pouvons donc quitter
            le mode édition en cliquant sur le bouton <b>Fermer</b> dans l'onglet
            tâche de la vue combinée.</p><p><img src= %s/></p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=5m07s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 contrainte de symétrie.")]
        step["checks"] = ['MoocChecker.constraint_presence(sketch_label="Sketch", count=1, type="Symmetric")',]
        self.data_tutorial["steps"].append(step)

        # Step 7
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Pad.svg')
        img2 = os.path.join(moocWB_images_path, 'Lesson2Step7-1.png')
        img3 = os.path.join(moocWB_images_path, 'Lesson2Step7-2.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Faire une protrusion</h3>
            <p>Nous allons maintenant créer une protrusion de 55 mm à partir de
            cette esquisse afin de générer du volume.</p>
            <p>On commence par sélectionner l'esquisse qui servira de base à la
            protrusion, puis on clique sur l'icône <img src= %s width="25"/>.</p>
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivants :
            <ul><li>Type : Dimension ou Cote</li>
            <li>Longueur : 55 mm</li>
            <li>Symétrique au plan : coché</li>
            <li>Inversée : décoché</li></ul></p>
            <p><img src= %s/><img src= %s/></p>''') % (img1, img3, img2)

        step["video"] = str(url) + str('?start=5m55s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 protrusion (Pad) de 55 mm, symétrique au plan de l'esquisse.")]
        step["checks"] = ['MoocChecker.pad_presence(type = "Length", length = 55.0, midplane = True )',]
        self.data_tutorial["steps"].append(step)

        # Step 8
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_External.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Arêtes externe</h3>
            <p>Dans cette étape nous allons créer une nouvelle esquisse sur le plan YZ
            pour dessiner un triangle qui nous permettra d'enlever de la matière
            pour faire les pentes du chapeau. Pour positionner abilement le triangle
            nous utiliseront les arêtes externes.</p>
            <p>Les arêtes externes nous permettent de projeter des arêtes du
            volume sous jacent dans le plan de l'esquisse et ainsi y contraindre des géométries.</p>
            <p>On va cliquer sur l'icône <img src= %s width="25"/> et ensuite
            cliquer sur les arêtes du volume que l'on souhaite utiliser.</p>''') % (img1)

        step["video"] = str(url) + str('?start=6m34s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse (Sketch001) sur le plan YZ."),
            app.Qt.translate("MOOC", "1 contour fermé à 3 côtés."),
            app.Qt.translate("MOOC", "2 arêtes externes.")]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch001", support="YZ_Plane")',
        'MoocChecker.geometry_presence(sketch_label="Sketch001", count=3, isclosed=True)',
        'MoocChecker.external_geometry_presence(sketch_label="Sketch001", count=2)',]
        self.data_tutorial["steps"].append(step)

        # Step 9
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Pocket.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Faire une cavité</h3>
            <p>Une cavité (pocket en anglais) est une fonction qui sert à enlever de la matière.</p>
            <p>On commence par sélectionner l'esquisse qui servira de base à la
            cavité, puis on clique sur l'icône <img src= %s width="25"/>.</p>
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivants :
            <ul><li>Type : À travers tout</li>
            <li>Symétrique au plan : coché</li>
            <li>Inversée : décoché</li></ul></p>''') % (img1)

        step["video"] = str(url) + str('?start=7m35s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 cavité (Pocket), à travers tout, symétrique au plan.")]
        step["checks"] = ['MoocChecker.pocket_presence(name="Pocket", type="ThroughAll", midplane=True)',]
        self.data_tutorial["steps"].append(step)

        # Step 10
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Mirrored.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Répétition</h3>
            <p>Nous n'avons fait qu'un côté du chapeau. On pourrait répéter
            l'opération (esquisse + cavité) ou alors dessiner une esquisse
            plus complexe à l'étape précédente. Mais nous avons à disposition
            des outils de répétition. Ainsi nous allons facilement répéter la
            fonction cavité par miroir.</p>
            <p>On sélectionne en premier lieu la fonction à répéter, puis on
            clique sur l'icône <img src= %s width="25"/>.</p>
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivants :
            <ul><li>Plan : axe d'esquisse vertical</li></ul></p>''') % (img1)

        step["video"] = str(url) + str('?start=8m02s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 répétition par symétrie (Mirrored).")]
        step["checks"] = ['MoocChecker.mirrored_pattern_presence(name="Mirrored", plane_name="Sketch001", plane_axis="V_Axis")',]
        self.data_tutorial["steps"].append(step)

        # Step 11
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateSlot.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Contour oblong</h3>
            <p>Pour faire l'espace entre les jambes du Korrigan, nous allons
            enlever de la matière à l'aide d'une forme oblongue.</p>
            Nous devons donc dessiner le contour de cette forme dans une nouvelle
            esquisse sur le plan YZ. Dans cette esquisse, nous allons utiliser l'outil
            <b>Créer une rainure</b> :
            <ul><li>en cliquant sur le bouton <img src= %s width="25"/></li>
            <li>ou par le menu <i>Sketch > Géométries d'esquisse > Créer une rainure</i></li></ul></p>
            <p>Une fois l'outil actif, vous allez cliquer une première fois sur la
            position voulue du centre d'un des arcs de cercle puis sur la position
            d'un des points du second cercle. L'outil ajoute automatiquement les
            contraintes géométriques.</p>''') % (img1)

        step["video"] = str(url) + str('?start=8m39s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse (Sketch002) sur le plan YZ."),
            app.Qt.translate("MOOC", "1 contour fermé."),
            app.Qt.translate("MOOC", "4 contraintes de tangence.")]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch002", support="YZ_Plane")',
        'MoocChecker.geometry_presence(sketch_label="Sketch002", count=4, isclosed=True)',
        'MoocChecker.constraint_presence(sketch_label="Sketch002", count=4, type="Tangent")',]
        self.data_tutorial["steps"].append(step)

        # Step 12
        step = {}
        step["description"] = app.Qt.translate("MOOC", '''<h3>Faire l'espace entre les jambes</h3>
            <p>L'opération consiste à faire une cavité à partir de l'esquisse
            précédente (le contour oblong). C'est la même démarche qu'à l'étape numéro 9.</p>
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant :
            <ul><li>Type : À travers tout</li>
            <li>Symétrique au plan : décoché</li>
            <li>Inversée : coché</li></ul></p>''')

        step["video"] = str(url) + str('?start=9m55s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 cavité (Pocket001), à travers tout, direction inversée.")]
        step["checks"] = ['MoocChecker.pocket_presence(name="Pocket001", type = "ThroughAll", midplane = False, reversed=True)',]
        self.data_tutorial["steps"].append(step)

        # Step 13
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_PolarPattern.svg')
        step["description"] = app.Qt.translate("MOOC",'''<h3>Répétition circulaire</h3>
            <p>On va répéter la cavité 4 fois autour du centre pour obtenir les 4
            espaces entre les jambes.</p>
            <p>On sélectionne en premier lieu la fonction à répéter (ici Pocket001), puis on
            clique sur l'icône <img src= %s width="25"/>.</p>
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivants :
            <ul><li>Axe : Axe Z</li>
            <li>Inverser la direction : décoché</li>
            <li>Angle : 360°</li>
            <li>Occurences : 4</li></ul></p>''') % (img1)

        step["video"] = str(url) + str('?start=10m21s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 répétition circulaire (PolarPattern) de 4 occurences autour de l'axe vertical.")]
        step["checks"] = ['MoocChecker.polar_pattern_presence(name="PolarPattern", occurrences=4, axis="Z_Axis")',]
        self.data_tutorial["steps"].append(step)

        # Step 14
        step = {}
        step["description"] = app.Qt.translate("MOOC",'''<h3>Une oreille.</h3>
            <p>On va réaliser une oreille à l'aide d'une esquisse qui forme un
            triangle rectangle de 25 mm x 20 mm :
            <ul><li>Créer une nouvelle esquisse sur le paln YZ</li>
            <li>Créer une nouvelle esquisse sur le plan YZ</li>
            <li>Dessiner le triangle rectangle à l'aide de l'outil polyligne.</li>
            <li>Récupérer des arêtes externes pour positionner le triangle.</li>
            <li>Réaliser une protrusion :
            <ul><li>Type : Dimension ou Cote</li>
            <li>Longueur : 15 mm</li>
            <li>Symétrique au plan : coché</li></ul></li></ul></p>''')

        step["video"] = str(url) + str('?start=10m56s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse (Sketch003) sur le plan YZ."),
            app.Qt.translate("MOOC", "1 protrusion (Pad001) de 15 mm symétrique au plan.")]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch003", support="YZ_Plane")',
        'MoocChecker.pad_presence(name="Pad001", length=15.0, midplane=True)',]
        self.data_tutorial["steps"].append(step)

        # Step 15
        step = {}
        step["description"] = app.Qt.translate("MOOC", '''<h3>Oreille par symétrie</h3>
            <p>Pour faire l'oreille de l'autre côté, rien de plus facile que
            d'utiliser une fonction de répétition symétrique comme vu à l'étape 10.</p>
            <p>Sélectionner la fonction précédente (Pad001), cliquer sur l'outil
            répétition symétrique et appliquer les paramètres suivants :
            <ul><li>Plan : axe d'esquisse vertical</li></ul></p>''')

        step["video"] = str(url) + str('?start=11m50s')
        step["objectives"] = [app.Qt.translate("MOOC","1 répétition par symétrie (Mirrored001).")]
        step["checks"] = ['MoocChecker.mirrored_pattern_presence(name="Mirrored001", plane_name="Sketch003", plane_axis="V_Axis")',]
        self.data_tutorial["steps"].append(step)

        # Step 16
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Plane.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Créer un plan de référence</h3>
            <p>Nous avons besoin d'un plan de travail décalé par rapport
            au plan YZ pour y appliquer une nouvelle esquisse.</p>
            <p>On commence par afficher l'origine du corps de pièce
            (barre espace sur la fonction Origin), ensuite on clique sur l'icône
            <img src= %s width="25"/>.''') % (img1)

        step["video"] = str(url) + str('?start=12m12s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 plan de référence (DatumPlane).")]
        step["checks"] = ['MoocChecker.datum_plane_presence(label="DatumPlane", support="YZ_Plane", offset=[0.0, 0.0, 27.5, 0.0, 0.0, 1.0, 0.0])',]
        self.data_tutorial["steps"].append(step)

        # Step 17
        step = {}
        step["description"] = app.Qt.translate("MOOC", '''<h3>Faire le nez</h3>
            <p>Pour faire le nez on va dessiner dans une esquisse appliquée au
            plan de référence un cercle et faire une protrusion.</p>
            <p>On sélectionne le plan de référence (datum plane) et on clique
            sur l'icône de création d'esquisse. On dessine un cercle dont on
            contraint le rayon à 3 mm puis on contraint le centre sur l'axe
            verticale de l'esquisse et à 120 mm de l'origine.</p>''')

        step["video"] = str(url) + str('?start=12m50s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse (Sketch004) sur le plan de référence."),
            app.Qt.translate("MOOC", "1 cercle de 3 mm de rayon"),
            app.Qt.translate("MOOC", "1 Protrusion (Pad002) de 12 mm.")]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch004", support="DatumPlane")',
        'MoocChecker.constraint_presence(sketch_label="Sketch004", count=1, type="Radius", value=3.0 )',
        'MoocChecker.pad_presence(name="Pad002", length=12.0)',]
        self.data_tutorial["steps"].append(step)

        # Step 18
        step = {}
        step["description"] = app.Qt.translate("MOOC", '''<h3>Faire les yeux</h3>
            <p>Enfin pour faire les yeux on utilisera des méthodes déjà employées :
            <ul><li>Un cercle dans une esquisse servira à percer le premier trou.
            <li>et on répètera cette opération par symétrie.</li></ul></p>''')

        step["video"] = str(url) + str('?start=13m37s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse (Sketch005) sur le plan de référence."),
            app.Qt.translate("MOOC", "1 cercle de rayon 1,5 mm."),
            app.Qt.translate("MOOC", "1 cavité (Pocket002) de 10 mm."),
            app.Qt.translate("MOOC", "1 Répétition de symétrie.")]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch005", support="DatumPlane")',
        'MoocChecker.constraint_presence(sketch_label="Sketch005", count=1, type="Radius", value=1.5 )',
        'MoocChecker.pocket_presence(name="Pocket002", length=10.0)',
        'MoocChecker.mirrored_pattern_presence(name="Mirrored002", plane_name="Sketch005", plane_axis="V_Axis")',]
        self.data_tutorial["steps"].append(step)

        # Step 19
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Document-save.svg')
        img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')

        step["description"] = app.Qt.translate("MOOC", '''<h3>Sauvegarder le document.</h3>
            <p><img src=%s width="25"/> Sauvegarder le document sous le nom <b>Korrigans</b> :
            <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li>
            <li>à l'aide du raccourci <b>Ctrl+Maj+S</b></li></lu></p>
            <p><img src=%s width="360"/></p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=14m22s')

        step["objectives"] = [app.Qt.translate("MOOC", "Sauvegardé le document sous le nom Korrigans.")]

        step["checks"] = ['MoocChecker.document_save("Korrigans")',]

        self.data_tutorial["steps"].append(step)

    def get_title(self):
        return self.data_tutorial["title"]

    def get_description(self):
        return self.data_tutorial["description"]

    def get_lesson_len(self):
        return len(self.data_tutorial["steps"])

    def get_data_step(self, stepid, ):
        return self.data_tutorial["steps"][stepid]

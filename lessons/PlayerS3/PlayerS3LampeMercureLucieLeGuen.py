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
        self.data_tutorial["title"] = app.Qt.translate("MOOC", '[FR] MOOC Semaine 3 - Lampe Mercure \
de Lucie Le Guen')
        self.data_tutorial["description"] = app.Qt.translate("MOOC", '''[FR] MOOC Semaine 3 : \nCette \
semaine nous allons modéliser \
la Lampe Mercure de Lucie Le Guen. Nous allons travailler dans l'atelier \
Part Design et utiliser des opérations de lissage, balayage et révolution.''')
        url = 'https://open.tube/videos/embed/579d5229-f1a8-426b-80ad-ec4ef1aa0a87'
        self.data_tutorial["steps"] = []

        # Step 1
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Document-new.svg')
        img2 = os.path.join(moocWB_icons_path, 'Workbench_PartDesign.svg')
        img3 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
        img4 = os.path.join(moocWB_images_path, 'korrigans_final.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Préparation</h3>
            <p>Créer un nouveau document :
            <ul><li>en cliquant sur l'icone <img src= %s width="25"/> </li>
            <li>à l'aide du menu <i>Fichier</i> puis <i>Nouveau.</li>
            <li>à l'aide du raccourci Ctrl + N (sur Winodws et Linux ) ou Cmd ⌘ + N (sur Mac)</li></ul></p>
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
            <li>en modifiant la propriété <b>Label</b> dans l'onglet <b>Données</b> de ses paramètres</li></ul></p>''') % (img1, img2, img3)

        step["video"] = str(url) + str('?start=0m00s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "Créer un nouveau document."),
            app.Qt.translate("MOOC", "Basculer dans l'atelier PartDesign."),
            app.Qt.translate("MOOC", "1 corps de pièce nommé 'Lampe'.")]
        step["checks"] = [
            'MoocChecker.document_presence()',
            'MoocChecker.active_workbench("PartDesignWorkbench")',
            'MoocChecker.body_presence(label="Lampe")',]
        self.data_tutorial["steps"].append(step)

        # Step 2
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Plane.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Créer des plans de référence</h3>
            <p>Nous avons besoin de 3 plans de références pour placer nos
             profils. Ils seront coplanaires au plan YZ et décalés respectivement de
             0mm, 50mm et 100 mm selon l'axe Z.</p>
            <p>Pour créer le premier plan de référence, on commence par afficher
            l'origine du corps de pièce (barre espace sur la fonction Origin),
            ensuite on clique sur l'icône <img src= %s width="25"/>.</p>
            <p>On valide la création du premier plan en cliquant sur Ok dans
            l'onglet Tâches ou en appuyant sur la touche Entrer.</p>
            <p>Pour créer les plans suivants on reproduit la même manipulaution mais
            cette fois on va paramétrer une compensation de placement dans l'onglet
            Tâches. Dans les paramètres de compensation on décalera le deuxième plan
            de 50 mm selon Z et le troisième plan de 100 mm selon Z.</p>''') % (img1)

        step["video"] = str(url) + str('?start=0m45s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 plan de référence coplanaire à YZ et décalé de 0 mm selon Z."),
            app.Qt.translate("MOOC", "1 plan de référence coplanaire à YZ et décalé de 50 mm selon Z."),
            app.Qt.translate("MOOC", "1 plan de référence coplanaire à YZ et décalé de 100 mm selon Z.")]
        step["checks"] = [
            'MoocChecker.datum_plane_presence(support="YZ_Plane", offset=[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0])',
            'MoocChecker.datum_plane_presence(support="YZ_Plane", offset=[0.0, 0.0, 50.0, 0.0, 0.0, 1.0, 0.0])',
            'MoocChecker.datum_plane_presence(support="YZ_Plane", offset=[0.0, 0.0, 100.0, 0.0, 0.0, 1.0, 0.0])',]
        self.data_tutorial["steps"].append(step)

        # Step 3
        step = {}
        img0 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateHexagon.svg')
        img2 = os.path.join(moocWB_icons_path, 'Constraint_Vertical.svg')
        img3 = os.path.join(moocWB_icons_path, 'Constraint_Radius.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Création de la première esquisse</h3>
            <p>
            Créer une esquisse sur le premier plan de
            référence (DatumPlane) :<br>
            Sélectionner DatumPlane dans l’arborescence ou la vue 3D puis créer une
            nouvelle esquisse <img src= %s width="25"/>.<br>
            Dans l'esquisse, dessiner un polygone régulier <img src= %s width="25"/>.<br>
            Choisir Hexagone dans la liste des polygone disponible.<br>
            Cliquer sur l'origine de l'esquisse pour placer le centre du polygone
            puis écarter le curseur pour définir le rayon du cercle circonscrit au polygone.<br>
            Contraindre verticalement <img src= %s width="25"/> un des segments.<br>
            Définir le rayon du cercle de construction (en bleu) à 20 mm <img src= %s width="25"/>.<br>
            </p>
            <p>
            Pour modéliser directement l'épaisseur de la lampe, dessiner un second
            polygone à l'intérieur du premier mais cette fois le rayon sera de 17 mm
             afin d'avoir une épaisseur de paroie de 3 mm.<br>
            Contraindre verticalement un des segments du second polygone.<br>
            L'esquisse est entièrement contrainte, fermer l'esquisse en cliquant
            sur Fermer dans l'onglet Tâches.
            </p>''') % (img0, img1, img2, img3,)

        step["video"] = str(url) + str('?start=1m45s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse sur plan de référence."),
            app.Qt.translate("MOOC", "2 hexagones réguliers de ø 40 mm."),
            app.Qt.translate("MOOC", "1 contrainte de rayon de 17 mm."),
            app.Qt.translate("MOOC", "1 contrainte de rayon de 20 mm.")]
        step["checks"] = [
            'MoocChecker.sketch_presence(label="Sketch", support="DatumPlane")',
            'MoocChecker.geometry_presence(sketch_label="Sketch", count=14, isclosed=True)',
            'MoocChecker.dimension_constraint_presence(sketch_label="Sketch", type="Radius", value=17.0)',
            'MoocChecker.dimension_constraint_presence(sketch_label="Sketch", type="Radius", value=20.0)',]
        self.data_tutorial["steps"].append(step)

        # Step 4
        step = {}
        img0 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateHexagon.svg')
        img2 = os.path.join(moocWB_icons_path, 'Constraint_Vertical.svg')
        img3 = os.path.join(moocWB_icons_path, 'Constraint_Radius.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Création de la deuxième esquisse</h3>
            <p>
            Créer une esquisse sur le deuxième plan de
            référence (DatumPlane001) :<br>
            Sélectionner DatumPlane001 dans l’arborescence ou la vue 3D puis créer une
            nouvelle esquisse <img src= %s width="25"/>.<br>
            Dans l'esquisse, dessiner un polygone régulier <img src= %s width="25"/>.<br>
            Choisir Hexagone dans la liste des polygone disponible.<br>
            Cliquer sur l'origine de l'esquisse pour placer le centre du polygone
            puis écarter le curseur pour définir le rayon du cercle circonscrit au polygone.<br>
            Contraindre verticalement <img src= %s width="25"/> un des segments.<br>
            Définir le rayon du cercle de construction (en bleu) à 50 mm <img src= %s width="25"/>.<br>
            </p>
            <p>
            Pour modéliser directement l'épaisseur de la lampe, dessiner un second
            polygone à l'intérieur du premier mais cette fois le rayon sera de 47 mm
             afin d'avoir une épaisseur de paroie de 3 mm.<br>
            Contraindre verticalement un des segments du second polygone.<br>
            L'esquisse est entièrement contrainte, fermer l'esquisse en cliquant
            sur Fermer dans l'onglet Tâches.
            </p>''') % (img0, img1, img2, img3,)

        step["video"] = str(url) + str('?start=2m57s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse sur DatumPlane001."),
            app.Qt.translate("MOOC", "2 hexagones réguliers."),
            app.Qt.translate("MOOC", "1 contrainte de rayon de 47 mm."),
            app.Qt.translate("MOOC", "1 contrainte de rayon de 50 mm.")]
        step["checks"] = [
            'MoocChecker.sketch_presence(label="Sketch001", support="DatumPlane001")',
            'MoocChecker.geometry_presence(sketch_label="Sketch001", count=14, isclosed=True)',
            'MoocChecker.dimension_constraint_presence(sketch_label="Sketch001", type="Radius", value=47.0)',
            'MoocChecker.dimension_constraint_presence(sketch_label="Sketch001", type="Radius", value=50.0)',]
        self.data_tutorial["steps"].append(step)

        # Step 5
        step = {}
        img0 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateCircle.svg')
        img3 = os.path.join(moocWB_icons_path, 'Constraint_Radius.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Création de la troisième esquisse</h3>
            <p>
            Créer une esquisse sur le troisème plan de
            référence (DatumPlane002) :<br>
            Sélectionner DatumPlane002 dans l’arborescence ou la vue 3D puis créer une
            nouvelle esquisse <img src= %s width="25"/>.<br>
            Dans l'esquisse, dessiner un premier cercle <img src= %s width="25"/> dont
            le centre est coïncident avec l'origine de l'esquisse.<br>
            Créer un deuxième cercle légèrement plus petit dont le centre est coïncident avec l'origine de l'esquisse.<br>
            Définir le rayon d'un des cercles à 17mm <img src= %s width="25"/>.<br>
            Définir le rayon d'un des cercles à 20mm <img src= %s width="25"/>.<br>
            L'esquisse est entièrement contrainte, fermer l'esquisse en cliquant
            sur Fermer dans l'onglet Tâches.
            </p>''') % (img0, img1, img3, img3,)

        step["video"] = str(url) + str('?start=3m47s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 esquisse sur DatumPlane002."),
            app.Qt.translate("MOOC", "2 cercles."),
            app.Qt.translate("MOOC", "1 contrainte de rayon de 17 mm."),
            app.Qt.translate("MOOC", "1 contrainte de rayon de 20 mm.")]
        step["checks"] = [
            'MoocChecker.sketch_presence(\
                label="Sketch002", support="DatumPlane002")',
            'MoocChecker.geometry_presence(\
                sketch_label="Sketch002", count=2, isclosed=True)',
            'MoocChecker.dimension_constraint_presence(\
                sketch_label="Sketch002", type="Radius", value=17.0)',
            'MoocChecker.dimension_constraint_presence(\
                sketch_label="Sketch002", type="Radius", value=20.0)', ]
        self.data_tutorial["steps"].append(step)

        # Step 6
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Additive_Loft.svg')
        img2 = os.path.join(moocWB_images_path, 'partdesign_loft_task.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Lissage additif</h3>
            <p>
            Créer un lissage qui passe par les 3 esquisses précédement créées :<br>
            <b>Sélectionner</b> la première esquisse, puis cliquer sur l'outil <img src= %s width="25"/> Lissage Additif.<br>
            <img src= %s/><br>
            Dans l'onglet tâches : cliquer sur <b>Ajouter une section</b> puis cliquer
            sur l'esquisse Sketch001 dans la vue 3D.<br>
            Recommencer en cliquant de nouveau sur "<b>Ajouter une section</b> puis
            cliquer sur Sketch002 dans la vue 3D.<br>
            Cocher la case <b>Surface réglée</b> dans l'onglet taches.<br>
            La prévisualisation montre des surface planes et des arêtes vives.<br>
            <b>Valider</b> la forme en cliquant sur <b>OK</b>.
            </p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=4m25s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 lissage additif passant par 3 esquisses avec surface réglée.")]
        step["checks"] = [
            'MoocChecker.additiveloft_presence(\
            outlist=3, ruled=True, closed=False)', ]
        self.data_tutorial["steps"].append(step)

        # Step 7
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateArc.svg')
        img2 = os.path.join(moocWB_icons_path, 'Sketcher_CreateLine.svg')
        img3 = os.path.join(moocWB_icons_path, 'Constraint_Horizontal.svg')
        img4 = os.path.join(moocWB_icons_path, 'Constraint_Vertical.svg')
        img5 = os.path.join(moocWB_icons_path, 'Sketcher_External.svg')
        img6 = os.path.join(moocWB_icons_path, 'Constraint_Tangent.svg')
        img7 = os.path.join(moocWB_icons_path, 'Constraint_Perpendicular.svg')
        img8 = os.path.join(moocWB_images_path, 'lampe_external.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Esquisse profil de révolution</h3>
            <p>
            Sélectionner le corps de pièce <b>Lampe</b> puis créer une nouvelle
            esquisse sur le plan XY.<br>
            Dessiner le contour à l'aide de 2 arcs de cercle
             <img src= %s width="25"/>
            concentriques et les relier avec 2 segments
             <img src= %s width="25"/>
            , un horizontal et un vertical.<br>
            Ajouter des contraintes horizontales
             <img src= %s width="25"/>
             ou verticales
             <img src= %s width="25"/>
            , au besoin.<br>
            Récupèrer une arête externe <img src= %s width="25"/> qui existe sur une des faces du volume
            sous-jacent et contraindre l'extrémité de l'arc de cercle à être
            tangent à l'extrémité de l’arête.<br>
            Sélectionner ces 2 points puis cliquer sur la contrainte de tangence <img src= %s width="25"/>.<br>
            Enfin containdre perpendiculairement <img src= %s width="25"/> l'autre extrémité de l'arc de cercle et l'axe X.<br>
            <img src= %s width="320"/><br>
            <b>Fermer</b> l'esquisse lorsqu'elle est entièrement contrainte.
            </p>''') % (img1, img2, img3, img4, img5, img6, img7, img8)

        step["video"] = str(url) + str('?start=5m20s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 esquisse Sketch003 sur plan XY.")]
        step["checks"] = ['MoocChecker.sketch_presence(label="Sketch003", support="XY_Plane")',]
        self.data_tutorial["steps"].append(step)

        # Step 8
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Revolution.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Révolution</h3>
            <p>
            Sélectionner l'esquisse Sketch003 puis cliquer sur <img src= %s width="25"/> <b>Révolution</b>.<br>
            Choisir <b>Axe d'esquisse horizontal</b>.<br>
            Valider l'opération en cliquant sur OK.
            </p>''') % (img1)

        step["video"] = str(url) + str('?start=6m57s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 révolution de 360°.")]
        step["checks"] = ['MoocChecker.revolution_presence()',]
        self.data_tutorial["steps"].append(step)

        # Step 9
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Fillet.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Congés (Fillet)</h3>
            <p>
            Nous allons appliquer des congés sur toutes les arêtes du volume.
            Pour sélectionner toutes les arêtes on va
            basculer en vue <b>Filaire</b> depuis le bouton Style de représentation.<br>
            Ou aussi depuis le menu Affichage puis Style de représentation, choisir Filaire. Le raccourcis associé est <b>V,4</b>.
            Sélectionner toutes les arêtes à l'aide de la touche contrôle et
            cliquer sur l'outil <img src= %s width="25"/> Congé.<br>
            Paramétrer un rayon de 10 mm puis valider en cliquant sur OK.<br>
            Notre lampe est terminée.
            </p>''') % (img1)

        step["video"] = str(url) + str('?start=7m32s')
        step["objectives"] = [app.Qt.translate("MOOC", "1 fillet.")]
        step["checks"] = ['MoocChecker.fillet_presence(label="Fillet")', ]
        self.data_tutorial["steps"].append(step)

        # Step 10
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
        img2 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        img3 = os.path.join(moocWB_icons_path, 'PartDesign_Revolution.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Modéliser le Capuchon</h3>
            <p>
            Créer un corps de pièce <img src= %s width="25"/> et le renommer en
            <b>Capuchon</b>.<br>
            Créer une esquisse <img src= %s width="25"/> sur le plan XZ et dessiner un arc de cercle avec épaisseur.<br>
            Réaliser une révolution <img src= %s width="25"/>.
            </p>''') % (img1, img2, img3)

        step["video"] = str(url) + str('?start=8m56s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce Capuchon."),
            app.Qt.translate("MOOC", "1 esquisse ."),
            app.Qt.translate("MOOC", "1 révolution.")]
        step["checks"] = [
            'MoocChecker.body_presence(label="Capuchon")',
            'MoocChecker.sketch_presence(label="Sketch004", support="XZ_Plane001")',
            'MoocChecker.revolution_presence()',]
        self.data_tutorial["steps"].append(step)

        # Step 11
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Sketcher_CreateBSpline.svg')
        img2 = os.path.join(moocWB_icons_path, 'PartDesign_Additive_Pipe.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Modéliser le Fil</h3>
            <p>
            Modéliser le fil électrique à l'aide de l'outil Balayage qui permet de
            générer du volume selon un ou plusieurs profils et le long d'un chemin.<br>
            Commencer par créer un nouveau corps de pièce nommé "Fil".<br>
            Créer une nouvelle esquisse dans le plan XY.<br>
            </p>
            <p>
            Dessiner une courbe Spline qui définira le chemin :<br>
            Cliquer sur l'outil Spline <img src= %s width="25"/> puis cliquer plusieurs point de passage.<br>
            Terminer en faisant un clic droit pour voir la courbe de type Spline.
            On va faire en sorte que l'extrémité de la spline passe par le milieu du capuchon
            Pour faire ça on va contraindre le point d'extrémité à 10mm en x de l'origine comme ceci. Et à 0mm en Y de l'origine.
            De plus pour que l'extrémité soit tangent à l'axe X on va contraindre le 2eme point de passage sur l'axe x comme ceci.
            On valide l'esquisse en cliquant sur Ok.
            </p>
            <p>
            Maintenant il faut dessiner le profil du fil, c'est à dire un cercle de 5mm de diamètre, mais ce cercle doit être sur un plan normal à la spline et passant par un des points d'extrémité de celle ci.
            On va donc créer un plan de référence normal à la spline.
            On sélectionne la spline puis on clique sur Plan de référence juste ici.
            On va cliquer sur le bouton Référence 2 puis sur le point d'extrémité de la spline comme ceci.
            On dit lire Sketch:Sommet1
            Ensuite dans le mode d'accrochage on sélectionne Normal à l'arête.
            On valide en cliquant sur Ok.
            </p>
            <p>
            Maintenant on va créer une nouvelle esquisse sur le plan de référence créé.
            On clique sur le plan puis sur l'icone de création d'une nouvelle esquisse comme ceci.
            Dans l'esquisse on dessine un cercle dont le centre passe par l'origine, on remarque que l'origine de l'esquisse est le point d'extrémité de la spline.
            On contraint le raton à 2.5 mm. on valide l'esquisse en cliquant sur Fermer.
            </p>
            <p>
            Maintenant on va générer notre balayage.
            On sélectionne le cercle précédemment créé puis on clique sur l'outil Balayage <img src= %s width="25"/>.
            Dans l'onglet tâche on clique sur Ajouter une arête, juste ici, puis on clique sur la spline.
            On laisse les autre paramètres inchangés.
            On valide en cliquant sur Ok.

            Et voilà on vient de créer un volume qui à une forme circulaire et suit un chemin spécifique.
            </p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=10m52s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce Fil."),
            app.Qt.translate("MOOC", "1 esquisse sur le plan XY."),
            app.Qt.translate("MOOC", "1 plan de référence normal à la Spline."),
            app.Qt.translate("MOOC", "1 esquisse sur DatumPlane003"),
            app.Qt.translate("MOOC", "1 balayage.")]
        step["checks"] = [
            'MoocChecker.body_presence(label="Fil")',
            'MoocChecker.sketch_presence(label="Sketch005", support="XY_Plane002")',
            'MoocChecker.datum_plane_presence(support="Sketch005")',
            'MoocChecker.sketch_presence(label="Sketch006", support="DatumPlane003")',
            'MoocChecker.additivepipe_presence(outlist=2)',]
        self.data_tutorial["steps"].append(step)

        # Step 12
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Document-save.svg')
        img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Sauvegarder le document.</h3>
            <p><img src=%s width="25"/> Sauvegader le document sous le nom <b>Lampe Mercure</b> :
            <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li>
            <li>à l'aide du raccourcis <b>Ctrl+Maj+S</b></li></lu></p>
            <p><img src=%s width="360"/></p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=14m18s')
        step["objectives"] = [app.Qt.translate("MOOC", 'Document sauvegardé : "Lampe Mercure"')]
        step["checks"] = ['MoocChecker.document_save("Lampe Mercure")',]
        self.data_tutorial["steps"].append(step)

    def get_title(self):
        return self.data_tutorial["title"]

    def get_description(self):
        return self.data_tutorial["description"]

    def get_lesson_len(self):
        return len(self.data_tutorial["steps"])

    def get_data_step(self, stepid, ):
        return self.data_tutorial["steps"][stepid]

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
        self.data_tutorial["title"] = app.Qt.translate("MOOC", '[FR] MOOC Semaine 4 - Tabouret Kouign de Thomas Dellys')
        self.data_tutorial["description"] = app.Qt.translate("MOOC", '''[FR] MOOC Semaine 4 : Cette semaine nous allons modéliser \
    le tabouret Kouign de Thomas Dellys. Nous allons travailler dans l'atelier \
    Part Design pour créer chaque élément puis nous allons utiliser l'atelier A2plus pour faire un assemblage.''')
        url = 'https://open.tube/videos/watch/b915ad6c-f7d2-4257-a717-668bd6d3041e'
        self.data_tutorial["steps"] = []

        # Step 1
        step = {}
        img1 = os.path.join(moocWB_images_path, 'addon_manager_a2plus.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Installer l'atelier A2plus</h3>
            <p>Ouvrir l'addon manager depuis le menu <b>Outils</b> puis
            <b>Addon manager</b></p>
            <p>Dans la fenêtre qui s'ouvre et après que la liste des atelier se soit
            actualisé on sélectionne <b>A2plus</b> puis on clique sur le bouton
            <b>Install/Update</b>.</p>
            <p><img src= %s/></p>
            <p>Une fois l'installation terminé, lorsque la fenêtre indique
            <b>"Succesfully installed"</b> il faut fermer la fenêtre en cliquant sur
            le bouton <b>Close</b> et, comme indiquer dans la fenêtre de dialogue,
            <b>Redémarrer FreeCAD</b>.</p>
            <p>On se retrouve après le redémarrage de FreeCAD.</p>''') % (img1)

        step["video"] = str(url) + str('?start=0m00s')
        step["objectives"] = [app.Qt.translate("MOOC", "Ouvrir l'Addon manager.")]
        step["checks"] = ['MoocChecker.workbench_presence("a2pWorkbench")',]
        self.data_tutorial['steps'].append(step)

        # Step 2
        step = {}
        img1 = os.path.join(moocWB_images_path, 'workbench_list_a2plus.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Vérifier l'installation</h3>
            <p>Vérifier que l'atelier A2plus est bien installé en
            parcourant la liste des ateliers disponible depuis le sélecteur d'atelier :<br>
            <img src= %s/><br>
            Si il y a bien A2plus dans la liste alors l'installation à réussi.</p>''') % (img1)

        step["video"] = str(url) + str('?start=1m07s')
        step["objectives"] = [app.Qt.translate("MOOC", "L'atelier A2plus est installé.")]
        step["checks"] = ['MoocChecker.workbench_presence("a2pWorkbench")',]
        self.data_tutorial['steps'].append(step)

        # Step 3
        step = {}
        img1 = os.path.join(moocWB_images_path, 'entretoise_3d.png')
        img2 = os.path.join(moocWB_images_path, 'entretoise_plan.png')
        img3 = os.path.join(moocWB_icons_path, 'Document-new.svg')
        img4 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
        img5 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        img6 = os.path.join(moocWB_icons_path, 'Sketcher_CreateRectangle.svg')
        img7 = os.path.join(moocWB_icons_path, 'Constraint_Symmetric.svg')
        img8 = os.path.join(moocWB_icons_path, 'Constraint_HorizontalDistance.svg')
        img9 = os.path.join(moocWB_icons_path, 'Constraint_VerticalDistance.svg')
        img10 = os.path.join(moocWB_icons_path, 'PartDesign_Pad.svg')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Modélisation de l'Entretoise</h3>
            <p>Plan et vue 3d de la pièce à modéliser :<br>
            <img src= %s width="360"/><br>
            <img src= %s width="360"/><br>
            Voir la vidéo pour une meilleure résolution d'image.</p>
            <p>Dans un nouveau document <img src= %s width="25">, créer un corps de pièce.<img src= %s width="25"><br>
            Démarrer une nouvelle esquisse <img src= %s width="25"> sur le plan XY.<br>
            Dessiner un rectangle.<img src= %s width="25"><br>
            Centrer le rectangle par rapport à l'origine de l'esquisse :<br>
            Sélectionner 2 coins en diagonale du rectangle puis le point d'origine
             de l'esquisse et appliquer une contrainte de symétrie.<img src= %s width="25"><br>
            Contraindre les dimensions du rectangle :<br>
            Sélectionner le segment horizontal puis cliquer sur Distance horizontale <img src= %s width="25">,
            paramètrer une distance de 355 mm puis et valider en cliquant sur Ok.<br>
            Ensuite sélectionner un segment verticale puis cliquer sur
            Distance verticale <img src= %s width="25">, paramètrer une distance de 58 mm et valider.<br>
            L’esquisse est entièrement contrainte on peut donc valider en cliquant sur Fermer.<br>
            On va réaliser une protrusion <img src= %s width="25"> de 29 mm et symétrique au plan de l'esquisse.</p>
            <p>On sauvegarde le document sous le nom Entretoise.</p>''') % (img1, img2, img3, img4, img5, img6, img7, img8, img9, img10 )

        step["video"] = str(url) + str('?start=1m30s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce."),
            app.Qt.translate("MOOC", "1 esquisse sur plan XY."),
            app.Qt.translate("MOOC", "1 protrusion de 29 mm."),
            app.Qt.translate("MOOC", "La boite englobante est correcte."),
            app.Qt.translate("MOOC", "Le volume du modèle est correct."),
            app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret - Entretoise'.")]
        step["checks"] = [
            'MoocChecker.body_presence()',
            'MoocChecker.sketch_presence(label="Sketch", support="XY_Plane")',
            'MoocChecker.pad_presence(length=29.00)',
            'MoocChecker.boundbox_dimensions(typeId="PartDesign::Body", x=355, y=58, z=29)',
            'MoocChecker.volume(typeId="PartDesign::Body", target=597110)',
            'MoocChecker.document_save("Tabouret - Entretoise")',]
        self.data_tutorial['steps'].append(step)

        # Step 4
        step = {}
        img1 = os.path.join(moocWB_images_path, 'assise_3d.png')
        img2 = os.path.join(moocWB_images_path, 'assise_plan.png')
        img3 = os.path.join(moocWB_icons_path, 'Document-new.svg')
        img4 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
        img5 = os.path.join(moocWB_icons_path, 'Sketcher_NewSketch.svg')
        img6 = os.path.join(moocWB_icons_path, 'Sketcher_CreateRectangle.svg')
        img7 = os.path.join(moocWB_icons_path, 'Sketcher_CreateFillet.svg')
        img8 = os.path.join(moocWB_icons_path, 'Constraint_EqualLength.svg')
        img9 = os.path.join(moocWB_icons_path, 'Constraint_Symmetric.svg')
        img10 = os.path.join(moocWB_icons_path, 'Constraint_HorizontalDistance.svg')
        img11 = os.path.join(moocWB_icons_path, 'Constraint_Radius.svg')
        img12 = os.path.join(moocWB_icons_path, 'PartDesign_Pad.svg')
        img13 = os.path.join(moocWB_icons_path, 'Sketcher_ViewSection.svg')
        img14 = os.path.join(moocWB_icons_path, 'PartDesign_Pocket.svg')
        img15 = os.path.join(moocWB_icons_path, 'PartDesign_PolarPattern.svg')
        step["description"] =  app.Qt.translate("MOOC", '''<h3>Modélisation de l'Assise</h3>
            <p>
            Plan et vue 3d de la pièce à modéliser :<br>
            <img src= %s width="360"/><br>
            <img src= %s width="360"/><br>
            Voir la vidéo pour une meilleure résolution d'image.
            </p>
            <p>
            Dans un nouveau document <img src= %s width="25">, créer un nouveau corps de pièce.<img src= %s width="25"><br>
            Créer une nouvelle esquisse <img src= %s width="25"> dans le plan XY.<br>
            Dessiner un carré avec l'outil rectangle.<img src= %s width="25"><br>
            Ensuite, créer des arrondis à chaque angle.<img src= %s width="25"><br>
            Sélectionner les 4 arc de cercle et appliquer une contrainte
            d’égalité pour qu'ils aient tous le même rayon. <img src= %s width="25"><br>
            Ensuite, sélectionner 2 segment, un horizontal et un verticale et
            appliquer une contrainte d'égalité car l'assise est carré.<img src= %s width="25"><br>
            Il reste à fixé le centre du carré par rapport à l'origine de l'esquisse,
            on peut faire ça avec la contrainte de symétrie qui permet de fixé un
            point au milieu de 2 autres. Sélectionner 2 centres d'arc de cercles
            opposé en diagonal puis l'origine de l'esquisse et enfin cliquer sur
            l'outil contrainte de symétrie.<img src= %s width="25"><br>
            Pour finir définir la longueur du carré et le rayon des arcs de cercle :<br>
            Avec l'outil contrainte de dimension horizontale <img src= %s width="25"> définir la
            distance entre ces 2 point à 368 mm. Et avec l'outil contrainte de rayon <img src= %s width="25">,
            définir le rayon d'un des arc de cercle à 30 mm.<br>
            Mon esquisse est entièrement contrainte je peux donc la valider en
            cliquant sur Fermer.
            </p>
            <p>
            Créer du volume avec l'outil protrusion.<img src= %s width="25"><br>
            La protrusion mesure 16 mm de longueur.
            </p>
            <p>
            Maintenant il faut enlever de la matière pour faire la croix au milieu de l'assise,
            là où les pieds viendront s'insérer :<br>
            Créer une nouvelle esquisse <img src= %s width="25"> sur le plan XY, vu qu'on est dans la
            matière on ne voit pas notre esquisse alors on bascule en vue section
            avec le bouton <img src= %s width="25">.<br>
            Dessiner un rectangle <img src= %s width="25"> qui mesure 75 mm par
            29 mm et dont un des segments est centré par rapport à l'origine.<br>
            Mon esquisse est entièrement contrainte je peux donc la valider en
            cliquant sur Fermer.<br>
            Réaliser une cavité <img src= %s width="25"> de type à travers tous, et inversé.<br>
            Maintenant on va répéter cette cavité pour faire la croix.<br>
            Cliquer sur répétition circulaire <img src= %s width="25" alt="PartDesign_PolarPattern.svg"> puis définir 4 occurrences et valider.<br>
            </p>
            <p>
            L' Assise est terminée, sauvegarder le document sous le nom <b>Assise</b>.
            </p>''') % (img1, img2, img3, img4, img5, img6, img7, img8, img8, img9,
            img10, img11, img12, img5, img13, img6, img14, img15)

        step["video"] = str(url) + str('?start=3m45s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce."),
            app.Qt.translate("MOOC", "La boite englobante est correcte."),
            app.Qt.translate("MOOC", "Le volume du modèle est correct."),
            app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret - Assise'")]
        step["checks"] = [
            'MoocChecker.body_presence()',
            'MoocChecker.boundbox_dimensions(typeId="PartDesign::Body", x=368, y=368, z=16)',
            'MoocChecker.volume(typeId="PartDesign::Body", target=2028678)',
            'MoocChecker.document_save("Tabouret - Assise")',]
        self.data_tutorial['steps'].append(step)

        # Step 5
        step = {}
        img1 = os.path.join(moocWB_images_path, 'piedA_3d.png')
        img2 = os.path.join(moocWB_images_path, 'piedA_plan.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Modélisation Pied A</h3>
            <p>
            Plan et vue 3d de la pièce à modéliser :<br>
            <img src= %s width="360"/><br>
            <img src= %s width="360"/><br>
            Voir la vidéo pour une meilleure résolution d'image.
            </p>
            <p>
            Créer un nouveau document, basculer dans l'atelier Part Design et créer un corps de pièce. <br>
            Sauvegarder le document sous le nom <b>Tabouret-Pied A</b> et commencer à modéliser la pièce.
            <p>
            <b>Conseils :</b><br>
            <ul>
            <li>Dessiner la <b>moitié</b> du pied car il y a symétrie.</li>
            <li>Prendre son <b>temps</b> sur l'esquisse car il y aura beaucoup de géométrie et de contrainte.</li>
            <li>Commencer par dessiner le <b>contour</b> avec les contraintes automatique.</li>
            <li>Ajouter ensuite uniquement des contraintes <b>géométrique</b>.</li>
            <li>Enfin, ajouter des contrainte de <b>distances</b>.</li>
            </ul>
            </p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=7m22s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce."),
            app.Qt.translate("MOOC", "La boite englobante est correcte."),
            app.Qt.translate("MOOC", "Le volume du modèle est correct."),
            app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret-Pied A'")]
        step["checks"] = [
            'MoocChecker.body_presence()',
            'MoocChecker.boundbox_dimensions(typeId="PartDesign::Body", x=452, y=736, z=29)',
            'MoocChecker.volume(typeId="PartDesign::Body", target=2402935)',
            'MoocChecker.document_save("Tabouret - Pied A")',]
        self.data_tutorial['steps'].append(step)

        # Step 6
        step = {}
        img1 = os.path.join(moocWB_images_path, 'piedB_3d.png')
        img2 = os.path.join(moocWB_images_path, 'piedB_plan.png')
        step["description"] = app.Qt.translate("MOOC", '''<h3>Modélisation Pied B</h3>
            <p>
            Plan et vue 3d de la pièce à modéliser :<br>
            <img src= %s width="360"/><br>
            <img src= %s width="360"/><br>
            Voir la vidéo pour une meilleure résolution d'image.
            </p>
            <p>
            Créer un nouveau document, basculer dans l'atelier Part Design et créer un corps de pièce. <br>
            Sauvegarder le document sous le nom <b>Tabouret-Pied B</b> et commencer à modéliser la pièce.
            <p>
            <b>Conseils :</b><br>
            <ul>
            <li>Dessiner la <b>moitié</b> du pied car il y a symétrie.</li>
            <li>Prendre son <b>temps</b> sur l'esquisse car il y aura beaucoup de géométrie et de contrainte.</li>
            <li>Commencer par dessiner le <b>contour</b> avec les contraintes automatique.</li>
            <li>Ajouter ensuite uniquement des contraintes <b>géométrique</b>.</li>
            <li>Enfin, ajouter des contrainte de <b>distances</b>.</li>
            </ul>
            </p>''') % (img1, img2)

        step["video"] = str(url) + str('?start=11m40s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce."),
            app.Qt.translate("MOOC", "La boite englobante est correcte."),
            app.Qt.translate("MOOC", "Le volume du modèle est correct."),
            app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret - Pied B'")]
        step["checks"] = [
            'MoocChecker.body_presence()',
            'MoocChecker.boundbox_dimensions(typeId="PartDesign::Body", x=452, y=736, z=29)',
            'MoocChecker.volume(typeId="PartDesign::Body", target=2986647)',
            'MoocChecker.document_save("Tabouret - Pied B")',]
        self.data_tutorial['steps'].append(step)

        # Step 7
        step = {}
        img0 = os.path.join(moocWB_images_path, 'tabouret_3d.png')
        img1 = os.path.join(moocWB_icons_path, 'a2p_Workbench.svg')
        img2 = os.path.join(moocWB_icons_path, 'a2p_ImportPart.svg')
        img3 = os.path.join(moocWB_icons_path, 'a2p_PlaneCoincidentConstraint.svg')
        img4 = os.path.join(moocWB_icons_path, 'a2p_PlanesParallelConstraint.svg')
        img5 = os.path.join(moocWB_icons_path, 'a2p_AxialConstraint.svg')
        img6 = os.path.join(moocWB_icons_path, 'a2p_DOFs.svg')
        img7 = os.path.join(moocWB_icons_path, 'a2p_MovePart.svg')

        step["description"] = app.Qt.translate("MOOC", '''<h3>Assemblage</h3>
            <p>
            Vue d'ensemble :<br>
            <img src= %s width="300"/>
            </p>
            <p>
            <b>Basculer</b> dans l'atelier <img src= %s width="25"> <b>A2plus</b>.
            </p>
            <p>
            Créer un nouveau document et le sauvegarder sous le nom
            <b>Tabouret - Assemblage</b>.
            </p>
            <p>
            Importer la première pièce en cliquant sur l'outil <img src= %s width="25"> "Add a part".<br>
            Chercher le document Pied A et cliquer sur Ok.
            </p>
            <p>
            Déplacer la pièce importée de façon à ce qu'elle soit orientée vers le haut (axe Z) :<br>
            Faire un clic droit sur l'objet dans l’arborescence puis cliquer sur <b>Transformer</b>.<br>
            Dans la vue 3D il y a 3 vecteurs et 3 boules, les vecteurs permettent de
            déplacer l'objet par translation et les boules par rotation.<br>
            Cliquer et maintenir le clic sur la boule rouge et déplacer le curseur
            pour faire pivoter l'objet jusqu'à ce qu'il soit verticale.<br>
            On peut voir dans l'onglet tache que chaque incrémentation correspond à 15° de rotation.<br>
            Une fois vertical on clic sur Ok.
            </p>
            <p>
            Importer Pied B : <img src= %s width="25"> "Add a part".<br>
            La pièce se retrouve sous le curseur et attend un clic quelque part dans
            la vue 3d pour être positionné.<br>
            La position de départ n'a pas d'importance.
            </p>
            <p>
            Appliquer des contrainte mécanique pour positionner Pied B par rapport à Pied A :
            Sélectionner la face inférieur de l'encoche, et avec la touche contrôle
            enfoncée, ajouter à la sélection la face de Pied B.<br>
            Cliquer sur <img src= %s width="25"> "Add a Plane Coincident constraint".<br>
            Cliquer sur "Accept" pour ajouter la contrainte.<br>
            Sélectionner les 2 faces antérieur des encoches de Pied A et Pied B.<br>
            Ajouter une contrainte de plan coïncident <img src= %s width="25">.<br>
            Cliquer sur "Accept" pour valider.<br>
            Sélectionner les 2 arêtes supérieures de Pied A et Pied B et ajouter
            une contrainte d'axe coïncident en cliquant sur <img src= %s width="25">
            "Add an AxisCoincident constraint".<br>
            Pour s'assurer que Pied B est entièrement contraint, cliquer sur <img src= %s width="25"> "Toggle Printing detailed DOF".<br>
            <b>DOF:0</b> signifie qu'il reste 0 degrés de liberté. DOF signifiant Degree of FreeDOM.
            </p>
            <p>
            Importer Entretoise : <img src= %s width="25"> "Add a Part".<br>
            Sélectionner 2 arêtes et ajouter une contrainte d'axe coïncident <img src= %s width="25">.<br>
            Sélectionner 2 faces et ajouter une contrainte de plan coïncident <img src= %s width="25">.<br>
            L'entretoise semble bien en place mais si on clique sur
            Afficher les degré de liberté <img src= %s width="25"> on voit qu'il
            reste 1 degré de liberté.<br>
            En effet l'entretoise peut pivoter autour de l’arête contrainte tout en
            restant coplanaire aux plans sélectionné précédemment.<br>
            Déplacer l'entretoise le temps de faire une sélection:<br>
            Sélectionner l'entretoise puis cliquer sur <img src= %s width="25"> "Move the selected Part".<br>
            Sélectionner la face supérieur de l'entretoise et la face inférieure de l'encoche.<br>
            Ajouter une contrainte de plan parallèle <img src= %s width="25">.
            </p>
            <p>
            Vérifier le nombre de degré de liberté restant en cliquant sur Print DOF <img src= %s width="25">.<br>
            On a bien DOF:0.
            </p>
            <p>
            Importer Assise :<img src= %s width="25"> "Add a Part".<br>
            Sélectionner 2 arêtes et appliquer une contrainte d'axe coïncident <img src= %s width="25">.<br>
            Recommencer avec 2 autres arêtes.
            </p>
            <p>
            <b>Sauvegarder le document.</b>
            </p>''') % (img0, img1, img2, img2, img3, img3, img5, img6, img2, img5, img3, img6, img7, img4, img6, img2, img5)

        step["video"] = str(url) + str('?start=15m27s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "Basculer dans l'atelier A2plus"),
            app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret - Assemblage'"),
            app.Qt.translate("MOOC", "Importer Pied A"),
            app.Qt.translate("MOOC", "Importer Pied B"),
            app.Qt.translate("MOOC", "Contrainte Plans Coïncident"),
            app.Qt.translate("MOOC", "Contrainte Axes Coïncident"),
            app.Qt.translate("MOOC", "Importer Entretoise"),
            app.Qt.translate("MOOC", "Contrainte de plans prallèles"),
            app.Qt.translate("MOOC", "Importer Assise"), ]
        step["checks"] = [
            'MoocChecker.active_workbench("A2plusWorkbench")',
            'MoocChecker.document_save("Tabouret - Assemblage")',
            'MoocChecker.a2p_importedPart_presence(label="pied a")',
            'MoocChecker.a2p_importedPart_presence(label="pied b")',
            'MoocChecker.a2p_constraint_presence(type="plane")',
            'MoocChecker.a2p_constraint_presence(type="axial")',
            'MoocChecker.a2p_importedPart_presence(label="entretoise")',
            'MoocChecker.a2p_constraint_presence(type="planesParallel")',
            'MoocChecker.a2p_importedPart_presence(label="assise")', ]
        self.data_tutorial['steps'].append(step)

        # Step 8
        step = {}
        img1 = os.path.join(moocWB_images_path, 'entretoise_mod_3d.png')
        img2 = os.path.join(moocWB_icons_path, 'a2p_EditPart.svg')
        img3 = os.path.join(moocWB_icons_path, 'a2p_ImportPart_Update.svg')
        img4 = os.path.join(moocWB_icons_path, 'a2p_DeleteConnections.svg')

        step["description"] = app.Qt.translate("MOOC", '''<h3>Modification</h3>
            <p>
            <img src= %s width="300"/>
            </p>
            <p>
            Il manque une encoche dans la pièce Entretoise.<br>
            Il faut donc modifier le fichier Entretoise puis mettre à jour l'assemblage.<br>
            Sélectionner l'entretoise dnas l'assemblage puis cliquer sur
            <img src= %s width="25"> "Edit an Imported Part".
            </p>
            <p>
            Ajouter une cavité pour faire l'encoche manquante.<br>
            Enregistrer le document.
            </p>
            <p>
            Retourner dans le document Tabouret - Assemblage et mettre à jour l'assemblage en
            cliquant <img src= %s width="25"> "Updates Parts".<br>
            Il risque d'y avoir une message d'erreur ou d'avertissement qui nous
            demande de supprimer des contraintes car les références des contraintes
            sur les objets ont changé, en effet avec la modification qu'on a fait
            le nombre de face à augmentés donc les contraintes qui faisaient
            référence à certaine face se retrouvent incompatible.<br>
            </p>
            <p>
            Si la pièce se retrouve déplacée, le plus simple c'est de supprimer les
            contraintes associées à l'entretoise en sélectionnant l'entretoise puis
            en cliquant sur <img src= %s width="25"> "Delete all constraints".<br>
            Il faudra alors re-contraindre la pièce comme vu précédemment.
            </p>''') % (img1, img2, img3, img4)

        step["video"] = str(url) + str('?start=20m48s')
        step["objectives"] = [
            app.Qt.translate("MOOC", "1 corps de pièce."),
            app.Qt.translate("MOOC", "1 esquisse sur plan XY."),
            app.Qt.translate("MOOC", "1 protrusion de 29 mm."),
            app.Qt.translate("MOOC", "1 cavité."),
            app.Qt.translate("MOOC", "La boite englobante est correcte."),
            app.Qt.translate("MOOC", "Le volume du modèle est correct."),
            app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret - Entretoise'.")]
        step["checks"] = [
            'MoocChecker.body_presence()',
            'MoocChecker.sketch_presence(label="Sketch", support="XY_Plane")',
            'MoocChecker.pad_presence(length=29.00)',
            'MoocChecker.boundbox_dimensions(typeId="PartDesign::Body", x=355, y=58, z=29)',
            'MoocChecker.pocket_presence()',
            'MoocChecker.volume(typeId="PartDesign::Body", target=572721)',
            'MoocChecker.document_save("Tabouret - Entretoise")',]
        self.data_tutorial['steps'].append(step)

        # Step 9
        step = {}
        step["description"] = app.Qt.translate("MOOC", '''<h3>Fin</h3>
            <p>Félicitation vous venez de faire votre premier assemblage à l'aide de l'atelier A2plus.<br>
            Pensez à sauvegarder votre travail sous le nom <b>Assemblage Tabouret</b>.</p>''')

        step["video"] = str(url) + str('?start=23m30s')
        step["objectives"] = [app.Qt.translate("MOOC", "Document sauvegardé : 'Tabouret - Assemblage'.")]
        step["checks"] = ['MoocChecker.document_save("Tabouret - Assemblage")',]
        self.data_tutorial['steps'].append(step)

    def get_title(self):
        return self.data_tutorial["title"]

    def get_description(self):
        return self.data_tutorial["description"]

    def get_lesson_len(self):
        return len(self.data_tutorial["steps"])

    def get_data_step(self, stepid, ):
        return self.data_tutorial["steps"][stepid]

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


class lesson(object):
    def __init__(self):
        moocWB_path = os.path.dirname(moocwb_locator.__file__)
        moocWB_medias_path = os.path.join(moocWB_path, "medias")
        moocWB_icons_path = os.path.join(moocWB_medias_path, "icons")
        moocWB_images_path = os.path.join(moocWB_medias_path, 'images')
        self.data_tutorial = {}
        self.data_tutorial["title"] = '[FR] MOOC Semaine 1 - Humidificateur de Steven Akoun'
        self.data_tutorial["description"] = '''[FR] Part Design Primitives \
Semaine 1 : \nCette semaine nous allons voir comment modéliser \
l'humidificateur de Steven avec des formes primitives uniquement.'''
        self.data_tutorial["steps"] = []

        # Step 1
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Document-new.svg')
        img2 = os.path.join(moocWB_icons_path, 'Workbench_PartDesign.svg')
        img3 = os.path.join(moocWB_icons_path, 'NavigationGesture.svg')
        img4 = os.path.join(moocWB_images_path, 'korrigans_final.png')
        step["description"] = u'''<h3>Préparation</h3>
            <p><img src= %s width="25"/> Créer un nouveau document :
            <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Nouveau.</li>
            <li>à l'aide du raccourcis Ctrl + N</li></ul></p>
            <p><img src= %s width="25"/> Basculer dans l'atelier <b>Part Design</b> :
            <ul><li>à l'aide du sélecteur d'atelier.</li>
            <li>depuis le menu <i>Affichage</i> puis <i>Atelier</i></li></ul></p>
            <p><img src= %s width="25"/>Changer le style de navigation :
            <ul><li>à l'aide d'un clic droit dans l'espace de travail, style de navigation puis choisir Gesture.</li>
            <li>à l'aide du sélecteur de style de navigation dans la barre de status en bas à droite de la fenêtre.</li> \
            </ul></p> ''' % (img1, img2, img3)

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=0m00s'
        step["objectives"] = [u"Créer un nouveau document.", u"Basculer dans l'atelier PartDesign.", u"Mode de navigation : Gesture"]
        step["checks"] = [
            "MoocChecker.document_presence()",
            "MoocChecker.active_workbench('PartDesignWorkbench')",
            "MoocChecker.navigation_style('Gui::GestureNavigationStyle')", ]
        self.data_tutorial['steps'].append(step)

        # Step 2
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Body.png')
        step["description"] = u'''<h3>Corps de pièce</h3>
            <p>Pour modéliser un solide dans l'atelier Part Design nous avons
            besoin d'un corps de pièce qui contiendra toutes nos opérations.</p>
            <p><img src= %s width="25"/>Créer un nouveau corps de pièce :
            <ul><li>à l'aide du menu <i>Part Design</i> puis <i>Créer un corps</i>.</li>
            <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li> \
            </ul></p>''' % (img1)

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=1m03s'
        step["objectives"] = [u"1 Corps de piece"]
        step["checks"] = ["MoocChecker.body_presence()"]
        self.data_tutorial['steps'].append(step)

        #step 3
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

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=2m23s'
        step["objectives"] = [u"1 Cube additif (Box) 100 x 80 x 140 mm sur le plan XY"]
        step["checks"] = ["MoocChecker.primitive_presence(label='Box', typeId='PartDesign::AdditiveBox', dimensions=[100,80,140], support='XY_Plane', offset=[0,0,0,0,0,1,0])"]
        self.data_tutorial['steps'].append(step)

        #step 4
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
            <p>Pour déplacer le cylindre à la position désirée nous allons
            compenser la position de la primitives par rapport à sa référence.
            On peut faire ça dans le panneau Compensation d'accrochage en paramétrant les valeures suivantes :
            <ul><li>X = 0 mm</li>
            <li>Y = 40 mm</li>
            <li>Z = 0 mm</li></ul></p>
            <p>On valide la tâche en cours en cliquant sur OK''' % ( img1 )

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=3m32s'
        step["objectives"] = [u"1 Cylindre additif (Cylindre) Ø80 x 140 mm sur le plan XY et décalé de 40 mm selon Y."]
        step["checks"] = ["MoocChecker.primitive_presence(label='Cylinder', typeId='PartDesign::AdditiveCylinder', dimensions=[40,140], support='XY_Plane', offset=[0,40,0,0,0,1,0])"]
        self.data_tutorial['steps'].append(step)

        #step 5
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

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=4m21s'
        step["objectives"] = [u"1 Cylindre additif Ø80 x 140 mm"]
        step["checks"] = ["MoocChecker.primitive_presence(label='Cylinder001', typeId='PartDesign::AdditiveCylinder', dimensions=[40,140], support='XY_Plane', offset=[100,40,0,0,0,1,0])"]
        self.data_tutorial['steps'].append(step)

        # Step 6
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Subtractive_Box.svg')
        step["description"] = u'''<h3>Cube soustractif</h3>
            <p>Pour enlever de la matière en bas de la pièce nous allons ajouter un cube soustractif.</p>
            <p><img src= %s width="25"/> Créer un cube soustractif :
            <ul><li>à l'aide du menu <i>Part Design</i> puis
            <i>Créer une primitive soustractive</i> puis <i>Cube soustractif</i>.</li>
            <li>à l'aide du lien dans l'onglet Tâche de la vue combinée.</li></ul></p>
            <p>Dans l'onglet tâches de la vue combinée on paramètre les dimensions suivantes :
            <ul><li>Longueur = 80 mm</li>
            <li>Largeur = 80 mm</li>
            <li>Hauteur = 20 mm</li></ul></p>
            <p>Maintenant nous allons attacher la primitive au plan XY du corps de
            pièce en cliquant sur le plan XY dans la vue 3D.</p>
            <p> Enfin il faut compenser la position de la primitives par rapport à sa référence :
            <ul><li>X = 10 mm</li>
            <li>Y = 0 mm</li>
            <li>Z = 0 mm</li></ul></p>
            <p>On valide la tâche en cours en cliquant sur OK''' % (img1)

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=4m52s'
        step["objectives"] = [u"1 Cube soustractif de 80 x 80 x 20 mm" ]
        step["checks"] = ["MoocChecker.primitive_presence(label='Box001', typeId='PartDesign::SubtractiveBox', dimensions=[80,80,20], support='XY_Plane', offset=[10.0,0.0,0.0,0.0,0.0,1.0,0.0])"]
        self.data_tutorial['steps'].append(step)

        # Step 7
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

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=5m38s'
        step["objectives"] = [u"1 cylindre soustractif de Ø72 x 30 mm."]
        step["checks"] = ["MoocChecker.primitive_presence(label='Cylinder002', typeId='PartDesign::SubtractiveCylinder', dimensions=[36,30], support='XY_Plane', offset=[0,40,110,0,0,1,0])"]
        self.data_tutorial['steps'].append(step)

        # Step 8
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

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=6m20s'
        step["objectives"] = [u"1 cylindre soustractif de Ø72 x 30 mm."]
        step["checks"] = ["MoocChecker.primitive_presence(label='Cylinder003', typeId='PartDesign::SubtractiveCylinder', dimensions=[36,30], support='XY_Plane', offset=[100,40,110,0,0,1,0])"]
        self.data_tutorial['steps'].append(step)

        # Step 9
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

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=6m51s'
        step["objectives"] = [u"1 cube soustractif de 100 x 72 x 30 mm."]
        step["checks"] = ["MoocChecker.primitive_presence(label='Box002', typeId='PartDesign::SubtractiveBox', dimensions=[100,72,30], support='XY_Plane', offset=[0,4,110,0,0,1,0])"]
        self.data_tutorial['steps'].append(step)

        # Step 10
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'PartDesign_Fillet.svg')
        step["description"] = u'''<h3>Faire une congé</h3> \
            <p>Pour arrondir les angles en bas de la pièce nous allons utiliser
            l'outil Congé qui créer un arrondi sur les arêtes sélectionné et selon le rayon demandé.</p>
            <p>On sélectionne plusieurs arêtes à l'aide de la touche Ctrl (sur Windows et Linux) ou de la touche Cmd ⌘ (sur Mac).</p>
            <p><img src= %s width="25"/> Créer un congé :
            <ul><li>Sélectionner les arêtes à arrondir.</li>
            <li>à l'aide du menu <i>Part Design</i> puis
            <i>Congé</i>.</li></ul><p>''' % (img1)

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=7m47s'
        step["objectives"] = [u"1 congé de 9 mm de rayon"]
        step["checks"] = ["MoocChecker.fillet_presence(label='Fillet', radius=9)"]
        self.data_tutorial['steps'].append(step)

        # Step 11
        step = {}
        img1 = os.path.join(moocWB_icons_path, 'Document-save.svg')
        img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')
        step["description"] = u'''<h3>Sauvegarder le document.</h3> \
            <p><img src=%s width="25"/> Sauvegader le document sous le nom <b>Humidificateur</b> : \
            <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li> \
            <li>à l'aide du raccourcis <b>Ctrl+Maj+S</b></li></lu></p> \
            <p><img src=%s width="360"/></p>''' % (img1, img2)

        step["video"] = 'https://open.tube/videos/embed/f5773731-9864-470b-a3d5-9e805c419f96?start=9m45s'
        step["objectives"] = [u"1 Sauvegarder le document sous le nom Humidificateur."]
        step["checks"] = ["MoocChecker.document_save('Humidificateur')"]
        self.data_tutorial['steps'].append(step)

    def get_title(self):
        return self.data_tutorial["title"]

    def get_description(self):
        return self.data_tutorial["description"]

    def get_lesson_len(self):
        return len(self.data_tutorial["steps"])

    def get_data_step(self, stepid, ):
        return self.data_tutorial["steps"][stepid]

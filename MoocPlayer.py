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

# import pyside2 module for ui
from PySide2 import QtCore, QtGui, QtWidgets

# for handling paths
import os, moocwb_locator

# import freecad and its gui
import FreeCAD as app
import FreeCADGui as gui
import WebGui

# import webbrowser to play video inside defaut web Browser
import webbrowser

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

# for debug purposes
DEBUG = True
#DEBUG = False

def debug():
    if DEBUG:print("debug")

# set global timer
TIMER = QtCore.QTimer()
TIMER.start(200)
if DEBUG:TIMER.timeout.connect(debug)

moocWBpath = os.path.dirname(moocwb_locator.__file__)
moocWBpath_medias = os.path.join(moocWBpath, 'medias')
moocWB_icons_path = os.path.join( moocWBpath_medias, 'icons')


class Ui_FreeCADPlayer(QtWidgets.QDialog):
    '''The FreeCAd Player interface'''
    def __init__(self, parent=gui.getMainWindow()):
        super(Ui_FreeCADPlayer, self).__init__(parent)
        self.setObjectName("FreeCADPlayer")
        self.resize(380, 520)
        mw_size = parent.size()
        mw_pos = parent.pos()
        move_x = mw_pos.x() + mw_size.width() - self.size().width()
        move_y = mw_pos.y() + mw_size.height()/2 - self.size().height()/2
        self.move(move_x, move_y)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.verticalLayout_left = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        self.label_resume = QtWidgets.QLabel(self)
        self.label_resume.setObjectName("label_resume")
        self.verticalLayout_left.addWidget(self.label_resume)
        self.text_resume = QtWidgets.QTextBrowser(self)
        self.text_resume.setAcceptRichText(True)
        self.text_resume.setObjectName("text_resume")
        #self.text_resume.setOpenExternalLinks(True)
        #self.text_resume.setOpenLinks(True)
        ## TODO: should open link in external browser
        self.verticalLayout_left.addWidget(self.text_resume)
        self.horizontalLayout_play = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_play.setObjectName("horizontalLayout_play")
        self.btn_play = QtWidgets.QPushButton(self)
        self.btn_play.setObjectName("btn_play")
        self.btn_play.setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'media-playback-start.svg')))
        self.horizontalLayout_play.addWidget(self.btn_play)
        self.btn_help = QtWidgets.QPushButton(self)
        self.btn_help.setObjectName("btn_help")
        self.btn_help.setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'help-contents.svg')))
        self.horizontalLayout_play.addWidget(self.btn_help)
        self.verticalLayout_left.addLayout(self.horizontalLayout_play)
        self.label_objectifs = QtWidgets.QLabel(self)
        self.label_objectifs.setObjectName("label_objectifs")
        self.verticalLayout_left.addWidget(self.label_objectifs)
        self.listWidget_objectifs = QtWidgets.QListWidget(self)
        self.listWidget_objectifs.setObjectName("listWidget_objectifs")
        self.verticalLayout_left.addWidget(self.listWidget_objectifs)
        self.horizontalLayout_change_step = QtWidgets.QHBoxLayout()
        self.horizontalLayout_change_step.setObjectName("horizontalLayout_change_step")
        self.btn_previous_step = QtWidgets.QPushButton(self)
        self.btn_previous_step.setObjectName("btn_previous_step")
        self.btn_previous_step.setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'go-previous.svg')))
        self.horizontalLayout_change_step.addWidget(self.btn_previous_step)
        self.label_step = QtWidgets.QLabel(self)
        self.label_step.setAlignment(QtCore.Qt.AlignCenter)
        self.label_step.setObjectName("label_step")
        self.horizontalLayout_change_step.addWidget(self.label_step)
        self.btn_next_step = QtWidgets.QPushButton(self)
        self.btn_next_step.setObjectName("btn_next_step")
        self.btn_next_step.setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'go-next.svg')))
        self.horizontalLayout_change_step.addWidget(self.btn_next_step)
        self.verticalLayout_left.addLayout(self.horizontalLayout_change_step)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()


    def retranslateUi(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("FreeCADPlayer", "FreeCAD Tutorials", None, -1))
        self.label_resume.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Résumé de la leçon", None, -1))
        self.label_objectifs.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Objectifs à réaliser", None, -1))
        self.btn_help.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Aide", None, -1))
        #self.label_movie.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "video", None, -1))
        #self.btn_play_pause.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Play/Pause", None, -1))
        self.btn_previous_step.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Précédent", None, -1))
        self.label_step.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Étape X / X", None, -1))
        self.btn_next_step.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Suivant", None, -1))
        self.btn_play.setText(QtWidgets.QApplication.translate("FreeCADPlayer", "Voir la vidéo", None, -1))


    def closeEvent(self,  event):
        TIMER.stop()
        #self.timer.stop()
        #print("Stop timer")
        if DEBUG:print("Closing")



class Ui_Manager():
    '''functions to control and update the dialog'''
    def __init__(self, data_tutorial):
        self.form = Ui_FreeCADPlayer()

        self.data_tutorial = data_tutorial
        self.form.setWindowTitle(QtWidgets.QApplication.translate("FreeCADPlayer", self.data_tutorial['title'], None, -1))
        self.current_step_id = 0
        self.total_step = len(self.data_tutorial['steps'])
        self.fill_data()

        self.form.btn_play.clicked.connect(self.play_video)
        self.form.btn_next_step.clicked.connect(self.forward_step)
        self.form.btn_previous_step.clicked.connect(self.backward_step)
        if DEBUG:print(self.data_tutorial['title'])
        if DEBUG:print(self.get_label_step())

        TIMER.timeout.connect(self.update)

        self.form.exec_()

    def get_label_step(self):
        label = "Étape " + str(self.current_step_id + 1) + " / "+ str(self.total_step)
        return label

    def forward_step(self):
        if self.current_step_id + 1 < self.total_step :
            self.current_step_id += 1
            if DEBUG:print(self.get_label_step())
            self.fill_data()
        else:
            if DEBUG:print("This is the end !")
            pass

    def backward_step(self):
        if self.current_step_id > 0 :
            self.current_step_id -= 1
            if DEBUG:print(self.get_label_step())
            self.fill_data()
        else:
            if DEBUG:print("This is the begining !")
            pass


    def fill_data(self):
        self.form.label_step.setText(QtWidgets.QApplication.translate("FreeCADPlayer", self.get_label_step(), None, -1))
        step_data = self.data_tutorial['steps'][self.current_step_id]
        self.form.text_resume.setHtml(step_data["description"])
        self.form.listWidget_objectifs.clear()
        for obj in step_data["objectives"]:
            self.form.listWidget_objectifs.addItem(obj)
        self.form.listWidget_objectifs.setFixedHeight(
            (self.form.listWidget_objectifs.sizeHintForRow(0)+10) *
            self.form.listWidget_objectifs.count() +
            10 * self.form.listWidget_objectifs.frameWidth())


    def play_video(self):
        link_url = self.data_tutorial['steps'][self.current_step_id]["video"]
        webbrowser.open(link_url, new=2)
        '''
        mw = gui.getMainWindow()
        mdi = mw.findChild(QtWidgets.QMdiArea)
        subList = mdi.subWindowList()
        for sub in subList:
            if ".cloudfront.net" in sub.windowTitle() :
                sub.close()
            if "Start" in sub.windowTitle() :
                sub.close()
            if "Page" in sub.windowTitle() :
                sub.close()
            if "Browser" in sub.windowTitle() :
                sub.close()

        src = '<iframe width="640" height="480" src=%s></iframe>' % (link_url)
        if DEBUG:print(u'source de la vidéo : %s' % (src))
        WebGui.openBrowser(link_url)
        #WebGui.openBrowserHTML(src)
        mdi.tileSubWindows()
        '''

    def get_results(self):
        fcplayer = self.data_tutorial['episode']
        if fcplayer == "FCPlayer1":
            results = FCPlayer1().CheckResult(self.current_step_id)
            return results

        elif fcplayer == "FCPlayer2":
            results = FCPlayer2().CheckResult(self.current_step_id)
            return results

#        elif fcplayer == "FCPlayer3":
#            results = FCPlayer3().CheckResult(self.current_step_id)
#            return results

#        elif fcplayer == "FCPlayer4":
#            results = FCPlayer4().CheckResult(self.current_step_id)
#            return results

        else:
            if DEBUG:print("No FCPlayer found !")
            pass

    def update(self):
        if DEBUG:print("Ui_Manager.update")
        results = self.get_results()
        brush_green = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush_green.setStyle(QtCore.Qt.NoBrush)
        brush_red = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush_red.setStyle(QtCore.Qt.NoBrush)

        idx = 0
        if results:
            for x in results:
                if x == 0 :
                    self.form.listWidget_objectifs.item(idx).setForeground(brush_red)
                    self.form.listWidget_objectifs.item(idx).setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path , 'window-close.svg')))
                elif x == 1 :
                    self.form.listWidget_objectifs.item(idx).setForeground(brush_green)
                    self.form.listWidget_objectifs.item(idx).setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path , 'dialog-apply.svg')))
                idx += 1



class FCPlayer1():
    "the first week"
    def IsActive(self):
        if DEBUG:print("FCPlayer 1 is active")
        return True


class FCPlayer2():
    '''the second week'''
    def IsActive(self):
        if DEBUG:print("FCPlayer 2 is active")
        return True

    def Activated(self):
        Ui_Manager(self.MakeDataTutorial())

    def MakeDataTutorial(self):
        data_tutorial = {}
        data_tutorial['episode'] = "FCPlayer2"
        data_tutorial['title'] = u'MOOC Semaine 2 : Korrigans'
        data_tutorial['steps'] = []
        moocWBpath = os.path.dirname(moocwb_locator.__file__)
        moocWBpath_medias = os.path.join(moocWBpath, 'medias')
        moocWB_images_path = os.path.join(moocWBpath_medias, 'images')

        step = {}
        img1 = os.path.join(moocWB_images_path, 'Document-new.svg')
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

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/JaSg66nimGFq/HD.mp4'
        step["objectives"] = [u"Créer un nouveau document.", u"Basculer dans l'atelier PartDesign.", u"1 corps de pièce (Body)."]
        data_tutorial['steps'].append(step)

        #step2
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Sketcher_NewSketch.svg')
        step["description"] = u'''<h3>Esquisse</h3> \
            <p>Pour créer la base de l'objet, on va d'abord créer une esquisse \
            sur le plan XZ du corps de pièce.</p> \
            <p><img src= %s width="25"/> Pour cela on clique sur l'icone \
            Nouvelle Esquisse et on choisit le plan XZ dans la liste visible \
            dans l'onglet Tâche de la vue combinée.</p>''' % (img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 esquisse (Sketch) sur le plan XZ.", u"TODO : Taille de la grille de 10 mm."]
        data_tutorial['steps'].append(step)

        #step3
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Constraint_Horizontal.svg')
        img2 = os.path.join(moocWB_images_path, 'Constraint_Vertical.svg')
        img3 = os.path.join(moocWB_images_path, 'Constraint_PointOnPoint.svg')
        step["description"] = u'''<h3>Géométries et contraintes</h3> \
            <p>Dessiner un contour fermé de 5 coté à l'aide de l'outil polyligne.<p> \
            <p><img src=%s width="25"/> L'outil polyligne ajoute \
            automatiquement des contrainte de coïncidence entre chaque extrémités de segment.<p>\
            <p>Faire en sorte d'avoir des contraintes verticales <img src= %s width="25"/> \
             et horizontales <img src=%s width="25"/>  sur les bons éléments.</p> \
            <p>À ce stade l'esquisse dispose de 7 degrès de liberté \
            restants.</p>''' % (img3, img1, img2)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 contour fermé de 5 segments.", u"5 contraintes de coïncidence.", u"2 contraintes d'orientation verticales.",
                            u"1 contrainte d'orientation horizontale."]
        data_tutorial['steps'].append(step)

        #step4
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Constraint_EqualLength.svg')
        step["description"] =  u'''<h3>Contrainte d'égalité</h3> \
            <p>Nous pouvons contraindre 2 segments à être égaux, dans notre cas \
            on veut que les 2 segments verticaux soient égaux entre eux et de \
            même pour les 2 segments obliques.</p> \
            <p>On sélectionne d'abord les 2 segments verticaux puis on clique \
            sur l'icône <img src=%s width="25"/>. Et on recommence pour les 2 segments obliques.<p>''' %(img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"2 paires de contraintes d'égalités", ]
        data_tutorial['steps'].append(step)

        #step5
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Constraint_HorizontalDistance.svg')
        img2 = os.path.join(moocWB_images_path, 'Constraint_VerticalDistance.svg')
        img3 = os.path.join(moocWB_images_path, 'Constraint_InternalAngle.svg')
        step["description"] = u'''<h3>Dimensions</h3> \
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
        step["objectives"] = [u"1 contrainte de dimension verticale de 150mm.", u"1 contrainte de dimensions horizontale de 55 mm.", u"1 contrainte de valeure angulaire de 55°." ]
        data_tutorial['steps'].append(step)

        #step6
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Constraint_Symmetric.svg')
        step["description"] = u'''<h3>Contrainte de symétrie</h3> \
            <p>Il nous reste 2 degrès de libertés qui sont les positions X et Y  \
            de notre contour dans l'esquisse.<p> \
            <p>Nous allons contraindre le contour de façon à ce que l'origine  \
            passe par le milieu du segment horizontal.<p> \
            <p><img src= %s width="25"/>Pour contraindre un point au milieu \
            d'un segment on utilise une contrainte de symétrie.<p>''' % (img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 contrainte de symétrie."]
        data_tutorial['steps'].append(step)

        #step7
        step = {}
        img1 = os.path.join(moocWB_images_path, 'PartDesign_Pad.svg')
        step["description"] = u'''<h3>Faire une protrusion</h3> \
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
        step["objectives"] = [u"1 protrusion (Pad) de 55 mm, symétrique au plan de l'esquisse."]
        data_tutorial['steps'].append(step)

        #step8
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Sketcher_External.svg')
        step["description"] = u'''<h3>Arêtes externe</h3> \
            <p>Dans cette étape nous allons créer une nouvelle esquisse sur le plan YZ \
            pour dessiner un triangle qui nous permettra d'enlever de la matière \
            pour faire les pentes du chapeau. Pour positionner abilement le triangle \
            nous utiliseront les arêtes externes.</p> \
            <p>Les arêtes externes nous permettent de projeter des arêtes du \
            volume sous jacent dans le plan de l'esquisse et ainsi y contraindre des géométries.<p> \
            <p>On va cliquer sur l'icône <img src= %s width="25"/> et ensuite \
            cliquer sur les arêtes du volume que l'on souhaite utiliser.</p>''' % (img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 esquisse (Sketch001) sur le plan YZ.", u"1 contour fermé à 3 cotés.", "2 arêtes externe."]
        data_tutorial['steps'].append(step)

        #step9
        step = {}
        img1 = os.path.join(moocWB_images_path, 'PartDesign_Pocket.svg')
        step["description"] = u'''<h3>Faire une cavité</h3> \
            <p>Une cavité (pocket en anglais) est une fonction qui sert à enlever de la matière.</p> \
            <p>On commence par sélectionner l'esquisse qui servira de base à la \
            cavité, puis on clique sur l'icone <img src= %s width="25"/>.</p> \
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant : \
            <ul><li>Type : À travers tout</li> \
            <li>Symétrique au plan : coché</li> \
            <li>Inversée : décoché</li></ul></p>''' % (img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 cavité (Pocket), à travers tout, symétrique au plan."]
        data_tutorial['steps'].append(step)

        #step10
        step = {}
        img1 = os.path.join(moocWB_images_path, 'PartDesign_Mirrored.svg')
        step["description"] = u'''<h3>Répétition</h3> \
            <p>Nous n'avons fais qu'un coté du chapeau. On pourrait répéter \
            l'opération (esquisse + cavité), on aurait pus dessiner une esquisse \
            plus complexe à l'étape précédente. Mais nous avons à disposition \
            des outils de répétition. Ainsi nous allons facilement répéter la \
            fonction cavité par mirroir.</p> \
            <p>On sélectionne en premier lieu la fonction à répéter, puis on \
            clique sur l'icône <img src= %s width="25"/>.</p> \
            <p>Dans le panneau de l'onglet tâche on va définir les paramètres suivant : \
            <ul><li>Plan : axe d'esquisse vertical</li></ul></p>''' % (img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 répétition par symétrie (Mirrored)."]
        data_tutorial['steps'].append(step)

        #step11
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Sketcher_CreateSlot.svg')
        step["description"] = u'''<h3>Contour oblong</h3> \
            <p>Esquisse avec un contour fermé formant un trou oblong.<p>'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 esquisse (Sketch002) sur le plan YZ.", u"1 contour fermé.", u"4 contraintes de tangence."]
        data_tutorial['steps'].append(step)

        #step12
        step = {}
        step["description"] = u'''<h3>Un entrejambe</h3> \
            <p>L'opération consiste à faire une cavité à partir de l'esquisse \
            précédente. C'est la même démarche qu'à l'étape numéro 9.<p>'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 cavité (Pocket001), à travers tout, direction inversée."]
        data_tutorial['steps'].append(step)

        #step13
        step = {}
        img1 = os.path.join(moocWB_images_path, 'PartDesign_PolarPattern.svg')
        step["description"] = u'''<h3>Répétition circulaire</h3> \
            <p>On va répéter la cavité 4 fois autour du centre pour obtenir les 4 jambes.<p>'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 répétition circulaire (PolarPattern) de 4 occurences autour de l'axe vertical."]
        data_tutorial['steps'].append(step)

        #step14
        step = {}
        step["description"] = u'''<h3>Une oreille.</h3> \
            <p>On va réaliser une oreille à l'aide d'une esquisse en forme de  \
            triangle de 25 mm x 20 mm.<p>" \
            <p>Puis une protrusion de 15 mm.<p>'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 esquisse (Sketch003) sur le plan YZ.", u"1 protrusion (Pad001) de 15 mm symétrique au plan."]
        data_tutorial['steps'].append(step)

        #step15
        step = {}
        step["description"] = u'''<h3>Oreille par symétrie</h3> \
            <p>Répétition par symétrie.<p>'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 répétition par symétrie (Mirrored001)."]
        data_tutorial['steps'].append(step)

        #step16
        step = {}
        img1 = os.path.join(moocWB_images_path, 'PartDesign_Plane.svg')
        step["description"] = u'''<h3>Créer un plan de référence</h3> \
            <p>Nous avons besoin d'un plan de travail décalé par rapport \
            au plan YZ pour y appliquer une nouvelle esquisse.<p>
            <p>On commence par afficher l'origine du corps de pièce \
            (barre espace sur la fonction Origin), ensuite on clique sur l'icône \
            <img src= %s width="25"/>.''' % (img1)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 plan de référence (DatumPlane)."]
        data_tutorial['steps'].append(step)

        #step17
        step = {}
        step["description"] = u'''<h3>Faire le nez</h3> \
            <p>Pour faire le nez on va dessiner dans une esquisse appliquée au \
            plan de référence un cercle et faire une protrusion.<p>\
            <p>On sélectionne le plan de référence (datum plane) et on clique \
            sur l'icone de création d'esquisse. On dessine un cercle dont on \
            contraint le rayon à 3 mm et on contraint le centre sur l'axe \
            verticale de l'esquisse et à 120 mm de l'origine.'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 esquisse (Sketch004) sur le plan de référence.", u"1 cercle de 3 mm de rayon", u"1 Protrusion (Pad002) de 12 mm."]
        data_tutorial['steps'].append(step)

        #step18
        step = {}
        step["description"] = u'''<h3>Faire les yeux</h3> \
            <p>Enfin pour faire les yeux on utilisera des méthodes déjà employés : \
            <ul><li>Un cercle dans une esquisse servira à percer le premier trou. \
            <li>et on répètera cette opération par symétrie.</li></ul></p>'''

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 esquisse (Sketch005) sur le plan de référence.", u"1 cercle de rayon 1,5 mm.", u"1 cavité (Pocket002) de 10 mm.", u"1 Répétition de symétrie."]
        data_tutorial['steps'].append(step)

        #step19
        step = {}
        img1 = os.path.join(moocWB_images_path, 'Document-save.svg')
        img2 = os.path.join(moocWB_images_path, 'freecadSaveDetail.png')
        step["description"] = u'''<h3>Sauvegarder le document.</h3> \
            <p><img src=%s width="25"/> Sauvegader le document sous le nom <b>Korrigans</b> : \
            <ul><li>à l'aide du menu <i>Fichier</i> puis <i>Enregistrer sous ...</i></li> \
            <li>à l'aide du raccourcis <b>Ctrl+Maj+S</b></li></lu></p> \
            <p><img src=%s width="360"/></p>''' % (img1, img2)

        step["video"] = 'https://d381hmu4snvm3e.cloudfront.net/videos/ogXi1cPygQ3H/HD.mp4'
        step["objectives"] = [u"1 Sauvegardé le document sous le nom Korrigans."]
        data_tutorial['steps'].append(step)

        return data_tutorial

    def CheckResult(self, step_id):
        if DEBUG:print(u"FCPlayer02.CheckResult(step_id = %s)" % step_id)

        if step_id == 0:
            results = []
            results.append(Check.document_presence())
            results.append(Check.active_workbench("PartDesignWorkbench"))
            results.append(Check.body_presence())
            return results

        # create a new body, show it's origin and relabel it
        if step_id == 1:
            results = []
            results.append(Check.sketch_presence(label="Sketch", support="XZ_Plane"))
            return results

        if step_id == 2:
            results = []
            results.append(Check.geometry_presence(sketch_label="Sketch", count=5, isclosed=True))
            results.append(Check.constraint_presence(sketch_label="Sketch", count=5, type='Coincident'))
            results.append(Check.constraint_presence(sketch_label="Sketch", count=2, type='Vertical'))
            results.append(Check.constraint_presence(sketch_label="Sketch", count=1, type='Horizontal'))
            return results

        if step_id == 3:
            results = []
            results.append(Check.constraint_presence(sketch_label="Sketch", count=2, type="Equal"))
            return results

        if step_id == 4:
            results = []
            results.append(Check.constraint_presence(sketch_label="Sketch", count=1, type="DistanceY", value=150.0 ))
            results.append(Check.constraint_presence(sketch_label="Sketch", count=1, type="DistanceX", value=55.0 ))
            results.append(Check.constraint_presence(sketch_label="Sketch", count=1, type="Angle", value=55.0 ))
            return results


        if step_id == 5:
            results = []
            results.append(Check.constraint_presence(sketch_label="Sketch", count=1, type="Symmetric"))
            return results


        if step_id == 6:
            results = []
            results.append(Check.pad_presence(type = 'Length', length = 55.0, midplane = True ))
            return results

        if step_id == 7:
            results = []
            results.append(Check.sketch_presence(label="Sketch001", support="YZ_Plane"))
            results.append(Check.geometry_presence(sketch_label="Sketch001", count=3, isclosed=True))
            results.append(Check.external_geometry_presence(sketch_label="Sketch001", count=2))
            return results

        if step_id == 8:
            results = []
            results.append(Check.pocket_presence(name="Pocket", type = 'ThroughAll', midplane = True ))
            return results

        if step_id == 9:
            results = []
            results.append(Check.mirrored_pattern_presence(name="Mirrored", plane_name="Sketch001", plane_axis="V_Axis"))
            return results

        if step_id == 10:
            results = []
            results.append(Check.sketch_presence(label="Sketch002", support="YZ_Plane"))
            results.append(Check.geometry_presence(sketch_label="Sketch002", count=4, isclosed=True))
            results.append(Check.constraint_presence(sketch_label="Sketch002", count=4, type="Tangent"))
            return results

        if step_id == 11:
            results = []
            results.append(Check.pocket_presence(name="Pocket001", type = 'ThroughAll', midplane = False, reversed=True ))
            return results

        if step_id == 12:
            results = []
            results.append(Check.polar_pattern_presence(name="PolarPattern", occurrences=4, axis="V_Axis"))
            return results

        if step_id == 13:
            results = []
            results.append(Check.sketch_presence(label="Sketch003", support="YZ_Plane"))
            results.append(Check.pad_presence(name="Pad001", length=15.0, midplane=True))
            return results

        if step_id == 14:
            results = []
            results.append(Check.mirrored_pattern_presence(name="Mirrored001", plane_name="Sketch003", plane_axis="V_Axis"))
            return results

        if step_id == 15:
            results = []
            results.append(Check.datum_plane_presence(label="DatumPlane", support="YZ_Plane", offset=[0.0, 0.0, 27.5, 0.0, 0.0, 1.0, 0.0]))
            return results

        if step_id == 16:
            results = []
            results.append(Check.sketch_presence(label="Sketch004", support="DatumPlane"))
            results.append(Check.constraint_presence(sketch_label="Sketch004", count=1, type="Radius", value=3.0 ))
            results.append(Check.pad_presence(name="Pad002", length=12.0))
            return results

        if step_id == 17:
            results = []
            results.append(Check.sketch_presence(label="Sketch005", support="DatumPlane"))
            results.append(Check.constraint_presence(sketch_label="Sketch005", count=1, type="Radius", value=1.5 ))
            results.append(Check.pocket_presence(name="Pocket002", length=10.0))
            results.append(Check.mirrored_pattern_presence(name="Mirrored002", plane_name="Sketch005", plane_axis="V_Axis"))
            return results

        if step_id == 18:
            results = []
            results.append(Check.document_save('Korrigans'))
            return results


class FCPlayer3():
    "the first week"
    def __init__(self):
        if DEBUG:print("init FCPlayer3")
        pass


class FCPlayer4():
    "the first week"
    def __init__(self):
        if DEBUG:print("init FCPlayer4")
        pass

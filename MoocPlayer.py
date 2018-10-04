# -*- coding: utf-8 -*-
################################################
#
#  Init.py
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

__title__="Mooc API"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"

import FreeCAD as app
import FreeCADGui as gui
from PySide import QtCore, QtGui

import os
__dir__ = os.path.dirname(__file__)
ImagesFolder=os.path.join(os.path.dirname(__file__),'Medias')


class GifWidget(QtGui.QLabel):
    """custom widget to show animated gif TODO : or video"""
    def __init__(self, parent=None):
        super(GifWidget, self).__init__(parent)
        self.setFrameStyle(QtGui.QFrame.WinPanel | QtGui.QFrame.Sunken)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        
        trashGif = open(os.path.join(ImagesFolder, 'part_step1.gif'), 'rb').read()
        self.gifByteArray = QtCore.QByteArray(trashGif)
        self.gifBuffer = QtCore.QBuffer(self.gifByteArray)
        
        self.movie = QtGui.QMovie()
        self.movie.setFormat('GIF')
        self.movie.setDevice(self.gifBuffer)
        self.movie.setCacheMode(QtGui.QMovie.CacheNone)
        self.movie.setSpeed(50)
        self.setMovie(self.movie)
        self.movie.jumpToFrame(0)
        
    def load_gif(self, gif_name):
        self.movie.stop()
        self.gifByteArray.clear()
        trashGif = open(os.path.join(ImagesFolder,gif_name), 'rb').read()
        self.gifByteArray = QtCore.QByteArray(trashGif)
        self.gifBuffer = QtCore.QBuffer(self.gifByteArray)
        self.movie.setDevice(self.gifBuffer)
        

class Dialog(QtGui.QDialog):
    """"""
    def __init__(self):
        super(Dialog,  self).__init__()
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.initUI()
    
    def initUI(self):
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_desc_title = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_desc_title.setFont(font)
        self.label_desc_title.setObjectName("label_desc_title")
        self.verticalLayout_2.addWidget(self.label_desc_title)
        self.label_desc_body = QtGui.QLabel(self)
        self.label_desc_body.setObjectName("label_desc_body")
        self.verticalLayout_2.addWidget(self.label_desc_body)
        self.label_desc_link = QtGui.QLabel(self)
        self.label_desc_link.setObjectName("label_desc_link")
        self.verticalLayout_2.addWidget(self.label_desc_link)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        
        #self.label_gifs = QtGui.QLabel(self)
        self.label_gifs = GifWidget(self)
        self.label_gifs.setObjectName("label_gifs")
        self.horizontalLayout.addWidget(self.label_gifs)
        self.verticalLayout.addLayout(self.horizontalLayout)

        
        
        self.label_objectif_title = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_objectif_title.setFont(font)
        self.label_objectif_title.setObjectName("label_objectif_title")
        self.verticalLayout.addWidget(self.label_objectif_title)
        self.lW_objectifs = QtGui.QListWidget(self)
        self.lW_objectifs.setMinimumSize(QtCore.QSize(0, 0))
        self.lW_objectifs.setResizeMode(QtGui.QListView.Adjust)
        self.lW_objectifs.setObjectName("lW_objectifs")
        QtGui.QListWidgetItem(self.lW_objectifs)
        QtGui.QListWidgetItem(self.lW_objectifs)
        self.verticalLayout.addWidget(self.lW_objectifs)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pB_prev = QtGui.QPushButton(self)
        self.pB_prev.setObjectName("pB_prev")
        self.horizontalLayout_2.addWidget(self.pB_prev)
        self.label_step_count = QtGui.QLabel(self)
        self.label_step_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_step_count.setObjectName("label_step_count")
        self.horizontalLayout_2.addWidget(self.label_step_count)
        self.pB_next = QtGui.QPushButton(self)
        self.pB_next.setObjectName("pB_next")
        self.horizontalLayout_2.addWidget(self.pB_next)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.tuto_data = DataTutorial()
        self.retranslateUi(self)
        #self.initialGif
        self.fillTutoScreen()
        #self.set_gif()

        #self.connect(self, SIGNAL('triggered()'), self.closeEvent)
        self.pB_next.clicked.connect(self.stepforward)
        self.pB_prev.clicked.connect(self.stepbackward)

        QtCore.QMetaObject.connectSlotsByName(self)
        
        # now make the window visible
        
        self.show()
        self.init_timer()
        
    def init_timer(self):
        # timer to check objectives
        self.timer = QtCore.QTimer(self)
        self.timer.start(500)
        self.timer.timeout.connect(self.update)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "FreeCAD Tutorials", None, QtGui.QApplication.UnicodeUTF8))
        self.label_desc_title.setText(QtGui.QApplication.translate("Dialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_objectif_title.setText(QtGui.QApplication.translate("Dialog", "Objectif(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_prev.setText(QtGui.QApplication.translate("Dialog", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_next.setText(QtGui.QApplication.translate("Dialog", "Next", None, QtGui.QApplication.UnicodeUTF8))
        
    def fillTutoScreen(self):
        step_data = self.tuto_data.get_step_data()
        self.label_desc_body.setText(step_data["description"])
        self.label_desc_link.setText(step_data["link"])
        self.label_step_count.setText("Step " + str(self.tuto_data.step_id) + " / " + str(self.tuto_data.total_step))
        item_count = 0
        for item in step_data["objectifs"]:
            self.lW_objectifs.item(item_count).setText(item)
            item_count += 1
        
        #self.label_gifs.movie.stop()
        #print("je plante")
        self.label_gifs.load_gif(step_data["gif"])
        self.label_gifs.movie.start()
    
    def update(self):
        result = self.tuto_data.check_step()
        #print("update : result = ") 
        #print(result)

        brush_green = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush_green.setStyle(QtCore.Qt.NoBrush)
        brush_red = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush_red.setStyle(QtCore.Qt.NoBrush)
        
        idx = 0
        for x in result:
            if x == 0 :
                self.lW_objectifs.item(idx).setForeground(brush_red)
            elif x == 1 :
                self.lW_objectifs.item(idx).setForeground(brush_green)
            idx += 1
    
    def stepforward(self):
        self.tuto_data.stepmanager('forward')
        self.fillTutoScreen()

    def stepbackward(self):
        self.tuto_data.stepmanager('backward')
        self.fillTutoScreen()
   
    def closeEvent(self, event):
        self.timer.stop()
        print("Stop timer")
        print("Closing")
        #self.destory()


class DataTutorial():
    def __init__(self):
        self.total_step = 3
        self.step_id = 1
        
    def stepmanager(self,  step_move):
        if step_move == 'forward':
            if self.step_id + 1 <= self.total_step :
                self.step_id += 1
                
        if step_move == 'backward':
            if self.step_id - 1 > 0 :
                self.step_id -= 1
        
        print("move to step " + str(self.step_id))
    
    def get_step_data(self):
        if self.step_id == 1:
            step_data ={}
            step_data["description"] = (u"1 Créer un nouveau document.\n"
                                                            u"et basculer dans l'atelier Part.\n"
                                                            )
            step_data["link"] = u"https://freecadweb.org/"
            step_data["gif"] = 'part_step1.gif'
            step_data["objectifs"] = [u"Céer un nouveau document.", u"Basculer dans l'atelier Part."]
            return step_data
            
        if self.step_id == 2:
            step_data ={}
            step_data["description"] = u"2 Changer le style de navigation"
            step_data["link"] = u"https://freecadweb.org/"
            step_data["gif"] = 'part_step1.gif'
            step_data["objectifs"] = [u"Céer un nouveau document.", u"Basculer dans l'atelier Part."]
            return step_data
            
        if self.step_id == 3:
            step_data ={}
            step_data["description"] = u"3 Créer un nouveau document et basculer dans l'atelier Part"
            step_data["link"] = u"https://freecadweb.org/"
            step_data["gif"] = 'part_step1.gif'
            step_data["objectifs"] = [u"Céer un nouveau document.", u"3Basculer dans l'atelier Part."]
            return step_data
        
    
    def check_step(self):
        if self.step_id == 1:
            results = []
            if  gui.ActiveDocument == None:
                results.append(0)
            else:
                results.append(1)
            if gui.activeWorkbench().name() != "PartWorkbench":
                results.append(0)
            else:
                results.append(1)
            return results
        
        if self.step_id == 2:
            results = []
            if  gui.ActiveDocument == None:
                results.append(0)
            else:
                results.append(1)
            if gui.activeWorkbench().name() != "PartWorkbench":
                results.append(0)
            else:
                results.append(1)
            return results
        
        if self.step_id == 3:
            results = []
            param = app.ParamGet("User parameter:BaseApp/Preferences/View")
            nav = param.GetString('NavigationStyle')
            if  nav != 'Gui::GestureNavigationStyle':
                results.append(0)
            else:
                results.append(1)
            return results
        


class FCPlayer1():
        "the first week"
        def GetResources(self):
           return {'Pixmap'  : __dir__ + '/Icons/fun-mooc.svg',
                    'MenuText': QtCore.QT_TRANSLATE_NOOP("Mooc","Jouer la semaine 1"),
                    'ToolTip': QtCore.QT_TRANSLATE_NOOP("Mooc","Jouer la semaine 1")}

        def IsActive(self):
            return True

        def Activated(self):
            form = Dialog()
            form.exec_()
            #panel = _ListingTaskPanel()
            #gui.Control.showDialog(form)

if app.GuiUp:
    #FreeCADGui.addCommand('Timber_Listing',_FCPlayer1())
    gui.addCommand( 'Mooc_Semaine1' , FCPlayer1() )

# coding: utf-8
################################################
#
#  MoocGrader.py
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



import datetime
import base64

def make_b64_hash(grader_dict):
    # construction du hash de l'évaluation
    now = datetime.datetime.now()
    grader_export = [ now.year, now.month, now.day, now.hour, now.minute, now.second ]
    for note in grader_dict:
        grader_export.append(note)
    grader_export_str = ''.join(map(str, grader_export))
    encoded_grader = base64.b64encode(grader_export_str.encode())
    # impression de la chaine de caractere à coller
    #print(encoded_grader.decode())
    return encoded_grader

def grader01(doc_name):
    print("MOOC FreeCAD - Grader 01 ")
    return None

def grader02(doc_name):
    print("MOOC FreeCAD - Grader 02 ")
    print("importing MoocChecker")
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



    grader_dict = {"notes": [], "messages": []}

    doc = app.getDocument(doc_name)

    step_id = 0
    # Check for a Body presence
    grader_dict["notes"].append(Check.body_presence(doc))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a un corps de pièce.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de corps de pièce.")

    step_id += 1
    # Check for a Pad presence
    grader_dict["notes"].append(Check.pad_presence(doc, name=None, type="Length", length=18.0, midplane=True))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une protrusion de 18 mm.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de protrusion de 18 mm.")

    step_id += 1
    # Check for a Pocket presence
    grader_dict["notes"].append(Check.pocket_presence(doc, name=None, type="ThroughAll", length=None, midplane=None, reversed=None))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Il y a une cavité de type À Travers Tout.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Il n'y a pas de cavité de type À Travers Tout.")

    step_id += 1
    # Check volume
    grader_dict["notes"].append(Check.volume(doc, name=None, obj_type='PartDesign::Body', target=28605.00))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Le volume correspond.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Le volume ne correspond pas.")

    step_id += 1
    # Check boundbox
    grader_dict["notes"].append(Check.boundbox_dimensions(doc, name=None, obj_type='PartDesign::Body', x=40.00, y=18.00, z=65.00))
    if grader_dict["notes"][step_id] == 1 :
        grader_dict["messages"].append(u"Les dimensions de la boite englobante correpsondent.")
    elif grader_dict["notes"][step_id] == 0 :
        grader_dict["messages"].append(u"Les dimensions de la boite englobante ne correpsondent pas.")


    return grader_dict

def grader03(doc_name):
    print("MOOC FreeCAD - Grader 03 ")
    return None

def grader04(doc_name):
    print("MOOC FreeCAD - Grader 04 ")
    return None


class Ui_FreeCADGrader(QtWidgets.QDialog):
    def __init__(self, parent=gui.getMainWindow()):
        super(Ui_FreeCADGrader, self).__init__(parent)
        self.setObjectName("FreeCADGrader")
        self.resize(695, 306)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_docs_row = QtWidgets.QHBoxLayout(self)

        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setObjectName("comboBox_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        #TODO: set QtWidgets.QSizePolicy.Expanding
        self.horizontalLayout_docs_row.addWidget(self.comboBox_2)

        self.pushButton_refresh_docList = QtWidgets.QPushButton(self)
        self.pushButton_refresh_docList.setObjectName("pushButton_refresh_docList")
        self.pushButton_refresh_docList.setIcon(QtGui.QIcon.fromTheme("view-refresh"))
        self.horizontalLayout_docs_row.addWidget(self.pushButton_refresh_docList)

        self.verticalLayout.addLayout(self.horizontalLayout_docs_row)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        #self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.fill_comboBox_2()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.eval_button)
        self.pushButton_2.clicked.connect(self.show_hash)
        self.pushButton_refresh_docList.clicked.connect(self.fill_comboBox_2)

    def retranslateUi(self, FreeCADGrader):
        FreeCADGrader.setWindowTitle(QtWidgets.QApplication.translate("FreeCADGrader", "FreeCAD Grader", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("FreeCADGrader", "1. Évaluation", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("FreeCADGrader", "Choisissez l\'exercice à évaluer dans la liste suivante :", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("FreeCADGrader", "Semaine 1", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("FreeCADGrader", "Semaine 2", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("FreeCADGrader", "Semaine 3", None, -1))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("FreeCADGrader", "Semaine 4", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("FreeCADGrader", "Choisissez le document à évaluer dans la liste suivante :", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("FreeCADGrader", "Lancer l\'évaluation", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("FreeCADGrader", "2. Résultats", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("FreeCADGrader", "Envoyer les résultats", None, -1))

    def fill_comboBox_2(self):
        self.comboBox_2.clear()
        self.listWidget.clear()
        self.grader_messages = None
        self.grader_notes = None
        document_list = app.listDocuments()
        if len(document_list)> 0 :
            n = 0
            for doc in document_list.items():
                self.comboBox_2.addItem(doc[1].Label)
                n += 1
        else:
            self.comboBox_2.addItem(u"Il n'y a pas de document à évaluer.")

    def eval_button(self):
        print(u"Eval button clicked")
        doc_name = None
        document_list = app.listDocuments()
        for doc in document_list.items():
            if doc[1].Label == self.comboBox_2.currentText():
                doc_name = doc[1].Name
        if doc_name:
            self.grader_launch(doc_name)
        else:
            self.grader_notes = None
            self.listWidget.clear()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(u"Il n'y aucun document à évaluer !")
            msgBox.setText(u"Veuillez ouvrir un document et relancer FreeCAD Grader")
            msgBox.exec_()

    def grader_launch(self, doc_name):
        print(u"grader launch")
        self.listWidget.clear()
        mooc_session = self.comboBox.currentIndex()
        #document_label = self.comboBox_2.currentText()
        if mooc_session == 0:
            grader_result = grader02(doc_name)
            print(grader_result)
        elif mooc_session == 1:
            grader_result = grader02(doc_name)
        elif mooc_session == 2:
            grader_result = grader03(doc_name)
        elif mooc_session == 3:
            grader_result = grader04(doc_name)
        #elif mooc_session == 0:

        brush_green = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush_green.setStyle(QtCore.Qt.NoBrush)
        brush_red = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush_red.setStyle(QtCore.Qt.NoBrush)

        if grader_result :
            self.grader_messages = grader_result["messages"]
            self.grader_notes = grader_result["notes"]
            #print(self.grader_notes)
            n = 0
            for msg in self.grader_messages:
                self.listWidget.addItem(msg)
                if self.grader_notes[n] == 0:
                    self.listWidget.item(n).setForeground(brush_red)
                    self.listWidget.item(n).setIcon(QtGui.QIcon.fromTheme("dialog-cancel"))
                else:
                    self.listWidget.item(n).setForeground(brush_green)
                    self.listWidget.item(n).setIcon(QtGui.QIcon.fromTheme("dialog-ok"))
                n += 1
            self.listWidget.setFixedWidth(self.listWidget.sizeHintForColumn(0) + 2 * self.listWidget.frameWidth())
        else:
            print("No results")
            self.grader_notes = None
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(u"Cela n'a donné aucun résultat :(")
            msgBox.exec_()

    def show_hash(self):
        if self.grader_notes :
            code = make_b64_hash(self.grader_notes)
            dialog = Ui_FreeCADGraderResults()
            dialog.lineEdit.setText(code.decode())
            dialog.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(u"Veuillez d'abord lancer l'évaluation pour obtenir des résultats.")
            msgBox.exec_()

    def closeEvent(self,event):
        #self.timer.stop()
        #print("Stop timer")
        #print(event)
        print(u"Closing FreeCAD Grader")

class Ui_FreeCADGraderResults(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_FreeCADGraderResults, self).__init__(parent)
        #def setupUi(self, FreeCADGraderResults):
        self.setObjectName("FreeCADGraderResults")
        self.resize(600, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon.fromTheme("edit-copy"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_clipboard_copy = QtWidgets.QLabel(self)
        self.label_clipboard_copy.setObjectName("label_clipboard_copy")
        self.verticalLayout.addWidget(self.label_clipboard_copy)
        """
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        """

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.copy_to_clipboard)

    def retranslateUi(self, FreeCADGraderResults):
        FreeCADGraderResults.setWindowTitle(QtWidgets.QApplication.translate("FreeCADGraderResults", "Envoyer les résultats", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("FreeCADGraderResults", "3. Copier/coller le code suivant dans l\'interface du MOOC", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("FreeCADGraderResults", "Copier", None, -1))

    def copy_to_clipboard(self):
        cb = QtGui.QClipboard()
        #self.lineEdit.copy()
        #cb = QtGui.QClipboard
        #print
        #cb.clear(QtGui.QClipboard.Clipboard)
        cb.setText(self.lineEdit.text())
        self.pushButton.setText(QtWidgets.QApplication.translate("FreeCADGraderResults", "Copié !", None, -1))
        self.label_clipboard_copy.setText(QtWidgets.QApplication.translate("FreeCADGraderResults", u"Le code est copié dans le presse papier."
                                                                          u" Coller le à l'aide d'un clic droit ou du"
                                                                          u" raccourcis clavier CTRL+V.", None, -1))



class MoocGraderCommand():
        "class to choose the lesson"
        def GetResources(self):
            moocWBpath = os.path.dirname(moocwb_locator.__file__)
            moocWBpath_medias = os.path.join(moocWBpath, 'medias')
            moocWB_icons_path = os.path.join( moocWBpath_medias, 'icons')
            return {'Pixmap'  : os.path.join( moocWB_icons_path , 'fun-mooc.svg'),
                    'MenuText': QtCore.QT_TRANSLATE_NOOP(u"Mooc",u"Évaluation de l'exercice."),
                    'ToolTip': QtCore.QT_TRANSLATE_NOOP(u"Mooc",u"Évaluation de l'exercice.")}

        def IsActive(self):
            return True

        def Activated(self):
            dialog = Ui_FreeCADGrader()
            dialog.show()

if app.GuiUp:
    gui.addCommand('Mooc_Grader', MoocGraderCommand())

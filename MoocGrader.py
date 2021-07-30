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

__title__ = "MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "https://www.freecadweb.org"

# to make GUI
from PySide import QtCore, QtGui

# to handle resources paths
import os
import sys
import moocwb_locator

# to load module from path
from os import listdir
from os.path import isfile, join

if (sys.version_info > (3, 0)):  # py3
    import importlib
else:  # py2
    import imp

# import freecad and its gui
import FreeCAD as app
import FreeCADGui as gui

# to hash results
import datetime
import base64

# to open instructions in PDF
import webbrowser

# to DEBUG purpose
DEBUG = False

moocWB_path = os.path.dirname(moocwb_locator.__file__)
moocWB_medias_path = os.path.join(moocWB_path, 'medias')
moocWB_icons_path = os.path.join(moocWB_medias_path, 'icons')
moocWB_exercises_path = os.path.join(moocWB_path, 'exercises')
moocWB_instructions_path = os.path.join(moocWB_medias_path, 'instructions')

def make_b64_hash(grader_dict):
    # construction du hash de l'évaluation
    now = datetime.datetime.now()
    grader_export = [now.year, now.month, now.day, now.hour, now.minute, now.second]
    for note in grader_dict:
        grader_export.append(note)
    grader_export_str = ''.join(map(str, grader_export))
    encoded_grader = base64.b64encode(grader_export_str.encode())
    return encoded_grader


QtWidgets = QtGui

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
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton_show_instructions = QtWidgets.QPushButton(self)
        self.pushButton_show_instructions.setObjectName("pushButton_show_instructions")
        self.verticalLayout.addWidget(self.pushButton_show_instructions)
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
        self.horizontalLayout_docs_row.addWidget(self.comboBox_2)

        self.pushButton_refresh_docList = QtWidgets.QPushButton(self)
        self.pushButton_refresh_docList.setObjectName("pushButton_refresh_docList")
        self.pushButton_refresh_docList.setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'view-refresh.svg')))
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
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.get_exercises_title_list()
        self.fill_comboBox_2()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.eval_button)
        self.pushButton_2.clicked.connect(self.show_hash)
        self.pushButton_refresh_docList.clicked.connect(self.fill_comboBox_2)
        self.pushButton_show_instructions.clicked.connect(self.show_instructions)

    def retranslateUi(self, FreeCADGrader):
        FreeCADGrader.setWindowTitle(app.Qt.translate("MOOC", "FreeCAD Grader"))
        self.label.setText(app.Qt.translate("MOOC", "1. Évaluation"))
        self.label_2.setText(app.Qt.translate("MOOC", "Choisissez l'exercice à évaluer dans la liste suivante :"))
        self.label_3.setText(app.Qt.translate("MOOC", "Choisissez le document à évaluer dans la liste suivante :"))
        self.pushButton.setText(app.Qt.translate("MOOC", "Lancer l\'évaluation"))
        self.label_4.setText(app.Qt.translate("MOOC", "2. Résultats"))
        self.pushButton_2.setText(app.Qt.translate("MOOC", "Envoyer les résultats"))
        self.pushButton_show_instructions.setText(app.Qt.translate("MOOC", "Voir les instructions"))

    def fill_comboBox_2(self):
        self.comboBox_2.clear()
        self.listWidget.clear()
        self.grader_messages = None
        self.grader_notes = None
        document_list = app.listDocuments()
        if len(document_list) > 0 :
            n = 0
            for doc in document_list.items():
                self.comboBox_2.addItem(doc[1].Label)
                n += 1
        else:
            self.comboBox_2.addItem(app.Qt.translate("MOOC", "Il n'y a pas de document à évaluer."))

    def eval_button(self):
        if DEBUG:
            print("Eval button clicked")
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
            msgBox.setText(app.Qt.translate("MOOC", "Il n'y aucun document à évaluer !"))
            msgBox.setText(app.Qt.translate("MOOC", "Veuillez ouvrir un document et relancer FreeCAD Grader"))
            msgBox.exec_()

    def grader_launch(self, doc_name):
        if DEBUG:
            print("grader launch")
        self.listWidget.clear()
        mooc_session = self.comboBox.currentIndex()
        exercise = self.exercises_infos_list[mooc_session][2]
        grader_result = exercise.grader(doc_name)

        brush_green = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush_green.setStyle(QtCore.Qt.NoBrush)
        brush_red = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush_red.setStyle(QtCore.Qt.NoBrush)

        if grader_result :
            self.grader_messages = grader_result["messages"]
            self.grader_notes = grader_result["notes"]
            n = 0
            for msg in self.grader_messages:
                self.listWidget.addItem(msg)
                if self.grader_notes[n] == 0:
                    self.listWidget.item(n).setForeground(brush_red)
                    self.listWidget.item(n).setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'window-close.svg')))
                else:
                    self.listWidget.item(n).setForeground(brush_green)
                    self.listWidget.item(n).setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'dialog-apply.svg')))
                n += 1
            self.listWidget.setFixedWidth(self.listWidget.sizeHintForColumn(0) + 2 * self.listWidget.frameWidth())
        else:
            if DEBUG:
                print("No results")
            self.grader_notes = None
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(app.Qt.translate("MOOC", "Cela n'a donné aucun résultat :("))
            msgBox.exec_()

    def show_hash(self):
        if self.grader_notes:
            code = make_b64_hash(self.grader_notes)
            dialog = Ui_FreeCADGraderResults()
            dialog.lineEdit.setText(code.decode())
            dialog.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(app.Qt.translate("MOOC", "Veuillez d'abord lancer l'évaluation pour obtenir des résultats."))
            msgBox.exec_()

    def closeEvent(self, event):
        if DEBUG:
            print("Closing FreeCAD Grader")

    def get_exercises_title_list(self):
        self.exercises_infos_list = []
        files = [f for f in listdir(moocWB_exercises_path) if isfile(join(moocWB_exercises_path, f))]
        onlyfiles = [f for f in files if os.path.splitext(f)[1] == '.py']
        onlyfiles.sort()
        if DEBUG:
            print(onlyfiles)
        for exercise in onlyfiles:
            name, ext = os.path.splitext(exercise)
            path = os.path.join(moocWB_exercises_path, exercise)
            if (sys.version_info > (3, 0)):
                spec = importlib.util.spec_from_file_location(name, path)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
            else:
                foo = imp.load_source(name, path)
            self.exercises_infos_list.append([foo.get_title(), foo.get_description(), foo, foo.get_instructions()])
            self.comboBox.addItem(foo.get_title())

    def show_instructions(self):
        mooc_session = self.comboBox.currentIndex()
        instructions = self.exercises_infos_list[mooc_session][3]
        file = os.path.join(moocWB_instructions_path, str(instructions))
        webbrowser.open(file)

class Ui_FreeCADGraderResults(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_FreeCADGraderResults, self).__init__(parent)
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
        self.pushButton.setIcon(QtGui.QIcon(os.path.join(moocWB_icons_path, 'edit-copy.svg')))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_clipboard_copy = QtWidgets.QLabel(self)
        self.label_clipboard_copy.setObjectName("label_clipboard_copy")
        self.verticalLayout.addWidget(self.label_clipboard_copy)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.copy_to_clipboard)

    def retranslateUi(self, FreeCADGraderResults):
        FreeCADGraderResults.setWindowTitle(app.Qt.translate("MOOC", "Envoyer les résultats"))
        self.label.setText(app.Qt.translate("MOOC", "3. Copier/coller le code suivant dans l\'interface FUN-MOOC"))
        self.pushButton.setText(app.Qt.translate("MOOC", "Copier"))

    def copy_to_clipboard(self):
        cb = QtGui.QClipboard()
        cb.setText(self.lineEdit.text())
        self.pushButton.setText(app.Qt.translate("MOOC", "Copié !"))
        self.label_clipboard_copy.setText(app.Qt.translate("MOOC", "Le code est copié dans le presse papier.\nColler le à l'aide d'un clic droit ou du raccourcis clavier CTRL+V."))


class MoocGraderCommand():
    """command for the Grader"""

    def GetResources(self):
        return {'Pixmap': os.path.join(moocWB_icons_path, 'mooc-grader.svg'),
                'MenuText': app.Qt.translate("MOOC", "Évaluer un exercice."),
                'ToolTip': app.Qt.translate("MOOC", "Éxécute l'outil d'analyse et vérification d'un document FreeCAD.")}

    def IsActive(self):
        return True

    def Activated(self):
        dialog = Ui_FreeCADGrader()
        dialog.show()


if app.GuiUp:
    gui.addCommand('Mooc_Grader', MoocGraderCommand())

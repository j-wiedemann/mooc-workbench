# coding: utf-8
################################################
#
#  MoocChecker.py
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

import FreeCAD as app
import FreeCADGui as gui

import math


# for debug purposes
DEBUG = True
#DEBUG = False

if DEBUG:print("MOOC CHECKER")

def make_result(r):
    ''' make final result from list of result
    to get 1 there must not be 0 in r
    r=[1,1,1,0] => result = 0
    r=[1,1,1,1] => result = 1
    '''
    if DEBUG:print(u'r = ', r)
    if len(r)>0:
        if 0 in r:
            result = 0
        else:
            result = 1
    else:
        result = 0
    if DEBUG:print(u'result = ', result)
    if DEBUG:print(u'End check')
    return result


def get_document(doc):
    '''get document from name or active doc if None'''
    if type(doc)=='str':
        doc = app.getDocument(doc)
    elif doc is None:
        if document_presence() == 1:
            doc = app.activeDocument()
    return doc

def get_sketch(sketch):
    # TODO: method to get sketch
    if DEBUG:print("TODO: method to get sketch")
    pass


def document_presence(name=None, label=None):
    '''check if there is a specific doc or an active one'''
    r = []
    if name is None and label is None:
        if app.ActiveDocument:
            r.append(1)
        else:
            r.append(0)
    elif name != None and label != None:
        if app.ActiveDocument.Name == name:
            r.append(1)
        else:
            r.append(0)
        if app.ActiveDocument.Label == label:
            r.append(1)
        else:
            r.append(0)
    elif name != None and label is None:
        if app.ActiveDocument.Name == name:
            r.append(1)
        else:
            r.append(0)
    elif name is None and label != None:
        if app.ActiveDocument.label == label:
            r.append(1)
        else:
            r.append(0)

    return make_result(r)


def get_object_by_typeId(doc=None, typeId=None):
    for obj in doc.Objects:
        if obj.TypeId==typeId:
            return obj
            break


def document_save(name=None):
    '''check if a doc is saved'''
    r=[]
    if app.ActiveDocument == None:
        r.append(0)
    else:
        if name != None:
            if app.ActiveDocument.Label == name:
                r.append(1)
            else:
                r.append(0)
        else:
            if app.ActiveDocument:
                r.append(1)
    return make_result(r)


def active_workbench(wb):
    '''Check if the active workbench is the good one
    PartDesignWorkbench", "PartWorkbench", "DraftWorkbench", "SketcherWorkbench"
    '''
    r = []
    if gui.activeWorkbench().name() != wb:
        r.append(0)
    else:
        r.append(1)
    return make_result(r)


def label_object(doc=None, obj=None, label_required=None):
    '''check if there is an object with the specific label'''
    r = []
    doc = get_document(doc)
    if doc != None:
        for obj in doc:
            if obj:
                if obj.Label == label_required:
                    r.append(1)
                else:
                    r.append(0)
            else:
                r.append(0)
    return make_result(r)



def body_presence(doc=None):
    '''Check if there is a body in the document'''
    r = []
    doc = get_document(doc)
    if doc != None:
        if len(doc.Objects)>0:
            body_list = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Body':
                    body_list.append(obj)
            if len(body_list)>0:
                    r.append(1)
            else:
                r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)

def body_features(body):
    '''Check if the body contains required features'''
    if DEBUG:print(body.OutList)
    pass


def primitive_presence(doc=None, label=None, typeId=None, dimensions=None, support=None, offset=None):
    '''check the presence of datum plane'''
    '''type :   'PartDesign::SubstractiveCylinder'
                'PartDesign::AdditiveBox' '''
    if DEBUG:print(u'Check primitive presence')
    r=[]
    doc = get_document(doc)
    reference = None
    # if doc and name, get reference by name
    if doc:
        if label != None:
            reference = doc.getObject(label)
        else:
            #if DEBUG:print(u'label is None')
            reference = get_object_by_typeId(doc, typeId)
            #pass
    if reference:
        if type != None:
            if DEBUG:print(u'target',typeId,u'actual',reference.TypeId )
            if reference.TypeId == typeId:
                r.append(1)
            else:
                r.append(0)
        if dimensions:
            if 'Box' in reference.TypeId :
                    if dimensions[0] == reference.Length:
                        r.append(1)
                    else:
                        r.append(0)
                    if dimensions[1] == reference.Width:
                        r.append(1)
                    else:
                        r.append(0)
                    if dimensions[2] == reference.Height:
                        r.append(1)
                    else:
                        r.append(0)

            if 'Cylinder' in reference.TypeId :
                    if dimensions[0] == reference.Radius:
                        r.append(1)
                    else:
                        r.append(0)
                    if dimensions[1] == reference.Height:
                        r.append(1)
                    else:
                        r.append(0)

        if support != None:
            if reference.Support[0][0].Name == support:
                r.append(1)
            else:
                r.append(0)
        if offset != None:
            attachOffset = []
            attachOffset.append(reference.AttachmentOffset.Base.x)
            attachOffset.append(reference.AttachmentOffset.Base.y)
            attachOffset.append(reference.AttachmentOffset.Base.z)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.x)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.y)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.z)
            attachOffset.append(reference.AttachmentOffset.Rotation.Angle)
            if DEBUG:print(attachOffset, offset)
            if offset == attachOffset:
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)
    return make_result(r)


def fillet_presence(doc=None, label=None, radius=None):
    '''check fillet presence'''
    r=[]
    doc = get_document(doc)
    if doc:
        if label != None:
            reference = doc.getObject(label)
        else:
            if DEBUG:print("TODO: make list of fillet")
            pass
    if reference:
        if reference.TypeId == 'PartDesign::Fillet':
            r.append(1)
        else:
            r.append(0)
        if reference.Radius == radius:
            r.append(1)
        else:
            r.append(0)
    return make_result(r)


def datum_plane_presence(doc=None, label=None, support=None, offset=None):
    '''check the presence of datum plane'''
    r=[]
    doc = get_document(doc)
    reference = None
    # if doc and name, get reference by name
    if doc:
        if label != None:
            reference = doc.getObject(label)
        else:
            if DEBUG:print("TODO: make list of datum_plane")
            pass
    if reference:
        r.append(1)
        if support != None:
            if reference.Support[0][0].Name == support:
                r.append(1)
            else:
                r.append(0)
        if offset != None:
            attachOffset = []
            attachOffset.append(reference.AttachmentOffset.Base.x)
            attachOffset.append(reference.AttachmentOffset.Base.y)
            attachOffset.append(reference.AttachmentOffset.Base.z)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.x)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.y)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.z)
            attachOffset.append(reference.AttachmentOffset.Rotation.Angle)
            if DEBUG:print(attachOffset, offset)
            if offset == attachOffset:
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)
    if len(r)>0:
        if 0 in r:
            result = 0
        else:
            result = 1
    else:
        result = 0
    return result

def sketch_presence(doc=None, label=None, support=None):
    '''check the presence of sketch'''
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if label :
            if len(doc.getObjectsByLabel(label)) > 0:
                sk = doc.getObjectsByLabel(label)[0]
        else:
            sk = []
            for obj in doc.Objects:
                if obj.TypeId == 'Sketcher::SketchObject':
                    sk.append(obj)
    if sk:
        if support:
            if type(sk) is list:
                got_support = False
                for s in sk:
                    if len(s.Support) > 0:
                        if s.Support[0][0].Name == support:
                            got_support = True
                if got_support is True:
                    r.append(1) # got at least one sketch with the right Support
                else:
                    r.append(0) # got at least one sketch but not the right Support
            else:
                if len(sk.Support) > 0:
                    if sk.Support[0][0].Name == support:
                        r.append(1) # got the sketch with the right Support
                    else:
                        r.append(0) # got the sketch but not the right Support
        else:
            r.append(1) # got a sketch
    else:
        r.append(0) # do not got sketch
    make_result(r)
    return make_result(r)

def geometry_presence(doc=None, sketch_label=None, count=None, isclosed=None):
    '''check if the skecth contain the count of geometrie and if the wire is closed'''
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label :
            if len(doc.getObjectsByLabel(sketch_label)) > 0:
                sk = doc.getObjectsByLabel(sketch_label)[0]
        else:
            sk = []
            for obj in doc.Objects:
                if obj.TypeId == 'Sketcher::SketchObject':
                    sk.append(obj)
    if sk:
        if type(sk) is list:
            for s in sk:
                if s.GeometryCount.__int__() == count:
                    r.append(1)
                    if isclosed == True:
                        if s.Shape.isClosed() == True:
                            r.append(1)
                        else:
                            r.append(0)
                    elif isclosed == False:
                        if s.Shape.isClosed() == False:
                            r.append(1)
                        else:
                            r.append(0)
        else:
            if sk.GeometryCount.__int__() == count:
                r.append(1)
                if isclosed == True:
                    if sk.Shape.isClosed() == True:
                        r.append(1)
                    else:
                        r.append(0)
                elif isclosed == False:
                    if sk.Shape.isClosed() == False:
                        r.append(1)
                    else:
                        r.append(0)
    else:
        r.append(0)
    return make_result(r)


def external_geometry_presence(doc=None, sketch_label=None, count=None):
    '''Check if the skecth contain the count of geometrie and if the wire is closed'''
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label :
            if len(doc.getObjectsByLabel(sketch_label)) > 0:
                sk = doc.getObjectsByLabel(sketch_label)[0]
        else:
            sk = []
            for obj in doc.Objects:
                if obj.TypeId == 'Sketcher::SketchObject':
                    sk.append(obj)

    if sk:
        externalqty = 0
        external = sk.ExternalGeometry
        for x in external:
            externalqty += len(x[1])
        if externalqty == count:
            r.append(1)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)

def constraint_presence(doc=None, sketch_label=None, count=None, type=None, value=None):
    '''Check if the skecth contain the count of constraint's type and value'''
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label :
            if len(doc.getObjectsByLabel(sketch_label)) > 0:
                sk = doc.getObjectsByLabel(sketch_label)[0]
        else:
            sk = []
            for obj in doc.Objects:
                if obj.TypeId == 'Sketcher::SketchObject':
                    sk.append(obj)

    if sk:
        if type != None:
            constraints_list=[]
            for constraint in sk.Constraints:
                if constraint.Type == type:
                    constraints_list.append(constraint) # list of constraint matching type
            if value != None :
                find_value = False
                for constraint in constraints_list:
                    if type == 'Angle':
                        angle = constraint.Value * 180 / math.pi
                        if angle == value:
                            find_value = True
                    else:
                        if constraint.Value == value:
                            find_value = True
                if find_value == True:
                    r.append(1)
                else:
                    r.append(0)
            if len(constraints_list) == count:
                r.append(1)
            else:
                r.append(0)
        else:
            if sk.ConstraintCount.__int__() == count:
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)

    return make_result(r)

def pad_presence(doc=None, name=None, type=None, length=None, midplane=None):
    '''check the presence of pad'''
    r=[]
    doc = get_document(doc)
    if DEBUG:print(doc)
    feature = None
    if doc:
        if name != None :
            feature = doc.getObject(name)
        else:
            objs=[]
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Pad':
                    objs.append(obj)
            if len(objs)>0:
                feature=objs[0]
    if feature:
        r.append(1)
        if type != None:
            if feature.Type == str(type):
                r.append(1)
            else:
                r.append(0)
        if length != None:
            if feature.Length.Value == length:
                r.append(1)
            else:
                r.append(0)
        if midplane != None:
            if feature.Midplane == midplane:
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)

    return make_result(r)

def pocket_presence(doc=None, name=None, type=None, length=None, midplane=None, reversed=None):
    '''check the presence of pocket'''
    r=[]
    doc = get_document(doc)
    feature = None
    features_list = None
    if doc:
        if name != None :
            feature = doc.getObject(name)
        else:
            features_list = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Pocket':
                    features_list.append(obj)

    if feature:
        r.append(1)
        if type != None:
            if feature.Type == str(type):
                r.append(1)
            else:
                r.append(0)
        if length != None:
            if feature.Length.Value == length:
                r.append(1)
            else:
                r.append(0)
        if midplane != None:
            if feature.Midplane == midplane:
                r.append(1)
            else:
                r.append(0)
        if reversed != None:
            if feature.Reversed == reversed:
                r.append(1)
            else:
                r.append(0)

    elif features_list:
        r.append(1)
        for feature in features_list:
            got_it = []
            if type != None:
                if feature.Type == str(type):
                    got_it.append(1)
                else:
                    got_it.append(0)
            if length != None:
                if feature.Length.Value == length:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if midplane != None:
                if feature.Midplane == midplane:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if reversed != None:
                if feature.Reversed == reversed:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if not 0 in got_it:
                r.append(1)

    else:
        r.append(0)

    return make_result(r)

def revolution_presence(doc=None):
    '''check the presence of revolution'''
    r=[]
    doc = get_document(doc)
    for obj in doc.Objects:
        if obj.TypeId == 'PartDesign::Revolution':
            r.append(1)
    return make_result(r)

def groove_presence(doc=None):
    '''check the presence of groove'''
    r=[]
    doc = get_document(doc)
    for obj in doc.Objects:
        if obj.TypeId == 'PartDesign::Groove':
            r.append(1)
    return make_result(r)

def polar_pattern_presence(doc=None, name=None, reversed=None, angle=None, occurrences=None, axis=None):
    '''check the presence of polar pattern'''
    r=[]
    doc = get_document(doc)
    feature = None
    if app.ActiveDocument:
        doc = app.ActiveDocument
        if name != None :
            feature = doc.getObject(name)
        else:
            objs=[]
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::PolarPattern':
                    objs.append(obj)
            if len(objs)>0:
                feature=objs[0]
        if feature:
            if reversed:
                if feature.Reversed == reversed:
                    r.append(1)
                else:
                    r.append(0)
            if angle:
                if feature.Angle == angle:
                    r.append(1)
                else:
                    r.append(0)
            if occurrences:
                if feature.Occurrences == occurrences:
                    r.append(1)
                else:
                    r.append(0)
            if axis:
                if feature.Axis[1][0] == axis:
                    r.append(1)
                else:
                    r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)

def linear_pattern_presence(doc=None):
    '''check the presence of linear pattern'''
    r=[]
    doc = get_document(doc)
    for obj in doc.Objects:
        if obj.TypeId == 'PartDesign::LinearPattern':
            r.append(1)
    return make_result(r)

def mirrored_pattern_presence(doc=None, name=None, plane_name=None, plane_axis=None, bf_name=None):
    '''check the presence of mirrored pattern'''
    r=[]
    doc = get_document(doc)
    if app.ActiveDocument:
        doc = app.ActiveDocument
        if name != None :
            feature = doc.getObject(name)
        else:
            objs=[]
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Mirrored':
                    objs.append(obj)
            if len(objs)>0:
                feature=objs[0]
        if feature:
            r.append(1)
            if plane_name != None:
                if feature.MirrorPlane[0].Name == plane_name:
                    r.append(1)
                else:
                    r.append(0)
            if plane_axis != None:
                if feature.MirrorPlane[1][0] == plane_axis:
                    r.append(1)
                else:
                    r.append(0)
            if bf_name != None:
                if feature.BaseFeature.Name == bf_name:
                    r.append(1)
                else:
                    r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)
    if len(r)>0:
        if 0 in r:
            result = 0
        else:
            result = 1
    else:
        result = 0
    return result

def boundbox_dimensions(doc=None, name=None, typeId=None, x=None, y=None, z=None):
    '''Check the length's dimensions of boundbox'''
    r = []
    doc = get_document(doc)
    features_list = []
    if doc:
        for feature in doc.Objects:
            if typeId:
                if feature.TypeId == typeId:
                    features_list.append(feature)
            else:
                features_list.append(feaure)
    if features_list:
        got_it = 0
        for feature in features_list:
            if not feature.Shape.isNull():
                bb_lengths = [ round(feature.Shape.BoundBox.XLength,2), round(feature.Shape.BoundBox.YLength,2), round(feature.Shape.BoundBox.ZLength,2) ]
                dim_count = 0
                if x in bb_lengths:
                    bb_lengths.remove(x)
                    dim_count += 1
                if y in bb_lengths:
                    bb_lengths.remove(y)
                    dim_count += 1
                if z in bb_lengths:
                    bb_lengths.remove(z)
                    dim_count += 1
                if dim_count == 3:
                    got_it = 1
        if got_it == 1:
            r.append(1)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)

def volume(doc=None, name=None, typeId=None, target=None):
    '''Check the project volume'''
    if DEBUG:print('Check volume')
    r=[]
    doc = get_document(doc)
    features_list = []
    if doc:
        for feature in doc.Objects:
            if typeId:
                if feature.TypeId == typeId:
                    features_list.append(feature)
            else:
                features_list.append(feaure)
    if features_list and target:
        got_it = 0
        for feature in features_list:
            if not feature.Shape.isNull():
                if DEBUG:print('actual volume is : ', feature.Shape.Volume)
                if DEBUG:print('target volume is between : ', target - 10, u'and' , target + 10)
                if (target - 10) < feature.Shape.Volume < (target + 10):
                #if round(target,0) == round(feature.Shape.Volume,0):
                    got_it = 1
        if got_it == 1:
            r.append(1)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)



def navigation_style(style):
    '''Check navigation style'''
    param = app.ParamGet("User parameter:BaseApp/Preferences/View")
    nav = param.GetString('NavigationStyle')
    if nav != style:
        result = 0
    else:
        result = 1
    return result

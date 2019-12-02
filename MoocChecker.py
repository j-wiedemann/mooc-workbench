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

__title__ = "MOOC Workbench"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"

import FreeCAD as app
import FreeCADGui as gui

import math


# for debug purposes
DEBUG = False

if DEBUG:
    print("MOOC CHECKER")


def make_result(r):
    '''make_result(r) -> 0 or 1
    make final result from list of result
    to get 1 there must not be 0 in r
    r=[1,1,1,0] => result = 0
    r=[1,1,1,1] => result = 1
    '''
    if DEBUG:
        print('Check.make_result(r = %s)' % r)
    if len(r) > 0:
        if 0 in r:
            result = 0
        else:
            result = 1
    else:
        result = 0
    # if DEBUG:print('result = ', result)
    # if DEBUG:print('End check')
    return result


def get_document(doc):
    '''get_document(doc) -> FreeCAD Document
    get document from name or active doc if None
    '''
    if DEBUG:
        print('Check.get_document(doc=%s)' % doc)
    if type(doc) == 'str':
        doc = app.getDocument(doc)
        # doc.recompute()
        if DEBUG:
            print('doc.Name is %s, doc.Label is %s' % (doc.Name, doc.Label))
    elif doc is None:
        if document_presence() == 1:
            doc = app.activeDocument()
            # doc.recompute()
            if DEBUG:
                print('doc.Name is %s, doc.Label is %s' % (doc.Name, doc.Label))
        else:
            if DEBUG:
                print('doc is None')
            pass

    return doc


def document_presence(name=None, label=None):
    '''document_presence(name=None, label=None) -> 0 or 1
    check if there is a specific doc or an active one
    '''
    if DEBUG:
        print('Check.document_presence(name=%s, label=%s)' % (name, label))
    r = []
    if name is None and label is None:
        if app.ActiveDocument:
            r.append(1)
        else:
            r.append(0)
    elif name is not None and label is not None:
        if app.ActiveDocument.Name == name:
            r.append(1)
        else:
            r.append(0)
        if app.ActiveDocument.Label == label:
            r.append(1)
        else:
            r.append(0)
    elif name is not None and label is None:
        if app.ActiveDocument.Name == name:
            r.append(1)
        else:
            r.append(0)
    elif name is None and label is not None:
        if app.ActiveDocument.label == label:
            r.append(1)
        else:
            r.append(0)

    return make_result(r)


def get_object_by_typeId(doc=None, typeId=None):
    '''get_object_by_typeId(doc=None, typeId=None) -> 0 or 1
    return obj with given TypeId in given doc
    '''
    for obj in doc.Objects:
        if obj.TypeId == typeId:
            return obj
            break


def document_save(name=None):
    '''document_save(name=None) -> 0 or 1
    check if a doc is saved
    '''
    if DEBUG:
        print("Check.document_save(name=%s)" % (name))
    r = []
    if app.ActiveDocument is None:
        r.append(0)
    else:
        if name is not None:
            if name in app.ActiveDocument.Label:
                r.append(1)
            else:
                r.append(0)
        else:
            if app.ActiveDocument:
                r.append(1)
    return make_result(r)


def active_workbench(wb):
    '''active_workbench(wb) -> 0 or 1
    Check if the active workbench is the good one
    "PartDesignWorkbench",
    "PartWorkbench",
    "DraftWorkbench",
    "SketcherWorkbench"
    '''
    if DEBUG:
        print("Check.active_workbench(wb=%s)" % (wb))
    r = []
    if gui.activeWorkbench().name() != wb:
        r.append(0)
    else:
        r.append(1)
    return make_result(r)


def label_object(doc=None, obj=None, label_required=None):
    '''label_object(doc=None, obj=None, label_required=None) -> 0 or 1
    check if there is an object with the specific label
    '''
    r = []
    doc = get_document(doc)
    if doc is not None:
        for obj in doc:
            if obj:
                if obj.Label == label_required:
                    r.append(1)
                else:
                    r.append(0)
            else:
                r.append(0)
    return make_result(r)


def body_presence(doc=None, label=None):
    '''body_presence(doc=None, label=None) -> 0 or 1
    Check if there is a body in the document
    '''
    r = []
    doc = get_document(doc)
    if doc is not None:
        if len(doc.Objects) > 0:
            body_list = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Body':
                    body_list.append(obj)
            if len(body_list) > 0:
                r.append(1)
                if label is not None:
                    label_ok = False
                    for obj in body_list:
                        if obj.Label == label:
                            label_ok = True
                            break
                    if label_ok is True:
                        r.append(1)
                    else:
                        r.append(0)
            else:
                r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)


def primitive_presence(doc=None,
                       label=None,
                       typeId=None,
                       dimensions=None,
                       support=None,
                       offset=None):
    '''primitive_presence(doc=None,
                           label=None,
                           typeId=None,
                           dimensions=None,
                           support=None,
                           offset=None) -> 0 or 1
    check the presence of primitive
    types : "PartDesign::SubstractiveCylinder"
            "PartDesign::AdditiveBox"
    '''
    if DEBUG:
        print('Check.primitive_presence(doc=%s, label=%s, typeId=%s, \
dimensions=%s, support=%s, offset=%s)' % (doc,
                                          label,
                                          typeId,
                                          dimensions,
                                          support,
                                          offset))
    r = []
    doc = get_document(doc)
    reference = None
    # if doc and name, get reference by name
    if doc:
        if label is not None:
            reference = doc.getObject(label)
        else:
            reference = get_object_by_typeId(doc, typeId)
    if reference:
        if type is not None:
            if DEBUG:
                print('target', typeId, 'actual', reference.TypeId)
            if reference.TypeId == typeId:
                r.append(1)
            else:
                r.append(0)
        if dimensions:
            if 'Box' in reference.TypeId:
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

            if 'Cylinder' in reference.TypeId:
                if dimensions[0] == reference.Radius:
                    r.append(1)
                else:
                    r.append(0)
                if dimensions[1] == reference.Height:
                    r.append(1)
                else:
                    r.append(0)

        if support is not None:
            if reference:
                if len(reference.Support) > 0:
                    if reference.Support[0][0].Name == support:
                        r.append(1)
                    else:
                        r.append(0)
                else:
                    r.append(0)
            else:
                r.append(0)

        if offset is not None:
            attachOffset = []
            attachOffset.append(reference.AttachmentOffset.Base.x)
            attachOffset.append(reference.AttachmentOffset.Base.y)
            attachOffset.append(reference.AttachmentOffset.Base.z)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.x)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.y)
            attachOffset.append(reference.AttachmentOffset.Rotation.Axis.z)
            attachOffset.append(reference.AttachmentOffset.Rotation.Angle)
            if DEBUG:
                print(attachOffset, offset)
            if offset == attachOffset:
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)
    return make_result(r)


def fillet_presence(doc=None, label=None, radius=None):
    '''fillet_presence(doc=None, label=None, radius=None) -> 0 or 1
    check fillet presence
    '''
    if DEBUG:
        print('Check.fillet_presence(doc=%s, label=%s, radius=%s)' % (
            doc,
            label,
            radius))
    r = []
    doc = get_document(doc)
    reference = None
    if doc:
        if label is not None:
            reference = doc.getObject(label)
            if DEBUG:
                print(reference)
        else:
            if DEBUG:
                print("TODO: make list of fillet")
            pass
    if reference:
        if reference.TypeId == 'PartDesign::Fillet':
            r.append(1)
        else:
            r.append(0)
        if radius:
            if reference.Radius == radius:
                r.append(1)
            else:
                r.append(0)
    return make_result(r)


def datum_plane_presence(doc=None, label=None, support=None, offset=None):
    '''datum_plane_presence(doc=None,
                            label=None,
                            support=None,
                            offset=None) -> 0 or 1
    check the presence of datum plane
    '''
    if DEBUG:
        print("Check.datum_plane_presence(doc=%s, label=%s, support=%s, \
        offset=%s)" % (doc, label, support, offset,))
    r = []
    doc = get_document(doc)
    datum_plane_list = []
    # reference = None
    references_label = []
    references_support = []
    references_offset = []
    # if doc and name, get reference by name
    if doc:
        for obj in doc.Objects:
            if obj.TypeId == 'PartDesign::Plane':
                datum_plane_list.append(obj)

    if len(datum_plane_list) > 0:
        # good there is at least 1 datum plane
        r.append(1)
        if label is not None:
            # check if a datum plane got the right label
            for datum_plane in datum_plane_list:
                if datum_plane.Label == label:
                    references_label.append(datum_plane)
                    # break
            if len(references_label) > 0:
                r.append(1)
            else:
                r.append(0)

        if support is not None:
            # check if a datum plane got the right support
            for datum_plane in datum_plane_list:
                if datum_plane.Support[0][0].Name == support:
                    references_support.append(datum_plane)
            if len(references_support) > 0:
                r.append(1)
            else:
                r.append(0)

        if offset is not None:
            # check if a datum plane got the right offset
            for datum_plane in datum_plane_list:
                attachOffset = []
                attachOffset.append(datum_plane.AttachmentOffset.Base.x)
                attachOffset.append(datum_plane.AttachmentOffset.Base.y)
                attachOffset.append(datum_plane.AttachmentOffset.Base.z)
                attachOffset.append(datum_plane.AttachmentOffset.Rotation.Axis.x)
                attachOffset.append(datum_plane.AttachmentOffset.Rotation.Axis.y)
                attachOffset.append(datum_plane.AttachmentOffset.Rotation.Axis.z)
                attachOffset.append(datum_plane.AttachmentOffset.Rotation.Angle)
                if DEBUG:
                    print(attachOffset, offset)
                if offset == attachOffset:
                    references_offset.append(datum_plane)
            if len(references_offset) > 0:
                r.append(1)
            else:
                r.append(0)

        if support is not None and offset is not None:
            match = False
            for x in references_support:
                if x in references_offset:
                    match = True
                    break
            if match is True:
                r.append(1)
            else:
                r.append(0)

    return make_result(r)


def sketch_presence(doc=None, label=None, support=None):
    '''sketch_presence(doc=None, label=None, support=None) -> 0 or 1
    check the presence of sketch
    '''
    if DEBUG:
        print("Check.sketch_presence(doc=%s, \
        label=%s, support=%s)" % (doc, label, support))
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if label:
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
                    r.append(1)  # got at least one sketch with the right Support
                else:
                    r.append(0)  # got at least one sketch but not the right Support
            else:
                if len(sk.Support) > 0:
                    if sk.Support[0][0].Name == support:
                        r.append(1)  # got the sketch with the right Support
                    else:
                        r.append(0)  # got the sketch but not the right Support
        else:
            r.append(1)  # got a sketch
    else:
        r.append(0)  # do not got sketch
    make_result(r)
    return make_result(r)


def geometry_presence(doc=None, sketch_label=None, count=None, isclosed=None):
    '''geometry_presence(doc=None,
                         sketch_label=None,
                         count=None,
                         isclosed=None) -> 0 or 1
    check if the skecth have the count of geometrie and if the wire is closed
    '''
    if DEBUG:
        print("Check.geometry_presence(doc=%s, sketch_label=%s, count=%s, \
        isclosed=%s)" % (doc, sketch_label, count, isclosed))
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label:
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
                    if isclosed is True:
                        if s.Shape.isClosed() is True:
                            r.append(1)
                        else:
                            r.append(0)
                    elif isclosed is False:
                        if s.Shape.isClosed() is False:
                            r.append(1)
                        else:
                            r.append(0)
        else:
            if sk.GeometryCount.__int__() == count:
                r.append(1)
                if isclosed is True:
                    if sk.Shape.isClosed() is True:
                        r.append(1)
                    else:
                        r.append(0)
                elif isclosed is False:
                    if sk.Shape.isClosed() is False:
                        r.append(1)
                    else:
                        r.append(0)
    else:
        r.append(0)
    return make_result(r)


def external_geometry_presence(doc=None,
                               sketch_label=None,
                               count=None):
    '''external_geometry_presence(doc=None,
                                  sketch_label=None,
                                  count=None) -> 0 or 1
    Check if the skecth contain the count of geometrie and if the wire is
     closed.
     '''
    if DEBUG:
        print("Check.external_geometry_presence(doc=%s, sketch_label=%s, \
count=%s)" % (doc, sketch_label, count))
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label:
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


def constraint_presence(doc=None,
                        sketch_label=None,
                        count=None,
                        type=None,
                        value=None):
    '''constraint_presence(doc=None,
                            sketch_label=None,
                            count=None,
                            type=None,
                            value=None) -> 0 or 1
    Check if the skecth contain the count of constraint's type and value.
    '''
    if DEBUG:
        print('Check.constraint_presence(doc=%s, sketch_label=%s, count=%s, \
type=%s, value=%s)' % (doc, sketch_label, count, type, value))
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label:
            if len(doc.getObjectsByLabel(sketch_label)) > 0:
                sk = doc.getObjectsByLabel(sketch_label)[0]
        else:
            sk = []
            for obj in doc.Objects:
                if obj.TypeId == 'Sketcher::SketchObject':
                    sk.append(obj)

    if sk:
        if type is not None:
            constraints_list = []
            for constraint in sk.Constraints:
                if constraint.Type == type:
                    constraints_list.append(constraint)  # list of constraint matching type
            if value is not None:
                find_value = False
                for constraint in constraints_list:
                    if type == 'Angle':
                        angle = constraint.Value * 180 / math.pi
                        if angle == value:
                            find_value = True
                    else:
                        if constraint.Value == value:
                            find_value = True
                if find_value is True:
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


def dimension_constraint_presence(doc=None,
                                  sketch_label=None,
                                  type=None,
                                  value=None,
                                  count=None):
    '''dimension_constraint_presence(doc=None,
                                      sketch_label=None,
                                      type=None,
                                      value=None,
                                      count=None) -> 0 or 1
    Check if the skecth contain the count of constraint's type and value.
    '''
    if DEBUG:
        print('Check.dimension_constraint_presence(doc=%s, sketch_label=%s, \
type=%s, value=%s)' % (doc, sketch_label, type, value))
    r = []
    doc = get_document(doc)
    sk = None
    if doc:
        if sketch_label:
            if len(doc.getObjectsByLabel(sketch_label)) > 0:
                sk = doc.getObjectsByLabel(sketch_label)[0]
        else:
            sk = []
            for obj in doc.Objects:
                if obj.TypeId == 'Sketcher::SketchObject':
                    sk.append(obj)

    if sk:
        if type is not None:
            constraints_list = []
            for constraint in sk.Constraints:
                if constraint.Type == type:
                    constraints_list.append(constraint)
            if value is not None:
                find_value = False
                for constraint in constraints_list:
                    if type == 'Angle':
                        angle = constraint.Value * 180 / math.pi
                        if angle == value:
                            find_value = True
                    else:
                        if constraint.Value == value:
                            find_value = True
                if find_value is True:
                    r.append(1)
                else:
                    r.append(0)
        elif count is not None:
            if sk.ConstraintCount.__int__() == count:
                r.append(1)
            else:
                r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)

    return make_result(r)


def pad_presence(doc=None,
                 name=None,
                 type=None,
                 length=None,
                 midplane=None):
    '''pad_presence(doc=None,
                     name=None,
                     type=None,
                     length=None,
                     midplane=None) -> 0 or 1
    Check the presence of pad.
    '''
    r = []
    doc = get_document(doc)
    if DEBUG:
        print(doc)
    feature = None
    if doc:
        if name is not None:
            feature = doc.getObject(name)
        else:
            objs = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Pad':
                    objs.append(obj)
            if len(objs) > 0:
                feature = objs[0]
    if feature:
        r.append(1)
        if type is not None:
            if feature.Type == str(type):
                r.append(1)
            else:
                r.append(0)
        if length is not None:
            if feature.Length.Value == length:
                r.append(1)
            else:
                r.append(0)
        if midplane is not None:
            if feature.Midplane == midplane:
                r.append(1)
            else:
                r.append(0)
    else:
        r.append(0)

    return make_result(r)


def pocket_presence(doc=None,
                    name=None,
                    type=None,
                    length=None,
                    midplane=None,
                    reversed=None):
    '''pocket_presence(doc=None,
                        name=None,
                        type=None,
                        length=None,
                        midplane=None,
                        reversed=None) -> 0 or 1
    Check the presence of pocket.
    '''
    if DEBUG:
        print('Check.pocket_presence(doc=%s, name=%s, type=%s, length=%s, \
midplane=%s, reversed=%s)' % (doc, name, type, length, midplane, reversed))
    r = []
    doc = get_document(doc)
    feature = None
    features_list = None
    if doc:
        if name is not None:
            feature = doc.getObject(name)
        else:
            features_list = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Pocket':
                    features_list.append(obj)

    if feature:
        r.append(1)
        if type is not None:
            if feature.Type == str(type):
                r.append(1)
            else:
                r.append(0)
        if length is not None:
            if feature.Length.Value == length:
                r.append(1)
            else:
                r.append(0)
        if midplane is not None:
            if feature.Midplane == midplane:
                r.append(1)
            else:
                r.append(0)
        if reversed is not None:
            if feature.Reversed == reversed:
                r.append(1)
            else:
                r.append(0)

    elif features_list:
        r.append(1)
        for feature in features_list:
            got_it = []
            if type is not None:
                if feature.Type == str(type):
                    got_it.append(1)
                else:
                    got_it.append(0)
            if length is not None:
                if feature.Length.Value == length:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if midplane is not None:
                if feature.Midplane == midplane:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if reversed is not None:
                if feature.Reversed == reversed:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if 0 not in got_it:
                r.append(1)

    else:
        r.append(0)

    return make_result(r)


def additiveloft_presence(doc=None,
                          name=None,
                          outlist=None,
                          ruled=None,
                          closed=None):
    '''additiveloft_presence(doc=None,
                              name=None,
                              outlist=None,
                              ruled=None,
                              closed=None) -> 0 or 1
    Check the presence of pocket.
    '''
    if DEBUG:
        print('Check.additiveloft_presence(doc=%s, name=%s, outlist=%s, \
ruled=%s, closed=%s)' % (doc, name, outlist, ruled, closed))
    r = []
    doc = get_document(doc)
    feature = None
    features_list = []
    if doc:
        if name is not None:
            feature = doc.getObject(name)
        else:
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::AdditiveLoft':
                    features_list.append(obj)

    if feature:
        r.append(1)
        if outlist is not None:
            if len(feature.OutList) == int(outlist):
                r.append(1)
            else:
                r.append(0)
        if ruled is not None:
            if feature.Ruled == ruled:
                r.append(1)
            else:
                r.append(0)
        if closed is not None:
            if feature.Closed == closed:
                r.append(1)
            else:
                r.append(0)

    elif len(features_list) > 0:
        r.append(1)
        for feature in features_list:
            got_it = []
            if outlist is not None:
                if feature.OutList == int(outlist):
                    got_it.append(1)
                else:
                    got_it.append(0)
            if ruled is not None:
                if feature.Ruled == ruled:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if closed is not None:
                if feature.Closed == closed:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if 0 not in got_it:
                r.append(1)

    else:
        r.append(0)

    return make_result(r)


def additivepipe_presence(doc=None,
                          name=None,
                          outlist=None,
                          ruled=None,
                          closed=None):
    '''additivepipe_presence(doc=None,
                              name=None,
                              outlist=None,
                              ruled=None,
                              closed=None) -> 0 or 1
    Check the presence of pocket.
    '''
    if DEBUG:
        print('Check.additivepipe_presence(doc=%s, name=%s, outlist=%s, \
ruled=%s, closed=%s)' % (doc, name, outlist, ruled, closed))
    r = []
    doc = get_document(doc)
    feature = None
    features_list = []
    if doc:
        if name is not None:
            feature = doc.getObject(name)
        else:
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::AdditivePipe':
                    features_list.append(obj)

    if feature:
        r.append(1)
        if outlist is not None:
            if len(feature.OutList) == int(outlist):
                r.append(1)
            else:
                r.append(0)
        if ruled is not None:
            if feature.Ruled == ruled:
                r.append(1)
            else:
                r.append(0)
        if closed is not None:
            if feature.Closed == closed:
                r.append(1)
            else:
                r.append(0)

    elif len(features_list) > 0:
        r.append(1)
        for feature in features_list:
            got_it = []
            if outlist is not None:
                if feature.OutList == int(outlist):
                    got_it.append(1)
                else:
                    got_it.append(0)
            if ruled is not None:
                if feature.Ruled == ruled:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if closed is not None:
                if feature.Closed == closed:
                    got_it.append(1)
                else:
                    got_it.append(0)
            if 0 not in got_it:
                r.append(1)

    else:
        r.append(0)

    return make_result(r)


def revolution_presence(doc=None):
    '''revolution_presence(doc=None) -> 0 or 1
    Check the presence of revolution.
    '''
    r = []
    doc = get_document(doc)
    if doc:
        for obj in doc.Objects:
            if obj.TypeId == 'PartDesign::Revolution':
                r.append(1)
    else:
        r.append(0)
    return make_result(r)


def groove_presence(doc=None):
    '''groove_presence(doc=None) -> 0 or 1
    Check the presence of groove.
    '''
    r = []
    doc = get_document(doc)
    if doc:
        for obj in doc.Objects:
            if obj.TypeId == 'PartDesign::Groove':
                r.append(1)
    else:
        r.append(0)
    return make_result(r)


def polar_pattern_presence(doc=None,
                           name=None,
                           reversed=None,
                           angle=None,
                           occurrences=None,
                           axis=None):
    '''polar_pattern_presence(doc=None,
                               name=None,
                               reversed=None,
                               angle=None,
                               occurrences=None,
                               axis=None) -> 0 or 1
    Check the presence of polar pattern.
    '''
    r = []
    doc = get_document(doc)
    feature = None
    if doc:
        if name is not None:
            feature = doc.getObject(name)
        else:
            objs = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::PolarPattern':
                    objs.append(obj)
            if len(objs) > 0:
                feature = objs[0]
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
                #print('Axis')
                #print(feature.Axis[0].Name)
                #print(axis)
                if feature.Axis[0].Name == axis:
                    r.append(1)
                else:
                    r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)


def linear_pattern_presence(doc=None):
    '''linear_pattern_presence(doc=None) -> 0 or 1
    Check the presence of linear pattern.
    '''
    r = []
    doc = get_document(doc)
    if doc:
        for obj in doc.Objects:
            if obj.TypeId == 'PartDesign::LinearPattern':
                r.append(1)
    else:
        r.append(0)
    return make_result(r)


def mirrored_pattern_presence(doc=None,
                              name=None,
                              plane_name=None,
                              plane_axis=None,
                              bf_name=None):
    '''mirrored_pattern_presence(doc=None,
                                  name=None,
                                  plane_name=None,
                                  plane_axis=None,
                                  bf_name=None) -> 0 or 1
    Check the presence of mirrored pattern.
    '''
    r = []
    doc = get_document(doc)
    if doc:
        if name is not None:
            feature = doc.getObject(name)
        else:
            objs = []
            for obj in doc.Objects:
                if obj.TypeId == 'PartDesign::Mirrored':
                    objs.append(obj)
            if len(objs) > 0:
                feature = objs[0]
        if feature:
            r.append(1)
            if plane_name is not None:
                if feature.MirrorPlane[0].Name == plane_name:
                    r.append(1)
                else:
                    r.append(0)
            if plane_axis is not None:
                if feature.MirrorPlane[1][0] == plane_axis:
                    r.append(1)
                else:
                    r.append(0)
            if bf_name is not None:
                if feature.BaseFeature.Name == bf_name:
                    r.append(1)
                else:
                    r.append(0)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)


def boundbox_dimensions(doc=None,
                        name=None,
                        typeId=None,
                        x=None,
                        y=None,
                        z=None):
    '''boundbox_dimensions(doc=None,
                            name=None,
                            typeId=None,
                            x=None,
                            y=None,
                            z=None) -> 0 or 1
    Check the length's dimensions of boundbox.
    '''
    r = []
    doc = get_document(doc)
    features_list = []
    if doc:
        for feature in doc.Objects:
            if typeId:
                if feature.TypeId == typeId:
                    features_list.append(feature)
            else:
                features_list.append(feature)
    if features_list:
        got_it = 0
        for feature in features_list:
            if not feature.Shape.isNull():
                bb_lengths = [round(feature.Shape.BoundBox.XLength, 2), round(feature.Shape.BoundBox.YLength, 2), round(feature.Shape.BoundBox.ZLength, 2)]
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


def volume(doc=None, name=None, typeId=None, target=None, offset=10):
    '''volume(doc=None, name=None, typeId=None,
     target=None, offset=10) -> 0 or 1
    Check the project volume
    '''
    if DEBUG:
        print('Check volume')
    r = []
    doc = get_document(doc)
    features_list = []
    if doc:
        for feature in doc.Objects:
            if typeId:
                if feature.TypeId == typeId:
                    features_list.append(feature)
            else:
                features_list.append(feature)
    if features_list and target:
        got_it = 0
        for feature in features_list:
            if not feature.Shape.isNull():
                if DEBUG:
                    print('actual volume is : ', feature.Shape.Volume)
                    print('target volume is between : ', target - offset, 'and', target + offset)
                if (target - offset) < feature.Shape.Volume < (target + offset):
                    # if round(target,0) == round(feature.Shape.Volume,0):
                    got_it = 1
        if got_it == 1:
            r.append(1)
        else:
            r.append(0)
    else:
        r.append(0)
    return make_result(r)


def navigation_style(style):
    '''navigation_style(style) -> 0 or 1
    Check navigation style
    '''
    param = app.ParamGet("User parameter:BaseApp/Preferences/View")
    nav = param.GetString('NavigationStyle')
    if nav != style:
        r = [0]
    else:
        r = [1]
    return make_result(r)


def workbench_presence(wb):
    '''workbench_presence(wb) -> 0 or 1
    Check workbench presence in FreeCAD
    '''
    r = [0]
    for wb in gui.listWorkbenches():
        if wb == wb:
            r = [1]
            break
    return make_result(r)


def a2p_importedPart_presence(doc=None, label=None):
    '''a2p_importedPart_presence(doc=None, label=None) -> 0 or 1
    check if object with corresponding label is an a2p import
    '''
    doc = get_document(doc)
    r = [0]
    if doc:
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy'):
                if 'a2p' in obj.Proxy.__str__():
                    if hasattr(obj, 'a2p_Version'):
                        if label is not None:
                            if label.lower() in obj.Label.lower():
                                r = [1]
                                break
                        else:
                            r = [1]
                            break

    return make_result(r)


def a2p_constraint_presence(doc=None, type=None):
    '''a2p_constraint_presence(doc=None, type=None) -> 0 or 1
    types : plane, axial, planesParallel
    '''
    doc = get_document(doc)
    r = [0]
    if doc:
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy'):
                if 'a2p' in obj.Proxy.__str__():
                    if not hasattr(obj, 'a2p_Version'):
                        if obj.Type == type:
                            r = [1]
                            break

    return make_result(r)

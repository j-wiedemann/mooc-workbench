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
        self.data_tutorial = {}
        self.data_tutorial["title"] = "[Test] Test1"
        self.data_tutorial["description"] = """One test with one objective."""
        url = "https://video_url.com"
        self.data_tutorial["steps"] = []
        # Step 1
        step = {}
        img1 = os.path.join(moocWB_icons_path, "Document-new.svg")
        step["video"] = str(url) + "?start=0m00s"
        step["objectives"] = ["Create a new document."]
        step["checks"] = ["MoocChecker.document_presence()"]

        step["description"] = """<h3>Preparation</h3>
            <p><img src= %s width="25"/> Create a new document :
            <ul><li>with menu <i>File</i> then <i>New.</li>
            <li>with the shortcut Ctrl + N</li></ul></p> """ % (img1, )

        self.data_tutorial["steps"].append(step)

    def get_title(self):
        return self.data_tutorial["title"]

    def get_description(self):
        return self.data_tutorial["description"]

    def get_lesson_len(self):
        return len(self.data_tutorial["steps"])

    def get_data_step(self, stepid, ):
        return self.data_tutorial["steps"][stepid]

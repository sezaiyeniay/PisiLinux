#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

NoStrip = ["/usr/kde/4/share/", "/usr/share"]
shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DWITH_PulseAudio=ON \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DDEBUG_PACKAGE_INSTALLER_NAME=\"installdbgsymbols.py\"")

def build():
    kde4.make()

def install():
    kde4.install()

    #remove index.theme file of hicolor icon theme, correct source for the file is the hicolor icon theme package itself
    pisitools.remove("/usr/share/icons/hicolor/index.theme")

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static\
                         --disable-schemas-install")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")     

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

WorkDir = "./"

def install():
    pisitools.insinto("%s/ksplash/Themes/" % kde4.appsdir, "Pisilinux-ksplash-theme", "PisiLinux")

#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi import api as pisiapi
import platform
import os

fileassociations = open("/usr/share/applications/mimeapps.list","a")
fileassociations.write("application/x-pisi=package-manager.desktop;\n")
fileassociations.write("x-scheme-handler/http=mozillafirefox.desktop;\n")
fileassociations.write("x-scheme-handler/https=mozillafirefox.desktop;\n")
fileassociations.write("x-scheme-handler/about=mozillafirefox.desktop;\n")
fileassociations.write("x-scheme-handler/mailto=sylpheed.desktop;\n")
fileassociations.write("application/x-extension-eml=sylpheed.desktop;\n")
fileassociations.write("message/rfc822=sylpheed.desktop;\n")
fileassociations.write("inode/directory=caja-folder-handler.desktop;\n")
fileassociations.write("text/plain=pluma.desktop;\n")
fileassociations.write("audio/mpeg=gnome-mplayer.desktop;\n")
fileassociations.write("audio/x-mpegurl=gnome-mplayer.desktop;\n")
fileassociations.write("audio/x-scpls=gnome-mplayer.desktop;\n")
fileassociations.write("audio/x-vorbis+ogg=gnome-mplayer.desktop;\n")
fileassociations.write("audio/x-wav=gnome-mplayer.desktop;\n")
fileassociations.write("video/mp4=smplayer_enqueue.desktop;\n")
fileassociations.write("video/mpeg=smplayer_enqueue.desktop;\n")
fileassociations.write("video/mp2t=smplayer_enqueue.desktop;\n")
fileassociations.write("video/msvideo=smplayer_enqueue.desktop;\n")
fileassociations.write("video/quicktime=smplayer_enqueue.desktop;\n")
fileassociations.write("video/webm=smplayer_enqueue.desktop;\n")
fileassociations.write("video/x-avi=smplayer_enqueue.desktop;\n")
fileassociations.write("video/x-flv=smplayer_enqueue.desktop;\n")
fileassociations.write("video/x-matroska=smplayer_enqueue.desktop;\n")
fileassociations.write("video/x-mpeg=smplayer_enqueue.desktop;\n")
fileassociations.write("video/x-ogm+ogg=smplayer_enqueue.desktop;\n")
fileassociations.write("image/bmp=eom.desktop;\n")
fileassociations.write("image/gif=eom.desktop;\n")
fileassociations.write("image/jpeg=eom.desktop;\n")
fileassociations.write("image/png=eom.desktop;\n")
fileassociations.write("image/tiff=eom.desktop;\n")
fileassociations.write("image/x-ms-bmp=eom.desktop;\n")
fileassociations.write("text/plain=pluma.desktop;\n")
fileassociations.write("text/x-patch=pluma.desktop;\n")
fileassociations.write("text/x-patch=pluma.desktop;\n")
fileassociations.write("text/x-python=pluma.desktop;\n")
fileassociations.write("text/x-python=pluma.desktop;\n")
fileassociations.write("application/xml=pluma.desktop;\n")
fileassociations.write("application/xml=pluma.desktop;\n")
fileassociations.write("application/pdf=atril.desktop;\n")
fileassociations.write("application/zip=engrampa.desktop;\n")
fileassociations.write("application/x-rar=engrampa.desktop;\n")
fileassociations.write("application/x-compressed-tar=engrampa.desktop;\n")
fileassociations.write("application/x-tar=engrampa.desktop;\n")
fileassociations.write("application/x-bzip-compressed-tar=engrampa.desktop;\n")
fileassociations.close()

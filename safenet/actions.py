#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    shelltools.system("unzip Safenet_Linux_Installer_DEB_x64.zip")
    shelltools.system("ar xvf safenetauthenticationclient_10.7.77_amd64.deb")
    shelltools.system("tar xvf %s/data.tar.xz" %get.workDIR())

def build():
    pass

def install():
    pisitools.dodir("/etc")
    pisitools.insinto("/etc/", "etc/eToken.conf")
    pisitools.insinto("/etc/", "etc/eToken.common.conf")
    pisitools.dodir("/etc/init.d")
    pisitools.insinto("/etc/init.d/", "etc/init.d/safenetauthenticationclient")
    pisitools.dodir("/usr/bin/")
    pisitools.insinto("/usr/bin/", "usr/bin/*")
    pisitools.dodir("/usr/lib")
    pisitools.insinto("/usr/lib/", "usr/lib/*.so")
    pisitools.dodir("/usr/lib/SAC")
    pisitools.insinto("/usr/lib/SAC/", "usr/lib/SAC/SACUIProcess")
    pisitools.dodir("/usr/lib/pkcs11")
    pisitools.insinto("/usr/lib/pkcs11/", "usr/lib/pkcs11/*")
    pisitools.dodir("/usr/share/applications")
    pisitools.insinto("/usr/share/applications/", "usr/share/applications/*")
    pisitools.dodoc("usr/share/doc/safenetauthenticationclient/SACHelp.pdf", "usr/share/doc/safenetauthenticationclient/changelog.gz", "usr/share/doc/safenetauthenticationclient/copyright")
    pisitools.dodir("/usr/share/eToken/languages")
    pisitools.insinto("/usr/share/eToken/languages/", "usr/share/eToken/languages/*")
    pisitools.dodir("/usr/share/gnome/autostart")
    pisitools.insinto("/usr/share/gnome/autostart", "usr/share/gnome/autostart/SACMonitor.desktop")
    pisitools.dodir("/usr/share/icons")
    pisitools.insinto("/usr/share/icons/", "usr/share/icons/*")

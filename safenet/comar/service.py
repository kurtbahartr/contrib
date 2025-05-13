# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Safenet Authentication Client Daemon",
                 "tr": "Safenet Kimlik Doğrulama İstemcisi Daemon'u"})
serviceDefault = "on"

PIDFILE="/run/safenetauthenticationclient.pid"

@synchronized
def start():
    # path to executable
    # creates a pid file, sets the working directory and calls the jar file
    startService(command="/etc/init.d/safenetauthenticationclient",
                 args="start",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def ready():
    start()

def status():
    return isServiceRunning(pidfile=PIDFILE)

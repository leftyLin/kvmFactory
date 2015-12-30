#!/usr/bin/env python
# Author:lefty
# 
# #fab -H root@mark29 sync 
#
# Start a UbuntuVM, using root@mark29, projname=test1
# $fab -H root@mark29 start:test1,ubuntu
#
from fabric.api import local,run,put,parallel,hosts

def help():
    print ""
    print "kvmFactory"
    print "func: "
    print('    initial, create, destroy, localcreate, localdestroy, localsync, syncfile, syncimg')
    print "usage: "
    print("    fab -H root@mark29 create:test1,ubuntu")

def initial():
    # Setup Server 
    run("if [ ! -d /var/lib/libvirt/images/fab ];then mkdir /var/lib/libvirt/images/fab;fi")
    run("mkdir /var/lib/libvirt/images/fab/pool")
    run("mkdir /var/lib/libvirt/images/fab/bin")
    run("mkdir /var/lib/libvirt/images/fab/base")
    run("mkdir /var/lib/libvirt/images/fab/xml")

def create(proj=None,os=None):
    print ""
    print "###################################"
    print "              Initial              "
    print "       The House Party Protocol    "
    print "###################################"
    print ""
    # Create VM-Robot & Start
    if proj is None or os is None:
        print "Proj=? OS=?"
    else:
        print "Let's Do it!"
        run("~/fab/bin/create %s %s" %(proj, os))

def localcreate(proj=None,os=None):
    print ""
    print "###################################"
    print "              Initial              "
    print "       The House Party Protocol    "
    print "###################################"
    print ""
    # Create VM-Robot & Start
    if proj is None or os is None:
        print "Proj=? OS=?"
    else:
        print "Let's Do it!"
        local("sudo ~/desktop/repo/fab/bin/create %s %s" %(proj, os))

def localsync():
    local("rm -rf ~/desktop/repo/fab/bin")
    local("rm -rf ~/desktop/repo/fab/xml")
    local("cp -r ~/CloudStation/mytools/kvmFactory/xml ~/desktop/repo/fab")
    local("cp -r ~/CloudStation/mytools/kvmFactory/bin ~/desktop/repo/fab")
    local("chmod 755 ~/desktop/repo/fab/bin/*")

@parallel
@hosts('root@mark29')
def syncfile():
    # Sync xml/, bin/
    run("if [ ! -d /var/lib/libvirt/images/fab ];then mkdir /var/lib/libvirt/images/fab;fi")
    run("if [ ! -d /var/lib/libvirt/images/fab/pool ];then mkdir /var/lib/libvirt/images/fab/pool;fi")
    run("rm -rf /var/lib/libvirt/images/fab/bin")
    run("rm -rf /var/lib/libvirt/images/fab/xml")
    put("~/CloudStation/mytools/kvmFactory/xml","/var/lib/libvirt/images/fab")
    put("~/CloudStation/mytools/kvmFactory/bin","/var/lib/libvirt/images/fab")
    run("chmod 755 /var/lib/libvirt/images/fab/bin/*")

@parallel
@hosts('root@mark29')
def syncimg():
    # Sync img
    put("~/desktop/repo/fab/base","/var/lib/libvirt/images/fab/")

@parallel
@hosts('root@mark29')
def destroyall():
    # Destroy all, Erase all
    print ""
    print "################################"
    print "       !!! WARNING !!!          "
    print "    The Clean Slate Protocol    "
    print "################################"
    print ""
    run("~/fab/bin/destroy")

def destroy():
    # Destroy
    print ""
    print "################################"
    print "       !!! WARNING !!!          "
    print "    The Clean Slate Protocol    "
    print "################################"
    print ""
    run("~/fab/bin/destroy")

def localdestroy():
    # Destroy all, Erase all
    print ""
    print "################################"
    print "       !!! WARNING !!!          "
    print "    The Clean Slate Protocol    "
    print "################################"
    print ""
    local("sudo ~/desktop/repo/fab/bin/destroy")

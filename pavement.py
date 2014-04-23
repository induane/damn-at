"""
.. module:: pavement
   :synopsis: pavement setup script
.. moduleauthor:: Brant Watson <oldspiceap@gmail.com>
"""
# Standard
import os
import shutil

# Paver
from paver.easy import (
    sh,
    task,
    needs,
)

# Dist utils
from distutils.dir_util import copy_tree

INSTALL_PATH = '/opt/owlad/site-packages/'
VERSION = '1.0.0-dev0'
BUILD_DIR = os.path.abspath('damn_at_build_%s' % VERSION)
PKG_NAME = 'damn-at'
CONTROL_TEXT = """
Package: %s
Priority: optional
Section: python
Maintainer: Owlad
Architecture: all
Version: %s
Depends: python-django, apache2, python-mysqldb, libapache2-mod-wsgi
Description: Digital assets managed nicely.
""" % (PKG_NAME, VERSION)

###############################################################################
# Helper functions section:
# Some paver tasks require some helper methods, the first section of this
# script contains these methods. Do not put any tasks here pretty please! :-)
###############################################################################


###############################################################################
# Tasks Section:
# Paver tasks should all be listed starting here. If the task requires any
# helper methods, please place them in the Helper Functions section. Thanks!
###############################################################################

@task
def clean():
    """Clean up local directory"""
    sh('find -name *.pyc -delete')
    sh('find -name *.orig -delete')
    for asset in os.listdir('.'):
        if asset.startswith('damn-at'):
            try:
                shutil.rmtree(asset)
            except OSError:
                pass
            else:
                print('Removed folder %s' % asset)
        if asset.endswith('.deb'):
            try:
                os.remove(asset)
            except Exception:
                pass
            else:
                print('Removed deb package %s' % asset)


@task
@needs('clean')
def build_deb(options):
    """Create a debian package"""
    # Create the build folder
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    deb_folder = os.path.join(BUILD_DIR, 'DEBIAN')
    if not os.path.exists(deb_folder):
        os.makedirs(deb_folder)

    ctrl = open(os.path.join(deb_folder, 'control'), "wb")
    ctrl.write(CONTROL_TEXT)
    ctrl.close()

    install_folder = os.path.join(BUILD_DIR, INSTALL_PATH.lstrip("/"))
    if not os.path.exists(install_folder):
        os.makedirs(install_folder)

    print('Install folder: %s' % install_folder)
    for asset in os.listdir(os.path.abspath('src')):
        if 'egg-info' in str(asset):
            continue
        src = os.path.join(os.path.abspath('src'), os.path.basename(asset))
        if os.path.isdir(src):
            dest = os.path.join(install_folder, os.path.basename(src))
            print('Copy tree %s to %s' % (src, dest))
            copy_tree(src, dest)
    apache_folder = os.path.join(BUILD_DIR, 'etc/apache2/conf.d/')
    print('Creating apache config folder. %s' % apache_folder)
    os.makedirs(apache_folder)
    dest_conf_file = os.path.join(apache_folder, 'doors.conf')
    shutil.copyfile('config/doors.conf', dest_conf_file)

    sh('dpkg-deb -z8 -Zgzip --build %s' % BUILD_DIR)
    try:
        shutil.rmtree(BUILD_DIR)
    except OSError:
        pass

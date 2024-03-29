# -*- coding: utf-8 -*-
# Copyright (C) 2024 Mike Sims <sims.mike@gmail.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of SoloFolder and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from setuptools import setup

__plugin_name__ = 'SoloFolder'
__author__ = 'Mike Sims'
__author_email__ = 'sims.mike@gmail.com'
__version__ = '1.0.0'
__url__ = 'https://github.com/EasyG0ing1/SoloFolder'
__license__ = 'GPLv3'
__description__ = 'Forces Deluge to create a folder for torrents that have only a single file in them.'
__long_description__ = """Creates a subfolder for torrents that have only a single file in them, keeping your download folder clutter free."""
__pkg_data__ = {__plugin_name__.lower(): ["template/*", "data/*"]}

setup(
    name=__plugin_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__ if __long_description__ else __description__,

    packages=[__plugin_name__.lower()],
    package_data = __pkg_data__,

    entry_points="""
    [deluge.plugin.core]
    %s = %s:CorePlugin
    [deluge.plugin.gtkui]
    %s = %s:GtkUIPlugin
    [deluge.plugin.web]
    %s = %s:WebUIPlugin
    """ % ((__plugin_name__, __plugin_name__.lower())*3)
)

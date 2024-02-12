# -*- coding: utf-8 -*-
# Copyright (C) 2024 Mike Sims <sims.mike@gmail.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of SoloFolder and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from deluge.plugins.init import PluginInitBase

class CorePlugin(PluginInitBase):
    def __init__(self, plugin_name):
        from .core import Core as _plugin_cls
        self._plugin_cls = _plugin_cls
        super(CorePlugin, self).__init__(plugin_name)

class GtkUIPlugin(PluginInitBase):
    def __init__(self, plugin_name):
        from .gtkui import GtkUI as _plugin_cls
        self._plugin_cls = _plugin_cls
        super(GtkUIPlugin, self).__init__(plugin_name)

class WebUIPlugin(PluginInitBase):
    def __init__(self, plugin_name):
        from .webui import WebUI as _plugin_cls
        self._plugin_cls = _plugin_cls
        super(WebUIPlugin, self).__init__(plugin_name)

class Gtk3UIPlugin(PluginInitBase):
    def __init__(self, plugin_name):
        from .gtkui import Gtk3UI as _plugin_cls
        self._plugin_cls = _plugin_cls
        super(Gtk3UIPlugin, self).__init__(plugin_name)
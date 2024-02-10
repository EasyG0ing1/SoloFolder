# -*- coding: utf-8 -*-
# Copyright (C) 2024 Mike Sims <sims.mike@gmail.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of SoloFolder and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.

from __future__ import unicode_literals
import logging
import deluge.configmanager
import deluge.component as component
import deluge.configmanager
from deluge.plugins.pluginbase import CorePluginBase
from deluge.core.rpcserver import export
import os
import re

log = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "createfolder": True
}


class Core(CorePluginBase):
    def enable(self):
        self.config = deluge.configmanager.ConfigManager('solofolder.conf', DEFAULT_CONFIG)
        core = component.get("Core")
        self.torrent_manager = component.get("TorrentManager")
        self.torrents = core.torrentmanager.torrents
        self.event_manager = component.get("EventManager");
        self.event_manager.register_event_handler("TorrentAddedEvent", self.torrent_added)

    def disable(self):
        self.event_manager.deregister_event_handler("TorrentAddedEvent", self.torrent_added)

    def torrent_added(self, torrent_id):
        if not (self.config['createfolder']):
            log.debug('createfolder is false, not creating new folder')
            return
        torrent = self.torrents[torrent_id]
        torrent.pause()
        status_keys = ["files", "save_path", "name"]
        status = torrent.get_status(status_keys)
        if self.config['createfolder'] and not re.match('.*/.*', status["files"][0]["path"]):
            newFolderPath = os.path.splitext(status["name"])[0] + "/" + status["files"][0]["path"]
            torrent.rename_files([[0, newFolderPath]])
            torrent.force_recheck()
            log.info('created new folder: ' + newFolderPath)
        torrent.resume()

    def update(self):
        pass

    @export
    def set_config(self, config):
        """Sets the config dictionary"""
        for key in config:
            self.config[key] = config[key]
        self.config.save()

    @export
    def get_config(self):
        """Returns the config dictionary"""
        return self.config.config

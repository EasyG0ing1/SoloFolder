/**
 * Script: solofolder.js
 *     The client-side javascript code for the SoloFolder plugin.
 *
 * Copyright:
 *     (C) Mike Sims 2024 <sims.mike@gmail.com>
 *
 *     This file is part of SoloFolder and is licensed under GNU GPL 3.0, or
 *     later, with the additional special exception to link portions of this
 *     program with the OpenSSL library. See LICENSE for more details.
 */

SoloFolderPlugin = Ext.extend(Deluge.Plugin, {
    constructor: function(config) {
        config = Ext.apply({
            name: 'SoloFolder'
        }, config);
        SoloFolderPlugin.superclass.constructor.call(this, config);
    },

    onDisable: function() {
        deluge.preferences.removePage(this.prefsPage);
    },

    onEnable: function() {
        this.prefsPage = deluge.preferences.addPage(
            new Deluge.ux.preferences.SoloFolderPage());
    }
});
new SoloFolderPlugin();

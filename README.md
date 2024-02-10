# SoloFolder

This is a deluge plugin that does a very simple task.

When a torrent is added to Deluge, it checks the first file in the torrent and if that file does not exist in a folder, it creates a folder and moves the file into it.

Deluge, by default (and no way to change this behavior) does not create folders for torrents when the torrent only has one file in it.

Over time, this can clutter the download folder, so this plugin solves that problem by making sure all torrents exist within their own sub-folder.

## Installation
Download [SoloFolder-0.0.1-py2.7.egg](https://github.com/EasyG0ing1/SoloFolder/releases/download/0.0.1/SoloFolder-0.0.1-py2.7.egg) file from the releases page, then from Preferences within Deluge, go to Plug-ins, then click on Install and then grab the egg file. Once it uploads and installs, just check the box to enable it.
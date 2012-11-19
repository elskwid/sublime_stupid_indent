#!/usr/bin/env python
# coding: utf8

import os.path
import fnmatch
import sublime
import sublime_plugin

TAB_SIZE = 'tab_size'
TRANSLATE = 'translate_tabs_to_spaces'

settings = sublime.load_settings("Stupid Indent.sublime-settings")

class StupidIndent(sublime_plugin.EventListener):
	def on_load(self, view):
		file_name = os.path.basename(view.file_name());
		view_settings = view.settings()

		for indentation in settings.get('indentations', []):
			for pattern in indentation.get('patterns', []):
				if fnmatch.fnmatch(file_name, pattern):
					tab_size = indentation.get(TAB_SIZE, view_settings.get(TAB_SIZE))
					translate = indentation.get(TRANSLATE, view_settings.get(TRANSLATE))

					# update view with new settings or defaults from above
					view_settings.set(TAB_SIZE, tab_size)
					view_settings.set(TRANSLATE, translate)
					return

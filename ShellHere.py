import sublime, sublime_plugin
import webbrowser
import tempfile
import os
import sys
import subprocess

class ShellHereCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return self.view.file_name() != None

    def is_visible(self):
        return True 

    def run(self, edit):
        settings = sublime.load_settings(__name__ + '.sublime-settings')
        print settings.get("shell")
        d = os.path.dirname(self.view.file_name())
        pwd = os.getcwd()
        os.chdir(d)
        os.environ["SHELLHERE_PATH"]=d
        subprocess.Popen(settings.get("shell"))
        os.chdir(pwd)

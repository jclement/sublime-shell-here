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
        d = os.path.dirname(self.view.file_name())
        pwd = os.getcwd()
        os.chdir(d)
        subprocess.call([r"C:\\cygwin\\bin\\mintty.exe","-i","/Cygwin-Terminal.ico","-"])
        os.chdir(pwd)

import sublime
import sublime_plugin


class DebugVersionPrintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("Debug print:")
        print("Sublime version: {}".format(sublime.version()))
        print("Sublime platform: {}".format(sublime.platform()))
        print("Sublime channel: {}".format(sublime.channel()))

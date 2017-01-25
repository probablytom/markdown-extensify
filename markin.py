from Commonmark import Commonmark


class PluginActionable:

    def process(self, markin_code):
        return markin_code
        # Repeatedly:

        #     Search by regex for action list

        #     Convert action list into HTML

        #     Replace markin code with HTML code

        # Return generated markin code with inline HTML


class Markin:
    "The Markin processor class"

    def __init__(self):
        self.processor = Commonmark.commonmark
        self.plugin_list = []

    def process(self, markdown):
        for plugin in self.plugin_list:
            markdown = plugin.process(markdown)
        return Commonmark.commonmark(markdown)

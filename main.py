from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import subprocess

class pmExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        # event is instance of ItemEnterEvent

        data = event.get_data()
        if data == 'Shutdown':
            subprocess.run(['poweroff'])
        
        elif data == 'Restart':
            subprocess.run(['reboot'])
        
        elif data == 'Lock':
            subprocess.run(['hyprlock'])


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        states = ['Shutdown', 'Restart', 'Lock']
        for i in states:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=i,
                                             description="",
                                             on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    pmExtension().run()
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CurrentItemAction import CurrentItemAction
import os

class VSCodeLauncher(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())



class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        # get the name of folders
        projects_folder = extension.preferences['projects_library']

        projects = [f for f in os.listdir(projects_folder) if os.path.isdir(os.path.join(projects_folder, f))]
        projects.sort()


        temp_folder = extension.preferences['temp_folder']
        temp_projects = [f for f in os.listdir(temp_folder) if os.path.isdir(os.path.join(temp_folder, f))]
        temp_projects.sort()

        # get the query
        # query = event.get_argument() or str()

        # filter the projects

        # first we need to check if the query is temp or project

        # for example if its project we should give the user list of projects
        # example 

        


        items = []
        for i in range(5):
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='Item %s' % i,
                                             description='Item defdef %s' % i,
                                             on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    VSCodeLauncher().run()

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import os
# logger = logging.getLogger(__name__)
# to see this logging we need to use the command below
# journalctl -f -o cat -u ulauncher.service | grep -i demo_extension

class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        # get the query
        query = event.get_argument() or str()
        os.system(f'notify-send "Query:{query}"')

        projects_folder = extension.preferences['projects_folder']
        # projects = [f for f in os.listdir(projects_folder) if os.path.isdir(os.path.join(projects_folder, f))]


        # temp_folder = extension.preferences['temp_projects_folder']
        # temp_projects = [f for f in os.listdir(temp_folder) if os.path.isdir(os.path.join(temp_folder, f))]

        # if " " in query:
        #     [project_type, project_name] = query.split(" ")
        # else:
        #     project_type = "p"
        #     project_name = "dotfiles"
        # # p = project
        # # t = temp project


        # if project_type == "p":
        #     for i in range(5):
        #         items.append(ExtensionResultItem(icon='images/icon.png',
        #                                         name=f'Item {projects[0]}'',
        #                                         description='Open project in vscode',
        #                                         on_enter=HideWindowAction()))

        # elif project_type == "t":
        #     for i in range(5):
        #         items.append(ExtensionResultItem(icon='images/icon.png',
        #                                         name=f'Item {temp_projects[0]}',
        #                                         description=s'Open temp project in vscode',
        #                                         on_enter=HideWindowAction()))            

        # else:
        #     items.append(ExtensionResultItem(icon='images/icon.png',
        #                                     name="Select p or t",
        #                                     description="p for project and t for temp project",
        #                                     on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()


# from ulauncher.api.client.Extension import Extension
# from ulauncher.api.client.EventListener import EventListener
# from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
# from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
# from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
# from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
# from ulauncher.api.shared.action.CurrentItemAction import CurrentItemAction
# import os
# import logging

# logger = logging.getLogger(__name__)
# # what this line does is that it will create a logger object for us
# # and we can use it to log our messages
# # and if we want to see the logs we can use the command below
# # journalctl -f -o cat -u ulauncher.service | grep -i vscode_launcher


# class VSCodeLauncher(Extension):
#     def __init__(self):
#         super().__init__()
#         self.logger.info("Inializing Extension")
#         self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
#         self.subscribe(ItemEnterEvent, ItemEnterEventListener())


# class KeywordQueryEventListener(EventListener):

#     def on_event(self, event, extension):

#         # get the name of folders
#         projects_folder = extension.preferences['projects_library']

#         projects = [f for f in os.listdir(projects_folder) if os.path.isdir(os.path.join(projects_folder, f))]
#         projects.sort()


#         temp_folder = extension.preferences['temp_folder']
#         temp_projects = [f for f in os.listdir(temp_folder) if os.path.isdir(os.path.join(temp_folder, f))]
#         temp_projects.sort()


#         args = event.get_argument()
#         logger.info('args: %s', args)
        
#         # get the query
#         # query = event.get_argument() or str()

#         # filter the projects

#         # first we need to check if the query is temp or project

#         # for example if its project we should give the user list of projects
#         # example 

        
#         logger.info('projects: %s', projects)
#         logger.info('temp_projects: %s', temp_projects)

#         items = []
#         for i in range(5):
#             items.append(ExtensionResultItem(icon='images/icon.png',
#                                              name='Item %s' % i,
#                                              description='Item description %s' % i,
#                                              on_enter=HideWindowAction()))

#         return RenderResultListAction(items)

# if __name__ == '__main__':
#     VSCodeLauncher().run()

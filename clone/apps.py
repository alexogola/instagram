from django.apps import AppConfig


class cloneConfig(AppConfig):
    name = 'clone'


# class cloneAppConfig(cloneConfig):
#     def ready(self):
#     story_model = apps.get_model("story_", "Story")
#     secretballot.enable_voting_on(story_model)
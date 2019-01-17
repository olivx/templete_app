from rest_framework.routers import DefaultRouter


class CustomRouter(DefaultRouter):
    def __init__(self, *args, api_root, **kwargs):
        self.APIRootView = api_root
        super().__init__(*args, api_root, **kwargs)

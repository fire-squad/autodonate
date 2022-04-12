from aiohttp.web import Application, StreamResponse, Request, Response
from autodonate.utils.config import Config
from autodonate.plugin_models import Plugin, Route


__api_version__ = 1


class ExamplePlugin(Plugin):
    pass


def setup(app: Application, config: Config) -> Plugin:
    plugin = ExamplePlugin(app, config)
    return plugin
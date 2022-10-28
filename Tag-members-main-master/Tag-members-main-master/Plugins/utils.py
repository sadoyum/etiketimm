import sys
import logging
import importlib
from pathlib import Path

def load_mahoaga(plugin_name):
    path = Path(f"Plugins/mahoaga/{plugin_name}.py")
    name = "Plugins.mahoaga.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Plugins.mahoaga." + plugin_name] = load
    print("Bot Başladı " + plugin_name)

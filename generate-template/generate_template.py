import sys
import os

if len(sys.argv) != 2:
    print("Usage: generate_template.py apworld_name")
    sys.exit(1)


ap_root = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
sys.path.insert(0, ap_root)

from worlds.AutoWorld import AutoWorldRegister
from Options import generate_yaml_templates

def world_name_from_apworld_name(apworld_name):
    for name, world in AutoWorldRegister.world_types.items():
        if world.__module__ == f"worlds.{apworld_name}" or world.__module__.startswith(f"worlds.{apworld_name}."):
            return name

    raise Exception(f"Couldn't find loaded world with world: {apworld_name}")

apworld_name = sys.argv[1]
world_name = world_name_from_apworld_name(apworld_name)

# Shamelessly stolen from https://github.com/Eijebong/Archipelago-yaml-checker
# remove all worlds except the one we want a template of
loaded_worlds = list(AutoWorldRegister.world_types.keys())
for loaded_world in loaded_worlds:
    if loaded_world != world_name:
        del AutoWorldRegister.world_types[loaded_world]

generate_yaml_templates("templates")

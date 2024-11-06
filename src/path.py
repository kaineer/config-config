from .functions import value
from .env import home

def default_dir(slug):
    return f"{home}/.config/{slug}"

def assigned_dir(full_path):
    return value(full_path)

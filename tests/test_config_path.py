from src.path import default_dir, assigned_dir

from os import environ

home = environ["HOME"]

class TestConfigPathFunctions:
    def test_default_function(self):
        assert default_dir("tmux") == home + '/.config/tmux'

    def test_assigned_path(self):
        path = f"{home}/.tmux.conf"
        assert assigned_dir(path)() == path


import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break
    return game_paths

def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names

def create_dir(path):
    if not os.path.exists:
        os.mkdir(path)

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "game")

    print(new_game_dirs)

    create_dir(target_path)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a (source, target) directory - only.")

    source, target = args[1:]

    main(source, target)
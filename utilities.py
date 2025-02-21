"""
utilities.py
"""

### IMPORT ###
from pathlib import Path

### FUNCTIONS ###

def create_directory_with_gitkeep(directory: str) -> None:
    """Creates a directory and adds a .gitkeep file inside.

    Args:
        directory (str): The directory path to create.
    """
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    gitkeep_path = dir_path / '.gitkeep'
    gitkeep_path.touch(exist_ok=True)
    print(f"Directory '{dir_path}' and .gitkeep file created")


def create_directories_with_gitkeep(dir_output: list) -> None:
    """
    Creates directories from a list and adds a .gitkeep file in each.

    Args:
        dir_output (list): List of directory names to create.
    """
    for dir_name in dir_output:
        dir_path = Path(dir_name)
        dir_path.mkdir(parents=True, exist_ok=True)
        gitkeep_path = dir_path / '.gitkeep'
        gitkeep_path.touch(exist_ok=True)
        print(f"Directory '{dir_path}' and .gitkeep file created")
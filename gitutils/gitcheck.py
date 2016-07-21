"""
python module for misc. git checks.
"""

from git import Repo
import os
from git.exc import InvalidGitRepositoryError



def is_repo_dirty(repo_path=None):
    """Returns human readable unicode icon if a repo has uncommited files or not."""
    try:
        repo = Repo(repo_path)
        if repo.is_dirty(untracked_files=True) == True:
            return u'[\u2717]'
        return u'[\u2713]'
    except InvalidGitRepositoryError:
        return "[?]"



def check_repos(repo_path):
    """Runs is_repo_dirty() on each of the folders in 'repo_path'."""
    folders = os.listdir(repo_path)
    if len(folders) == 0:
        print("No folders found in {}".format())
        exit(0)
    for folder in folders:
        if folder.startswith("."):
            continue
        folder_location = os.path.join(repo_path,folder)
        if not os.path.isdir(folder_location):
            continue
        print("{}  {}".format(is_repo_dirty(folder_location), folder))

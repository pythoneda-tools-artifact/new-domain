# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/clone_repository_locally.py

This file defines the CloneRepositoryLocally class.

Copyright (C) 2023-today rydnr's pythoneda-tools-artifact/new-domain

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import abc
import atexit
import os
from pythoneda.shared import EventListener, listen
from pythoneda.shared.git import (
    GitClone,
)
import shutil
import tempfile
from typing import List


class CloneRepositoryLocally(EventListener, abc.ABC):
    """
    Manages the cloning of repositories locally.

    Class name: CloneRepositoryLocally

    Responsibilities:
        - Know the steps required to clone a git repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.*
    """

    _token = None

    def __init__(self):
        """
        Creates a new CloneRepositoryLocally instance.
        """
        super().__init__()

    @classmethod
    async def clone(cls, url: str, name: str) -> str:
        """
        Clones given repository in a temporary folder.
        :param url: The url of the repository.
        :type url: str
        :param name: The repository name.
        :type name: str
        :return: The folder with the cloned repository.
        :rtype: str
        """
        temp_dir = tempfile.mkdtemp()
        atexit.register(lambda: cleanup_temp_dir(temp_dir))
        repo = GitClone(temp_dir).clone(url, name)
        return os.path.join(temp_dir, name)


def cleanup_temp_dir(folder: str):
    """
    Exit hook to delete given folder.
    :param folder: The folder to delete.
    :type folder: str
    """
    shutil.rmtree(folder)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

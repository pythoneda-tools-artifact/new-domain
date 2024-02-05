# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/push_repository.py

This file defines the PushRepository class.

Copyright (C) 2024-today rydnr's pythoneda-tools-artifact/new-domain

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
from pythoneda.shared import EventListener
from pythoneda.shared.git import GitPush


class PushRepository(EventListener, abc.ABC):
    """
    Performs git push on a repository.

    Class name: PushRepository

    Responsibilities:
        - Know the steps required to do a git push in the domain repository.

    Collaborators:
        - pythoneda.shared.EventListener
    """

    _token = None

    def __init__(self):
        """
        Creates a new PushRepository instance.
        """
        super().__init__()

    @classmethod
    async def push(cls, repoFolder: str, branch: str = "main", remote: str = "origin"):
        """
        Pushes the changes in the domain repository.
        :param repoFolder: The repository folder.
        :type repoFolder: str
        :param branch: The local branch.
        :type branch: str
        :param remote: The name of the remote.
        :type remote: str
        """
        git_push = GitPush(repoFolder)
        await git_push.push_branch(branch, remote)
        await git_push.push_tags()


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

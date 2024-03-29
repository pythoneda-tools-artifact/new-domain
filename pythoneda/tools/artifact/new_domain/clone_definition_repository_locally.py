# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/clone_definition_repository_locally.py

This file defines the CloneDefinitionRepositoryLocally class.

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
from .clone_repository_locally import CloneRepositoryLocally
from pythoneda.shared import listen
from pythoneda.shared.git import GitBranch
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryCloned,
    DefinitionRepositoryCloneRequested,
)
from typing import List


class CloneDefinitionRepositoryLocally(CloneRepositoryLocally):
    """
    Manages the cloning of definition repositories.

    Class name: CloneDefinitionRepositoryLocally

    Responsibilities:
        - Know the steps required to clone a definition repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.*
    """

    _token = None

    def __init__(self):
        """
        Creates a new CloneDefinitionRepositoryLocally instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.CloneDefinitionRepositoryLocally
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DefinitionRepositoryCloneRequested)
    async def listen_DefinitionRepositoryCloneRequested(
        cls, event: DefinitionRepositoryCloneRequested
    ) -> DefinitionRepositoryCloned:
        """
        Clones the definition repository into a local folder.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCloneRequested
        :return: The event representing the repository has been clone locally.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCloned
        """
        repo_folder = await cls.clone(event.context["def-url"], event.name)
        await GitBranch(repo_folder).branch("main")
        event.context["def-repo-folder"] = repo_folder
        return DefinitionRepositoryCloned(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

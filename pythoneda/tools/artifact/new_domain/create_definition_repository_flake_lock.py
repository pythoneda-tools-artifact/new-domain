# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/create_definition_repository_flake_lock.py

This file defines the CreateDefinitionRepositoryFlakeLock class.

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
from pythoneda.shared import EventListener, listen
from pythoneda.shared.git import GitAdd
from pythoneda.shared.nix.flake import NixFlake
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryFlakeLockCreated,
    DefinitionRepositoryFlakeLockRequested,
)


class CreateDefinitionRepositoryFlakeLock(EventListener):
    """
    Manages the creation of the flake.lock file in the definition repository.

    Class name: CreateDefinitionRepositoryFlakeLock

    Responsibilities:
        - Know the steps required to create the flake.lock file in the new definition repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryFlakeLockCreated
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryFlakeLockRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new CreateDefinitionRepositoryFlakeLock instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.CreateDefinitionRepositoryFlakeLock
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DefinitionRepositoryFlakeLockRequested)
    async def listen_DefinitionRepositoryFlakeLockRequested(
        cls, event: DefinitionRepositoryFlakeLockRequested
    ) -> DefinitionRepositoryFlakeLockCreated:
        """
        Creates the flake.lock file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryFlakeLockRequested
        :return: The event representing the flake.lock file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryFlakeLockCreated
        """
        repo_folder = event.context["def-repo-folder"]
        await NixFlake.update_flake_lock(repo_folder)
        await GitAdd(repo_folder).add("flake.lock")
        return DefinitionRepositoryFlakeLockCreated(
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

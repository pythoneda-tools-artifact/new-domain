# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/create_definition_repository.py

This file defines the CreateDefinitionRepository class.

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
from pythoneda.shared.git.github import Repository
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryCreated,
    DefinitionRepositoryRequested,
)
from typing import List


class CreateDefinitionRepository(EventListener):
    """
    Manages the creation of a definition repository.

    Class name: CreateDefinitionRepository

    Responsibilities:
        - Know the steps required to create a definition repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCreated
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new CreateDefinitionRepository instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.CreateDefinitionRepository
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DefinitionRepositoryRequested)
    async def listen_DefinitionRepositoryRequested(
        cls, event: DefinitionRepositoryRequested
    ) -> DefinitionRepositoryCreated:
        """
        Creates a definition repository upon receiving a DefinitionRepositoryRequested event.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryRequested
        :return: The event representing the definition repository has been created, or None if the process failed.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCreated
        """
        r = Repository(event.github_token)
        response = await r.create(event.context["def-org"], event.name)
        return (
            DefinitionRepositoryCreated(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

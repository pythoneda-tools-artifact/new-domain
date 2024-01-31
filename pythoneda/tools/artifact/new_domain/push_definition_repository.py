# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/push_definition_repository.py

This file defines the PushDefinitionRepositoryReadme class.

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
from .push_repository import PushRepository
from pythoneda.shared import listen
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryChangesPushed,
    DefinitionRepositoryPushRequested,
)


class PushDefinitionRepository(PushRepository):
    """
    Manages the pushging of the definition repository.

    Class name: PushDefinitionRepository

    Responsibilities:
        - Know the steps required to create the push in the definition repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesPushed
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryPushRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new PushDefinitionRepository instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.PushDefinitionRepository
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DefinitionRepositoryPushRequested)
    async def listen_DefinitionRepositoryPushRequested(
        cls, event: DefinitionRepositoryPushRequested
    ) -> DefinitionRepositoryChangesPushed:
        """
        Pushes the changes in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryPushRequested
        :return: The event representing the changes have been pushed.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesPushed
        """
        await cls.push(event.context["def-repo-folder"], "main", "origin")
        return DefinitionRepositoryChangesPushed(
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

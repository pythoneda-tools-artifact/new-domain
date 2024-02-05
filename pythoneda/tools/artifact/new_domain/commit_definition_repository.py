# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/commit_definition_repository.py

This file defines the CommitDefinitionRepositoryReadme class.

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
from pythoneda.shared.git import GitCommit
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryChangesCommitted,
    DefinitionRepositoryCommitRequested,
)
from typing import List


class CommitDefinitionRepository(EventListener):
    """
    Manages the commitging of the definition repository.

    Class name: CommitDefinitionRepository

    Responsibilities:
        - Know the steps required to create the commit in the definition repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesCommitted
        - pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCommitRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new CommitDefinitionRepository instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.CommitDefinitionRepository
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DefinitionRepositoryCommitRequested)
    async def listen_DefinitionRepositoryCommitRequested(
        cls, event: DefinitionRepositoryCommitRequested
    ) -> DefinitionRepositoryChangesCommitted:
        """
        Commits the changes in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCommitRequested
        :return: The event representing the commit has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesCommitted
        """
        repo_folder = event.context["def-repo-folder"]
        version = event.context["version"]
        await GitCommit(repo_folder).commit("Initial commit", False)
        return DefinitionRepositoryChangesCommitted(
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

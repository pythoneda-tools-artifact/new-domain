# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/tag_domain_repository.py

This file defines the TagDomainRepositoryReadme class.

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
from pythoneda.shared.git import GitTag
from pythoneda.tools.artifact.new_domain.events import (
    DomainRepositoryChangesTagged,
    DomainRepositoryTagRequested,
)
from typing import List


class TagDomainRepository(EventListener):
    """
    Manages the tagging of the domain repository.

    Class name: TagDomainRepository

    Responsibilities:
        - Know the steps required to create the tag in the domain repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DomainRepositoryChangesTagged
        - pythoneda.tools.artifact.new_domain.events.DomainRepositoryTagRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new TagDomainRepository instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.TagDomainRepository
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DomainRepositoryTagRequested)
    async def listen_DomainRepositoryTagRequested(
        cls, event: DomainRepositoryTagRequested
    ) -> DomainRepositoryChangesTagged:
        """
        Pushes the changes in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryTagRequested
        :return: The event representing the tag has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryChangesTagged
        """
        repo_folder = event.context["repo-folder"]
        version = event.context["version"]
        GitTag(repo_folder).tag(version, "Initial tag")
        return DomainRepositoryChangesTagged(
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

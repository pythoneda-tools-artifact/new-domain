# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/create_domain_repository_readme.py

This file defines the CreateDomainRepositoryReadme class.

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
from pythoneda.tools.artifact.new_domain.events import (
    DomainRepositoryReadmeCreated,
    DomainRepositoryReadmeRequested,
)
from .domain_readme import DomainReadme
from typing import List


class CreateDomainRepositoryReadme(EventListener):
    """
    Manages the creation of the README file in the domain repository.

    Class name: CreateDomainRepositoryReadme

    Responsibilities:
        - Know the steps required to create the README file in the new domain repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeCreated
        - pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new CreateDomainRepositoryReadme instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.CreateDomainRepositoryReadme
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DomainRepositoryReadmeRequested)
    async def listen_DomainRepositoryReadmeRequested(
        cls, event: DomainRepositoryReadmeRequested
    ) -> DomainRepositoryReadmeCreated:
        """
        Creates the README file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeRequested
        :return: The event representing the README file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeCreated
        """
        readme = DomainReadme(
            event.org,
            event.name,
            event.description,
            event.package,
            event.context["def-org"],
            event.context["url"],
            event.context["def-url"],
        )
        repo_folder = event.context["repo-folder"]
        readme_file = readme.generate(repo_folder)
        GitAdd(repo_folder).add(readme_file)
        return DomainRepositoryReadmeCreated(
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

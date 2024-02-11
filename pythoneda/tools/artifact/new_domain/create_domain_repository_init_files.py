# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/create_domain_repository_init_files.py

This file defines the CreateDomainRepositoryInitFiles class.

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
import datetime
from .init import Init
import os
from pythoneda.shared import EventListener, listen
from pythoneda.shared.git import GitAdd
from pythoneda.tools.artifact.new_domain.events import (
    DomainRepositoryInitFilesCreated,
    DomainRepositoryInitFilesRequested,
)
from typing import List


class CreateDomainRepositoryInitFiles(EventListener):
    """
    Manages the creation of the __init__.py files in the domain repository.

    Class name: CreateDomainRepositoryInitFiles

    Responsibilities:
        - Know the steps required to create the __init__.py files in the new domain repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.DomainRepositoryInitFilesCreated
        - pythoneda.tools.artifact.new_domain.events.DomainRepositoryInitFilesRequested
    """

    _token = None

    def __init__(self):
        """
        Creates a new CreateDomainRepositoryInitFiles instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.CreateDomainRepositoryInitFiles
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DomainRepositoryInitFilesRequested)
    async def listen_DomainRepositoryInitFilesRequested(
        cls, event: DomainRepositoryInitFilesRequested
    ) -> DomainRepositoryInitFilesCreated:
        """
        Creates the .gitignore file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryInitFilesRequested
        :return: The event representing the .gitignore file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryInitFilesCreated
        """
        repo_folder = event.context["repo-folder"]
        current_folder = repo_folder
        relative_folder = None
        relative_package = None
        subfolders = event.package.split(".")
        for subfolder in subfolders:
            current_folder = os.path.join(current_folder, subfolder)
            if os.path.exists(current_folder):
                if not os.path.isdir(current_folder):
                    os.delete(current_folder)
            else:
                os.mkdir(current_folder)
            if relative_package is None:
                relative_package = subfolder
            else:
                relative_package = f"{relative_package}.{subfolder}"
            if relative_folder is None:
                relative_folder = subfolder
            else:
                relative_folder = f"{relative_folder}/{subfolder}"
            init_file = await Init(
                event.org,
                event.name,
                relative_package,
                relative_folder,
                datetime.datetime.now().year,
            ).generate(current_folder)
            await GitAdd(repo_folder).add(init_file)
        return DomainRepositoryInitFilesCreated(
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

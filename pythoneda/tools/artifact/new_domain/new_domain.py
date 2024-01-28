# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/new_domain.py

This file defines the NewDomain class.

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
import asyncio
import atexit
import os
from pythoneda.shared import EventListener, listen
from pythoneda.shared.git import (
    GitAdd,
    GitBranch,
    GitClone,
    GitCommit,
    GitPush,
    GitRemote,
)
from pythoneda.shared.git.github import Repository
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryCreated,
    DefinitionRepositoryRequested,
    DomainRepositoryCreated,
    DomainRepositoryGitattributesCreated,
    DomainRepositoryGitattributesRequested,
    DomainRepositoryGitignoreCreated,
    DomainRepositoryGitignoreRequested,
    DomainRepositoryRequested,
    DomainRepositoryReadmeCreated,
    DomainRepositoryReadmeRequested,
    NewDomainCreated,
    NewDomainRequested,
)
from .readme import Readme
import shutil
import tempfile
from typing import List


class NewDomain(EventListener):
    """
    Manages the creation of new domains.

    Class name: NewDomain

    Responsibilities:
        - Know the steps required to create new domains.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.*
    """

    _token = None

    def __init__(self):
        """
        Creates a new NewDomain instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.NewDomain
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(NewDomainRequested)
    async def listen_NewDomainRequested(
        cls, event: NewDomainRequested
    ) -> NewDomainCreated:
        """
        Creates a new domain upon receiving a NewDomainRequested event.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.NewDomainRequested
        :return: The event representing the new domain has been created, or None if the process failed.
        :rtype: pythoneda.tools.artifact.new_domain.events.NewDomainCreated
        """
        print(
            f"new_domain_requested: {event} ({event.github_token.get()}) [{type(event.github_token)}]"
        )
        def_org = cls.definition_repository_org_for(event.org)
        event.context["def-org"] = def_org
        event.context["url"] = f"https://github.com/{event.org}/{event.name}"
        event.context["def-url"] = f"https://github.com/{def_org}/{event.name}"
        print(f"context -> {event.context}")
        return DomainRepositoryRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    def definition_repository_org_for(cls, org: str) -> str:
        """
        Retrieves the github organization for the definition repository associated to the organization of the domain repository given.
        :param org: The organization of the domain repository.
        :type org: str
        :return: The organization of the definition repository.
        :rtype: str
        """
        return f"{org}-def"

    @classmethod
    @listen(DomainRepositoryRequested)
    async def listen_DomainRepositoryRequested(
        cls, event: DomainRepositoryRequested
    ) -> List:
        """
        Creates a domain repository upon receiving a NewDomainRequested event.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.NewDomainRequested
        :return: The event representing the new domain has been created, or None if the process failed.
        :rtype: pythoneda.tools.artifact.new_domain.events.NewDomainCreated
        """
        print(f"domain_repository_requested: {event} ({event.github_token.get()})")
        r = Repository(event.github_token)
        response = await r.create(event.org, event.name)
        print(response)
        return [
            DomainRepositoryCreated(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
            DefinitionRepositoryRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
        ]

    @classmethod
    @listen(DefinitionRepositoryRequested)
    async def listen_DefinitionRepositoryRequested(
        cls, event: DefinitionRepositoryRequested
    ) -> List:
        """
        Creates a definition repository upon receiving a DefinitionRepositoryRequested event.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DefinitionRepositoryRequested
        :return: The event representing the new domain has been created, or None if the process failed.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCreated
        """
        print(f"definition_repository_requested: {event} ({event.github_token})")
        r = Repository(event.github_token)
        response = await r.create(event.org, event.name)
        return DefinitionRepositoryCreated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryCreated)
    async def listen_DomainRepositoryCreated(
        cls, event: DomainRepositoryCreated
    ) -> List:
        """
        Creates some files the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryRequested
        :return: Events requesting the creation of some files in given repository.
        :rtype: List[pythoneda.tools.artifact.new_domain.events.*]
        """
        temp_dir = tempfile.mkdtemp()
        atexit.register(lambda: cleanup_temp_dir(temp_dir))
        repo = GitClone(temp_dir).clone(event.context["url"])
        repo_folder = os.path.join(temp_dir, event.name)
        GitBranch(repo_folder).branch("main")
        event.context["repo-folder"] = repo_folder
        return [
            DomainRepositoryReadmeRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
            DomainRepositoryGitattributesRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
            DomainRepositoryGitignoreRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
        ]

    @classmethod
    @listen(DomainRepositoryReadmeRequested)
    async def listen_DomainRepositoryReadmeRequested(
        cls, event: DomainRepositoryReadmeCreated
    ) -> DomainRepositoryReadmeCreated:
        """
        Creates the README file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryReadmeRequested
        :return: The event representing the README file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeCreated
        """
        readme = Readme(
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
        GitCommit(repo_folder).commit("Added README file", False)
        GitPush(repo_folder).push_branch("main", "origin")

    @classmethod
    @listen(DomainRepositoryGitattributesRequested)
    async def listen_DomainRepositoryGitattributesRequested(
        cls, event: DomainRepositoryGitattributesCreated
    ) -> DomainRepositoryGitattributesCreated:
        """
        Creates the .gitattributes file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryGitattributesRequested
        :return: The event representing the .gitattributes file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitattributesCreated
        """
        # TODO
        print(f"TODO: create .gitatttributes in domain repository")

    @classmethod
    @listen(DomainRepositoryGitignoreRequested)
    async def listen_DomainRepositoryGitignoreRequested(
        cls, event: DomainRepositoryGitignoreCreated
    ) -> DomainRepositoryGitignoreCreated:
        """
        Creates the .gitignore file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryGitignoreRequested
        :return: The event representing the .gitignore file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitignoreCreated
        """
        # TODO
        print(f"TODO: create .gitignore in domain repository")


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

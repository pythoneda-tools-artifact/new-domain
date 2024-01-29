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
from pythoneda.shared.nix.flake import (
    FlakeUtilsNixFlake,
    NixosNixFlake,
    PythonedaNixFlake,
    PythonedaSharedBannerNixFlake,
    PythonedaSharedDomainNixFlake,
)
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryChangesPushed,
    DefinitionRepositoryCreated,
    DefinitionRepositoryPyprojecttomlTemplateCreated,
    DefinitionRepositoryPyprojecttomlTemplateRequested,
    DefinitionRepositoryNixFlakeCreated,
    DefinitionRepositoryNixFlakeRequested,
    DefinitionRepositoryRequested,
    DefinitionRepositoryReadmeCreated,
    DefinitionRepositoryReadmeRequested,
    DomainRepositoryChangesPushed,
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
from .definition_readme import DefinitionReadme
from .domain_readme import DomainReadme
from .gitattributes import Gitattributes
from .gitignore import Gitignore
from .pyprojecttoml_template import PyprojecttomlTemplate
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
        def_org = cls.definition_repository_org_for(event.org)
        artifact_org = cls.artifact_repository_org_for(event.org)
        event.context["def-org"] = def_org
        event.context["artifact-org"] = artifact_org
        event.context["url"] = f"https://github.com/{event.org}/{event.name}"
        event.context["def-url"] = f"https://github.com/{def_org}/{event.name}"
        event.context[
            "artifact-url"
        ] = f"https://github.com/{artifact_org}/{event.name}"
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
    def artifact_repository_org_for(cls, org: str) -> str:
        """
        Retrieves the github organization for the artifact repository associated to the organization of the domain repository given.
        :param org: The organization of the domain repository.
        :type org: str
        :return: The organization of the artifact repository.
        :rtype: str
        """
        return f"{org}-artifact"

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
        r = Repository(event.github_token)
        response = await r.create(event.org, event.name)
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
        cls, event: DomainRepositoryReadmeRequested
    ) -> DomainRepositoryReadmeCreated:
        """
        Creates the README file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryReadmeRequested
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

    @classmethod
    @listen(DomainRepositoryGitattributesRequested)
    async def listen_DomainRepositoryGitattributesRequested(
        cls, event: DomainRepositoryGitattributesRequested
    ) -> DomainRepositoryGitattributesCreated:
        """
        Creates the .gitattributes file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryGitattributesRequested
        :return: The event representing the .gitattributes file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitattributesCreated
        """
        gitattributes = Gitattributes(
            event.context["def-url"],
            event.context["artifact-url"],
        )
        print(f'def-url: {event.context["def-url"]} -> {gitattributes}')
        repo_folder = event.context["repo-folder"]
        gitattributes_file = gitattributes.generate(repo_folder)
        GitAdd(repo_folder).add(gitattributes_file)
        return DomainRepositoryGitattributesCreated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryGitignoreRequested)
    async def listen_DomainRepositoryGitignoreRequested(
        cls, event: DomainRepositoryGitignoreRequested
    ) -> DomainRepositoryGitignoreCreated:
        """
        Creates the .gitignore file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryGitignoreRequested
        :return: The event representing the .gitignore file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitignoreCreated
        """
        gitignore = Gitignore()
        repo_folder = event.context["repo-folder"]
        gitignore_file = gitignore.generate(repo_folder)
        GitAdd(repo_folder).add(gitignore_file)
        return DomainRepositoryGitignoreCreated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryGitignoreCreated)
    async def listen_DomainRepositoryGitignoreCreated(
        cls, event: DomainRepositoryGitignoreCreated
    ) -> DomainRepositoryChangesPushed:
        """
        Pushes the changes in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DomainRepositoryGitignoreCreated
        :return: The event representing the changes have been pushe.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryChangesPushed
        """
        repo_folder = event.context["repo-folder"]
        GitCommit(repo_folder).commit("Initial commit", False)
        GitPush(repo_folder).push_branch("main", "origin")
        return DomainRepositoryChangesPushed(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

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
        r = Repository(event.github_token)
        response = await r.create(event.context["def-org"], event.name)
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
    @listen(DefinitionRepositoryCreated)
    async def listen_DefinitionRepositoryCreated(
        cls, event: DefinitionRepositoryCreated
    ) -> List:
        """
        Requests creating some files in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DefinitionRepositoryCreated
        :return: The event representing the new domain has been created, or None if the process failed.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCreated
        """
        temp_dir = tempfile.mkdtemp()
        atexit.register(lambda: cleanup_temp_dir(temp_dir))
        repo = GitClone(temp_dir).clone(event.context["def-url"])
        repo_folder = os.path.join(temp_dir, event.name)
        GitBranch(repo_folder).branch("main")
        event.context["def-repo-folder"] = repo_folder
        return [
            DefinitionRepositoryReadmeRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
            DefinitionRepositoryNixFlakeRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
            DefinitionRepositoryPyprojecttomlTemplateRequested(
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
    @listen(DefinitionRepositoryReadmeRequested)
    async def listen_DefinitionRepositoryReadmeRequested(
        cls, event: DefinitionRepositoryReadmeRequested
    ) -> DefinitionRepositoryReadmeCreated:
        """
        Creates the README file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DefinitionRepositoryReadmeRequested
        :return: The event representing the README file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryReadmeCreated
        """
        readme = DefinitionReadme(
            event.org,
            event.name,
            event.description,
            event.package,
            event.context["def-org"],
            event.context["url"],
            event.context["def-url"],
        )
        repo_folder = event.context["def-repo-folder"]
        readme_file = readme.generate(repo_folder)
        GitAdd(repo_folder).add(readme_file)
        return DefinitionRepositoryReadmeCreated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    def url_for(cls, url: str, version: str) -> str:
        """
        Retrieves the final url, including the version.
        :param url: The original url.
        :type url: str
        :param version: The version.
        :type version: str
        :return: The final url.
        :rtype: str
        """
        return lambda: f"{url}/{version}"

    @classmethod
    @listen(DefinitionRepositoryNixFlakeRequested)
    async def listen_DefinitionRepositoryNixFlakeRequested(
        cls, event: DefinitionRepositoryNixFlakeRequested
    ) -> DefinitionRepositoryNixFlakeCreated:
        """
        Creates the flake.nix file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DefinitionRepositoryNixFlakeRequested
        :return: The event representing the README file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryNixFlakeCreated
        """
        flake = PythonedaNixFlake(
            event.name,
            "0.0.0",
            lambda version: cls.url_for(event.context["url"], version),
            [
                FlakeUtilsNixFlake("v1.0.0"),
                NixosNixFlake("23.11"),
                PythonedaSharedBannerNixFlake("0.0.47"),
                PythonedaSharedDomainNixFlake("0.0.30"),
            ],
            event.description,
            event.context["url"],
            "B",
            "D",
            "D",
        )
        event.context["flake"] = flake
        repo_folder = event.context["def-repo-folder"]
        flake_file = flake.generate_flake(repo_folder)
        GitAdd(repo_folder).add(flake_file)
        return DefinitionRepositoryNixFlakeCreated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryPyprojecttomlTemplateRequested)
    async def listen_DefinitionRepositoryPyprojecttomlTemplateRequested(
        cls, event: DefinitionRepositoryPyprojecttomlTemplateRequested
    ) -> DefinitionRepositoryPyprojecttomlTemplateCreated:
        """
        Creates the README file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DefinitionRepositoryPyprojecttomlTemplateRequested
        :return: The event representing the pyprojecttoml.template file has been created.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryPyprojecttomlTemplateCreated
        """
        pyprojecttoml_template = PyprojecttomlTemplate(
            event.context["flake"],
        )
        repo_folder = event.context["def-repo-folder"]
        pyprojecttoml_template_file = pyprojecttoml_template.generate(repo_folder)
        GitAdd(repo_folder).add(pyprojecttoml_template_file)
        return DefinitionRepositoryPyprojecttomlTemplateCreated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryPyprojecttomlTemplateCreated)
    async def listen_DefinitionRepositoryPyprojecttomlTemplateCreated(
        cls, event: DefinitionRepositoryPyprojecttomlTemplateCreated
    ) -> DefinitionRepositoryChangesPushed:
        """
        Pushes the changes in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.event.DefinitionRepositoryPyprojecttomlCreated
        :return: The event representing the changes have been pushe.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesPushed
        """
        repo_folder = event.context["def-repo-folder"]
        GitCommit(repo_folder).commit("Initial commit", False)
        GitPush(repo_folder).push_branch("main", "origin")
        return DefinitionRepositoryChangesPushed(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )


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

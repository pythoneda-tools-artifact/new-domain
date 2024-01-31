# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/new_domain.py

This file defines the NewDomain class.

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
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryRequested,
    DomainRepositoryChangesCommitted,
    DomainRepositoryChangesPushed,
    DomainRepositoryChangesTagged,
    DomainRepositoryCloned,
    DomainRepositoryCloneRequested,
    DomainRepositoryCommitRequested,
    DomainRepositoryCreated,
    DomainRepositoryGitattributesCreated,
    DomainRepositoryGitattributesRequested,
    DomainRepositoryGitignoreCreated,
    DomainRepositoryGitignoreRequested,
    DomainRepositoryPushRequested,
    DomainRepositoryRequested,
    DomainRepositoryReadmeCreated,
    DomainRepositoryReadmeRequested,
    DomainRepositoryTagRequested,
    NewDomainRequested,
)


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
    @listen(NewDomainRequested)
    async def listen_NewDomainRequested(
        cls, event: NewDomainRequested
    ) -> DomainRepositoryRequested:
        """
        Creates a new domain upon receiving a NewDomainRequested event.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.NewDomainRequested
        :return: The event representing the new domain has been created, or None if the process failed.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryRequested
        """
        def_org = cls.definition_repository_org_for(event.org)
        artifact_org = cls.artifact_repository_org_for(event.org)
        event.context["def-org"] = def_org
        event.context["artifact-org"] = artifact_org
        event.context["url"] = f"https://github.com/{event.org}/{event.name}"
        event.context["def-url"] = f"https://github.com/{def_org}/{event.name}"
        event.context["version"] = "0.0.0"
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
    @listen(DomainRepositoryCreated)
    async def listen_DomainRepositoryCreated(
        cls, event: DomainRepositoryCreated
    ) -> DomainRepositoryCloneRequested:
        """
        Triggers the cloning of the new domain repository, and requests the
        creation of the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryCreated
        :return: The events requesting cloning the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryCloneRequested
        """
        return (
            DomainRepositoryCloneRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
        )

    @classmethod
    @listen(DomainRepositoryCloned)
    async def listen_DomainRepositoryCloned(
        cls, event: DomainRepositoryCloned
    ) -> DomainRepositoryReadmeRequested:
        """
        Triggers the creation of the README file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryCloned
        :return: The events requesting the creation of the README file in the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeRequested
        """
        return DomainRepositoryReadmeRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryReadmeCreated)
    async def listen_DomainRepositoryReadmeCreated(
        cls, event: DomainRepositoryReadmeCreated
    ) -> DomainRepositoryGitattributesRequested:
        """
        Triggers the creation of the .gitattributes file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryReadmeCreated
        :return: The events requesting the creation of the .gitattributes file in the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitattributesRequested
        """
        return DomainRepositoryGitattributesRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryGitattributesCreated)
    async def listen_DomainRepositoryGitattributesCreated(
        cls, event: DomainRepositoryGitattributesCreated
    ) -> DomainRepositoryGitignoreRequested:
        """
        Triggers the creation of the .gitignore file in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitattributesCreated
        :return: The events requesting the creation of the .gitignore file in the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryGitignoreRequested
        """
        return (
            DomainRepositoryGitignoreRequested(
                event.org,
                event.name,
                event.description,
                event.package,
                event.github_token,
                event.gpg_key_id,
                event.context,
            ),
        )

    @classmethod
    @listen(DomainRepositoryGitignoreCreated)
    async def listen_DomainRepositoryGitignoreCreated(
        cls, event: DomainRepositoryGitignoreCreated
    ) -> DomainRepositoryCommitRequested:
        """
        Requests a commit in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryCommitRequested
        :return: The event representing a request to commit the changes in the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryCommitRequested.
        """
        return DomainRepositoryCommitRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryChangesCommitted)
    async def listen_DomainRepositoryChangesCommitted(
        cls, event: DomainRepositoryChangesCommitted
    ) -> DomainRepositoryTagRequested:
        """
        Requests a tag in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryChangesCommitted
        :return: The event representing a request to commit the changes in the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryTagRequested.
        """
        return DomainRepositoryTagRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryChangesTagged)
    async def listen_DomainRepositoryChangesTagged(
        cls, event: DomainRepositoryChangesTagged
    ) -> DomainRepositoryPushRequested:
        """
        Pushes the changes in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryChangesTagged
        :return: The event representing a request to push the changes.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryPushRequested
        """
        return DomainRepositoryPushRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DomainRepositoryChangesPushed)
    async def listen_DomainRepositoryChangesPushed(
        cls, event: DomainRepositoryChangesPushed
    ) -> DefinitionRepositoryRequested:
        """
        Pushes the changes in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryChangesTagged
        :return: The event representing a request to push the changes.
        :rtype: pythoneda.tools.artifact.new_domain.events.DomainRepositoryPushRequested
        """
        return DefinitionRepositoryRequested(
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

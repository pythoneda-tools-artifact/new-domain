# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/new_definition.py

This file defines the NewDefinition class.

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
    DefinitionRepositoryChangesCommitted,
    DefinitionRepositoryChangesPushed,
    DefinitionRepositoryChangesTagged,
    DefinitionRepositoryCloned,
    DefinitionRepositoryCloneRequested,
    DefinitionRepositoryCommitRequested,
    DefinitionRepositoryCreated,
    DefinitionRepositoryFlakeLockCreated,
    DefinitionRepositoryFlakeLockRequested,
    DefinitionRepositoryPyprojecttomlTemplateCreated,
    DefinitionRepositoryPyprojecttomlTemplateRequested,
    DefinitionRepositoryNixFlakeCreated,
    DefinitionRepositoryNixFlakeRequested,
    DefinitionRepositoryPushRequested,
    DefinitionRepositoryRequested,
    DefinitionRepositoryReadmeCreated,
    DefinitionRepositoryReadmeRequested,
    DefinitionRepositoryTagRequested,
    DomainRepositoryChangesPushed,
    NewDomainCreated,
    Sha256InDefinitionRepositoryNixFlakeUpdated,
    UpdateSha256InDefinitionRepositoryNixFlakeRequested,
)


class NewDefinition(EventListener):
    """
    Manages the creation of definition repositories for new domains.

    Class name: NewDefinition

    Responsibilities:
        - Know the steps required to create definition repositories for new domains.

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
        :rtype: pythoneda.tools.artifact.new_domain.NewDefinition
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(DomainRepositoryChangesPushed)
    async def listen_DomainRepositoryChangesPushed(
        cls, event: DomainRepositoryChangesPushed
    ) -> DefinitionRepositoryRequested:
        """
        Pushes the changes in the domain repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DomainRepositoryTagCreated
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

    @classmethod
    @listen(DefinitionRepositoryCreated)
    async def listen_DefinitionRepositoryCreated(
        cls, event: DefinitionRepositoryCreated
    ) -> DefinitionRepositoryReadmeRequested:
        """
        Triggers the cloning of the new definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCreated
        :return: The events requesting cloning the domain repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCloneRequested
        """
        return (
            DefinitionRepositoryCloneRequested(
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
    @listen(DefinitionRepositoryCloned)
    async def listen_DefinitionRepositoryCloned(
        cls, event: DefinitionRepositoryCloned
    ) -> DefinitionRepositoryReadmeRequested:
        """
        Triggers the creation of the README file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCloned
        :return: The events requesting the creation of the README file in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryReadmeRequested
        """
        return DefinitionRepositoryReadmeRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryReadmeCreated)
    async def listen_DefinitionRepositoryReadmeCreated(
        cls, event: DefinitionRepositoryReadmeCreated
    ) -> DefinitionRepositoryNixFlakeRequested:
        """
        Requests the creation of the flake.nix file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryReadmeCreated
        :return: The event requesting a flake.nix file in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryNixFlakeRequested
        """
        return DefinitionRepositoryNixFlakeRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryNixFlakeCreated)
    async def listen_DefinitionRepositoryNixFlakeCreated(
        cls, event: DefinitionRepositoryNixFlakeCreated
    ) -> DefinitionRepositoryPyprojecttomlTemplateRequested:
        """
        Requests the creation of the pyprojecttoml.template file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryNixFlakeCreated
        :return: The event requesting the creation of the pyprojecttoml.template file in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryPyprojecttomlTemplateRequested
        """
        return DefinitionRepositoryPyprojecttomlTemplateRequested(
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
    ) -> DefinitionRepositoryFlakeLockRequested:
        """
        Requests the creation of the flake.lock file in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryPyprojecttomlTemplateCreated
        :return: The event requesting the creation of the flake.lock file.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryFlakeLockRequested
        """
        return DefinitionRepositoryFlakeLockRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryFlakeLockCreated)
    async def listen_DefinitionRepositoryFlakeLockCreated(
        cls, event: DefinitionRepositoryFlakeLockCreated
    ) -> UpdateSha256InDefinitionRepositoryNixFlakeRequested:
        """
        Requests the update of the sha256 checksum of the Nix flake in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryFlakeLockCreated
        :return: The event representing the changes have been pushe.
        :rtype: pythoneda.tools.artifact.new_domain.events.UpdateSha256InDefinitionRepositoryNixFlakeRequested
        """
        return UpdateSha256InDefinitionRepositoryNixFlakeRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(Sha256InDefinitionRepositoryNixFlakeUpdated)
    async def listen_Sha256InDefinitionRepositoryNixFlakeUpdated(
        cls, event: Sha256InDefinitionRepositoryNixFlakeUpdated
    ) -> DefinitionRepositoryCommitRequested:
        """
        Requests a commit with the changes in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.Sha256InDefinitionRepositoryNixFlakeUpdated
        :return: The event requesting a commit in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryCommitRequested
        """
        return DefinitionRepositoryCommitRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryChangesCommitted)
    async def listen_DefinitionRepositoryChangesCommitted(
        cls, event: DefinitionRepositoryChangesCommitted
    ) -> DefinitionRepositoryTagRequested:
        """
        Requests a tag in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesCommitted
        :return: The event requesting a tag in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryTagRequested
        """
        return DefinitionRepositoryTagRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryChangesTagged)
    async def listen_DefinitionRepositoryChangesTagged(
        cls, event: DefinitionRepositoryChangesTagged
    ) -> DefinitionRepositoryPushRequested:
        """
        Requests pushing the changes in the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesTagged
        :return: The event requesting the git push in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryPushRequested
        """
        return DefinitionRepositoryPushRequested(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )

    @classmethod
    @listen(DefinitionRepositoryChangesPushed)
    async def listen_DefinitionRepositoryChangesPushed(
        cls, event: DefinitionRepositoryChangesPushed
    ) -> NewDomainCreated:
        """
        Notifies all the domain has been created successfully.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.DefinitionRepositoryChangesPushed
        :return: The event requesting the git push in the definition repository.
        :rtype: pythoneda.tools.artifact.new_domain.events.NewDomainCreated
        """
        return NewDomainCreated(
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

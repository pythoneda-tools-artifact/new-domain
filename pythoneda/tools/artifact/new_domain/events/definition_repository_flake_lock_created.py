# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/definition_repository_flake_lock_created.py

This script defines the DefinitionRepositoryFlakeLockCreated class.

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
from .update_sha256_in_definition_repository_nix_flake_requested import (
    UpdateSha256InDefinitionRepositoryNixFlakeRequested,
)
from .new_domain_event import NewDomainEvent
from pythoneda.shared import attribute, sensitive
from typing import Dict, List


class DefinitionRepositoryFlakeLockCreated(NewDomainEvent):
    """
    Represents when the flake.lock file has been created in the definition repository.

    Class name: DefinitionRepositoryFlakeLockCreated

    Responsibilities:
        - Represent the fact that the flake.lock file has been created in the definition repository.

    Collaborators:
        - None
    """

    def __init__(
        self,
        org: str,
        name: str,
        description: str,
        package: str,
        githubToken: str,
        gpgKeyId: str,
        context: Dict = None,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new DefinitionRepositoryFlakeLockCreated instance.
        :param org: The name of the organization of the domain repository.
        :type org: str
        :param name: The name of the domain.
        :type name: str
        :param description: A brief description of the domain.
        :type description: str
        :param package: The Python package.
        :type package: str
        :param githubToken: The github token.
        :type githubToken: str
        :param gpgKeyId: The GnuPG key id.
        :type gpgKeyId: str
        :param context: A dictionary with additional values.
        :type context: Dict
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            org,
            name,
            description,
            package,
            githubToken,
            gpgKeyId,
            context,
            previousEventIds,
            reconstructedId,
        )

    async def maybe_trigger(
        self,
    ) -> List[UpdateSha256InDefinitionRepositoryNixFlakeRequested]:
        """
        Triggers new events.
        :return: The triggered events.
        :rtype: List[pythoneda.tools.artifact.new_domain.events.UpdateSha256InDefinitionRepositoryNixFlakeRequested]
        """
        return [
            UpdateSha256InDefinitionRepositoryNixFlakeRequested(
                self.org,
                self.name,
                self.description,
                self.package,
                self.github_token,
                self.gpg_key_id,
                self.context,
                [self.id] + self.previous_event_ids,
            ),
        ]


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

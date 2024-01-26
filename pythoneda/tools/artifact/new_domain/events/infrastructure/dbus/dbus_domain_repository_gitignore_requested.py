# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/dbus_domain_repository_gitignore_requested.py

This file defines the DbusDomainRepositoryGitignoreRequested class.

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
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject
from pythoneda.tools.artifact.new_domain.events import (
    DomainRepositoryGitignoreRequested,
)
from pythoneda.tools.artifact.new_domain.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusDomainRepositoryGitignoreRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for DomainRepositoryGitignoreRequested.

    Class name: DbusDomainRepositoryGitignoreRequested

    Responsibilities:
        - Define the d-bus interface for the DomainRepositoryGitignoreRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDomainRepositoryGitignoreRequested.
        """
        super().__init__(
            "Pythoneda_Tools_Artifact_DomainRepositoryGitignore_Events_DomainRepositoryGitignoreRequested"
        )

    @signal()
    def DomainRepositoryGitignoreRequested(
        self, org: "s", name: "s", package: "s", githubToken: "s", gpgKeyId: "s"
    ):
        """
        Defines the DomainRepositoryGitignoreRequested d-bus signal.
        :param org: The name of the organization.
        :type org: str
        :param name: The domain name.
        :type name: str
        :param package: The Python package.
        :type package: str
        :param githubToken: The github token.
        :type githubToken: str
        :param gpgKeyId: The GnuPG key id.
        :type gpgKeyId: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: DomainRepositoryGitignoreRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.runtime.events.lifecycle.DomainRepositoryGitignoreRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.org,
            event.name,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: DomainRepositoryGitignoreRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.runtime.events.lifecycle.DomainRepositoryGitignoreRequested
        :return: The signature.
        :rtype: str
        """
        return "sssss"

    @classmethod
    def parse(cls, message: Message) -> DomainRepositoryGitignoreRequested:
        """
        Parses given d-bus message containing a DomainRepositoryGitignoreRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DomainRepositoryGitignoreRequested event.
        :rtype: pythoneda.shared.runtime.events.lifecycle.DomainRepositoryGitignoreRequested
        """
        (
            org,
            name,
            package,
            github_token,
            gpg_key_id,
            event_id,
            prev_event_ids,
        ) = message.body
        return DomainRepositoryGitignoreRequested(
            org,
            name,
            package,
            github_token,
            gpg_key_id,
            None,
            event_id,
            json.loads(prev_event_ids),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

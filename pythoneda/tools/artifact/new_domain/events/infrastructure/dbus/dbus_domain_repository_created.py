# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/dbus_domain_repository_created.py

This file defines the DbusDomainRepositoryCreated class.

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
from pythoneda.tools.artifact.new_domain.events import DomainRepositoryCreated
from pythoneda.tools.artifact.new_domain.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusDomainRepositoryCreated(BaseObject, ServiceInterface):
    """
    D-Bus interface for DomainRepositoryCreated.

    Class name: DbusDomainRepositoryCreated

    Responsibilities:
        - Define the d-bus interface for the DomainRepositoryCreated event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDomainRepositoryCreated.
        """
        super().__init__(
            "Pythoneda_Tools_Artifact_DomainRepository_Events_DomainRepositoryCreated"
        )

    @signal()
    def DomainRepositoryCreated(self, url: "s", defUrl: "s"):
        """
        Defines the DomainRepositoryCreated d-bus signal.
        :param url: The url of the new domain.
        :type url: str
        :param defUrl: The url of the domain repository.
        :type defUrl: str
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
    def transform(cls, event: DomainRepositoryCreated) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.runtime.events.lifecycle.DomainRepositoryCreated
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.url,
            event.def_url,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: DomainRepositoryCreated) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.runtime.events.lifecycle.DomainRepositoryCreated
        :return: The signature.
        :rtype: str
        """
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> DomainRepositoryCreated:
        """
        Parses given d-bus message containing a DomainRepositoryCreated event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DomainRepositoryCreated event.
        :rtype: pythoneda.shared.runtime.events.lifecycle.DomainRepositoryCreated
        """
        url, def_url, event_id, prev_event_ids = message.body
        return DomainRepositoryCreated(
            url,
            def_url,
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

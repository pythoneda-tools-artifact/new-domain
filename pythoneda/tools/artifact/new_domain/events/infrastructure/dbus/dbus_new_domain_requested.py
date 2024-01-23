# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/dbus_new_domain_requested.py

This file defines the DbusNewDomainRequested class.

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
from pythoneda.tools.artifact.new_domain.events import NewDomainRequested
from pythoneda.tools.artifact.new_domain.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusNewDomainRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for NewDomainRequested.

    Class name: DbusNewDomainRequested

    Responsibilities:
        - Define the d-bus interface for the NewDomainRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusNewDomainRequested.
        """
        super().__init__("Pythoneda_Tools_Artifact_NewDomain_Events_NewDomainRequested")

    @signal()
    def NewDomainRequested(self, namespace: "s", githubToken: "s", gpgKeyId: "s"):
        """
        Defines the NewDomainRequested d-bus signal.
        :param namespace: The Python namespace.
        :type namespace: str
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
    def transform(cls, event: NewDomainRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.runtime.events.lifecycle.NewDomainRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.namespace,
            event.github_token,
            event.gpg_key_id,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: NewDomainRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.runtime.events.lifecycle.NewDomainRequested
        :return: The signature.
        :rtype: str
        """
        return "sssss"

    @classmethod
    def parse(cls, message: Message) -> NewDomainRequested:
        """
        Parses given d-bus message containing a NewDomainRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The NewDomainRequested event.
        :rtype: pythoneda.shared.runtime.events.lifecycle.NewDomainRequested
        """
        namespace, github_token, gpg_key_id, event_id, prev_event_ids = message.body
        return NewDomainRequested(
            namespace,
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

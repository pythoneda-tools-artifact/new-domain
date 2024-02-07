# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/dbus_new_domain_event.py

This file defines the DbusNewDomainEvent class.

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
import abc
from dbus_next import BusType, Message
from dbus_next.service import signal
import json
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.tools.artifact.new_domain.events import NewDomainEvent
from pythoneda.tools.artifact.new_domain.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusNewDomainEvent(DbusEvent, abc.ABC):
    """
    Abstract class for D-Bus interfaces of new-domain events.

    Class name: DbusNewDomainEvent

    Responsibilities:
        - Define the common logic for all d-bus interfaces of new-domain events.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusNewDomainEvent.
        """
        super().__init__(DBUS_PATH, BusType.SYSTEM)

    @classmethod
    def transform(cls, event: NewDomainEvent) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.tools.artifact.new_domain.NewDomainEvent
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token.get(),
            event.gpg_key_id,
            json.dumps(event.context),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: NewDomainEvent) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.tools.artifact.new_domain.NewDomainEvent
        :return: The signature.
        :rtype: str
        """
        return "sssssssss"

    @classmethod
    def parse(cls, message: Message) -> NewDomainEvent:
        """
        Parses given d-bus message containing a NewDomainEvent event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The specify NewDomainEvent event.
        :rtype: pythoneda.tools.artifact.new_domain.NewDomainEvent
        """
        (
            org,
            name,
            description,
            package,
            githubToken,
            gpgKeyId,
            context,
            event_id,
            prev_event_ids,
        ) = message.body
        return cls.event_class(
            org,
            name,
            description,
            package,
            githubToken,
            gpgKeyId,
            json.loads(context),
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

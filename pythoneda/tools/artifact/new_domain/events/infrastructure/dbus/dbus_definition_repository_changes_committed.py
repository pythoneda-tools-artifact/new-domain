# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/dbus_definition_repository_changes_committed.py

This file defines the DbusDefinitionRepositoryChangesCommitted class.

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
from .dbus_new_domain_event import DbusNewDomainEvent
from dbus_next.service import signal
from pythoneda.shared import Event
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryChangesCommitted,
)


class DbusDefinitionRepositoryChangesCommitted(DbusNewDomainEvent):
    """
    D-Bus interface for DefinitionRepositoryChangesCommitted.

    Class name: DbusDefinitionRepositoryChangesCommitted

    Responsibilities:
        - Define the d-bus interface for the DefinitionRepositoryChangesCommitted event.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.infrastructure.dbus.DbusNewDomainEvent
    """

    def __init__(self):
        """
        Creates a new DbusDefinitionRepositoryChangesCommitted.
        """
        super().__init__()

    @signal()
    def DefinitionRepositoryChangesCommitted(
        self,
        org: "s",
        name: "s",
        description: "s",
        package: "s",
        githubToken: "s",
        gpgKeyId: "s",
        context: "s",
    ):
        """
        Defines the DefinitionRepositoryCreated d-bus signal.
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
        """
        pass

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: Type[Event]
        """
        return DefinitionRepositoryChangesCommitted


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

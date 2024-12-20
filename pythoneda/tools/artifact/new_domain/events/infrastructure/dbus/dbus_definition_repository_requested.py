# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/dbus_definition_repository_requested.py

This file defines the DbusDefinitionRepositoryRequested class.

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
from pythoneda.tools.artifact.new_domain.events import DefinitionRepositoryRequested


class DbusDefinitionRepositoryRequested(DbusNewDomainEvent):
    """
    D-Bus interface for DefinitionRepositoryRequested.

    Class name: DbusDefinitionRepositoryRequested

    Responsibilities:
        - Define the d-bus interface for the DefinitionRepositoryRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDefinitionRepositoryRequested.
        """
        super().__init__()

    @signal()
    def DefinitionRepositoryRequested(
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
    def event_class(cls):
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.tools.artifact.new_domain.DefinitionRepositoryRequested)
        """
        return DefinitionRepositoryRequested


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

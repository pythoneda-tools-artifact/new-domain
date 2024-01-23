# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/infrastructure/dbus/new_domain_dbus_signal_emitter.py

This file defines the NewDomainDbusSignalEmitter class.

Copyright (C) 2023-today boot's pythoneda-tools-artifact/new-domain

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
from dbus_next import BusType
from pythoneda.tools.artifact.new_domain.events import (
    NewDomainRequested,
)
from pythoneda.tools.artifact.new_domain.events.infrastructure import (
    DbusNewDomainRequested,
)
from pythoneda.shared.infrastructure.dbus import DbusSignalEmitter
from typing import Dict


class NewDomainDbusSignalEmitter(DbusSignalEmitter):

    """
    A Port that emits NewDomain events as d-bus signals.

    Class name: NewDomainDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit infrastructure events as d-bus signals on behalf of NewDomain.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: Requests emitting events.
        - pythoneda.tools.artifact.new_domain.events.infrastructure.dbus.DbusNewDomainRequested
    """

    def __init__(self):
        """
        Creates a new NewDomainDbusSignalEmitter instance.
        """
        super().__init__()

    def signal_emitters(self) -> Dict:
        """
        Retrieves the configured event emitters.
        :return: For each event, a list with the event interface and the bus type.
        :rtype: Dict
        """
        result = {}
        key = self.__class__.full_class_name(NewDomainRequested)
        result[key] = [DbusNewDomainRequested, BusType.SYSTEM]

        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

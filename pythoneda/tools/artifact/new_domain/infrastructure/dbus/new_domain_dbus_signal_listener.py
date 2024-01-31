# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/infrastructure/dbus/new_domain_dbus_signal_listener.py

This file defines the NewDomainDbusSignalListener class.

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
from pythoneda.shared.infrastructure.dbus import DbusSignalListener
from .signals import Signals
from typing import Dict


class NewDomainDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to NewDomain-relevant d-bus signals.

    Class name: NewDomainDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to NewDomain.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: Receives relevant domain events.
        - pythoneda.tools.artifact.new_domain.events.infrastructure.dbus.*
    """

    def __init__(self):
        """
        Creates a new NewDomainDbusSignalListener instance.
        """
        super().__init__()

    def signal_receivers(self, app) -> Dict:
        """
        Retrieves the configured signal receivers.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :return: A dictionary with the signal name as key, and the tuple interface and bus type as the value.
        :rtype: Dict
        """
        return Signals.signals()


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

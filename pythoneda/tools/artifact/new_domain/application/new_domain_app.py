# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/application/new_domain_app.py

This file defines the NewDomainApp class.

Copyright (C) 2023-today rydnr's pythoneda-tools-artifact/new-domain

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
import asyncio
from pythoneda.shared.application import enable, PythonEDA
from pythoneda.tools.artifact.new_domain.events import NewDomainRequested
from pythoneda.tools.artifact.new_domain.infrastructure.cli import (
    NewDomainOptionsCli,
)
from pythoneda.shared.infrastructure.dbus import DbusSignalEmitter, DbusSignalListener
from typing import Dict


@enable(NewDomainOptionsCli)
@enable(
    DbusSignalEmitter("pythoneda.tools.artifact.new_domain.events.infrastructure.dbus")
)
@enable(
    DbusSignalListener("pythoneda.tools.artifact.new_domain.events.infrastructure.dbus")
)
class NewDomainApp(PythonEDA):
    """
    Runs the NewDomainApp PythonEDA app.

    Class name: NewDomainApp

    Responsibilities:
        - Launches NewDomain domain, to create a new PythonEDA domain.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.NewDomain
    """

    def __init__(self):
        """
        Creates a new NewDomainApp instance.
        """
        # new_domain_banner is automatically generated by pythoneda-tools-artifact-def/new-domain
        try:
            from pythoneda.tools.artifact.new_domain.application.NewDomainBanner_banner import (
                NewDomainBanner,
            )

            banner = NewDomainBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)
        self.accept_one_shot(True)

    async def accept_options(self, options: Dict):
        """
        Receives the options for creating a new domain.
        :param options: The options.
        :type options: Dict
        """
        new_domain_requested = NewDomainRequested(
            options.get("org", None),
            options.get("name", None),
            options.get("description", None),
            options.get("package", None),
            options.get("github-token", None),
            options.get("gpg-key-id", None),
        )
        if new_domain_requested:
            await self.accept(new_domain_requested)


if __name__ == "__main__":
    asyncio.run(
        NewDomainApp.main(
            "pythoneda.tools.artifact.new_domain.application.NewDomainApp"
        )
    )
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

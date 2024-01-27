# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/lifecycle/new_domain_created.py

This script defines the NewDomainCreated class.

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
from .new_domain_event import NewDomainEvent
from typing import List


class NewDomainCreated(NewDomainEvent):
    """
    Represents a new domain has been created.

    Class name: NewDomainCreated

    Responsibilities:
        - Represent the fact that a new domain has been created.

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
        previousEventId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new NewDomainCreated instance.
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
        :param url: The url of the new domain.
        :type url: str
        :param defUrl: The url of the definition repository of the new domain.
        :type defUrl: str
        :param previousEventId: The id of the previous event, if any.
        :type previousEventId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            org,
            name,
            description,
            package,
            githubToken,
            gpgKeyId,
            None,
            None,
            None,
            previous_events,
            reconstructedId,
            reconstructedPreviousEventIds,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

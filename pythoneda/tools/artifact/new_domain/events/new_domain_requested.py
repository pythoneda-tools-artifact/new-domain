# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/lifecycle/new_domain_requested.py

This script defines the NewDomainRequested class.

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
from pythoneda.shared import Event
from typing import List


class NewDomainRequested(Event):
    """
    Represents someone has requested a domain to be created.

    Class name: NewDomainRequested

    Responsibilities:
        - Represent the request of creating a new domain.

    Collaborators:
        - None
    """

    def __init__(
        self,
        namespace: str,
        githubToken: str,
        gpgKeyId: str,
        previousEventId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new NewDomainRequested instance.
        :param namespace: The Python namespace.
        :type namespace: str
        :param githubToken: The github token.
        :type githubToken: str
        :param gpgKeyId: The GnuPG key id.
        :type gpgKeyId: str
        :param previousEventId: The id of the previous event, if any.
        :type previousEventId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        previous_events = None
        if previousEventId:
            previous_events = [previousEventId]
        super().__init__(
            previous_events, reconstructedId, reconstructedPreviousEventIds
        )
        self._namespace = namespace
        self._github_token = githubToken
        self._gpg_key_id = gpgKeyId

    @property
    def namespace(self) -> str:
        """
        Retrieves the Python namespace.
        :return: Such namespace.
        :rtype: str
        """
        return self._namespace

    @property
    def github_token(self) -> str:
        """
        Retrieves the github token.
        :return: Such token.
        :rtype: str
        """
        return self._github_token

    @property
    def gpg_key_id(self) -> str:
        """
        Retrieves the id of the GnuPG key.
        :return: Such id.
        :rtype: str
        """
        return self._gpg_key_id


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

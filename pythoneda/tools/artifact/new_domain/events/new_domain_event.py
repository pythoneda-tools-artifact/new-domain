# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/lifecycle/new_domain_event.py

This script defines the NewDomainEvent class.

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
from pythoneda.shared import attribute, Event, sensitive
from typing import List


class NewDomainEvent(Event):
    """
    Common logic for all events relevant to the new-domain domain.

    Class name: NewDomainEvent

    Responsibilities:
        - Provide context data to subclasses.

    Collaborators:
        - None
    """

    def __init__(
        self,
        org: str,
        name: str,
        package: str,
        githubToken: str,
        gpgKeyId: str,
        defOrg: str = None,
        url: str = None,
        defUrl: str = None,
        previousEventId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new NewDomainEvent instance.
        :param org: The name of the organization of the domain repository.
        :type org: str
        :param name: The name of the domain.
        :type name: str
        :param package: The Python package.
        :type package: str
        :param githubToken: The github token.
        :type githubToken: str
        :param gpgKeyId: The GnuPG key id.
        :type gpgKeyId: str
        :param defOrg: The name of the organization of the definition repository.
        :param defOrg: str
        :param url: The url of the domain repository.
        :type url: str
        :param defUrl: The url of the definition repository.
        :type defUrl: str
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
        self._org = org
        self._name = name
        self._package = package
        self._github_token = githubToken
        self._gpg_key_id = gpgKeyId
        self._def_org = defOrg
        self._url = url
        self._def_url = defUrl

    @property
    @attribute
    def org(self) -> str:
        """
        Retrieves the name of the organization of the domain repository.
        :return: Such information.
        :rtype: str
        """
        return self._org

    @property
    @attribute
    def name(self) -> str:
        """
        Retrieves the name of the domain.
        :return: Such information.
        :rtype: str
        """
        return self._name

    @property
    @attribute
    @sensitive
    def github_token(self) -> str:
        """
        Retrieves the github token.
        :return: Such token.
        :rtype: str
        """
        return self._github_token

    @property
    @attribute
    def gpg_key_id(self) -> str:
        """
        Retrieves the id of the GnuPG key.
        :return: Such id.
        :rtype: str
        """
        return self._gpg_key_id

    @property
    @attribute
    def package(self) -> str:
        """
        Retrieves the Python package.
        :return: Such package.
        :rtype: str
        """
        return self._package

    @property
    @attribute
    def def_org(self) -> str:
        """
        Retrieves the name of the organization of the definition repository.
        :return: Such name.
        :rtype: str
        """
        return self._def_org

    @property
    @attribute
    def url(self) -> str:
        """
        Retrieves the url of the domain repository.
        :return: Such url.
        :rtype: str
        """
        return self._url

    @property
    @attribute
    def def_url(self) -> str:
        """
        Retrieves the url of the definition repository.
        :return: Such url.
        :rtype: str
        """
        return self._def_url


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
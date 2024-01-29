# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/definition_nix_flake.py

This file defines the DefinitionNixFlake class.

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
import datetime
from .new_file_from_template import NewFileFromTemplate
from pythoneda.shared import attribute
from pythoneda.shared.nix.flake import NixFlake


class DefinitionNixFlake(NixFlake):
    """
    Represents a flake.nix file in the definition repository.

    Class name: DefinitionNixFlake

    Responsibilities:
        - Model a flake.nix file.
        - Know how to create a new DefinitionNixFlake from templates.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlake
    """

    def __init__(
        self,
        org: str,
        name: str,
        description: str,
        package: str,
        defOrg: str,
        url: str,
        defUrl: str,
        templateSubfolder: str = "pythoneda",
    ):
        """
        Creates a new DefinitionNixFlake instance.
        :param org: The name of the organization.
        :type org: str
        :param name: The repository name.
        :type name: str
        :param description: The repository description.
        :type description: str
        :param package: The Python package.
        :type package: str
        :param defOrg: The name of the organization of the definition repository.
        :type defOrg: str
        :param url: The url of the repository.
        :type url: str
        :param defUrl: The url of the definition repository.
        :type defUrl: str
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        """
        super().__init__(
            name,
            "0.0.0",
            self.__class__.url_for,
            [],
            templateSubfolder,
            description,
            url,
            "gplv3",
            ["rydnr"],
            datetime.datetime.now().year,
            "rydnr",
        )

    @property
    @attribute
    def org(self) -> str:
        """
        Retrieves the name of the organization of the definition repository.
        :return: Such information.
        :rtype: str
        """
        return self.vars["org"]

    @property
    @attribute
    def name(self) -> str:
        """
        Retrieves the name of the definition.
        :return: Such information.
        :rtype: str
        """
        return self.vars["name"]

    @property
    @attribute
    def description(self) -> str:
        """
        Retrieves the definition description.
        :return: Such information.
        :rtype: str
        """
        return self.vars["description"]

    @property
    @attribute
    def package(self) -> str:
        """
        Retrieves the Python package.
        :return: Such package.
        :rtype: str
        """
        return self.vars["package"]

    @property
    @attribute
    def def_org(self) -> str:
        """
        Retrieves the name of the organization of the definition repository.
        :return: Such name.
        :rtype: str
        """
        return self.vars["def-org"]

    @property
    @attribute
    def url(self) -> str:
        """
        Retrieves the url of the definition repository.
        :return: Such url.
        :rtype: str
        """
        return self.vars["url"]

    @property
    @attribute
    def def_url(self) -> str:
        """
        Retrieves the url of the definition repository.
        :return: Such url.
        :rtype: str
        """
        return self.vars["def-url"]

    def templates_folder(self) -> str:
        """
        Retrieves the templates folder.
        :return: Such location.
        :rtype: str
        """
        return NewFileFromTemplate.templates_folder()


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

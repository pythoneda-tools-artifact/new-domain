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
from pythoneda.shared.nix.flake import (
    FlakeUtilsNixFlake,
    NixosNixFlake,
    PythonedaNixFlake,
    PythonedaSharedBannerNixFlake,
    PythonedaSharedDomainNixFlake,
)


class DefinitionNixFlake(PythonedaNixFlake):
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
        url: str,
        version: str,
        templateSubfolder: str = "pythoneda",
    ):
        """
        Creates a new DefinitionNixFlake instance.
        :param name: The repository name.
        :type name: str
        :param description: The repository description.
        :type description: str
        :param package: The Python package.
        :type package: str
        :param url: The url of the repository.
        :type url: str
        :param version: The version.
        :type version: str
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        """
        super().__init__(
            name,
            version,
            f"{url}/{{version}}",
            [
                FlakeUtilsNixFlake.default(),
                NixosNixFlake.default(),
                PythonedaSharedBannerNixFlake.default(),
                PythonedaSharedDomainNixFlake.default(),
            ],
            description,
            url,
            "B",
            "D",
            "D",
            NewFileFromTemplate.templates_folder(),
        )
        self._org = org
        self._package = package

    @property
    @attribute
    def org(self) -> str:
        """
        Retrieves the organization name.
        :return: Such name.
        :rtype: str
        """
        return self._org

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
    def name_in_snake_case(self) -> str:
        """
        Retrieves the name, in snake case.
        :return: Such value.
        :rtype: str
        """
        return self.__class__.kebab_to_snake(self.name)

    @property
    def name_in_camel_case(self) -> str:
        """
        Retrieves the name, in snake case.
        :return: Such value.
        :rtype: str
        """
        return self.__class__.kebab_to_camel(self.name)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/definition_readme.py

This file defines the Readme class.

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
from .readme import Readme


class DefinitionReadme(Readme):
    """
    Represents the README file in the definition repository.

    Class name: DefinitionReadme

    Responsibilities:
        - Model a README file.
        - Know how to create a new README from templates.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.NewFileFromTemplate
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
        Creates a new DefinitionReadme instance.
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
            org,
            name,
            description,
            package,
            defOrg,
            url,
            defUrl,
            "definition_readme",
            "DefinitionReadme",
            "README.md",
            "root",
            templateSubfolder,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

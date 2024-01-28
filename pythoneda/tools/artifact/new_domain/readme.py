# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/readme.py

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
from .new_file_from_template import NewFileFromTemplate
from pythoneda.shared import attribute


class Readme(NewFileFromTemplate):
    """
    Represents a README file.

    Class name: Readme

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
        Creates a new Readme instance.
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
            {
                "org": org,
                "name": name,
                "description": description,
                "package": package,
                "def-org": defOrg,
                "url": url,
                "def-url": defUrl,
            },
            templateSubfolder,
        )

    @property
    @attribute
    def org(self) -> str:
        """
        Retrieves the name of the organization of the domain repository.
        :return: Such information.
        :rtype: str
        """
        return self.vars["org"]

    @property
    @attribute
    def name(self) -> str:
        """
        Retrieves the name of the domain.
        :return: Such information.
        :rtype: str
        """
        return self.vars["name"]

    @property
    @attribute
    def description(self) -> str:
        """
        Retrieves the domain description.
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
        Retrieves the url of the domain repository.
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

    def template_name(self) -> str:
        """
        Retrieves the name of the stg file to use.
        :return: Such information.
        :rtype: str
        """
        return "readme"

    def output_file(self) -> str:
        """
        Retrieves the name of the output file to generate.
        :return: Such information.
        :rtype: str
        """
        return "README.md"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

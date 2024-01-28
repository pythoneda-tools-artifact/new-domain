# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/gitattributes.py

This file defines the Gitattributes class.

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


class Gitattributes(NewFileFromTemplate):
    """
    Represents a .gitattributes file.

    Class name: Gitattributes

    Responsibilities:
        - Model a .gitattributes file.
        - Know how to create a new .gitattributes from templates.

    Collaborators:
        - None
    """

    def __init__(
        self,
        defUrl: str,
        artifactUrl: str = None,
        templateSubfolder: str = "pythoneda",
    ):
        """
        Creates a new Gitattributes instance.
        :param defUrl: The url of the definition repository.
        :type defUrl: str
        :param artifactUrl: The url of the artifact repository.
        :type artifactUrl: str
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        """
        super().__init__(
            {
                "def-url": defUrl,
                "artifact-url": artifactUrl,
            },
            templateSubfolder,
        )

    @property
    @attribute
    def def_url(self) -> str:
        """
        Retrieves the url of the definition repository.
        :return: Such information.
        :rtype: str
        """
        return self.vars["def-url"]

    @property
    @attribute
    def artifact_url(self) -> str:
        """
        Retrieves the url of the artifact repository.
        :return: Such information.
        :rtype: str
        """
        return self.vars["artifact-url"]

    def template_name(self) -> str:
        """
        Retrieves the name of the stg file to use.
        :return: Such information.
        :rtype: str
        """
        return "gitattributes"

    def output_file(self) -> str:
        """
        Retrieves the name of the output file to generate.
        :return: Such information.
        :rtype: str
        """
        return ".gitattributes"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

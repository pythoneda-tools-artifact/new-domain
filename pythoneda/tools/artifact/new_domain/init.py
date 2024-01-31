# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/init.py

This file defines the Init class.

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


class Init(NewFileFromTemplate):
    """
    Represents a __init__.py file.

    Class name: Init

    Responsibilities:
        - Model a __init__.py file.
        - Know how to create a new __init__.py from templates.

    Collaborators:
        - None
    """

    def __init__(
        self,
        org: str,
        name: str,
        package: str,
        path: str,
        year: int,
        templateSubfolder: str = "pythoneda",
    ):
        """
        Creates a new Init instance.
        :param org: The name of the organization.
        :type org: str
        :param name: The name of the repository.
        :type name: str
        :param package: The Python package.
        :type package: str
        :param path: The relative path of the __init__.py file.
        :type path: str
        :param year: The year.
        :type year: int
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        """
        super().__init__(
            {"org": org, "name": name, "package": package, "path": path, "year": year},
            "init",
            "Init",
            "__init__.py",
            "root",
            templateSubfolder,
        )

    @property
    @attribute
    def org(self) -> str:
        """
        Retrieves the name of the organization.
        :return: Such name.
        :rtype: str
        """
        return self.vars["org"]

    @property
    @attribute
    def name(self) -> str:
        """
        Retrieves the name of the repository.
        :return: Such name.
        :rtype: str
        """
        return self.vars["name"]

    @property
    @attribute
    def package(self) -> str:
        """
        Retrieves the package of the Init file
        :return: Such information.
        :rtype: str
        """
        return self.vars["package"]

    @property
    @attribute
    def path(self) -> str:
        """
        Retrieves the path of the Init file
        :return: Such information.
        :rtype: str
        """
        return self.vars["path"]

    @property
    @attribute
    def year(self) -> int:
        """
        Retrieves the year.
        :return: Such information.
        :rtype: str
        """
        return self.vars["year"]


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

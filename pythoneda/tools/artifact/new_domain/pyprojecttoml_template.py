# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/pyprojecttoml_template.py

This file defines the PyprojecttomlTemplate class.

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
from pythoneda.shared.nix.flake import NixFlake


class PyprojecttomlTemplate(NewFileFromTemplate):
    """
    Represents a pyprojecttoml.template file.

    Class name: PyprojecttomlTemplate

    Responsibilities:
        - Model a pyproject.toml file.
        - Know how to create a new PyprojecttomlTemplate from templates.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.NewFileFromTemplate
    """

    def __init__(
        self,
        flake: NixFlake,
        templateSubfolder: str = "pythoneda",
    ):
        """
        Creates a new PyprojecttomlTemplate instance.
        :param flake: The associated flake.nix file.
        :type flake: pythoneda.shared.nix.flake.NixFlake
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        """
        super().__init__(
            {
                "flake": flake,
            },
            "pyprojecttoml_template",
            "PyprojecttomlTemplate",
            "pyprojecttoml.template",
            "root",
            templateSubfolder,
        )

    @property
    @attribute
    def flake(self) -> NixFlake:
        """
        Retrieves the flake.nix instance.
        :return: Such instance.
        :rtype: pythoneda.shared.nix.flake.NixFlake
        """
        return self.vars["flake"]


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

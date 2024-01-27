# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/readme.py

This file defines the Readme class.

Copyright (C) 2023-today rydnr's pythoneda-tools-artifact/new-domain

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
import asyncio
import os
from pathlib import Path
from pythoneda.shared import attribute, Entity
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryCreated,
    DefinitionRepositoryRequested,
    DomainRepositoryCreated,
    DomainRepositoryGitattributesCreated,
    DomainRepositoryGitattributesRequested,
    DomainRepositoryGitignoreCreated,
    DomainRepositoryGitignoreRequested,
    DomainRepositoryRequested,
    DomainRepositoryReadmeCreated,
    DomainRepositoryReadmeRequested,
    NewDomainCreated,
    NewDomainRequested,
)
from stringtemplate3 import PathGroupLoader, StringTemplateGroup
from typing import List


class Readme(Entity):
    """
    Represents a README file.

    Class name: Readme

    Responsibilities:
        - Model a README file.
        - Know how to create a new README from templates.

    Collaborators:
        - None
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
        Creates a new README instance.
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
        super().__init__()
        self._org = org
        self._name = name
        self._description = description
        self._package = package
        self._def_org = defOrg
        self._url = url
        self._def_url = defUrl
        self._template_subfolder = templateSubfolder

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
    def description(self) -> str:
        """
        Retrieves the domain description.
        :return: Such information.
        :rtype: str
        """
        return self._description

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

    @property
    @attribute
    def template_subfolder(self) -> str:
        """
        Retrieves the template subfolder, if any.
        :return: Such subfolder.
        :rtype: str
        """
        return self._template_subfolder

    def parent_folder(self, path: str) -> str:
        """
        Retrieves the parent folder of given path.
        :param path: The path.
        :type path: str
        :return: The parent folder.
        :rtype: str
        """
        return os.path.dirname(path)

    def templates_folder(self) -> str:
        """
        Retrieves the templates folder.
        :return: Such location.
        :rtype: str
        """
        return (
            Path(
                self.parent_folder(
                    self.parent_folder(
                        self.parent_folder(
                            self.parent_folder(self.parent_folder(__file__))
                        )
                    )
                )
            )
            / "templates"
        )

    def generate(self, outputFolder: str):
        """
        Generates the file from a template.
        :param outputFolder: The output folder.
        :type outputFolder: str
        """
        self.process_template(
            outputFolder,
            "readme",
            Path(self.templates_folder()) / self.template_subfolder,
            "root",
            "README.md",
        )

    def process_template(
        self,
        outputFolder: str,
        groupName: str,
        templateFolder: str,
        rootTemplate: str,
        outputFileName: str,
    ):
        """
        Processes a template.
        :param outputFolder: The output folder.
        :type outputFolder: str
        :param groupName: The name of the stringtemplate group.
        :type groupName: str
        :param templateFolder: The subfolder with the templates.
        :type templateFolder: str
        :param rootTemplate: The root template.
        :type rootTemplate: str
        :param outputFileName: The name of the generated file.
        :type outputFileName: str
        """
        # Manually read the .stg file
        with open(
            Path(templateFolder) / f"{groupName}.stg", "r", encoding="utf-8"
        ) as f:
            # Create a group from the string content
            group = StringTemplateGroup(
                name=groupName, file=f, rootDir=str(templateFolder)
            )

            root_template = group.getInstanceOf("root")
            root_template["readme"] = self

        with open(Path("/tmp/debug") / outputFileName, "w") as output_file:
            output_file.write(str(root_template))

        with open(Path(outputFolder) / outputFileName, "w") as output_file:
            output_file.write(str(root_template))


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

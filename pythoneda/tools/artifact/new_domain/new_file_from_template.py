# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/new_file_from_template.py

This file defines the NewFileFromTemplate class.

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
import os
from pathlib import Path
from pythoneda.shared import attribute, Entity
from stringtemplate3 import PathGroupLoader, StringTemplateGroup
from typing import Dict


class NewFileFromTemplate(Entity):
    """
    A new file whose contents are generated from a StringTemplate template.

    Class name: NewFileFromTemplate

    Responsibilities:
        - Know how to create a new file from a templates.

    Collaborators:
        - None
    """

    def __init__(
        self,
        vars: Dict,
        templateName: str,
        templateGroup: str,
        outputFile: str,
        rootTemplate: str = "root",
        templateSubfolder: str = "pythoneda",
    ):
        """
        Creates a new NewFileFromTemplate instance.
        :param vars: The dynamic content used by the template.
        :type vars: Dict
        :param templateName: The name of the template file.
        :type templateName: str
        :param templateGroup: The name of the template group.
        :type templateGroup: str
        :param outputFile: The output file.
        :type outputFile: str
        :param rootTemplate: The root template.
        :type rootTemplate: str
        :param templateSubfolder: The template subfolder, if any.
        :type templateSubfolder: str
        """
        super().__init__()
        self._vars = vars
        self._template_name = templateName
        self._template_group = templateGroup
        self._output_file = outputFile
        self._root_template = rootTemplate
        self._template_subfolder = templateSubfolder

    @property
    @attribute
    def vars(self) -> Dict:
        """
        Retrieves the dynamic content.
        :return: Such information.
        :rtype: Dict
        """
        return self._vars

    @property
    @attribute
    def template_subfolder(self) -> str:
        """
        Retrieves the template subfolder, if any.
        :return: Such subfolder.
        :rtype: str
        """
        return self._template_subfolder

    @classmethod
    def parent_folder(cls, path: str) -> str:
        """
        Retrieves the parent folder of given path.
        :param path: The path.
        :type path: str
        :return: The parent folder.
        :rtype: str
        """
        return os.path.dirname(path)

    @classmethod
    def templates_folder(cls) -> str:
        """
        Retrieves the templates folder.
        :return: Such location.
        :rtype: str
        """
        return (
            Path(
                cls.parent_folder(
                    cls.parent_folder(
                        cls.parent_folder(
                            cls.parent_folder(cls.parent_folder(__file__))
                        )
                    )
                )
            )
            / "templates"
        )

    @property
    def template_name(self) -> str:
        """
        Retrieves the name of the stg file to use.
        :return: Such information.
        :rtype: str
        """
        return self._template_name

    @property
    def template_group(self) -> str:
        """
        Retrieves the name of the template group.
        :return: Such information.
        :rtype: str
        """
        return self._template_group

    @property
    def output_file(self) -> str:
        """
        Retrieves the name of the output file to generate.
        :return: Such information.
        :rtype: str
        """
        return self._output_file

    @property
    def root_template(self) -> str:
        """
        Retrieves the name of the root template.
        :return: Such information.
        :rtype: str
        """
        return self._root_template

    def generate(self, outputFolder: str) -> str:
        """
        Generates the file from a template.
        :param outputFolder: The output folder.
        :type outputFolder: str
        :return: The generated file.
        :rtype: str
        """
        self.process_template(
            outputFolder,
            self.template_name,
            self.template_group,
            Path(self.__class__.templates_folder()) / self.template_subfolder,
            self.output_file,
            self.root_template,
        )
        return Path(outputFolder) / self.output_file

    def process_template(
        self,
        outputFolder: str,
        templateName: str,
        templateGroup: str,
        templateFolder: str,
        outputFileName: str,
        rootTemplate: str,
    ):
        """
        Processes a template.
        :param outputFolder: The output folder.
        :type outputFolder: str
        :param templateName: The name of the stringtemplate template.
        :type templateName: str
        :param templateGroup: The name of the stringtemplate group.
        :type templateGroup: str
        :param templateFolder: The subfolder with the templates.
        :type templateFolder: str
        :param rootTemplate: The root template.
        :type rootTemplate: str
        :param outputFileName: The name of the generated file.
        :type outputFileName: str
        """
        # Manually read the .stg file
        with open(
            Path(templateFolder) / f"{templateName}.stg", "r", encoding="utf-8"
        ) as f:
            # Create a group from the string content
            group = StringTemplateGroup(
                name=templateGroup, file=f, rootDir=str(templateFolder)
            )

            root = group.getInstanceOf(rootTemplate)
            root[templateName] = self

        with open(Path(outputFolder) / outputFileName, "w") as output_file:
            output_file.write(str(root))


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

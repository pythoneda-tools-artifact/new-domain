# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/update_sha256_in_definition_repository_nix_flake.py

This file defines the UpdateSha256InDefinitionRepositoryNixFlake class.

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
from pythoneda.shared import EventListener, listen
from pythoneda.shared.git import GitAdd
from pythoneda.shared.nix.flake import NixFlake
from pythoneda.tools.artifact.new_domain.events import (
    Sha256InDefinitionRepositoryNixFlakeUpdated,
    UpdateSha256InDefinitionRepositoryNixFlakeRequested,
)
from .definition_nix_flake import DefinitionNixFlake
from typing import List


class UpdateSha256InDefinitionRepositoryNixFlake(EventListener):
    """
    Updates the sha256 value of the flake.nix file in the definition repository.

    Class name: UpdateSha256InDefinitionRepositoryNixFlake

    Responsibilities:
        - Know the steps required to update the sha256 of the flake.nix file in the new definition repository.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.Sha256InDefinitionRepositoryNixFlakeUpdated
        - pythoneda.tools.artifact.new_domain.events.UpdateSha256InDefinitionRepositoryNixFlakeRequested
    """

    _token = None

    def __init__(self):
        """
        UpdateSha256Ins a new UpdateSha256InDefinitionRepositoryNixFlake instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.tools.artifact.new_domain.UpdateSha256InDefinitionRepositoryNixFlake
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(UpdateSha256InDefinitionRepositoryNixFlakeRequested)
    async def listen_UpdateSha256InDefinitionRepositoryNixFlakeRequested(
        cls, event: UpdateSha256InDefinitionRepositoryNixFlakeRequested
    ) -> Sha256InDefinitionRepositoryNixFlakeUpdated:
        """
        Updates the sha256 checksum  in the Nix flake of the definition repository.
        :param event: The trigger event.
        :type event: pythoneda.tools.artifact.new_domain.events.UpdateSha256InDefinitionRepositoryNixFlakeRequested
        :return: The event representing the checksum has been updated.
        :rtype: pythoneda.tools.artifact.new_domain.events.Sha256InDefinitionRepositoryNixFlakeUpdated
        """
        url = event.context["url"]
        version = event.context["version"]
        repo_folder = event.context["def-repo-folder"]
        sha256 = await NixFlake.fetch_sha256(url, version)
        await NixFlake.update_sha256(sha256, repo_folder)
        await GitAdd(repo_folder).add("flake.nix")
        return Sha256InDefinitionRepositoryNixFlakeUpdated(
            event.org,
            event.name,
            event.description,
            event.package,
            event.github_token,
            event.gpg_key_id,
            event.context,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

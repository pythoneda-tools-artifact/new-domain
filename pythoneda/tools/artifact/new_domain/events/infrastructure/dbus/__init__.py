# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/infrastructure/dbus/__init__.py

This file ensures pythoneda.tools.artifact.new_domain.events.infrastructure.dbus is a namespace.

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

DBUS_PATH = "/pythoneda/tools/artifact/new_domain"

from .dbus_new_domain_event import DbusNewDomainEvent
from .dbus_definition_repository_changes_pushed import (
    DbusDefinitionRepositoryChangesPushed,
)
from .dbus_definition_repository_created import DbusDefinitionRepositoryCreated
from .dbus_definition_repository_flake_lock_created import (
    DbusDefinitionRepositoryFlakeLockCreated,
)
from .dbus_definition_repository_nix_flake_created import (
    DbusDefinitionRepositoryNixFlakeCreated,
)
from .dbus_definition_repository_nix_flake_requested import (
    DbusDefinitionRepositoryNixFlakeRequested,
)
from .dbus_definition_repository_pyprojecttoml_template_created import (
    DbusDefinitionRepositoryPyprojecttomlTemplateCreated,
)
from .dbus_definition_repository_pyprojecttoml_template_requested import (
    DbusDefinitionRepositoryPyprojecttomlTemplateRequested,
)
from .dbus_definition_repository_readme_created import (
    DbusDefinitionRepositoryReadmeCreated,
)
from .dbus_definition_repository_readme_requested import (
    DbusDefinitionRepositoryReadmeRequested,
)
from .dbus_definition_repository_requested import DbusDefinitionRepositoryRequested
from .dbus_domain_repository_changes_pushed import DbusDomainRepositoryChangesPushed
from .dbus_domain_repository_created import DbusDomainRepositoryCreated
from .dbus_domain_repository_gitattributes_created import (
    DbusDomainRepositoryGitattributesCreated,
)
from .dbus_domain_repository_gitattributes_requested import (
    DbusDomainRepositoryGitattributesRequested,
)
from .dbus_domain_repository_gitignore_created import (
    DbusDomainRepositoryGitignoreCreated,
)
from .dbus_domain_repository_gitignore_requested import (
    DbusDomainRepositoryGitignoreRequested,
)
from .dbus_domain_repository_readme_created import DbusDomainRepositoryReadmeCreated
from .dbus_domain_repository_readme_requested import DbusDomainRepositoryReadmeRequested
from .dbus_domain_repository_requested import DbusDomainRepositoryRequested
from .dbus_new_domain_created import DbusNewDomainCreated
from .dbus_new_domain_requested import DbusNewDomainRequested

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

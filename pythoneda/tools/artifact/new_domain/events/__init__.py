# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/events/__init__.py

This file ensures pythoneda.tools.artifact.new_domain.events is a namespace.

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

from .new_domain_event import NewDomainEvent
from .definition_repository_changes_pushed import DefinitionRepositoryChangesPushed
from .definition_repository_created import DefinitionRepositoryCreated
from .definition_repository_nix_flake_created import DefinitionRepositoryNixFlakeCreated
from .definition_repository_nix_flake_requested import (
    DefinitionRepositoryNixFlakeRequested,
)
from .definition_repository_pyprojecttoml_template_created import (
    DefinitionRepositoryPyprojecttomlTemplateCreated,
)
from .definition_repository_pyprojecttoml_template_requested import (
    DefinitionRepositoryPyprojecttomlTemplateRequested,
)
from .definition_repository_readme_created import DefinitionRepositoryReadmeCreated
from .definition_repository_readme_requested import DefinitionRepositoryReadmeRequested
from .definition_repository_requested import DefinitionRepositoryRequested
from .domain_repository_changes_pushed import DomainRepositoryChangesPushed
from .domain_repository_created import DomainRepositoryCreated
from .domain_repository_gitattributes_created import (
    DomainRepositoryGitattributesCreated,
)
from .domain_repository_gitattributes_requested import (
    DomainRepositoryGitattributesRequested,
)
from .domain_repository_gitignore_created import (
    DomainRepositoryGitignoreCreated,
)
from .domain_repository_gitignore_requested import (
    DomainRepositoryGitignoreRequested,
)
from .domain_repository_readme_created import DomainRepositoryReadmeCreated
from .domain_repository_readme_requested import DomainRepositoryReadmeRequested
from .domain_repository_requested import DomainRepositoryRequested
from .new_domain_created import NewDomainCreated
from .new_domain_requested import NewDomainRequested

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

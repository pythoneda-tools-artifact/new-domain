# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/new_domain/infrastructure/dbus/signals.py

This file defines the Signals class.

Copyright (C) 2024-today boot's pythoneda-tools-artifact/new-domain

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
from dbus_next import BusType
from pythoneda.tools.artifact.new_domain.events import (
    DefinitionRepositoryChangesCommitted,
    DefinitionRepositoryChangesPushed,
    DefinitionRepositoryChangesTagged,
    DefinitionRepositoryCloned,
    DefinitionRepositoryCloneRequested,
    DefinitionRepositoryCommitRequested,
    DefinitionRepositoryCreated,
    DefinitionRepositoryFlakeLockCreated,
    DefinitionRepositoryFlakeLockRequested,
    DefinitionRepositoryNixFlakeCreated,
    DefinitionRepositoryNixFlakeRequested,
    DefinitionRepositoryPyprojecttomlTemplateCreated,
    DefinitionRepositoryPyprojecttomlTemplateRequested,
    DefinitionRepositoryPushRequested,
    DefinitionRepositoryReadmeCreated,
    DefinitionRepositoryReadmeRequested,
    DefinitionRepositoryRequested,
    DefinitionRepositoryTagRequested,
    DomainRepositoryChangesCommitted,
    DomainRepositoryChangesPushed,
    DomainRepositoryChangesTagged,
    DomainRepositoryCloned,
    DomainRepositoryCloneRequested,
    DomainRepositoryCommitRequested,
    DomainRepositoryCreated,
    DomainRepositoryGitattributesCreated,
    DomainRepositoryGitattributesRequested,
    DomainRepositoryGitignoreCreated,
    DomainRepositoryGitignoreRequested,
    DomainRepositoryPushRequested,
    DomainRepositoryReadmeCreated,
    DomainRepositoryReadmeRequested,
    DomainRepositoryRequested,
    DomainRepositoryTagRequested,
    NewDomainCreated,
    NewDomainRequested,
    Sha256InDefinitionRepositoryNixFlakeUpdated,
    UpdateSha256InDefinitionRepositoryNixFlakeRequested,
)
from pythoneda.tools.artifact.new_domain.events.infrastructure.dbus import (
    DbusDefinitionRepositoryChangesCommitted,
    DbusDefinitionRepositoryChangesPushed,
    DbusDefinitionRepositoryChangesTagged,
    DbusDefinitionRepositoryCloned,
    DbusDefinitionRepositoryCloneRequested,
    DbusDefinitionRepositoryCommitRequested,
    DbusDefinitionRepositoryCreated,
    DbusDefinitionRepositoryFlakeLockCreated,
    DbusDefinitionRepositoryFlakeLockRequested,
    DbusDefinitionRepositoryNixFlakeCreated,
    DbusDefinitionRepositoryNixFlakeRequested,
    DbusDefinitionRepositoryPyprojecttomlTemplateCreated,
    DbusDefinitionRepositoryPyprojecttomlTemplateRequested,
    DbusDefinitionRepositoryReadmeCreated,
    DbusDefinitionRepositoryReadmeRequested,
    DbusDefinitionRepositoryRequested,
    DbusDomainRepositoryChangesCommitted,
    DbusDomainRepositoryChangesPushed,
    DbusDomainRepositoryChangesTagged,
    DbusDomainRepositoryCloneRequested,
    DbusDomainRepositoryCommitRequested,
    DbusDomainRepositoryCreated,
    DbusDomainRepositoryGitattributesCreated,
    DbusDomainRepositoryGitattributesRequested,
    DbusDomainRepositoryGitignoreCreated,
    DbusDomainRepositoryGitignoreRequested,
    DbusDomainRepositoryReadmeCreated,
    DbusDomainRepositoryReadmeRequested,
    DbusDomainRepositoryRequested,
    DbusDomainRepositoryTagRequested,
    DbusNewDomainCreated,
    DbusNewDomainRequested,
    DbusSha256InDefinitionRepositoryNixFlakeUpdated,
    DbusUpdateSha256InDefinitionRepositoryNixFlakeRequested,
)
from pythoneda.shared import BaseObject
from typing import Dict


class Signals(BaseObject):

    """
    Defines the new-domain d-bus signals.

    Class name: Signals

    Responsibilities:
        - Provide the d-bus signals.

    Collaborators:
        - pythoneda.tools.artifact.new_domain.events.infrastructure.dbus.*
    """

    def __init__(self):
        """
        Creates a new Signals instance.
        """
        super().__init__()

    @classmethod
    def signals(self) -> Dict:
        """
        Retrieves the signals.
        :return: A dictionary with the domain event class name as key, and a tuple of the dbus class and the bus type as value.
        :rtype: Dict
        """
        result = {}
        key = self.__class__.full_class_name(DefinitionRepositoryChangesCommitted)
        result[key] = [DbusDefinitionRepositoryChangesCommitted, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryChangesPushed)
        result[key] = [DbusDefinitionRepositoryChangesPushed, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryChangesTagged)
        result[key] = [DbusDefinitionRepositoryChangesTagged, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryCloned)
        result[key] = [DbusDefinitionRepositoryCloned, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryCloneRequested)
        result[key] = [DbusDefinitionRepositoryCloneRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryCommitRequested)
        result[key] = [DbusDefinitionRepositoryCommitRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryCreated)
        result[key] = [DbusDefinitionRepositoryCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryFlakeLockCreated)
        result[key] = [DbusDefinitionRepositoryFlakeLockCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryFlakeLockRequested)
        result[key] = [DbusDefinitionRepositoryFlakeLockRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryNixFlakeCreated)
        result[key] = [DbusDefinitionRepositoryNixFlakeCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryNixFlakeRequested)
        result[key] = [DbusDefinitionRepositoryNixFlakeRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(
            DefinitionRepositoryPyprojecttomlTemplateCreated
        )
        result[key] = [
            DbusDefinitionRepositoryPyprojecttomlTemplateCreated,
            BusType.SYSTEM,
        ]
        key = self.__class__.full_class_name(
            DefinitionRepositoryPyprojecttomlTemplateRequested
        )
        result[key] = [
            DbusDefinitionRepositoryPyprojecttomlTemplateRequested,
            BusType.SYSTEM,
        ]
        key = self.__class__.full_class_name(DefinitionRepositoryPushRequested)
        result[key] = [DbusDefinitionRepositoryPushRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryReadmeCreated)
        result[key] = [DbusDefinitionRepositoryReadmeCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryReadmeRequested)
        result[key] = [DbusDefinitionRepositoryReadmeRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryRequested)
        result[key] = [DbusDefinitionRepositoryRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DefinitionRepositoryTagRequested)
        result[key] = [DbusDefinitionRepositoryTagRequested, BusType.SYSTEM]

        key = self.__class__.full_class_name(DomainRepositoryChangesCommitted)
        result[key] = [DbusDomainRepositoryChangesCommitted, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryChangesPushed)
        result[key] = [DbusDomainRepositoryChangesPushed, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryChangesTagged)
        result[key] = [DbusDomainRepositoryChangesTagged, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryCloned)
        result[key] = [DbusDomainRepositoryCloned, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryCloneRequested)
        result[key] = [DbusDomainRepositoryCloneRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryCommitRequested)
        result[key] = [DbusDomainRepositoryCommitRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryCreated)
        result[key] = [DbusDomainRepositoryCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryGitattributesCreated)
        result[key] = [DbusDomainRepositoryGitattributesCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryGitattributesRequested)
        result[key] = [DbusDomainRepositoryGitattributesRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryGitignoreCreated)
        result[key] = [DbusDomainRepositoryGitignoreCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryGitignoreRequested)
        result[key] = [DbusDomainRepositoryGitignoreRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryPushRequested)
        result[key] = [DbusDomainRepositoryPushRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryReadmeCreated)
        result[key] = [DbusDomainRepositoryReadmeCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryReadmeRequested)
        result[key] = [DbusDomainRepositoryReadmeRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryRequested)
        result[key] = [DbusDomainRepositoryRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(DomainRepositoryTagRequested)
        result[key] = [DbusDomainRepositoryTagRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(NewDomainCreated)
        result[key] = [DbusNewDomainCreated, BusType.SYSTEM]
        key = self.__class__.full_class_name(NewDomainRequested)
        result[key] = [DbusNewDomainRequested, BusType.SYSTEM]
        key = self.__class__.full_class_name(
            UpdateSha256InDefinitionRepositoryNixFlakeRequested
        )
        result[key] = [
            DbusUpdateSha256InDefinitionRepositoryNixFlakeRequested,
            BusType.SYSTEM,
        ]
        key = self.__class__.full_class_name(
            Sha256InDefinitionRepositoryNixFlakeUpdated
        )
        result[key] = [DbusSha256InDefinitionRepositoryNixFlakeUpdated, BusType.SYSTEM]

        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:

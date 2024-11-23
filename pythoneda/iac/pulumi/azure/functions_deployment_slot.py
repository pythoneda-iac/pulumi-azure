# vim: set fileencoding=utf-8
"""
pythoneda/iac/pulumi/azure/functions_deployment_slot.py

This script defines the FunctionsDeploymentSlot class.

Copyright (C) 2024-today pythoneda's IaC Pulumi

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
from .resource_group import ResourceGroup
from .web_app import WebApp
from .web_app_deployment_slot import WebAppDeploymentSlot
import pulumi
import pulumi_azure_native


class FunctionsDeploymentSlot(WebAppDeploymentSlot):
    """
    Logic to define Licdata's functions deployment slots in Azure Webapps.

    Class name: FunctionsDeploymentSlot

    Responsibilities:
        - Deployment slots for Licdata functions.

    Collaborators:
        - None
    """

    def __init__(
        self,
        webApp: WebApp,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new WebAppDeploymentSlot instance.
        :param webApp: The web app.
        :type webApp: pythoneda.iac.pulumi.azure.WebApp
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pulumi_azure_native.resources.ResourceGroup
        """
        super().__init__("license_functions", "./rest.zip", webApp, resourceGroup)

    # @override
    def _resource_name(self, stackName: str, projectName: str, location: str) -> str:
        """
        Builds the resource name.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :return: The resource name.
        :rtype: str
        """
        return "dsf"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et

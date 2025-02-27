# Copyright 2022 Qiskit on IQM developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Qiskit Backend Provider for IQM backends.
"""
import json

from iqm_client.iqm_client import IQMClient

from qiskit_iqm.iqm_backend import IQMBackend


class IQMProvider:
    """Provider for IQM backends.

    Args:
        url: URL of the IQM Cortex server
        settings_path: path to the JSON settings file for the IQM backend, or None (default) to use latest
                       calibration data available

    Keyword Args:
        auth_server_url: URL of the user authentication server, if required by the IQM Cortex server.
            Can also be set in the ``IQM_AUTH_SERVER`` environment variable.
        username: Username, if required by the IQM Cortex server.
            Can also be set in the ``IQM_AUTH_USERNAME`` environment variable.
        password: Password, if required by the IQM Cortex server.
            Can also be set in the ``IQM_AUTH_PASSWORD`` environment variable.
    """
    def __init__(
            self,
            url: str,
            settings_path: str = None,
            **user_auth_args  # contains keyword args auth_server_url, username, password
    ):
        self.url = url
        self.settings_path = settings_path
        self.user_auth_args = user_auth_args

    def get_backend(self) -> IQMBackend:
        """An IQMBackend instance associated with this provider.
        """
        settings = None
        if self.settings_path:
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings = json.loads(f.read())
        client = IQMClient(self.url, settings, **self.user_auth_args)
        return IQMBackend(client)

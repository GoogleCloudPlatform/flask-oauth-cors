#!/usr/bin/python3
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.oauth2 import id_token
from google.auth.transport import requests

class Auth:
    def __init__(self, oauth_client_id, cors_allow_origin = "*", cors_allow_methods = "*", cors_allow_headers = "*", cors_max_age = "*"):
        self.__oauth_client_id = oauth_client_id
        self.__cors_allow_origin = cors_allow_origin
        self.__cors_allow_methods = cors_allow_methods
        self.__cors_allow_headers = cors_allow_headers
        self.__cors_max_age = cors_max_age

    def get_id_info(self, request):
        # Set CORS headers for the preflight request
        if request.method == 'OPTIONS':
            # Allows GET requests from any origin with the Content-Type
            # header and caches preflight response for an 3600s
            headers = {
                'Access-Control-Allow-Origin': self.__cors_allow_origin,
                'Access-Control-Allow-Methods': self.__cors_allow_methods,
                'Access-Control-Allow-Headers': self.__cors_allow_headers,
                'Access-Control-Max-Age': self.__cors_max_age,
                'Access-Control-Allow-Credentials': 'true'
            }
            self.__response = ('', 204, headers)
            return None

        token = request.headers['Authorization'].split(' ').pop()
        auth_request = requests.Request()
        id_info = id_token.verify_oauth2_token(token, auth_request, self.__oauth_client_id)
        if not id_info:
            self.__response = ('Unauthorized', 401, headers)
            return None
        return id_info

    def get_response(self):
        return self.__response

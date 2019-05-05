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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcloud-flask-oauth-cors",
    version="0.1.1",
    author="Jez Humble",
    author_email="humble@google.com",
    description="A tiny utility to authenticate requests using GCP OAuth and send CORS headers in Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/googlecloudplatform/flask-oauth-cors",
    install_requires=[
        "google-api-python-client",
        "google-auth"
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

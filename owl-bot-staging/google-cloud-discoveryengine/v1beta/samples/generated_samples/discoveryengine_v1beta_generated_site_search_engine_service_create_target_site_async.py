# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateTargetSite
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-discoveryengine


# [START discoveryengine_v1beta_generated_SiteSearchEngineService_CreateTargetSite_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import discoveryengine_v1beta


async def sample_create_target_site():
    # Create a client
    client = discoveryengine_v1beta.SiteSearchEngineServiceAsyncClient()

    # Initialize request argument(s)
    target_site = discoveryengine_v1beta.TargetSite()
    target_site.provided_uri_pattern = "provided_uri_pattern_value"

    request = discoveryengine_v1beta.CreateTargetSiteRequest(
        parent="parent_value",
        target_site=target_site,
    )

    # Make the request
    operation = client.create_target_site(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END discoveryengine_v1beta_generated_SiteSearchEngineService_CreateTargetSite_async]

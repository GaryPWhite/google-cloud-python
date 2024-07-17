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
from collections import OrderedDict
import functools
import re
from typing import Dict, Callable, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union

from google.cloud.discoveryengine_v1beta import gapic_version as package_version

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore


try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.discoveryengine_v1beta.services.sample_query_set_service import pagers
from google.cloud.discoveryengine_v1beta.types import sample_query_set
from google.cloud.discoveryengine_v1beta.types import sample_query_set as gcd_sample_query_set
from google.cloud.discoveryengine_v1beta.types import sample_query_set_service
from google.cloud.location import locations_pb2 # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import SampleQuerySetServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import SampleQuerySetServiceGrpcAsyncIOTransport
from .client import SampleQuerySetServiceClient


class SampleQuerySetServiceAsyncClient:
    """Service for managing
    [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]s,
    """

    _client: SampleQuerySetServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SampleQuerySetServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SampleQuerySetServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SampleQuerySetServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SampleQuerySetServiceClient._DEFAULT_UNIVERSE

    location_path = staticmethod(SampleQuerySetServiceClient.location_path)
    parse_location_path = staticmethod(SampleQuerySetServiceClient.parse_location_path)
    sample_query_set_path = staticmethod(SampleQuerySetServiceClient.sample_query_set_path)
    parse_sample_query_set_path = staticmethod(SampleQuerySetServiceClient.parse_sample_query_set_path)
    common_billing_account_path = staticmethod(SampleQuerySetServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(SampleQuerySetServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(SampleQuerySetServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(SampleQuerySetServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(SampleQuerySetServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(SampleQuerySetServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(SampleQuerySetServiceClient.common_project_path)
    parse_common_project_path = staticmethod(SampleQuerySetServiceClient.parse_common_project_path)
    common_location_path = staticmethod(SampleQuerySetServiceClient.common_location_path)
    parse_common_location_path = staticmethod(SampleQuerySetServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            SampleQuerySetServiceAsyncClient: The constructed client.
        """
        return SampleQuerySetServiceClient.from_service_account_info.__func__(SampleQuerySetServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            SampleQuerySetServiceAsyncClient: The constructed client.
        """
        return SampleQuerySetServiceClient.from_service_account_file.__func__(SampleQuerySetServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return SampleQuerySetServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> SampleQuerySetServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            SampleQuerySetServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = functools.partial(type(SampleQuerySetServiceClient).get_transport_class, type(SampleQuerySetServiceClient))

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Optional[Union[str, SampleQuerySetServiceTransport, Callable[..., SampleQuerySetServiceTransport]]] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the sample query set service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SampleQuerySetServiceTransport,Callable[..., SampleQuerySetServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SampleQuerySetServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = SampleQuerySetServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def get_sample_query_set(self,
            request: Optional[Union[sample_query_set_service.GetSampleQuerySetRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> sample_query_set.SampleQuerySet:
        r"""Gets a
        [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_get_sample_query_set():
                # Create a client
                client = discoveryengine_v1beta.SampleQuerySetServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.GetSampleQuerySetRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_sample_query_set(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.GetSampleQuerySetRequest, dict]]):
                The request object. Request message for
                [SampleQuerySetService.GetSampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet]
                method.
            name (:class:`str`):
                Required. Full resource name of
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                such as
                ``projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}``.

                If the caller does not have permission to access the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the requested
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]
                does not exist, a NOT_FOUND error is returned.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.SampleQuerySet:
                A SampleQuerySet is the parent
                resource of SampleQuery, and contains
                the configurations shared by all
                SampleQuery under it.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, sample_query_set_service.GetSampleQuerySetRequest):
            request = sample_query_set_service.GetSampleQuerySetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_sample_query_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_sample_query_sets(self,
            request: Optional[Union[sample_query_set_service.ListSampleQuerySetsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListSampleQuerySetsAsyncPager:
        r"""Gets a list of
        [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_list_sample_query_sets():
                # Create a client
                client = discoveryengine_v1beta.SampleQuerySetServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.ListSampleQuerySetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_sample_query_sets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsRequest, dict]]):
                The request object. Request message for
                [SampleQuerySetService.ListSampleQuerySets][google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets]
                method.
            parent (:class:`str`):
                Required. The parent location resource name, such as
                ``projects/{project}/locations/{location}``.

                If the caller does not have permission to list
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]s
                under this location, regardless of whether or not this
                location exists, a ``PERMISSION_DENIED`` error is
                returned.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.services.sample_query_set_service.pagers.ListSampleQuerySetsAsyncPager:
                Response message for
                   [SampleQuerySetService.ListSampleQuerySets][google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets]
                   method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, sample_query_set_service.ListSampleQuerySetsRequest):
            request = sample_query_set_service.ListSampleQuerySetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.list_sample_query_sets]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListSampleQuerySetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_sample_query_set(self,
            request: Optional[Union[sample_query_set_service.CreateSampleQuerySetRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            sample_query_set: Optional[gcd_sample_query_set.SampleQuerySet] = None,
            sample_query_set_id: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> gcd_sample_query_set.SampleQuerySet:
        r"""Creates a
        [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_create_sample_query_set():
                # Create a client
                client = discoveryengine_v1beta.SampleQuerySetServiceAsyncClient()

                # Initialize request argument(s)
                sample_query_set = discoveryengine_v1beta.SampleQuerySet()
                sample_query_set.display_name = "display_name_value"

                request = discoveryengine_v1beta.CreateSampleQuerySetRequest(
                    parent="parent_value",
                    sample_query_set=sample_query_set,
                    sample_query_set_id="sample_query_set_id_value",
                )

                # Make the request
                response = await client.create_sample_query_set(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.CreateSampleQuerySetRequest, dict]]):
                The request object. Request message for
                [SampleQuerySetService.CreateSampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet]
                method.
            parent (:class:`str`):
                Required. The parent resource name, such as
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            sample_query_set (:class:`google.cloud.discoveryengine_v1beta.types.SampleQuerySet`):
                Required. The
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]
                to create.

                This corresponds to the ``sample_query_set`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            sample_query_set_id (:class:`str`):
                Required. The ID to use for the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                which will become the final component of the
                [SampleQuerySet.name][google.cloud.discoveryengine.v1beta.SampleQuerySet.name].

                If the caller does not have permission to create the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                regardless of whether or not it exists, a
                ``PERMISSION_DENIED`` error is returned.

                This field must be unique among all
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]s
                with the same
                [parent][google.cloud.discoveryengine.v1beta.CreateSampleQuerySetRequest.parent].
                Otherwise, an ``ALREADY_EXISTS`` error is returned.

                This field must conform to
                `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__
                standard with a length limit of 63 characters.
                Otherwise, an ``INVALID_ARGUMENT`` error is returned.

                This corresponds to the ``sample_query_set_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.SampleQuerySet:
                A SampleQuerySet is the parent
                resource of SampleQuery, and contains
                the configurations shared by all
                SampleQuery under it.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, sample_query_set, sample_query_set_id])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, sample_query_set_service.CreateSampleQuerySetRequest):
            request = sample_query_set_service.CreateSampleQuerySetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if sample_query_set is not None:
            request.sample_query_set = sample_query_set
        if sample_query_set_id is not None:
            request.sample_query_set_id = sample_query_set_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.create_sample_query_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_sample_query_set(self,
            request: Optional[Union[sample_query_set_service.UpdateSampleQuerySetRequest, dict]] = None,
            *,
            sample_query_set: Optional[gcd_sample_query_set.SampleQuerySet] = None,
            update_mask: Optional[field_mask_pb2.FieldMask] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> gcd_sample_query_set.SampleQuerySet:
        r"""Updates a
        [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_update_sample_query_set():
                # Create a client
                client = discoveryengine_v1beta.SampleQuerySetServiceAsyncClient()

                # Initialize request argument(s)
                sample_query_set = discoveryengine_v1beta.SampleQuerySet()
                sample_query_set.display_name = "display_name_value"

                request = discoveryengine_v1beta.UpdateSampleQuerySetRequest(
                    sample_query_set=sample_query_set,
                )

                # Make the request
                response = await client.update_sample_query_set(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.UpdateSampleQuerySetRequest, dict]]):
                The request object. Request message for
                [SampleQuerySetService.UpdateSampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet]
                method.
            sample_query_set (:class:`google.cloud.discoveryengine_v1beta.types.SampleQuerySet`):
                Required. The sample query set to update.

                If the caller does not have permission to update the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                regardless of whether or not it exists, a
                ``PERMISSION_DENIED`` error is returned.

                If the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]
                to update does not exist a ``NOT_FOUND`` error is
                returned.

                This corresponds to the ``sample_query_set`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the
                provided imported 'sample query set' to
                update. If not set, will by default
                update all fields.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.SampleQuerySet:
                A SampleQuerySet is the parent
                resource of SampleQuery, and contains
                the configurations shared by all
                SampleQuery under it.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        has_flattened_params = any([sample_query_set, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, sample_query_set_service.UpdateSampleQuerySetRequest):
            request = sample_query_set_service.UpdateSampleQuerySetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if sample_query_set is not None:
            request.sample_query_set = sample_query_set
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.update_sample_query_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("sample_query_set.name", request.sample_query_set.name),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_sample_query_set(self,
            request: Optional[Union[sample_query_set_service.DeleteSampleQuerySetRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a
        [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_delete_sample_query_set():
                # Create a client
                client = discoveryengine_v1beta.SampleQuerySetServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.DeleteSampleQuerySetRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_sample_query_set(request=request)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.DeleteSampleQuerySetRequest, dict]]):
                The request object. Request message for
                [SampleQuerySetService.DeleteSampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet]
                method.
            name (:class:`str`):
                Required. Full resource name of
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                such as
                ``projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}``.

                If the caller does not have permission to delete the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet],
                regardless of whether or not it exists, a
                ``PERMISSION_DENIED`` error is returned.

                If the
                [SampleQuerySet][google.cloud.discoveryengine.v1beta.SampleQuerySet]
                to delete does not exist, a ``NOT_FOUND`` error is
                returned.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, sample_query_set_service.DeleteSampleQuerySetRequest):
            request = sample_query_set_service.DeleteSampleQuerySetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.delete_sample_query_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def list_operations(
        self,
        request: Optional[operations_pb2.ListOperationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[operations_pb2.GetOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def cancel_operation(
        self,
        request: Optional[operations_pb2.CancelOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.CancelOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.cancel_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

    async def __aenter__(self) -> "SampleQuerySetServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "SampleQuerySetServiceAsyncClient",
)

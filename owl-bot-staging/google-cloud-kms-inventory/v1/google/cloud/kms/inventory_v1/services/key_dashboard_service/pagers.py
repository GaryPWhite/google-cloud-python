# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.kms.inventory_v1.types import key_dashboard_service
from google.cloud.kms.v1 import resources_pb2  # type: ignore


class ListCryptoKeysPager:
    """A pager for iterating through ``list_crypto_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms.inventory_v1.types.ListCryptoKeysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``crypto_keys`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCryptoKeys`` requests and continue to iterate
    through the ``crypto_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms.inventory_v1.types.ListCryptoKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., key_dashboard_service.ListCryptoKeysResponse],
            request: key_dashboard_service.ListCryptoKeysRequest,
            response: key_dashboard_service.ListCryptoKeysResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms.inventory_v1.types.ListCryptoKeysRequest):
                The initial request object.
            response (google.cloud.kms.inventory_v1.types.ListCryptoKeysResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = key_dashboard_service.ListCryptoKeysRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[key_dashboard_service.ListCryptoKeysResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resources_pb2.CryptoKey]:
        for page in self.pages:
            yield from page.crypto_keys

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListCryptoKeysAsyncPager:
    """A pager for iterating through ``list_crypto_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms.inventory_v1.types.ListCryptoKeysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``crypto_keys`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCryptoKeys`` requests and continue to iterate
    through the ``crypto_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms.inventory_v1.types.ListCryptoKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[key_dashboard_service.ListCryptoKeysResponse]],
            request: key_dashboard_service.ListCryptoKeysRequest,
            response: key_dashboard_service.ListCryptoKeysResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms.inventory_v1.types.ListCryptoKeysRequest):
                The initial request object.
            response (google.cloud.kms.inventory_v1.types.ListCryptoKeysResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = key_dashboard_service.ListCryptoKeysRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[key_dashboard_service.ListCryptoKeysResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[resources_pb2.CryptoKey]:
        async def async_generator():
            async for page in self.pages:
                for response in page.crypto_keys:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)

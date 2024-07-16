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
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.discoveryengine_v1alpha.types import sample_query
from google.cloud.discoveryengine_v1alpha.types import sample_query_service


class ListSampleQueriesPager:
    """A pager for iterating through ``list_sample_queries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sample_queries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSampleQueries`` requests and continue to iterate
    through the ``sample_queries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., sample_query_service.ListSampleQueriesResponse],
            request: sample_query_service.ListSampleQueriesRequest,
            response: sample_query_service.ListSampleQueriesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesRequest):
                The initial request object.
            response (google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = sample_query_service.ListSampleQueriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[sample_query_service.ListSampleQueriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[sample_query.SampleQuery]:
        for page in self.pages:
            yield from page.sample_queries

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListSampleQueriesAsyncPager:
    """A pager for iterating through ``list_sample_queries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``sample_queries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSampleQueries`` requests and continue to iterate
    through the ``sample_queries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[sample_query_service.ListSampleQueriesResponse]],
            request: sample_query_service.ListSampleQueriesRequest,
            response: sample_query_service.ListSampleQueriesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesRequest):
                The initial request object.
            response (google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = sample_query_service.ListSampleQueriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[sample_query_service.ListSampleQueriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[sample_query.SampleQuery]:
        async def async_generator():
            async for page in self.pages:
                for response in page.sample_queries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)

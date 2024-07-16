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

from google.cloud.discoveryengine_v1alpha.types import evaluation
from google.cloud.discoveryengine_v1alpha.types import evaluation_service


class ListEvaluationsPager:
    """A pager for iterating through ``list_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., evaluation_service.ListEvaluationsResponse],
            request: evaluation_service.ListEvaluationsRequest,
            response: evaluation_service.ListEvaluationsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.discoveryengine_v1alpha.types.ListEvaluationsRequest):
                The initial request object.
            response (google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = evaluation_service.ListEvaluationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[evaluation.Evaluation]:
        for page in self.pages:
            yield from page.evaluations

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEvaluationsAsyncPager:
    """A pager for iterating through ``list_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[evaluation_service.ListEvaluationsResponse]],
            request: evaluation_service.ListEvaluationsRequest,
            response: evaluation_service.ListEvaluationsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.discoveryengine_v1alpha.types.ListEvaluationsRequest):
                The initial request object.
            response (google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = evaluation_service.ListEvaluationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[evaluation_service.ListEvaluationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[evaluation.Evaluation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEvaluationResultsPager:
    """A pager for iterating through ``list_evaluation_results`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluation_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluationResults`` requests and continue to iterate
    through the ``evaluation_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., evaluation_service.ListEvaluationResultsResponse],
            request: evaluation_service.ListEvaluationResultsRequest,
            response: evaluation_service.ListEvaluationResultsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsRequest):
                The initial request object.
            response (google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = evaluation_service.ListEvaluationResultsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationResultsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[evaluation_service.ListEvaluationResultsResponse.EvaluationResult]:
        for page in self.pages:
            yield from page.evaluation_results

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEvaluationResultsAsyncPager:
    """A pager for iterating through ``list_evaluation_results`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluation_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluationResults`` requests and continue to iterate
    through the ``evaluation_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[evaluation_service.ListEvaluationResultsResponse]],
            request: evaluation_service.ListEvaluationResultsRequest,
            response: evaluation_service.ListEvaluationResultsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsRequest):
                The initial request object.
            response (google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = evaluation_service.ListEvaluationResultsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[evaluation_service.ListEvaluationResultsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[evaluation_service.ListEvaluationResultsResponse.EvaluationResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluation_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)

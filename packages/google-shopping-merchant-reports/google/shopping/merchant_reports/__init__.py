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
from google.shopping.merchant_reports import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_reports_v1beta.services.report_service.async_client import (
    ReportServiceAsyncClient,
)
from google.shopping.merchant_reports_v1beta.services.report_service.client import (
    ReportServiceClient,
)
from google.shopping.merchant_reports_v1beta.types.reports import (
    BestSellersBrandView,
    BestSellersProductClusterView,
    CompetitiveVisibilityBenchmarkView,
    CompetitiveVisibilityCompetitorView,
    CompetitiveVisibilityTopMerchantView,
    MarketingMethod,
    NonProductPerformanceView,
    PriceCompetitivenessProductView,
    PriceInsightsProductView,
    ProductPerformanceView,
    ProductView,
    RelativeDemand,
    RelativeDemandChangeType,
    ReportGranularity,
    ReportRow,
    SearchRequest,
    SearchResponse,
    TrafficSource,
)

__all__ = (
    "ReportServiceClient",
    "ReportServiceAsyncClient",
    "BestSellersBrandView",
    "BestSellersProductClusterView",
    "CompetitiveVisibilityBenchmarkView",
    "CompetitiveVisibilityCompetitorView",
    "CompetitiveVisibilityTopMerchantView",
    "MarketingMethod",
    "NonProductPerformanceView",
    "PriceCompetitivenessProductView",
    "PriceInsightsProductView",
    "ProductPerformanceView",
    "ProductView",
    "RelativeDemand",
    "RelativeDemandChangeType",
    "ReportGranularity",
    "ReportRow",
    "SearchRequest",
    "SearchResponse",
    "TrafficSource",
)

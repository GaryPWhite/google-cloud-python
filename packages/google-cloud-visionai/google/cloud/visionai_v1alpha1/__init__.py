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
from google.cloud.visionai_v1alpha1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.app_platform import AppPlatformAsyncClient, AppPlatformClient
from .services.live_video_analytics import (
    LiveVideoAnalyticsAsyncClient,
    LiveVideoAnalyticsClient,
)
from .services.streaming_service import (
    StreamingServiceAsyncClient,
    StreamingServiceClient,
)
from .services.streams_service import StreamsServiceAsyncClient, StreamsServiceClient
from .services.warehouse import WarehouseAsyncClient, WarehouseClient
from .types.annotations import (
    AppPlatformCloudFunctionRequest,
    AppPlatformCloudFunctionResponse,
    AppPlatformEventBody,
    AppPlatformMetadata,
    ClassificationPredictionResult,
    ImageObjectDetectionPredictionResult,
    ImageSegmentationPredictionResult,
    NormalizedPolygon,
    NormalizedPolyline,
    NormalizedVertex,
    ObjectDetectionPredictionResult,
    OccupancyCountingPredictionResult,
    PersonalProtectiveEquipmentDetectionOutput,
    StreamAnnotation,
    StreamAnnotations,
    StreamAnnotationType,
    VideoActionRecognitionPredictionResult,
    VideoClassificationPredictionResult,
    VideoObjectTrackingPredictionResult,
)
from .types.common import Cluster, GcsSource, OperationMetadata
from .types.lva import AnalysisDefinition, AnalyzerDefinition, AttributeValue
from .types.lva_resources import Analysis
from .types.lva_service import (
    CreateAnalysisRequest,
    DeleteAnalysisRequest,
    GetAnalysisRequest,
    ListAnalysesRequest,
    ListAnalysesResponse,
    UpdateAnalysisRequest,
)
from .types.platform import (
    AcceleratorType,
    AddApplicationStreamInputRequest,
    AddApplicationStreamInputResponse,
    AIEnabledDevicesInputConfig,
    Application,
    ApplicationConfigs,
    ApplicationInstance,
    ApplicationNodeAnnotation,
    ApplicationStreamInput,
    AutoscalingMetricSpec,
    BigQueryConfig,
    CreateApplicationInstancesRequest,
    CreateApplicationInstancesResponse,
    CreateApplicationRequest,
    CreateDraftRequest,
    CreateProcessorRequest,
    CustomProcessorSourceInfo,
    DedicatedResources,
    DeleteApplicationInstancesRequest,
    DeleteApplicationInstancesResponse,
    DeleteApplicationRequest,
    DeleteDraftRequest,
    DeleteProcessorRequest,
    DeployApplicationRequest,
    DeployApplicationResponse,
    Draft,
    GeneralObjectDetectionConfig,
    GetApplicationRequest,
    GetDraftRequest,
    GetInstanceRequest,
    GetProcessorRequest,
    Instance,
    ListApplicationsRequest,
    ListApplicationsResponse,
    ListDraftsRequest,
    ListDraftsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListPrebuiltProcessorsRequest,
    ListPrebuiltProcessorsResponse,
    ListProcessorsRequest,
    ListProcessorsResponse,
    MachineSpec,
    MediaWarehouseConfig,
    ModelType,
    Node,
    OccupancyCountConfig,
    PersonalProtectiveEquipmentDetectionConfig,
    PersonBlurConfig,
    PersonVehicleDetectionConfig,
    Processor,
    ProcessorConfig,
    ProcessorIOSpec,
    RemoveApplicationStreamInputRequest,
    RemoveApplicationStreamInputResponse,
    ResourceAnnotations,
    StreamWithAnnotation,
    UndeployApplicationRequest,
    UndeployApplicationResponse,
    UpdateApplicationInstancesRequest,
    UpdateApplicationInstancesResponse,
    UpdateApplicationRequest,
    UpdateApplicationStreamInputRequest,
    UpdateApplicationStreamInputResponse,
    UpdateDraftRequest,
    UpdateProcessorRequest,
    VertexAutoMLVideoConfig,
    VertexAutoMLVisionConfig,
    VertexCustomConfig,
    VideoStreamInputConfig,
)
from .types.streaming_resources import (
    GstreamerBufferDescriptor,
    Packet,
    PacketHeader,
    PacketType,
    RawImageDescriptor,
    SeriesMetadata,
    ServerMetadata,
)
from .types.streaming_service import (
    AcquireLeaseRequest,
    CommitRequest,
    ControlledMode,
    EagerMode,
    EventUpdate,
    Lease,
    LeaseType,
    ReceiveEventsControlResponse,
    ReceiveEventsRequest,
    ReceiveEventsResponse,
    ReceivePacketsControlResponse,
    ReceivePacketsRequest,
    ReceivePacketsResponse,
    ReleaseLeaseRequest,
    ReleaseLeaseResponse,
    RenewLeaseRequest,
    RequestMetadata,
    SendPacketsRequest,
    SendPacketsResponse,
)
from .types.streams_resources import Channel, Event, Series, Stream
from .types.streams_service import (
    CreateClusterRequest,
    CreateEventRequest,
    CreateSeriesRequest,
    CreateStreamRequest,
    DeleteClusterRequest,
    DeleteEventRequest,
    DeleteSeriesRequest,
    DeleteStreamRequest,
    GenerateStreamHlsTokenRequest,
    GenerateStreamHlsTokenResponse,
    GetClusterRequest,
    GetEventRequest,
    GetSeriesRequest,
    GetStreamRequest,
    GetStreamThumbnailResponse,
    ListClustersRequest,
    ListClustersResponse,
    ListEventsRequest,
    ListEventsResponse,
    ListSeriesRequest,
    ListSeriesResponse,
    ListStreamsRequest,
    ListStreamsResponse,
    MaterializeChannelRequest,
    UpdateClusterRequest,
    UpdateEventRequest,
    UpdateSeriesRequest,
    UpdateStreamRequest,
)
from .types.warehouse import (
    Annotation,
    AnnotationMatchingResult,
    AnnotationValue,
    Asset,
    BoolValue,
    CircleArea,
    ClipAssetRequest,
    ClipAssetResponse,
    Corpus,
    CreateAnnotationRequest,
    CreateAssetRequest,
    CreateCorpusMetadata,
    CreateCorpusRequest,
    CreateDataSchemaRequest,
    CreateSearchConfigRequest,
    Criteria,
    DataSchema,
    DataSchemaDetails,
    DateTimeRange,
    DateTimeRangeArray,
    DeleteAnnotationRequest,
    DeleteAssetMetadata,
    DeleteAssetRequest,
    DeleteCorpusRequest,
    DeleteDataSchemaRequest,
    DeleteSearchConfigRequest,
    FacetBucket,
    FacetBucketType,
    FacetGroup,
    FacetProperty,
    FacetValue,
    FloatRange,
    FloatRangeArray,
    GenerateHlsUriRequest,
    GenerateHlsUriResponse,
    GeoCoordinate,
    GeoLocationArray,
    GetAnnotationRequest,
    GetAssetRequest,
    GetCorpusRequest,
    GetDataSchemaRequest,
    GetSearchConfigRequest,
    IngestAssetRequest,
    IngestAssetResponse,
    IntRange,
    IntRangeArray,
    ListAnnotationsRequest,
    ListAnnotationsResponse,
    ListAssetsRequest,
    ListAssetsResponse,
    ListCorporaRequest,
    ListCorporaResponse,
    ListDataSchemasRequest,
    ListDataSchemasResponse,
    ListSearchConfigsRequest,
    ListSearchConfigsResponse,
    Partition,
    SearchAssetsRequest,
    SearchAssetsResponse,
    SearchConfig,
    SearchCriteriaProperty,
    SearchResultItem,
    StringArray,
    UpdateAnnotationRequest,
    UpdateAssetRequest,
    UpdateCorpusRequest,
    UpdateDataSchemaRequest,
    UpdateSearchConfigRequest,
    UserSpecifiedAnnotation,
)

__all__ = (
    "AppPlatformAsyncClient",
    "LiveVideoAnalyticsAsyncClient",
    "StreamingServiceAsyncClient",
    "StreamsServiceAsyncClient",
    "WarehouseAsyncClient",
    "AIEnabledDevicesInputConfig",
    "AcceleratorType",
    "AcquireLeaseRequest",
    "AddApplicationStreamInputRequest",
    "AddApplicationStreamInputResponse",
    "Analysis",
    "AnalysisDefinition",
    "AnalyzerDefinition",
    "Annotation",
    "AnnotationMatchingResult",
    "AnnotationValue",
    "AppPlatformClient",
    "AppPlatformCloudFunctionRequest",
    "AppPlatformCloudFunctionResponse",
    "AppPlatformEventBody",
    "AppPlatformMetadata",
    "Application",
    "ApplicationConfigs",
    "ApplicationInstance",
    "ApplicationNodeAnnotation",
    "ApplicationStreamInput",
    "Asset",
    "AttributeValue",
    "AutoscalingMetricSpec",
    "BigQueryConfig",
    "BoolValue",
    "Channel",
    "CircleArea",
    "ClassificationPredictionResult",
    "ClipAssetRequest",
    "ClipAssetResponse",
    "Cluster",
    "CommitRequest",
    "ControlledMode",
    "Corpus",
    "CreateAnalysisRequest",
    "CreateAnnotationRequest",
    "CreateApplicationInstancesRequest",
    "CreateApplicationInstancesResponse",
    "CreateApplicationRequest",
    "CreateAssetRequest",
    "CreateClusterRequest",
    "CreateCorpusMetadata",
    "CreateCorpusRequest",
    "CreateDataSchemaRequest",
    "CreateDraftRequest",
    "CreateEventRequest",
    "CreateProcessorRequest",
    "CreateSearchConfigRequest",
    "CreateSeriesRequest",
    "CreateStreamRequest",
    "Criteria",
    "CustomProcessorSourceInfo",
    "DataSchema",
    "DataSchemaDetails",
    "DateTimeRange",
    "DateTimeRangeArray",
    "DedicatedResources",
    "DeleteAnalysisRequest",
    "DeleteAnnotationRequest",
    "DeleteApplicationInstancesRequest",
    "DeleteApplicationInstancesResponse",
    "DeleteApplicationRequest",
    "DeleteAssetMetadata",
    "DeleteAssetRequest",
    "DeleteClusterRequest",
    "DeleteCorpusRequest",
    "DeleteDataSchemaRequest",
    "DeleteDraftRequest",
    "DeleteEventRequest",
    "DeleteProcessorRequest",
    "DeleteSearchConfigRequest",
    "DeleteSeriesRequest",
    "DeleteStreamRequest",
    "DeployApplicationRequest",
    "DeployApplicationResponse",
    "Draft",
    "EagerMode",
    "Event",
    "EventUpdate",
    "FacetBucket",
    "FacetBucketType",
    "FacetGroup",
    "FacetProperty",
    "FacetValue",
    "FloatRange",
    "FloatRangeArray",
    "GcsSource",
    "GeneralObjectDetectionConfig",
    "GenerateHlsUriRequest",
    "GenerateHlsUriResponse",
    "GenerateStreamHlsTokenRequest",
    "GenerateStreamHlsTokenResponse",
    "GeoCoordinate",
    "GeoLocationArray",
    "GetAnalysisRequest",
    "GetAnnotationRequest",
    "GetApplicationRequest",
    "GetAssetRequest",
    "GetClusterRequest",
    "GetCorpusRequest",
    "GetDataSchemaRequest",
    "GetDraftRequest",
    "GetEventRequest",
    "GetInstanceRequest",
    "GetProcessorRequest",
    "GetSearchConfigRequest",
    "GetSeriesRequest",
    "GetStreamRequest",
    "GetStreamThumbnailResponse",
    "GstreamerBufferDescriptor",
    "ImageObjectDetectionPredictionResult",
    "ImageSegmentationPredictionResult",
    "IngestAssetRequest",
    "IngestAssetResponse",
    "Instance",
    "IntRange",
    "IntRangeArray",
    "Lease",
    "LeaseType",
    "ListAnalysesRequest",
    "ListAnalysesResponse",
    "ListAnnotationsRequest",
    "ListAnnotationsResponse",
    "ListApplicationsRequest",
    "ListApplicationsResponse",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListCorporaRequest",
    "ListCorporaResponse",
    "ListDataSchemasRequest",
    "ListDataSchemasResponse",
    "ListDraftsRequest",
    "ListDraftsResponse",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListPrebuiltProcessorsRequest",
    "ListPrebuiltProcessorsResponse",
    "ListProcessorsRequest",
    "ListProcessorsResponse",
    "ListSearchConfigsRequest",
    "ListSearchConfigsResponse",
    "ListSeriesRequest",
    "ListSeriesResponse",
    "ListStreamsRequest",
    "ListStreamsResponse",
    "LiveVideoAnalyticsClient",
    "MachineSpec",
    "MaterializeChannelRequest",
    "MediaWarehouseConfig",
    "ModelType",
    "Node",
    "NormalizedPolygon",
    "NormalizedPolyline",
    "NormalizedVertex",
    "ObjectDetectionPredictionResult",
    "OccupancyCountConfig",
    "OccupancyCountingPredictionResult",
    "OperationMetadata",
    "Packet",
    "PacketHeader",
    "PacketType",
    "Partition",
    "PersonBlurConfig",
    "PersonVehicleDetectionConfig",
    "PersonalProtectiveEquipmentDetectionConfig",
    "PersonalProtectiveEquipmentDetectionOutput",
    "Processor",
    "ProcessorConfig",
    "ProcessorIOSpec",
    "RawImageDescriptor",
    "ReceiveEventsControlResponse",
    "ReceiveEventsRequest",
    "ReceiveEventsResponse",
    "ReceivePacketsControlResponse",
    "ReceivePacketsRequest",
    "ReceivePacketsResponse",
    "ReleaseLeaseRequest",
    "ReleaseLeaseResponse",
    "RemoveApplicationStreamInputRequest",
    "RemoveApplicationStreamInputResponse",
    "RenewLeaseRequest",
    "RequestMetadata",
    "ResourceAnnotations",
    "SearchAssetsRequest",
    "SearchAssetsResponse",
    "SearchConfig",
    "SearchCriteriaProperty",
    "SearchResultItem",
    "SendPacketsRequest",
    "SendPacketsResponse",
    "Series",
    "SeriesMetadata",
    "ServerMetadata",
    "Stream",
    "StreamAnnotation",
    "StreamAnnotationType",
    "StreamAnnotations",
    "StreamWithAnnotation",
    "StreamingServiceClient",
    "StreamsServiceClient",
    "StringArray",
    "UndeployApplicationRequest",
    "UndeployApplicationResponse",
    "UpdateAnalysisRequest",
    "UpdateAnnotationRequest",
    "UpdateApplicationInstancesRequest",
    "UpdateApplicationInstancesResponse",
    "UpdateApplicationRequest",
    "UpdateApplicationStreamInputRequest",
    "UpdateApplicationStreamInputResponse",
    "UpdateAssetRequest",
    "UpdateClusterRequest",
    "UpdateCorpusRequest",
    "UpdateDataSchemaRequest",
    "UpdateDraftRequest",
    "UpdateEventRequest",
    "UpdateProcessorRequest",
    "UpdateSearchConfigRequest",
    "UpdateSeriesRequest",
    "UpdateStreamRequest",
    "UserSpecifiedAnnotation",
    "VertexAutoMLVideoConfig",
    "VertexAutoMLVisionConfig",
    "VertexCustomConfig",
    "VideoActionRecognitionPredictionResult",
    "VideoClassificationPredictionResult",
    "VideoObjectTrackingPredictionResult",
    "VideoStreamInputConfig",
    "WarehouseClient",
)

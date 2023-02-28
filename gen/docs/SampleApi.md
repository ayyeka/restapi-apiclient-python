# swagger_client.SampleApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sample_ack_sample_scalar_batch**](SampleApi.md#sample_ack_sample_scalar_batch) | **POST** /sample/batch/ack | ackSampleScalarBatch sample
[**sample_get_last_sample_scalar_batch**](SampleApi.md#sample_get_last_sample_scalar_batch) | **GET** /sample/batch/status | getLastSampleScalarBatch sample
[**sample_get_last_sample_scalar_by_stream**](SampleApi.md#sample_get_last_sample_scalar_by_stream) | **GET** /stream/{streamId}/sample/last | getLastSampleScalarByStream sample
[**sample_get_samples_scalar_aggregation_by_stream_and_date_range**](SampleApi.md#sample_get_samples_scalar_aggregation_by_stream_and_date_range) | **GET** /stream/{streamId}/sample/agg | getSamplesScalarAggregationByStreamAndDateRange sample
[**sample_get_samples_scalar_batch**](SampleApi.md#sample_get_samples_scalar_batch) | **GET** /sample/batch | getSamplesScalarBatch sample
[**sample_get_samples_scalar_batch_by_site**](SampleApi.md#sample_get_samples_scalar_batch_by_site) | **GET** /site/{siteId}/sample/batch | getSamplesScalarBatchBySite sample
[**sample_get_samples_scalar_batch_by_stream**](SampleApi.md#sample_get_samples_scalar_batch_by_stream) | **GET** /stream/{streamId}/sample/batch | getSamplesScalarBatchByStream sample
[**sample_get_samples_scalar_by_site**](SampleApi.md#sample_get_samples_scalar_by_site) | **GET** /site/{siteId}/sample | getSamplesScalarBySite sample
[**sample_get_samples_scalar_by_stream**](SampleApi.md#sample_get_samples_scalar_by_stream) | **GET** /stream/{streamId}/sample | getSamplesScalarByStream sample
[**sample_get_samples_scalar_by_stream_and_date_range**](SampleApi.md#sample_get_samples_scalar_by_stream_and_date_range) | **GET** /stream/{streamId}/sample/range | getSamplesScalarByStreamAndDateRange sample
[**sample_set_backfill_samples_scalar_batch**](SampleApi.md#sample_set_backfill_samples_scalar_batch) | **POST** /sample/batch/backfill | setBackfillSamplesScalarBatch sample

# **sample_ack_sample_scalar_batch**
> sample_ack_sample_scalar_batch(sample_id, agent=agent)

ackSampleScalarBatch sample

Notify which Sample was the Last Sample Received by the Client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 789 # int | The value to set in the last delivered sample id internal field
agent = 'agent_example' # str | User-Agent information, stored in the cloud to identify the applications that use the samples batch APIs (optional)

try:
    # ackSampleScalarBatch sample
    api_instance.sample_ack_sample_scalar_batch(sample_id, agent=agent)
except ApiException as e:
    print("Exception when calling SampleApi->sample_ack_sample_scalar_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| The value to set in the last delivered sample id internal field | 
 **agent** | **str**| User-Agent information, stored in the cloud to identify the applications that use the samples batch APIs | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_last_sample_scalar_batch**
> StoredSampleScalar sample_get_last_sample_scalar_batch()

getLastSampleScalarBatch sample

Get the Last Delivered Sample of the Last Delivered SamplesScalar Batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))

try:
    # getLastSampleScalarBatch sample
    api_response = api_instance.sample_get_last_sample_scalar_batch()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_last_sample_scalar_batch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredSampleScalar**](StoredSampleScalar.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_last_sample_scalar_by_stream**
> StoredSampleScalar sample_get_last_sample_scalar_by_stream(stream_id)

getLastSampleScalarByStream sample

Get Last Sample from Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose last sample should be returned

try:
    # getLastSampleScalarByStream sample
    api_response = api_instance.sample_get_last_sample_scalar_by_stream(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_last_sample_scalar_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose last sample should be returned | 

### Return type

[**StoredSampleScalar**](StoredSampleScalar.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_aggregation_by_stream_and_date_range**
> StoredSampleScalarAggregationBatch sample_get_samples_scalar_aggregation_by_stream_and_date_range(stream_id, time_frame, from_date, to_date)

getSamplesScalarAggregationByStreamAndDateRange sample

Returns samples aggregation from specified stream and date range

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose samples should be returned
time_frame = 56 # int | Time Frame of the aggregation 10 15 20 30 or 60 minutes
from_date = 789 # int | From date and time (Unix time, seconds since January 1, 1970 UTC.)
to_date = 789 # int | To date and time (Unix time, seconds since January 1, 1970 UTC.)

try:
    # getSamplesScalarAggregationByStreamAndDateRange sample
    api_response = api_instance.sample_get_samples_scalar_aggregation_by_stream_and_date_range(stream_id, time_frame, from_date, to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_aggregation_by_stream_and_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose samples should be returned | 
 **time_frame** | **int**| Time Frame of the aggregation 10 15 20 30 or 60 minutes | 
 **from_date** | **int**| From date and time (Unix time, seconds since January 1, 1970 UTC.) | 
 **to_date** | **int**| To date and time (Unix time, seconds since January 1, 1970 UTC.) | 

### Return type

[**StoredSampleScalarAggregationBatch**](StoredSampleScalarAggregationBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_batch**
> StoredSampleScalarBatch sample_get_samples_scalar_batch(enable_ack=enable_ack, sample_id=sample_id, backfill_hours=backfill_hours)

getSamplesScalarBatch sample

Get a Batch of New SamplesScalar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
enable_ack = true # bool | If set to false, then the internal last delivered sample id value is set to the last sample ID in the batch sent in response to this call (optional) (default to true)
sample_id = 789 # int | Specifies to send samples with an ID number strictly higher than the sampleID. For example, if the sampleID value is 1234, the response could include samples with IDs such as [1235, 1240, 1241] (optional)
backfill_hours = 56 # int | Specifies to send samples starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples of the past 24 hours (optional)

try:
    # getSamplesScalarBatch sample
    api_response = api_instance.sample_get_samples_scalar_batch(enable_ack=enable_ack, sample_id=sample_id, backfill_hours=backfill_hours)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_ack** | **bool**| If set to false, then the internal last delivered sample id value is set to the last sample ID in the batch sent in response to this call | [optional] [default to true]
 **sample_id** | **int**| Specifies to send samples with an ID number strictly higher than the sampleID. For example, if the sampleID value is 1234, the response could include samples with IDs such as [1235, 1240, 1241] | [optional] 
 **backfill_hours** | **int**| Specifies to send samples starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples of the past 24 hours | [optional] 

### Return type

[**StoredSampleScalarBatch**](StoredSampleScalarBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_batch_by_site**
> StoredSampleScalarBatch sample_get_samples_scalar_batch_by_site(site_id, sample_date)

getSamplesScalarBatchBySite sample

Get Batch of Recent SamplesScalar of a Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose recent samples should be returned
sample_date = 789 # int | The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.)

try:
    # getSamplesScalarBatchBySite sample
    api_response = api_instance.sample_get_samples_scalar_batch_by_site(site_id, sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_batch_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose recent samples should be returned | 
 **sample_date** | **int**| The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) | 

### Return type

[**StoredSampleScalarBatch**](StoredSampleScalarBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_batch_by_stream**
> StoredSampleScalarBatch sample_get_samples_scalar_batch_by_stream(stream_id, sample_date)

getSamplesScalarBatchByStream sample

Get Batch of Recent SamplesScalar of a Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose recent samples should be returned
sample_date = 789 # int | The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.)

try:
    # getSamplesScalarBatchByStream sample
    api_response = api_instance.sample_get_samples_scalar_batch_by_stream(stream_id, sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_batch_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose recent samples should be returned | 
 **sample_date** | **int**| The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) | 

### Return type

[**StoredSampleScalarBatch**](StoredSampleScalarBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_by_site**
> StoredSampleScalarCollection sample_get_samples_scalar_by_site(site_id, last_sample_id=last_sample_id)

getSamplesScalarBySite sample

Returns up to 100 samples from the specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose recent samples should be returned
last_sample_id = 789 # int | ID of the oldest sample from which to start returning samples (optional)

try:
    # getSamplesScalarBySite sample
    api_response = api_instance.sample_get_samples_scalar_by_site(site_id, last_sample_id=last_sample_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose recent samples should be returned | 
 **last_sample_id** | **int**| ID of the oldest sample from which to start returning samples | [optional] 

### Return type

[**StoredSampleScalarCollection**](StoredSampleScalarCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_by_stream**
> StoredSampleScalarCollection sample_get_samples_scalar_by_stream(stream_id, last_sample_id=last_sample_id)

getSamplesScalarByStream sample

Returns up to 100 samples from the specified stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose recent samples should be returned
last_sample_id = 789 # int | ID of the oldest sample from which to start returning samples (optional)

try:
    # getSamplesScalarByStream sample
    api_response = api_instance.sample_get_samples_scalar_by_stream(stream_id, last_sample_id=last_sample_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose recent samples should be returned | 
 **last_sample_id** | **int**| ID of the oldest sample from which to start returning samples | [optional] 

### Return type

[**StoredSampleScalarCollection**](StoredSampleScalarCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_scalar_by_stream_and_date_range**
> StoredSampleScalarBatch sample_get_samples_scalar_by_stream_and_date_range(stream_id, from_date, to_date, limit=limit, offset=offset)

getSamplesScalarByStreamAndDateRange sample

Returns samples from specified stream and date range

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose samples should be returned
from_date = 789 # int | From date and time (Unix time, seconds since January 1, 1970 UTC.)
to_date = 789 # int | To date and time (Unix time, seconds since January 1, 1970 UTC.)
limit = 789 # int | Limit the number of samples to return (optional)
offset = 56 # int | Get samples starting with an offset, where 1 is the first (optional)

try:
    # getSamplesScalarByStreamAndDateRange sample
    api_response = api_instance.sample_get_samples_scalar_by_stream_and_date_range(stream_id, from_date, to_date, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_scalar_by_stream_and_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose samples should be returned | 
 **from_date** | **int**| From date and time (Unix time, seconds since January 1, 1970 UTC.) | 
 **to_date** | **int**| To date and time (Unix time, seconds since January 1, 1970 UTC.) | 
 **limit** | **int**| Limit the number of samples to return | [optional] 
 **offset** | **int**| Get samples starting with an offset, where 1 is the first | [optional] 

### Return type

[**StoredSampleScalarBatch**](StoredSampleScalarBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_set_backfill_samples_scalar_batch**
> sample_set_backfill_samples_scalar_batch(sample_date, agent=agent)

setBackfillSamplesScalarBatch sample

Reset the DateTime starting point for the next SamplesScalar Batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_date = 789 # int | The date and time to use for setting the last delivered sample id internal field (Unix time, seconds since January 1, 1970 UTC.). The API resets the internal last delivered sample id value to the id of the sample whose date and time is closest to the specified date and time
agent = 'agent_example' # str | ser-Agent information, stored in the cloud to identify the applications that use the samples batch APIs (optional)

try:
    # setBackfillSamplesScalarBatch sample
    api_instance.sample_set_backfill_samples_scalar_batch(sample_date, agent=agent)
except ApiException as e:
    print("Exception when calling SampleApi->sample_set_backfill_samples_scalar_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_date** | **int**| The date and time to use for setting the last delivered sample id internal field (Unix time, seconds since January 1, 1970 UTC.). The API resets the internal last delivered sample id value to the id of the sample whose date and time is closest to the specified date and time | 
 **agent** | **str**| ser-Agent information, stored in the cloud to identify the applications that use the samples batch APIs | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


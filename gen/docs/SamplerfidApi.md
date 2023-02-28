# swagger_client.SamplerfidApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samplerfid_ack_sample_rfid_batch**](SamplerfidApi.md#samplerfid_ack_sample_rfid_batch) | **POST** /sample/rfid/batch/ack | ackSampleRFIDBatch samplerfid
[**samplerfid_get_last_sample_rfid_batch**](SamplerfidApi.md#samplerfid_get_last_sample_rfid_batch) | **GET** /sample/rfid/batch/status | getLastSampleRFIDBatch samplerfid
[**samplerfid_get_last_sample_rfidby_stream**](SamplerfidApi.md#samplerfid_get_last_sample_rfidby_stream) | **GET** /stream/{streamId}/sample/rfid/last | getLastSampleRFIDByStream samplerfid
[**samplerfid_get_samples_rfid_batch**](SamplerfidApi.md#samplerfid_get_samples_rfid_batch) | **GET** /sample/rfid/batch | getSamplesRFIDBatch samplerfid
[**samplerfid_get_samples_rfid_batch_by_site**](SamplerfidApi.md#samplerfid_get_samples_rfid_batch_by_site) | **GET** /site/{siteId}/sample/rfid/batch | getSamplesRFIDBatchBySite samplerfid
[**samplerfid_get_samples_rfid_batch_by_stream**](SamplerfidApi.md#samplerfid_get_samples_rfid_batch_by_stream) | **GET** /stream/{streamId}/sample/rfid/batch | getSamplesRFIDBatchByStream samplerfid
[**samplerfid_get_samples_rfidby_stream**](SamplerfidApi.md#samplerfid_get_samples_rfidby_stream) | **GET** /stream/{streamId}/sample/rfid | getSamplesRFIDByStream samplerfid
[**samplerfid_set_backfill_samples_rfid_batch**](SamplerfidApi.md#samplerfid_set_backfill_samples_rfid_batch) | **POST** /sample/rfid/batch/backfill | setBackfillSamplesRFIDBatch samplerfid

# **samplerfid_ack_sample_rfid_batch**
> samplerfid_ack_sample_rfid_batch(sample_id, agent=agent)

ackSampleRFIDBatch samplerfid

Notify which Sample RFID was the Last Sample RFID Received by the Client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
sample_id = 789 # int | The value to set in the last delivered sample RFID id internal field
agent = 'agent_example' # str | User-Agent information, stored in the cloud to identify the applications that use the sampleRFIDs batch APIs (optional)

try:
    # ackSampleRFIDBatch samplerfid
    api_instance.samplerfid_ack_sample_rfid_batch(sample_id, agent=agent)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_ack_sample_rfid_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| The value to set in the last delivered sample RFID id internal field | 
 **agent** | **str**| User-Agent information, stored in the cloud to identify the applications that use the sampleRFIDs batch APIs | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_get_last_sample_rfid_batch**
> AkapiStoredSampleRfid samplerfid_get_last_sample_rfid_batch()

getLastSampleRFIDBatch samplerfid

Get the Last Delivered Sample RFID of the Last Delivered Samples RFID Batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))

try:
    # getLastSampleRFIDBatch samplerfid
    api_response = api_instance.samplerfid_get_last_sample_rfid_batch()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_get_last_sample_rfid_batch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AkapiStoredSampleRfid**](AkapiStoredSampleRfid.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_get_last_sample_rfidby_stream**
> AkapiStoredSampleRfid samplerfid_get_last_sample_rfidby_stream(stream_id)

getLastSampleRFIDByStream samplerfid

Get Last Sample from Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose last sample should be returned

try:
    # getLastSampleRFIDByStream samplerfid
    api_response = api_instance.samplerfid_get_last_sample_rfidby_stream(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_get_last_sample_rfidby_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose last sample should be returned | 

### Return type

[**AkapiStoredSampleRfid**](AkapiStoredSampleRfid.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_get_samples_rfid_batch**
> StoredSampleRFIDBatch samplerfid_get_samples_rfid_batch(enable_ack=enable_ack, sample_id=sample_id, backfill_hours=backfill_hours)

getSamplesRFIDBatch samplerfid

Get a Batch of New Samples RFID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
enable_ack = true # bool | If set to false, then the internal last delivered sample RFID id value is set to the last sample RFID ID in the batch sent in response to this call. If set to true, then the internal last delivered sample RFID id remains untouched by this call. We recommend setting this parameter to 'true' and calling ackSamplesRFIDBatch to update the last delivered sample RFID id field (optional) (default to true)
sample_id = 789 # int | Specifies to send samples RFID with an ID number strictly higher than the sampleId. For example, if the sampleId value is 1234, the response could include samples RFID with IDs such as [1235, 1240, 1241] (optional)
backfill_hours = 56 # int | Specifies to send samples RFID starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples RFID of the past 24 hours (optional)

try:
    # getSamplesRFIDBatch samplerfid
    api_response = api_instance.samplerfid_get_samples_rfid_batch(enable_ack=enable_ack, sample_id=sample_id, backfill_hours=backfill_hours)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_get_samples_rfid_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_ack** | **bool**| If set to false, then the internal last delivered sample RFID id value is set to the last sample RFID ID in the batch sent in response to this call. If set to true, then the internal last delivered sample RFID id remains untouched by this call. We recommend setting this parameter to &#x27;true&#x27; and calling ackSamplesRFIDBatch to update the last delivered sample RFID id field | [optional] [default to true]
 **sample_id** | **int**| Specifies to send samples RFID with an ID number strictly higher than the sampleId. For example, if the sampleId value is 1234, the response could include samples RFID with IDs such as [1235, 1240, 1241] | [optional] 
 **backfill_hours** | **int**| Specifies to send samples RFID starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples RFID of the past 24 hours | [optional] 

### Return type

[**StoredSampleRFIDBatch**](StoredSampleRFIDBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_get_samples_rfid_batch_by_site**
> StoredSampleRFIDBatch samplerfid_get_samples_rfid_batch_by_site(site_id, sample_date)

getSamplesRFIDBatchBySite samplerfid

Get Batch of Recent Samples RFID of a Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose recent samples should be returned
sample_date = 789 # int | The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.)

try:
    # getSamplesRFIDBatchBySite samplerfid
    api_response = api_instance.samplerfid_get_samples_rfid_batch_by_site(site_id, sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_get_samples_rfid_batch_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose recent samples should be returned | 
 **sample_date** | **int**| The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) | 

### Return type

[**StoredSampleRFIDBatch**](StoredSampleRFIDBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_get_samples_rfid_batch_by_stream**
> StoredSampleRFIDBatch samplerfid_get_samples_rfid_batch_by_stream(stream_id, sample_date)

getSamplesRFIDBatchByStream samplerfid

Get Batch of Recent Samples RFID of a Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose recent samples should be returned
sample_date = 789 # int | The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.)

try:
    # getSamplesRFIDBatchByStream samplerfid
    api_response = api_instance.samplerfid_get_samples_rfid_batch_by_stream(stream_id, sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_get_samples_rfid_batch_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose recent samples should be returned | 
 **sample_date** | **int**| The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) | 

### Return type

[**StoredSampleRFIDBatch**](StoredSampleRFIDBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_get_samples_rfidby_stream**
> StoredSampleRFIDCollection samplerfid_get_samples_rfidby_stream(stream_id, last_sample_id=last_sample_id)

getSamplesRFIDByStream samplerfid

Returns up to 100 samples RFID from the specified stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose recent samples should be returned
last_sample_id = 789 # int | ID of the oldest sample from which to start returning samples (optional)

try:
    # getSamplesRFIDByStream samplerfid
    api_response = api_instance.samplerfid_get_samples_rfidby_stream(stream_id, last_sample_id=last_sample_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_get_samples_rfidby_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose recent samples should be returned | 
 **last_sample_id** | **int**| ID of the oldest sample from which to start returning samples | [optional] 

### Return type

[**StoredSampleRFIDCollection**](StoredSampleRFIDCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplerfid_set_backfill_samples_rfid_batch**
> samplerfid_set_backfill_samples_rfid_batch(sample_date, agent=agent)

setBackfillSamplesRFIDBatch samplerfid

Reset the DateTime starting point for the next Samples RFID Batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplerfidApi(swagger_client.ApiClient(configuration))
sample_date = 789 # int | The date and time to use for setting the last delivered sample id internal field (Unix time, seconds since January 1, 1970 UTC.). The API resets the internal last delivered sample id value to the id of the sample whose date and time is closest to the specified date and time
agent = 'agent_example' # str | ser-Agent information, stored in the cloud to identify the applications that use the samples batch APIs (optional)

try:
    # setBackfillSamplesRFIDBatch samplerfid
    api_instance.samplerfid_set_backfill_samples_rfid_batch(sample_date, agent=agent)
except ApiException as e:
    print("Exception when calling SamplerfidApi->samplerfid_set_backfill_samples_rfid_batch: %s\n" % e)
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


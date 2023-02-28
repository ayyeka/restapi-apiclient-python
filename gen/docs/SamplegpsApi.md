# swagger_client.SamplegpsApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samplegps_ack_sample_gps_batch**](SamplegpsApi.md#samplegps_ack_sample_gps_batch) | **POST** /sample/gps/batch/ack | ackSampleGPSBatch samplegps
[**samplegps_get_gpsby_device_id**](SamplegpsApi.md#samplegps_get_gpsby_device_id) | **GET** /device/id/{deviceId}/sample/gps | getGPSByDeviceId samplegps
[**samplegps_get_samples_gps_batch**](SamplegpsApi.md#samplegps_get_samples_gps_batch) | **GET** /sample/gps/batch | getSamplesGPSBatch samplegps
[**samplegps_get_samples_gps_batch_by_stream**](SamplegpsApi.md#samplegps_get_samples_gps_batch_by_stream) | **GET** /stream/{streamId}/sample/gps/batch | getSamplesGPSBatchByStream samplegps

# **samplegps_ack_sample_gps_batch**
> samplegps_ack_sample_gps_batch(sample_id, agent=agent)

ackSampleGPSBatch samplegps

Notify which Sample GPS was the Last Sample GPS Received by the Client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplegpsApi(swagger_client.ApiClient(configuration))
sample_id = 789 # int | The value to set in the last delivered sample GPS id internal field
agent = 'agent_example' # str | User-Agent information, stored in the cloud to identify the applications that use the sampleGPSs batch APIs (optional)

try:
    # ackSampleGPSBatch samplegps
    api_instance.samplegps_ack_sample_gps_batch(sample_id, agent=agent)
except ApiException as e:
    print("Exception when calling SamplegpsApi->samplegps_ack_sample_gps_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| The value to set in the last delivered sample GPS id internal field | 
 **agent** | **str**| User-Agent information, stored in the cloud to identify the applications that use the sampleGPSs batch APIs | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplegps_get_gpsby_device_id**
> AkapiStoredSampleGps samplegps_get_gpsby_device_id(device_id)

getGPSByDeviceId samplegps

Returns GPS information about specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplegpsApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose GPS data should be returned

try:
    # getGPSByDeviceId samplegps
    api_response = api_instance.samplegps_get_gpsby_device_id(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplegpsApi->samplegps_get_gpsby_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose GPS data should be returned | 

### Return type

[**AkapiStoredSampleGps**](AkapiStoredSampleGps.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplegps_get_samples_gps_batch**
> StoredSampleGPSBatch samplegps_get_samples_gps_batch(enable_ack=enable_ack, sample_id=sample_id, backfill_hours=backfill_hours)

getSamplesGPSBatch samplegps

Get a Batch of New Samples GPS

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplegpsApi(swagger_client.ApiClient(configuration))
enable_ack = true # bool | If set to false, then the internal last delivered sample GPS id value is set to the last sample GPS ID in the batch sent in response to this call. If set to true, then the internal last delivered sample GPS id remains untouched by this call. We recommend setting this parameter to 'true' and calling ackSamplesGPSBatch to update the last delivered sample GPS id field (optional) (default to true)
sample_id = 789 # int | Specifies to send samples GPS with an ID number strictly higher than the sampleID. For example, if the sampleID value is 1234, the response could include samples GPS with IDs such as [1235, 1240, 1241] (optional)
backfill_hours = 56 # int | Specifies to send samples GPS starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples GPS of the past 24 hours (optional)

try:
    # getSamplesGPSBatch samplegps
    api_response = api_instance.samplegps_get_samples_gps_batch(enable_ack=enable_ack, sample_id=sample_id, backfill_hours=backfill_hours)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplegpsApi->samplegps_get_samples_gps_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_ack** | **bool**| If set to false, then the internal last delivered sample GPS id value is set to the last sample GPS ID in the batch sent in response to this call. If set to true, then the internal last delivered sample GPS id remains untouched by this call. We recommend setting this parameter to &#x27;true&#x27; and calling ackSamplesGPSBatch to update the last delivered sample GPS id field | [optional] [default to true]
 **sample_id** | **int**| Specifies to send samples GPS with an ID number strictly higher than the sampleID. For example, if the sampleID value is 1234, the response could include samples GPS with IDs such as [1235, 1240, 1241] | [optional] 
 **backfill_hours** | **int**| Specifies to send samples GPS starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples GPS of the past 24 hours | [optional] 

### Return type

[**StoredSampleGPSBatch**](StoredSampleGPSBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplegps_get_samples_gps_batch_by_stream**
> StoredSampleGPSBatch samplegps_get_samples_gps_batch_by_stream(stream_id, sample_date)

getSamplesGPSBatchByStream samplegps

Get a Batch of New Samples GPS by stream id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SamplegpsApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose recent samples GPS should be returned
sample_date = 789 # int | The sampling date and time of the oldest sample GPS in the batch (Epoch timestamp >946688460)

try:
    # getSamplesGPSBatchByStream samplegps
    api_response = api_instance.samplegps_get_samples_gps_batch_by_stream(stream_id, sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplegpsApi->samplegps_get_samples_gps_batch_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose recent samples GPS should be returned | 
 **sample_date** | **int**| The sampling date and time of the oldest sample GPS in the batch (Epoch timestamp &gt;946688460) | 

### Return type

[**StoredSampleGPSBatch**](StoredSampleGPSBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


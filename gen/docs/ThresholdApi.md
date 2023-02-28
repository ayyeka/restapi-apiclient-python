# swagger_client.ThresholdApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**threshold_get_threshold_by_stream**](ThresholdApi.md#threshold_get_threshold_by_stream) | **GET** /stream/{streamId}/threshold | getThresholdByStream threshold
[**threshold_get_threshold_status**](ThresholdApi.md#threshold_get_threshold_status) | **GET** /stream/{streamId}/threshold/status | getThresholdStatus threshold
[**threshold_set_threshold_by_stream**](ThresholdApi.md#threshold_set_threshold_by_stream) | **POST** /stream/{streamId}/threshold | setThresholdByStream threshold

# **threshold_get_threshold_by_stream**
> GetThresholdByStreamResponseBody threshold_get_threshold_by_stream(stream_id)

getThresholdByStream threshold

Get thresholds for specified stream Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ThresholdApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | Stream Id

try:
    # getThresholdByStream threshold
    api_response = api_instance.threshold_get_threshold_by_stream(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdApi->threshold_get_threshold_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| Stream Id | 

### Return type

[**GetThresholdByStreamResponseBody**](GetThresholdByStreamResponseBody.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **threshold_get_threshold_status**
> ThresholdStatus threshold_get_threshold_status(stream_id)

getThresholdStatus threshold

Get thresholds for specified stream Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ThresholdApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | Stream Id

try:
    # getThresholdStatus threshold
    api_response = api_instance.threshold_get_threshold_status(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdApi->threshold_get_threshold_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| Stream Id | 

### Return type

[**ThresholdStatus**](ThresholdStatus.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **threshold_set_threshold_by_stream**
> threshold_set_threshold_by_stream(body, stream_id)

setThresholdByStream threshold

Set thresholds for specified stream Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ThresholdApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetThresholdByStreamRequestBody() # SetThresholdByStreamRequestBody | 
stream_id = 789 # int | Stream Id

try:
    # setThresholdByStream threshold
    api_instance.threshold_set_threshold_by_stream(body, stream_id)
except ApiException as e:
    print("Exception when calling ThresholdApi->threshold_set_threshold_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetThresholdByStreamRequestBody**](SetThresholdByStreamRequestBody.md)|  | 
 **stream_id** | **int**| Stream Id | 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


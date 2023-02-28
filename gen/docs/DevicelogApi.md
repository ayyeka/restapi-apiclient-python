# swagger_client.DevicelogApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicelog_get_device_logs**](DevicelogApi.md#devicelog_get_device_logs) | **GET** /device/{deviceId}/log | getDeviceLogs devicelog
[**devicelog_get_last_device_log**](DevicelogApi.md#devicelog_get_last_device_log) | **GET** /device/{deviceId}/lastLog | getLastDeviceLog devicelog

# **devicelog_get_device_logs**
> StoredDeviceLogCollection devicelog_get_device_logs(device_id, last_delivered_id=last_delivered_id)

getDeviceLogs devicelog

Returns up to 100 new logs from the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DevicelogApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose log counters should be returned
last_delivered_id = 789 # int | ID of the oldest log counter from which to start returning samples (optional)

try:
    # getDeviceLogs devicelog
    api_response = api_instance.devicelog_get_device_logs(device_id, last_delivered_id=last_delivered_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicelogApi->devicelog_get_device_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose log counters should be returned | 
 **last_delivered_id** | **int**| ID of the oldest log counter from which to start returning samples | [optional] 

### Return type

[**StoredDeviceLogCollection**](StoredDeviceLogCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicelog_get_last_device_log**
> StoredDeviceLogCollection devicelog_get_last_device_log(device_id)

getLastDeviceLog devicelog

Returns information about the last known log record from the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DevicelogApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose last log counters should be returned

try:
    # getLastDeviceLog devicelog
    api_response = api_instance.devicelog_get_last_device_log(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicelogApi->devicelog_get_last_device_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose last log counters should be returned | 

### Return type

[**StoredDeviceLogCollection**](StoredDeviceLogCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


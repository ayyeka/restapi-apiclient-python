# swagger_client.DevicehealthApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicehealth_get_device_healths**](DevicehealthApi.md#devicehealth_get_device_healths) | **GET** /device/{deviceId}/health | getDeviceHealths devicehealth
[**devicehealth_get_last_device_health**](DevicehealthApi.md#devicehealth_get_last_device_health) | **GET** /device/{deviceId}/lastHealth | getLastDeviceHealth devicehealth

# **devicehealth_get_device_healths**
> StoredDeviceHealthCollection devicehealth_get_device_healths(device_id, last_delivered_id=last_delivered_id)

getDeviceHealths devicehealth

Returns up to 100 new counters from the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DevicehealthApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose health counters should be returned
last_delivered_id = 789 # int | ID of the oldest health counter from which to start returning samples (optional)

try:
    # getDeviceHealths devicehealth
    api_response = api_instance.devicehealth_get_device_healths(device_id, last_delivered_id=last_delivered_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicehealthApi->devicehealth_get_device_healths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose health counters should be returned | 
 **last_delivered_id** | **int**| ID of the oldest health counter from which to start returning samples | [optional] 

### Return type

[**StoredDeviceHealthCollection**](StoredDeviceHealthCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicehealth_get_last_device_health**
> StoredDeviceHealthCollection devicehealth_get_last_device_health(device_id)

getLastDeviceHealth devicehealth

Returns information about the last known health counters from the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DevicehealthApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose last health counters should be returned

try:
    # getLastDeviceHealth devicehealth
    api_response = api_instance.devicehealth_get_last_device_health(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicehealthApi->devicehealth_get_last_device_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose last health counters should be returned | 

### Return type

[**StoredDeviceHealthCollection**](StoredDeviceHealthCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


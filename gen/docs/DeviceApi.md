# swagger_client.DeviceApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_get_all_devices**](DeviceApi.md#device_get_all_devices) | **GET** /device | getAllDevices device
[**device_get_device_by_id**](DeviceApi.md#device_get_device_by_id) | **GET** /device/id/{deviceId} | getDeviceById device
[**device_get_device_by_serial_number**](DeviceApi.md#device_get_device_by_serial_number) | **GET** /device/{serialNumber} | getDeviceBySerialNumber device
[**device_get_devices_by_site**](DeviceApi.md#device_get_devices_by_site) | **GET** /site/{siteId}/devices | getDevicesBySite device

# **device_get_all_devices**
> StoredDeviceCollection device_get_all_devices()

getAllDevices device

Returns information about all devices to which the client has access

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))

try:
    # getAllDevices device
    api_response = api_instance.device_get_all_devices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_all_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredDeviceCollection**](StoredDeviceCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_device_by_id**
> AkapiStoredDevice device_get_device_by_id(device_id)

getDeviceById device

Returns information about the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose information should be returned

try:
    # getDeviceById device
    api_response = api_instance.device_get_device_by_id(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose information should be returned | 

### Return type

[**AkapiStoredDevice**](AkapiStoredDevice.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_device_by_serial_number**
> AkapiStoredDevice device_get_device_by_serial_number(serial_number)

getDeviceBySerialNumber device

Returns information about the device corresponding to the specified serial number

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))
serial_number = 'serial_number_example' # str | Serial number of the device whose information should be returned

try:
    # getDeviceBySerialNumber device
    api_response = api_instance.device_get_device_by_serial_number(serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_device_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| Serial number of the device whose information should be returned | 

### Return type

[**AkapiStoredDevice**](AkapiStoredDevice.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get_devices_by_site**
> StoredDeviceCollection device_get_devices_by_site(site_id)

getDevicesBySite device

Get All Devices by Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose devices should be returned

try:
    # getDevicesBySite device
    api_response = api_instance.device_get_devices_by_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_devices_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose devices should be returned | 

### Return type

[**StoredDeviceCollection**](StoredDeviceCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


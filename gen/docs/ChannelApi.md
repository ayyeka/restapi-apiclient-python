# swagger_client.ChannelApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_get_all_channels**](ChannelApi.md#channel_get_all_channels) | **GET** /channel | getAllChannels channel
[**channel_get_channel_by_id**](ChannelApi.md#channel_get_channel_by_id) | **GET** /channel/{channelId} | getChannelById channel
[**channel_get_channels_by_device**](ChannelApi.md#channel_get_channels_by_device) | **GET** /device/{deviceId}/channels | getChannelsByDevice channel

# **channel_get_all_channels**
> StoredChannelCollection channel_get_all_channels()

getAllChannels channel

Returns information about all channels to which the client has access

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelApi(swagger_client.ApiClient(configuration))

try:
    # getAllChannels channel
    api_response = api_instance.channel_get_all_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->channel_get_all_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredChannelCollection**](StoredChannelCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_get_channel_by_id**
> AkapiStoredChannel channel_get_channel_by_id(channel_id)

getChannelById channel

Returns information about the specified channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelApi(swagger_client.ApiClient(configuration))
channel_id = 789 # int | ID of the channel whose information should be returned

try:
    # getChannelById channel
    api_response = api_instance.channel_get_channel_by_id(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->channel_get_channel_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| ID of the channel whose information should be returned | 

### Return type

[**AkapiStoredChannel**](AkapiStoredChannel.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_get_channels_by_device**
> StoredChannelCollection channel_get_channels_by_device(device_id)

getChannelsByDevice channel

Returns information about all channels of a specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelApi(swagger_client.ApiClient(configuration))
device_id = 789 # int | ID of the device whose channels should be returned

try:
    # getChannelsByDevice channel
    api_response = api_instance.channel_get_channels_by_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->channel_get_channels_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of the device whose channels should be returned | 

### Return type

[**StoredChannelCollection**](StoredChannelCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


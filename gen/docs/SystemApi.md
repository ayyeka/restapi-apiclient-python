# swagger_client.SystemApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_health_status**](SystemApi.md#system_health_status) | **GET** /health | healthStatus system

# **system_health_status**
> str system_health_status()

healthStatus system

Can be used to determine if the system is in a healthy state. When healthy, HTTP 200 is returned. When unhealthy, HTTP 503. Note: only use the HTTP status code to determine the health status since the response body is optional.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # healthStatus system
    api_response = api_instance.system_health_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_health_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


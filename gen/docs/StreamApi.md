# swagger_client.StreamApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_get_all_stream_custom_attribute_values**](StreamApi.md#stream_get_all_stream_custom_attribute_values) | **GET** /stream/customAttributes | getAllStreamCustomAttributeValues stream
[**stream_get_all_stream_custom_attributes_names**](StreamApi.md#stream_get_all_stream_custom_attributes_names) | **GET** /stream/customAttributes/names | getAllStreamCustomAttributesNames stream
[**stream_get_all_streams**](StreamApi.md#stream_get_all_streams) | **GET** /stream | getAllStreams stream
[**stream_get_stream_by_id**](StreamApi.md#stream_get_stream_by_id) | **GET** /stream/{streamId} | getStreamById stream
[**stream_get_stream_custom_attribute_values**](StreamApi.md#stream_get_stream_custom_attribute_values) | **GET** /stream/{streamId}/customAttributes | getStreamCustomAttributeValues stream
[**stream_get_stream_custom_attribute_values_by_site**](StreamApi.md#stream_get_stream_custom_attribute_values_by_site) | **GET** /site/{siteId}/streams/customAttributes | getStreamCustomAttributeValuesBySite stream
[**stream_get_streams_by_site**](StreamApi.md#stream_get_streams_by_site) | **GET** /site/{siteId}/streams | getStreamsBySite stream
[**stream_set_stream_custom_attribute_values**](StreamApi.md#stream_set_stream_custom_attribute_values) | **POST** /stream/customAttributes | setStreamCustomAttributeValues stream

# **stream_get_all_stream_custom_attribute_values**
> StoredStreamCustomAttributeValueCollection stream_get_all_stream_custom_attribute_values()

getAllStreamCustomAttributeValues stream

Get All Streams' Custom Attribute Names and Values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))

try:
    # getAllStreamCustomAttributeValues stream
    api_response = api_instance.stream_get_all_stream_custom_attribute_values()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_all_stream_custom_attribute_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredStreamCustomAttributeValueCollection**](StoredStreamCustomAttributeValueCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_all_stream_custom_attributes_names**
> StoredStreamCustomAttributeNameCollection stream_get_all_stream_custom_attributes_names()

getAllStreamCustomAttributesNames stream

Get All Streams' Custom Attributes Names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))

try:
    # getAllStreamCustomAttributesNames stream
    api_response = api_instance.stream_get_all_stream_custom_attributes_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_all_stream_custom_attributes_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredStreamCustomAttributeNameCollection**](StoredStreamCustomAttributeNameCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_all_streams**
> StoredStreamCollection stream_get_all_streams()

getAllStreams stream

Get All Streams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))

try:
    # getAllStreams stream
    api_response = api_instance.stream_get_all_streams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_all_streams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredStreamCollection**](StoredStreamCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_stream_by_id**
> AkapiStoredStream stream_get_stream_by_id(stream_id)

getStreamById stream

Get Stream by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose recent samples should be returned

try:
    # getStreamById stream
    api_response = api_instance.stream_get_stream_by_id(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_stream_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose recent samples should be returned | 

### Return type

[**AkapiStoredStream**](AkapiStoredStream.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_stream_custom_attribute_values**
> StoredStreamCustomAttributeValueCollection stream_get_stream_custom_attribute_values(stream_id)

getStreamCustomAttributeValues stream

Returns information about the custom attributes of a specified stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose custom attributes should be returned

try:
    # getStreamCustomAttributeValues stream
    api_response = api_instance.stream_get_stream_custom_attribute_values(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_stream_custom_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose custom attributes should be returned | 

### Return type

[**StoredStreamCustomAttributeValueCollection**](StoredStreamCustomAttributeValueCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_stream_custom_attribute_values_by_site**
> StoredStreamCustomAttributeValueCollection stream_get_stream_custom_attribute_values_by_site(site_id)

getStreamCustomAttributeValuesBySite stream

Get Custom Attributes of a Site's Streams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose streams' custom attributes should be returned

try:
    # getStreamCustomAttributeValuesBySite stream
    api_response = api_instance.stream_get_stream_custom_attribute_values_by_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_stream_custom_attribute_values_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose streams&#x27; custom attributes should be returned | 

### Return type

[**StoredStreamCustomAttributeValueCollection**](StoredStreamCustomAttributeValueCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_get_streams_by_site**
> StoredStreamCollection stream_get_streams_by_site(site_id)

getStreamsBySite stream

Get All Streams by Site (incl. gps)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose devices should be returned

try:
    # getStreamsBySite stream
    api_response = api_instance.stream_get_streams_by_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->stream_get_streams_by_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose devices should be returned | 

### Return type

[**StoredStreamCollection**](StoredStreamCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_set_stream_custom_attribute_values**
> stream_set_stream_custom_attribute_values(body)

setStreamCustomAttributeValues stream

Update Stream Custom Attributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetStreamCustomAttributeValuesRequestBody() # SetStreamCustomAttributeValuesRequestBody | 

try:
    # setStreamCustomAttributeValues stream
    api_instance.stream_set_stream_custom_attribute_values(body)
except ApiException as e:
    print("Exception when calling StreamApi->stream_set_stream_custom_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetStreamCustomAttributeValuesRequestBody**](SetStreamCustomAttributeValuesRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


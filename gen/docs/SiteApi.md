# swagger_client.SiteApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_get_all_site_custom_attribute_values**](SiteApi.md#site_get_all_site_custom_attribute_values) | **GET** /site/customAttributes | getAllSiteCustomAttributeValues site
[**site_get_all_site_custom_attributes_names**](SiteApi.md#site_get_all_site_custom_attributes_names) | **GET** /site/customAttributes/names | getAllSiteCustomAttributesNames site
[**site_get_all_sites**](SiteApi.md#site_get_all_sites) | **GET** /site | getAllSites site
[**site_get_site_by_id**](SiteApi.md#site_get_site_by_id) | **GET** /site/{siteId} | getSiteById site
[**site_get_site_custom_attribute_values**](SiteApi.md#site_get_site_custom_attribute_values) | **GET** /site/{siteId}/customAttributes | getSiteCustomAttributeValues site
[**site_set_site_custom_attribute_values**](SiteApi.md#site_set_site_custom_attribute_values) | **POST** /site/customAttributes | setSiteCustomAttributeValues site

# **site_get_all_site_custom_attribute_values**
> StoredSiteCustomAttributeValueCollection site_get_all_site_custom_attribute_values()

getAllSiteCustomAttributeValues site

Get All Sites' Custom Attribute Names and Values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))

try:
    # getAllSiteCustomAttributeValues site
    api_response = api_instance.site_get_all_site_custom_attribute_values()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->site_get_all_site_custom_attribute_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredSiteCustomAttributeValueCollection**](StoredSiteCustomAttributeValueCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_get_all_site_custom_attributes_names**
> StoredSiteCustomAttributeNameCollection site_get_all_site_custom_attributes_names()

getAllSiteCustomAttributesNames site

Get All Sites' Custom Attributes Names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))

try:
    # getAllSiteCustomAttributesNames site
    api_response = api_instance.site_get_all_site_custom_attributes_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->site_get_all_site_custom_attributes_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredSiteCustomAttributeNameCollection**](StoredSiteCustomAttributeNameCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_get_all_sites**
> StoredSiteCollection site_get_all_sites()

getAllSites site

Get All Sites

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))

try:
    # getAllSites site
    api_response = api_instance.site_get_all_sites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->site_get_all_sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredSiteCollection**](StoredSiteCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_get_site_by_id**
> AkapiStoredSite site_get_site_by_id(site_id)

getSiteById site

Get Site by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose recent samples should be returned

try:
    # getSiteById site
    api_response = api_instance.site_get_site_by_id(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->site_get_site_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose recent samples should be returned | 

### Return type

[**AkapiStoredSite**](AkapiStoredSite.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_get_site_custom_attribute_values**
> StoredSiteCustomAttributeValueCollection site_get_site_custom_attribute_values(site_id)

getSiteCustomAttributeValues site

Returns information about the custom attributes of a specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))
site_id = 789 # int | ID of the site whose custom attributes should be returned

try:
    # getSiteCustomAttributeValues site
    api_response = api_instance.site_get_site_custom_attribute_values(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->site_get_site_custom_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| ID of the site whose custom attributes should be returned | 

### Return type

[**StoredSiteCustomAttributeValueCollection**](StoredSiteCustomAttributeValueCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_set_site_custom_attribute_values**
> site_set_site_custom_attribute_values(body)

setSiteCustomAttributeValues site

Update Site Custom Attributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetSiteCustomAttributeValuesRequestBody() # SetSiteCustomAttributeValuesRequestBody | 

try:
    # setSiteCustomAttributeValues site
    api_instance.site_set_site_custom_attribute_values(body)
except ApiException as e:
    print("Exception when calling SiteApi->site_set_site_custom_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetSiteCustomAttributeValuesRequestBody**](SetSiteCustomAttributeValuesRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


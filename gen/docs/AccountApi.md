# swagger_client.AccountApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get_all_organizations**](AccountApi.md#account_get_all_organizations) | **GET** /account/organization | getAllOrganizations account
[**account_get_organization_by_id**](AccountApi.md#account_get_organization_by_id) | **GET** /account/organization/{organizationId} | getOrganizationById account

# **account_get_all_organizations**
> StoredOrganizationCollection account_get_all_organizations()

getAllOrganizations account

Returns all organizations belonging to the account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # getAllOrganizations account
    api_response = api_instance.account_get_all_organizations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_all_organizations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredOrganizationCollection**](StoredOrganizationCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_organization_by_id**
> AkapiStoredOrganization account_get_organization_by_id(organization_id)

getOrganizationById account

Returns information about the specified account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
organization_id = 789 # int | ID of the organization whose information should be returned

try:
    # getOrganizationById account
    api_response = api_instance.account_get_organization_by_id(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_organization_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the organization whose information should be returned | 

### Return type

[**AkapiStoredOrganization**](AkapiStoredOrganization.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.UserApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_all_users**](UserApi.md#user_get_all_users) | **GET** /user | getAllUsers user
[**user_get_ui_preferences**](UserApi.md#user_get_ui_preferences) | **GET** /user/uiPreferences | getUIPreferences user
[**user_get_user_by_id**](UserApi.md#user_get_user_by_id) | **GET** /user/{userId} | getUserById user

# **user_get_all_users**
> StoredUserCollection user_get_all_users()

getAllUsers user

Returns all users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # getAllUsers user
    api_response = api_instance.user_get_all_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_all_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredUserCollection**](StoredUserCollection.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_ui_preferences**
> StoredUIPreferences user_get_ui_preferences()

getUIPreferences user

Returns the current user's UI preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # getUIPreferences user
    api_response = api_instance.user_get_ui_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_ui_preferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoredUIPreferences**](StoredUIPreferences.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_user_by_id**
> StoredUserDetails user_get_user_by_id(user_id)

getUserById user

Returns information about the specified user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | ID of the user whose information should be returned

try:
    # getUserById user
    api_response = api_instance.user_get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user whose information should be returned | 

### Return type

[**StoredUserDetails**](StoredUserDetails.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


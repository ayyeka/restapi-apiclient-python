# swagger_client.SampleimageApi

All URIs are relative to *https://restapi.ayyeka.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sampleimage_get_last_sample_image_by_stream**](SampleimageApi.md#sampleimage_get_last_sample_image_by_stream) | **GET** /stream/{streamId}/sample/image/last | getLastSampleImageByStream sampleimage
[**sampleimage_get_sample_image_by_id**](SampleimageApi.md#sampleimage_get_sample_image_by_id) | **GET** /sample/image/id/{imageId} | getSampleImageById sampleimage
[**sampleimage_get_samples_image_batch**](SampleimageApi.md#sampleimage_get_samples_image_batch) | **GET** /sample/image/batch | getSamplesImageBatch sampleimage
[**sampleimage_get_samples_image_batch_by_stream**](SampleimageApi.md#sampleimage_get_samples_image_batch_by_stream) | **GET** /stream/{streamId}/sample/image/batch | getSamplesImageBatchByStream sampleimage

# **sampleimage_get_last_sample_image_by_stream**
> StoredSampleImage sampleimage_get_last_sample_image_by_stream(stream_id)

getLastSampleImageByStream sampleimage

Get Last Image Sample from Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleimageApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose last sample should be returned

try:
    # getLastSampleImageByStream sampleimage
    api_response = api_instance.sampleimage_get_last_sample_image_by_stream(stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleimageApi->sampleimage_get_last_sample_image_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose last sample should be returned | 

### Return type

[**StoredSampleImage**](StoredSampleImage.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sampleimage_get_sample_image_by_id**
> StoredSampleImage sampleimage_get_sample_image_by_id(image_id)

getSampleImageById sampleimage

Get Image Sample by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleimageApi(swagger_client.ApiClient(configuration))
image_id = 789 # int | Image Id of the image that should be returned

try:
    # getSampleImageById sampleimage
    api_response = api_instance.sampleimage_get_sample_image_by_id(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleimageApi->sampleimage_get_sample_image_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **int**| Image Id of the image that should be returned | 

### Return type

[**StoredSampleImage**](StoredSampleImage.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sampleimage_get_samples_image_batch**
> StoredSampleImageBatch sampleimage_get_samples_image_batch(sample_date)

getSamplesImageBatch sampleimage

Get Image Samples Batch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleimageApi(swagger_client.ApiClient(configuration))
sample_date = 789 # int | DateTime of oldest sample in batch in Unix Time format

try:
    # getSamplesImageBatch sampleimage
    api_response = api_instance.sampleimage_get_samples_image_batch(sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleimageApi->sampleimage_get_samples_image_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_date** | **int**| DateTime of oldest sample in batch in Unix Time format | 

### Return type

[**StoredSampleImageBatch**](StoredSampleImageBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sampleimage_get_samples_image_batch_by_stream**
> StoredSampleImageBatch sampleimage_get_samples_image_batch_by_stream(stream_id, sample_date)

getSamplesImageBatchByStream sampleimage

Get Image Samples Batch By Stream

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SampleimageApi(swagger_client.ApiClient(configuration))
stream_id = 789 # int | ID of the stream whose last sample should be returned
sample_date = 789 # int | DateTime of oldest sample in batch in Unix Time format

try:
    # getSamplesImageBatchByStream sampleimage
    api_response = api_instance.sampleimage_get_samples_image_batch_by_stream(stream_id, sample_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleimageApi->sampleimage_get_samples_image_batch_by_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **int**| ID of the stream whose last sample should be returned | 
 **sample_date** | **int**| DateTime of oldest sample in batch in Unix Time format | 

### Return type

[**StoredSampleImageBatch**](StoredSampleImageBatch.md)

### Authorization

[jwt_header_Authorization](../README.md#jwt_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


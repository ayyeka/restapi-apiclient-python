# ThresholdLevel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment for the threshold&#x27;s level | 
**display_name** | **str** | Name of the threshold&#x27;s level | 
**false_alarm_filter** | **int** | Threshold triggered interval in seconds | [default to 0]
**lower_limit** | **float** | Lower limit of the threshold range | 
**notification_actions** | [**list[ThresholdActionNotification]**](ThresholdActionNotification.md) |  | [optional] 
**output_actions** | [**list[ThresholdActionOutput]**](ThresholdActionOutput.md) |  | [optional] 
**sample_actions** | [**list[ThresholdActionSample]**](ThresholdActionSample.md) |  | [optional] 
**sample_interval** | **int** | Sample interval in seconds how often the device streams | [default to 300]
**transmission_interval** | **str** | Transmission device report interval | [default to 'normal']
**transmit_immediately** | **bool** | When a device reached threshold zone does he need to transmit immediately | [default to False]
**upper_limit** | **float** | Upper limit of the threshold range | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


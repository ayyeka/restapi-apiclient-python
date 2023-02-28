# coding: utf-8

"""
    RESTAPI Service

    RESTful API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SamplerfidApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def samplerfid_ack_sample_rfid_batch(self, sample_id, **kwargs):  # noqa: E501
        """ackSampleRFIDBatch samplerfid  # noqa: E501

        Notify which Sample RFID was the Last Sample RFID Received by the Client  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_ack_sample_rfid_batch(sample_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sample_id: The value to set in the last delivered sample RFID id internal field (required)
        :param str agent: User-Agent information, stored in the cloud to identify the applications that use the sampleRFIDs batch APIs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_ack_sample_rfid_batch_with_http_info(sample_id, **kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_ack_sample_rfid_batch_with_http_info(sample_id, **kwargs)  # noqa: E501
            return data

    def samplerfid_ack_sample_rfid_batch_with_http_info(self, sample_id, **kwargs):  # noqa: E501
        """ackSampleRFIDBatch samplerfid  # noqa: E501

        Notify which Sample RFID was the Last Sample RFID Received by the Client  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_ack_sample_rfid_batch_with_http_info(sample_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sample_id: The value to set in the last delivered sample RFID id internal field (required)
        :param str agent: User-Agent information, stored in the cloud to identify the applications that use the sampleRFIDs batch APIs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sample_id', 'agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_ack_sample_rfid_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sample_id' is set
        if ('sample_id' not in params or
                params['sample_id'] is None):
            raise ValueError("Missing the required parameter `sample_id` when calling `samplerfid_ack_sample_rfid_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sample_id' in params:
            query_params.append(('sample_id', params['sample_id']))  # noqa: E501
        if 'agent' in params:
            query_params.append(('agent', params['agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/sample/rfid/batch/ack', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_get_last_sample_rfid_batch(self, **kwargs):  # noqa: E501
        """getLastSampleRFIDBatch samplerfid  # noqa: E501

        Get the Last Delivered Sample RFID of the Last Delivered Samples RFID Batch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_last_sample_rfid_batch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AkapiStoredSampleRfid
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_get_last_sample_rfid_batch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_get_last_sample_rfid_batch_with_http_info(**kwargs)  # noqa: E501
            return data

    def samplerfid_get_last_sample_rfid_batch_with_http_info(self, **kwargs):  # noqa: E501
        """getLastSampleRFIDBatch samplerfid  # noqa: E501

        Get the Last Delivered Sample RFID of the Last Delivered Samples RFID Batch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_last_sample_rfid_batch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AkapiStoredSampleRfid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_get_last_sample_rfid_batch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/sample/rfid/batch/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AkapiStoredSampleRfid',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_get_last_sample_rfidby_stream(self, stream_id, **kwargs):  # noqa: E501
        """getLastSampleRFIDByStream samplerfid  # noqa: E501

        Get Last Sample from Stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_last_sample_rfidby_stream(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose last sample should be returned (required)
        :return: AkapiStoredSampleRfid
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_get_last_sample_rfidby_stream_with_http_info(stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_get_last_sample_rfidby_stream_with_http_info(stream_id, **kwargs)  # noqa: E501
            return data

    def samplerfid_get_last_sample_rfidby_stream_with_http_info(self, stream_id, **kwargs):  # noqa: E501
        """getLastSampleRFIDByStream samplerfid  # noqa: E501

        Get Last Sample from Stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_last_sample_rfidby_stream_with_http_info(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose last sample should be returned (required)
        :return: AkapiStoredSampleRfid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stream_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_get_last_sample_rfidby_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params or
                params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `samplerfid_get_last_sample_rfidby_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/stream/{streamId}/sample/rfid/last', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AkapiStoredSampleRfid',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_get_samples_rfid_batch(self, **kwargs):  # noqa: E501
        """getSamplesRFIDBatch samplerfid  # noqa: E501

        Get a Batch of New Samples RFID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfid_batch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool enable_ack: If set to false, then the internal last delivered sample RFID id value is set to the last sample RFID ID in the batch sent in response to this call. If set to true, then the internal last delivered sample RFID id remains untouched by this call. We recommend setting this parameter to 'true' and calling ackSamplesRFIDBatch to update the last delivered sample RFID id field
        :param int sample_id: Specifies to send samples RFID with an ID number strictly higher than the sampleId. For example, if the sampleId value is 1234, the response could include samples RFID with IDs such as [1235, 1240, 1241]
        :param int backfill_hours: Specifies to send samples RFID starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples RFID of the past 24 hours
        :return: StoredSampleRFIDBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_get_samples_rfid_batch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_get_samples_rfid_batch_with_http_info(**kwargs)  # noqa: E501
            return data

    def samplerfid_get_samples_rfid_batch_with_http_info(self, **kwargs):  # noqa: E501
        """getSamplesRFIDBatch samplerfid  # noqa: E501

        Get a Batch of New Samples RFID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfid_batch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool enable_ack: If set to false, then the internal last delivered sample RFID id value is set to the last sample RFID ID in the batch sent in response to this call. If set to true, then the internal last delivered sample RFID id remains untouched by this call. We recommend setting this parameter to 'true' and calling ackSamplesRFIDBatch to update the last delivered sample RFID id field
        :param int sample_id: Specifies to send samples RFID with an ID number strictly higher than the sampleId. For example, if the sampleId value is 1234, the response could include samples RFID with IDs such as [1235, 1240, 1241]
        :param int backfill_hours: Specifies to send samples RFID starting this many hours ago. For example, if the backfillHours value is 24, this is a request to provide all samples RFID of the past 24 hours
        :return: StoredSampleRFIDBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enable_ack', 'sample_id', 'backfill_hours']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_get_samples_rfid_batch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enable_ack' in params:
            query_params.append(('enableAck', params['enable_ack']))  # noqa: E501
        if 'sample_id' in params:
            query_params.append(('sampleId', params['sample_id']))  # noqa: E501
        if 'backfill_hours' in params:
            query_params.append(('backfillHours', params['backfill_hours']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/sample/rfid/batch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredSampleRFIDBatch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_get_samples_rfid_batch_by_site(self, site_id, sample_date, **kwargs):  # noqa: E501
        """getSamplesRFIDBatchBySite samplerfid  # noqa: E501

        Get Batch of Recent Samples RFID of a Site  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfid_batch_by_site(site_id, sample_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose recent samples should be returned (required)
        :param int sample_date: The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) (required)
        :return: StoredSampleRFIDBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_get_samples_rfid_batch_by_site_with_http_info(site_id, sample_date, **kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_get_samples_rfid_batch_by_site_with_http_info(site_id, sample_date, **kwargs)  # noqa: E501
            return data

    def samplerfid_get_samples_rfid_batch_by_site_with_http_info(self, site_id, sample_date, **kwargs):  # noqa: E501
        """getSamplesRFIDBatchBySite samplerfid  # noqa: E501

        Get Batch of Recent Samples RFID of a Site  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfid_batch_by_site_with_http_info(site_id, sample_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose recent samples should be returned (required)
        :param int sample_date: The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) (required)
        :return: StoredSampleRFIDBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'sample_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_get_samples_rfid_batch_by_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `samplerfid_get_samples_rfid_batch_by_site`")  # noqa: E501
        # verify the required parameter 'sample_date' is set
        if ('sample_date' not in params or
                params['sample_date'] is None):
            raise ValueError("Missing the required parameter `sample_date` when calling `samplerfid_get_samples_rfid_batch_by_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []
        if 'sample_date' in params:
            query_params.append(('sampleDate', params['sample_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/site/{siteId}/sample/rfid/batch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredSampleRFIDBatch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_get_samples_rfid_batch_by_stream(self, stream_id, sample_date, **kwargs):  # noqa: E501
        """getSamplesRFIDBatchByStream samplerfid  # noqa: E501

        Get Batch of Recent Samples RFID of a Stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfid_batch_by_stream(stream_id, sample_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose recent samples should be returned (required)
        :param int sample_date: The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) (required)
        :return: StoredSampleRFIDBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_get_samples_rfid_batch_by_stream_with_http_info(stream_id, sample_date, **kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_get_samples_rfid_batch_by_stream_with_http_info(stream_id, sample_date, **kwargs)  # noqa: E501
            return data

    def samplerfid_get_samples_rfid_batch_by_stream_with_http_info(self, stream_id, sample_date, **kwargs):  # noqa: E501
        """getSamplesRFIDBatchByStream samplerfid  # noqa: E501

        Get Batch of Recent Samples RFID of a Stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfid_batch_by_stream_with_http_info(stream_id, sample_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose recent samples should be returned (required)
        :param int sample_date: The sampling date and time of the oldest sample in the batch (Unix time, seconds since January 1, 1970 UTC.) (required)
        :return: StoredSampleRFIDBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stream_id', 'sample_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_get_samples_rfid_batch_by_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params or
                params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `samplerfid_get_samples_rfid_batch_by_stream`")  # noqa: E501
        # verify the required parameter 'sample_date' is set
        if ('sample_date' not in params or
                params['sample_date'] is None):
            raise ValueError("Missing the required parameter `sample_date` when calling `samplerfid_get_samples_rfid_batch_by_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']  # noqa: E501

        query_params = []
        if 'sample_date' in params:
            query_params.append(('sampleDate', params['sample_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/stream/{streamId}/sample/rfid/batch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredSampleRFIDBatch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_get_samples_rfidby_stream(self, stream_id, **kwargs):  # noqa: E501
        """getSamplesRFIDByStream samplerfid  # noqa: E501

        Returns up to 100 samples RFID from the specified stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfidby_stream(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose recent samples should be returned (required)
        :param int last_sample_id: ID of the oldest sample from which to start returning samples
        :return: StoredSampleRFIDCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_get_samples_rfidby_stream_with_http_info(stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_get_samples_rfidby_stream_with_http_info(stream_id, **kwargs)  # noqa: E501
            return data

    def samplerfid_get_samples_rfidby_stream_with_http_info(self, stream_id, **kwargs):  # noqa: E501
        """getSamplesRFIDByStream samplerfid  # noqa: E501

        Returns up to 100 samples RFID from the specified stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_get_samples_rfidby_stream_with_http_info(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose recent samples should be returned (required)
        :param int last_sample_id: ID of the oldest sample from which to start returning samples
        :return: StoredSampleRFIDCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stream_id', 'last_sample_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_get_samples_rfidby_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params or
                params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `samplerfid_get_samples_rfidby_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']  # noqa: E501

        query_params = []
        if 'last_sample_id' in params:
            query_params.append(('lastSampleId', params['last_sample_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/stream/{streamId}/sample/rfid', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredSampleRFIDCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def samplerfid_set_backfill_samples_rfid_batch(self, sample_date, **kwargs):  # noqa: E501
        """setBackfillSamplesRFIDBatch samplerfid  # noqa: E501

        Reset the DateTime starting point for the next Samples RFID Batch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_set_backfill_samples_rfid_batch(sample_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sample_date: The date and time to use for setting the last delivered sample id internal field (Unix time, seconds since January 1, 1970 UTC.). The API resets the internal last delivered sample id value to the id of the sample whose date and time is closest to the specified date and time (required)
        :param str agent: ser-Agent information, stored in the cloud to identify the applications that use the samples batch APIs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.samplerfid_set_backfill_samples_rfid_batch_with_http_info(sample_date, **kwargs)  # noqa: E501
        else:
            (data) = self.samplerfid_set_backfill_samples_rfid_batch_with_http_info(sample_date, **kwargs)  # noqa: E501
            return data

    def samplerfid_set_backfill_samples_rfid_batch_with_http_info(self, sample_date, **kwargs):  # noqa: E501
        """setBackfillSamplesRFIDBatch samplerfid  # noqa: E501

        Reset the DateTime starting point for the next Samples RFID Batch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.samplerfid_set_backfill_samples_rfid_batch_with_http_info(sample_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sample_date: The date and time to use for setting the last delivered sample id internal field (Unix time, seconds since January 1, 1970 UTC.). The API resets the internal last delivered sample id value to the id of the sample whose date and time is closest to the specified date and time (required)
        :param str agent: ser-Agent information, stored in the cloud to identify the applications that use the samples batch APIs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sample_date', 'agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method samplerfid_set_backfill_samples_rfid_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sample_date' is set
        if ('sample_date' not in params or
                params['sample_date'] is None):
            raise ValueError("Missing the required parameter `sample_date` when calling `samplerfid_set_backfill_samples_rfid_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sample_date' in params:
            query_params.append(('sample_date', params['sample_date']))  # noqa: E501
        if 'agent' in params:
            query_params.append(('agent', params['agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/sample/rfid/batch/backfill', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
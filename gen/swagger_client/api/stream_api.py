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


class StreamApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def stream_get_all_stream_custom_attribute_values(self, **kwargs):  # noqa: E501
        """getAllStreamCustomAttributeValues stream  # noqa: E501

        Get All Streams' Custom Attribute Names and Values  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_all_stream_custom_attribute_values(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredStreamCustomAttributeValueCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_all_stream_custom_attribute_values_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_all_stream_custom_attribute_values_with_http_info(**kwargs)  # noqa: E501
            return data

    def stream_get_all_stream_custom_attribute_values_with_http_info(self, **kwargs):  # noqa: E501
        """getAllStreamCustomAttributeValues stream  # noqa: E501

        Get All Streams' Custom Attribute Names and Values  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_all_stream_custom_attribute_values_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredStreamCustomAttributeValueCollection
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
                    " to method stream_get_all_stream_custom_attribute_values" % key
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
            '/stream/customAttributes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredStreamCustomAttributeValueCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_get_all_stream_custom_attributes_names(self, **kwargs):  # noqa: E501
        """getAllStreamCustomAttributesNames stream  # noqa: E501

        Get All Streams' Custom Attributes Names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_all_stream_custom_attributes_names(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredStreamCustomAttributeNameCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_all_stream_custom_attributes_names_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_all_stream_custom_attributes_names_with_http_info(**kwargs)  # noqa: E501
            return data

    def stream_get_all_stream_custom_attributes_names_with_http_info(self, **kwargs):  # noqa: E501
        """getAllStreamCustomAttributesNames stream  # noqa: E501

        Get All Streams' Custom Attributes Names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_all_stream_custom_attributes_names_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredStreamCustomAttributeNameCollection
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
                    " to method stream_get_all_stream_custom_attributes_names" % key
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
            '/stream/customAttributes/names', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredStreamCustomAttributeNameCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_get_all_streams(self, **kwargs):  # noqa: E501
        """getAllStreams stream  # noqa: E501

        Get All Streams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_all_streams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredStreamCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_all_streams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_all_streams_with_http_info(**kwargs)  # noqa: E501
            return data

    def stream_get_all_streams_with_http_info(self, **kwargs):  # noqa: E501
        """getAllStreams stream  # noqa: E501

        Get All Streams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_all_streams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredStreamCollection
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
                    " to method stream_get_all_streams" % key
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
            '/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredStreamCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_get_stream_by_id(self, stream_id, **kwargs):  # noqa: E501
        """getStreamById stream  # noqa: E501

        Get Stream by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_stream_by_id(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose recent samples should be returned (required)
        :return: AkapiStoredStream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_stream_by_id_with_http_info(stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_stream_by_id_with_http_info(stream_id, **kwargs)  # noqa: E501
            return data

    def stream_get_stream_by_id_with_http_info(self, stream_id, **kwargs):  # noqa: E501
        """getStreamById stream  # noqa: E501

        Get Stream by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_stream_by_id_with_http_info(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose recent samples should be returned (required)
        :return: AkapiStoredStream
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
                    " to method stream_get_stream_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params or
                params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `stream_get_stream_by_id`")  # noqa: E501

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
            '/stream/{streamId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AkapiStoredStream',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_get_stream_custom_attribute_values(self, stream_id, **kwargs):  # noqa: E501
        """getStreamCustomAttributeValues stream  # noqa: E501

        Returns information about the custom attributes of a specified stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_stream_custom_attribute_values(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose custom attributes should be returned (required)
        :return: StoredStreamCustomAttributeValueCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_stream_custom_attribute_values_with_http_info(stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_stream_custom_attribute_values_with_http_info(stream_id, **kwargs)  # noqa: E501
            return data

    def stream_get_stream_custom_attribute_values_with_http_info(self, stream_id, **kwargs):  # noqa: E501
        """getStreamCustomAttributeValues stream  # noqa: E501

        Returns information about the custom attributes of a specified stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_stream_custom_attribute_values_with_http_info(stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int stream_id: ID of the stream whose custom attributes should be returned (required)
        :return: StoredStreamCustomAttributeValueCollection
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
                    " to method stream_get_stream_custom_attribute_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params or
                params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `stream_get_stream_custom_attribute_values`")  # noqa: E501

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
            '/stream/{streamId}/customAttributes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredStreamCustomAttributeValueCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_get_stream_custom_attribute_values_by_site(self, site_id, **kwargs):  # noqa: E501
        """getStreamCustomAttributeValuesBySite stream  # noqa: E501

        Get Custom Attributes of a Site's Streams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_stream_custom_attribute_values_by_site(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose streams' custom attributes should be returned (required)
        :return: StoredStreamCustomAttributeValueCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_stream_custom_attribute_values_by_site_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_stream_custom_attribute_values_by_site_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def stream_get_stream_custom_attribute_values_by_site_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """getStreamCustomAttributeValuesBySite stream  # noqa: E501

        Get Custom Attributes of a Site's Streams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_stream_custom_attribute_values_by_site_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose streams' custom attributes should be returned (required)
        :return: StoredStreamCustomAttributeValueCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stream_get_stream_custom_attribute_values_by_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `stream_get_stream_custom_attribute_values_by_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

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
            '/site/{siteId}/streams/customAttributes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredStreamCustomAttributeValueCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_get_streams_by_site(self, site_id, **kwargs):  # noqa: E501
        """getStreamsBySite stream  # noqa: E501

        Get All Streams by Site (incl. gps)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_streams_by_site(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose devices should be returned (required)
        :return: StoredStreamCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_get_streams_by_site_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stream_get_streams_by_site_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def stream_get_streams_by_site_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """getStreamsBySite stream  # noqa: E501

        Get All Streams by Site (incl. gps)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_get_streams_by_site_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose devices should be returned (required)
        :return: StoredStreamCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stream_get_streams_by_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `stream_get_streams_by_site`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

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
            '/site/{siteId}/streams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredStreamCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_set_stream_custom_attribute_values(self, body, **kwargs):  # noqa: E501
        """setStreamCustomAttributeValues stream  # noqa: E501

        Update Stream Custom Attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_set_stream_custom_attribute_values(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SetStreamCustomAttributeValuesRequestBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_set_stream_custom_attribute_values_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.stream_set_stream_custom_attribute_values_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def stream_set_stream_custom_attribute_values_with_http_info(self, body, **kwargs):  # noqa: E501
        """setStreamCustomAttributeValues stream  # noqa: E501

        Update Stream Custom Attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_set_stream_custom_attribute_values_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SetStreamCustomAttributeValuesRequestBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stream_set_stream_custom_attribute_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `stream_set_stream_custom_attribute_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt_header_Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/stream/customAttributes', 'POST',
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

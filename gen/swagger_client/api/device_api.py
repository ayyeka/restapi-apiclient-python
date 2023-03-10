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


class DeviceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def device_get_all_devices(self, **kwargs):  # noqa: E501
        """getAllDevices device  # noqa: E501

        Returns information about all devices to which the client has access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_all_devices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredDeviceCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_get_all_devices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.device_get_all_devices_with_http_info(**kwargs)  # noqa: E501
            return data

    def device_get_all_devices_with_http_info(self, **kwargs):  # noqa: E501
        """getAllDevices device  # noqa: E501

        Returns information about all devices to which the client has access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_all_devices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StoredDeviceCollection
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
                    " to method device_get_all_devices" % key
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
            '/device', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredDeviceCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_get_device_by_id(self, device_id, **kwargs):  # noqa: E501
        """getDeviceById device  # noqa: E501

        Returns information about the specified device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_device_by_id(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int device_id: ID of the device whose information should be returned (required)
        :return: AkapiStoredDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_get_device_by_id_with_http_info(device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.device_get_device_by_id_with_http_info(device_id, **kwargs)  # noqa: E501
            return data

    def device_get_device_by_id_with_http_info(self, device_id, **kwargs):  # noqa: E501
        """getDeviceById device  # noqa: E501

        Returns information about the specified device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_device_by_id_with_http_info(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int device_id: ID of the device whose information should be returned (required)
        :return: AkapiStoredDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_get_device_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `device_get_device_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

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
            '/device/id/{deviceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AkapiStoredDevice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_get_device_by_serial_number(self, serial_number, **kwargs):  # noqa: E501
        """getDeviceBySerialNumber device  # noqa: E501

        Returns information about the device corresponding to the specified serial number  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_device_by_serial_number(serial_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str serial_number: Serial number of the device whose information should be returned (required)
        :return: AkapiStoredDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_get_device_by_serial_number_with_http_info(serial_number, **kwargs)  # noqa: E501
        else:
            (data) = self.device_get_device_by_serial_number_with_http_info(serial_number, **kwargs)  # noqa: E501
            return data

    def device_get_device_by_serial_number_with_http_info(self, serial_number, **kwargs):  # noqa: E501
        """getDeviceBySerialNumber device  # noqa: E501

        Returns information about the device corresponding to the specified serial number  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_device_by_serial_number_with_http_info(serial_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str serial_number: Serial number of the device whose information should be returned (required)
        :return: AkapiStoredDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['serial_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method device_get_device_by_serial_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'serial_number' is set
        if ('serial_number' not in params or
                params['serial_number'] is None):
            raise ValueError("Missing the required parameter `serial_number` when calling `device_get_device_by_serial_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'serial_number' in params:
            path_params['serialNumber'] = params['serial_number']  # noqa: E501

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
            '/device/{serialNumber}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AkapiStoredDevice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def device_get_devices_by_site(self, site_id, **kwargs):  # noqa: E501
        """getDevicesBySite device  # noqa: E501

        Get All Devices by Site  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_devices_by_site(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose devices should be returned (required)
        :return: StoredDeviceCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_get_devices_by_site_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.device_get_devices_by_site_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def device_get_devices_by_site_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """getDevicesBySite device  # noqa: E501

        Get All Devices by Site  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_get_devices_by_site_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: ID of the site whose devices should be returned (required)
        :return: StoredDeviceCollection
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
                    " to method device_get_devices_by_site" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `device_get_devices_by_site`")  # noqa: E501

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
            '/site/{siteId}/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoredDeviceCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

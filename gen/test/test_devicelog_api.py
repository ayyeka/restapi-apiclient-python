# coding: utf-8

"""
    RESTAPI Service

    RESTful API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.devicelog_api import DevicelogApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDevicelogApi(unittest.TestCase):
    """DevicelogApi unit test stubs"""

    def setUp(self):
        self.api = DevicelogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devicelog_get_device_logs(self):
        """Test case for devicelog_get_device_logs

        getDeviceLogs devicelog  # noqa: E501
        """
        pass

    def test_devicelog_get_last_device_log(self):
        """Test case for devicelog_get_last_device_log

        getLastDeviceLog devicelog  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
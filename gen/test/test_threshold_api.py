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
from swagger_client.api.threshold_api import ThresholdApi  # noqa: E501
from swagger_client.rest import ApiException


class TestThresholdApi(unittest.TestCase):
    """ThresholdApi unit test stubs"""

    def setUp(self):
        self.api = ThresholdApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_threshold_get_threshold_by_stream(self):
        """Test case for threshold_get_threshold_by_stream

        getThresholdByStream threshold  # noqa: E501
        """
        pass

    def test_threshold_get_threshold_status(self):
        """Test case for threshold_get_threshold_status

        getThresholdStatus threshold  # noqa: E501
        """
        pass

    def test_threshold_set_threshold_by_stream(self):
        """Test case for threshold_set_threshold_by_stream

        setThresholdByStream threshold  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from swagger_client.api.channel_api import ChannelApi  # noqa: E501
from swagger_client.rest import ApiException


class TestChannelApi(unittest.TestCase):
    """ChannelApi unit test stubs"""

    def setUp(self):
        self.api = ChannelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_channel_get_all_channels(self):
        """Test case for channel_get_all_channels

        getAllChannels channel  # noqa: E501
        """
        pass

    def test_channel_get_channel_by_id(self):
        """Test case for channel_get_channel_by_id

        getChannelById channel  # noqa: E501
        """
        pass

    def test_channel_get_channels_by_device(self):
        """Test case for channel_get_channels_by_device

        getChannelsByDevice channel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

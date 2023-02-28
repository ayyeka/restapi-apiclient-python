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
from swagger_client.api.sampleimage_api import SampleimageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSampleimageApi(unittest.TestCase):
    """SampleimageApi unit test stubs"""

    def setUp(self):
        self.api = SampleimageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sampleimage_get_last_sample_image_by_stream(self):
        """Test case for sampleimage_get_last_sample_image_by_stream

        getLastSampleImageByStream sampleimage  # noqa: E501
        """
        pass

    def test_sampleimage_get_sample_image_by_id(self):
        """Test case for sampleimage_get_sample_image_by_id

        getSampleImageById sampleimage  # noqa: E501
        """
        pass

    def test_sampleimage_get_samples_image_batch(self):
        """Test case for sampleimage_get_samples_image_batch

        getSamplesImageBatch sampleimage  # noqa: E501
        """
        pass

    def test_sampleimage_get_samples_image_batch_by_stream(self):
        """Test case for sampleimage_get_samples_image_batch_by_stream

        getSamplesImageBatchByStream sampleimage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
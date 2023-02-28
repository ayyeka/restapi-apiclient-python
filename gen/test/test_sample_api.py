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
from swagger_client.api.sample_api import SampleApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSampleApi(unittest.TestCase):
    """SampleApi unit test stubs"""

    def setUp(self):
        self.api = SampleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sample_ack_sample_scalar_batch(self):
        """Test case for sample_ack_sample_scalar_batch

        ackSampleScalarBatch sample  # noqa: E501
        """
        pass

    def test_sample_get_last_sample_scalar_batch(self):
        """Test case for sample_get_last_sample_scalar_batch

        getLastSampleScalarBatch sample  # noqa: E501
        """
        pass

    def test_sample_get_last_sample_scalar_by_stream(self):
        """Test case for sample_get_last_sample_scalar_by_stream

        getLastSampleScalarByStream sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_aggregation_by_stream_and_date_range(self):
        """Test case for sample_get_samples_scalar_aggregation_by_stream_and_date_range

        getSamplesScalarAggregationByStreamAndDateRange sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_batch(self):
        """Test case for sample_get_samples_scalar_batch

        getSamplesScalarBatch sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_batch_by_site(self):
        """Test case for sample_get_samples_scalar_batch_by_site

        getSamplesScalarBatchBySite sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_batch_by_stream(self):
        """Test case for sample_get_samples_scalar_batch_by_stream

        getSamplesScalarBatchByStream sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_by_site(self):
        """Test case for sample_get_samples_scalar_by_site

        getSamplesScalarBySite sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_by_stream(self):
        """Test case for sample_get_samples_scalar_by_stream

        getSamplesScalarByStream sample  # noqa: E501
        """
        pass

    def test_sample_get_samples_scalar_by_stream_and_date_range(self):
        """Test case for sample_get_samples_scalar_by_stream_and_date_range

        getSamplesScalarByStreamAndDateRange sample  # noqa: E501
        """
        pass

    def test_sample_set_backfill_samples_scalar_batch(self):
        """Test case for sample_set_backfill_samples_scalar_batch

        setBackfillSamplesScalarBatch sample  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

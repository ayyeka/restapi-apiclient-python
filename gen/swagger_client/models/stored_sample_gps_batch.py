# coding: utf-8

"""
    RESTAPI Service

    RESTful API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StoredSampleGPSBatch(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'has_more': 'bool',
        'samples': 'StoredSampleGPSCollection'
    }

    attribute_map = {
        'has_more': 'hasMore',
        'samples': 'samples'
    }

    def __init__(self, has_more=None, samples=None):  # noqa: E501
        """StoredSampleGPSBatch - a model defined in Swagger"""  # noqa: E501
        self._has_more = None
        self._samples = None
        self.discriminator = None
        self.has_more = has_more
        self.samples = samples

    @property
    def has_more(self):
        """Gets the has_more of this StoredSampleGPSBatch.  # noqa: E501

        The value is set to true if there is more samples GPS to retrieve  # noqa: E501

        :return: The has_more of this StoredSampleGPSBatch.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this StoredSampleGPSBatch.

        The value is set to true if there is more samples GPS to retrieve  # noqa: E501

        :param has_more: The has_more of this StoredSampleGPSBatch.  # noqa: E501
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

    @property
    def samples(self):
        """Gets the samples of this StoredSampleGPSBatch.  # noqa: E501


        :return: The samples of this StoredSampleGPSBatch.  # noqa: E501
        :rtype: StoredSampleGPSCollection
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this StoredSampleGPSBatch.


        :param samples: The samples of this StoredSampleGPSBatch.  # noqa: E501
        :type: StoredSampleGPSCollection
        """
        if samples is None:
            raise ValueError("Invalid value for `samples`, must not be `None`")  # noqa: E501

        self._samples = samples

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StoredSampleGPSBatch, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoredSampleGPSBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

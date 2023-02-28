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

class Aggregation(object):
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
        'avg': 'str',
        'max': 'str',
        'min': 'str',
        'sum': 'str'
    }

    attribute_map = {
        'avg': 'avg',
        'max': 'max',
        'min': 'min',
        'sum': 'sum'
    }

    def __init__(self, avg=None, max=None, min=None, sum=None):  # noqa: E501
        """Aggregation - a model defined in Swagger"""  # noqa: E501
        self._avg = None
        self._max = None
        self._min = None
        self._sum = None
        self.discriminator = None
        self.avg = avg
        self.max = max
        self.min = min
        self.sum = sum

    @property
    def avg(self):
        """Gets the avg of this Aggregation.  # noqa: E501

        Average  # noqa: E501

        :return: The avg of this Aggregation.  # noqa: E501
        :rtype: str
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this Aggregation.

        Average  # noqa: E501

        :param avg: The avg of this Aggregation.  # noqa: E501
        :type: str
        """
        if avg is None:
            raise ValueError("Invalid value for `avg`, must not be `None`")  # noqa: E501

        self._avg = avg

    @property
    def max(self):
        """Gets the max of this Aggregation.  # noqa: E501

        Maximum  # noqa: E501

        :return: The max of this Aggregation.  # noqa: E501
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Aggregation.

        Maximum  # noqa: E501

        :param max: The max of this Aggregation.  # noqa: E501
        :type: str
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self):
        """Gets the min of this Aggregation.  # noqa: E501

        Minimum  # noqa: E501

        :return: The min of this Aggregation.  # noqa: E501
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Aggregation.

        Minimum  # noqa: E501

        :param min: The min of this Aggregation.  # noqa: E501
        :type: str
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def sum(self):
        """Gets the sum of this Aggregation.  # noqa: E501

        Sum  # noqa: E501

        :return: The sum of this Aggregation.  # noqa: E501
        :rtype: str
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this Aggregation.

        Sum  # noqa: E501

        :param sum: The sum of this Aggregation.  # noqa: E501
        :type: str
        """
        if sum is None:
            raise ValueError("Invalid value for `sum`, must not be `None`")  # noqa: E501

        self._sum = sum

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
        if issubclass(Aggregation, dict):
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
        if not isinstance(other, Aggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

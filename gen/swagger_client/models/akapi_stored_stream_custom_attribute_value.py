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

class AkapiStoredStreamCustomAttributeValue(object):
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
        'display_name': 'str',
        'id': 'int',
        'parent_id': 'int',
        'value': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'id': 'id',
        'parent_id': 'parent_id',
        'value': 'value'
    }

    def __init__(self, display_name=None, id=None, parent_id=None, value=None):  # noqa: E501
        """AkapiStoredStreamCustomAttributeValue - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._id = None
        self._parent_id = None
        self._value = None
        self.discriminator = None
        self.display_name = display_name
        self.id = id
        self.parent_id = parent_id
        self.value = value

    @property
    def display_name(self):
        """Gets the display_name of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501

        Display name  # noqa: E501

        :return: The display_name of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AkapiStoredStreamCustomAttributeValue.

        Display name  # noqa: E501

        :param display_name: The display_name of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501

        ID is the unique id of the stream custom attribute value.  # noqa: E501

        :return: The id of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AkapiStoredStreamCustomAttributeValue.

        ID is the unique id of the stream custom attribute value.  # noqa: E501

        :param id: The id of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501

        Parent ID  # noqa: E501

        :return: The parent_id of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this AkapiStoredStreamCustomAttributeValue.

        Parent ID  # noqa: E501

        :param parent_id: The parent_id of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :type: int
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def value(self):
        """Gets the value of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501

        Value  # noqa: E501

        :return: The value of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AkapiStoredStreamCustomAttributeValue.

        Value  # noqa: E501

        :param value: The value of this AkapiStoredStreamCustomAttributeValue.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(AkapiStoredStreamCustomAttributeValue, dict):
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
        if not isinstance(other, AkapiStoredStreamCustomAttributeValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
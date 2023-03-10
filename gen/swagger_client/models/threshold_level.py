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

class ThresholdLevel(object):
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
        'comment': 'str',
        'display_name': 'str',
        'false_alarm_filter': 'int',
        'lower_limit': 'float',
        'notification_actions': 'list[ThresholdActionNotification]',
        'output_actions': 'list[ThresholdActionOutput]',
        'sample_actions': 'list[ThresholdActionSample]',
        'sample_interval': 'int',
        'transmission_interval': 'str',
        'transmit_immediately': 'bool',
        'upper_limit': 'float'
    }

    attribute_map = {
        'comment': 'comment',
        'display_name': 'display_name',
        'false_alarm_filter': 'false_alarm_filter',
        'lower_limit': 'lower_limit',
        'notification_actions': 'notification_actions',
        'output_actions': 'output_actions',
        'sample_actions': 'sample_actions',
        'sample_interval': 'sample_interval',
        'transmission_interval': 'transmission_interval',
        'transmit_immediately': 'transmit_immediately',
        'upper_limit': 'upper_limit'
    }

    def __init__(self, comment=None, display_name=None, false_alarm_filter=0, lower_limit=None, notification_actions=None, output_actions=None, sample_actions=None, sample_interval=300, transmission_interval='normal', transmit_immediately=False, upper_limit=None):  # noqa: E501
        """ThresholdLevel - a model defined in Swagger"""  # noqa: E501
        self._comment = None
        self._display_name = None
        self._false_alarm_filter = None
        self._lower_limit = None
        self._notification_actions = None
        self._output_actions = None
        self._sample_actions = None
        self._sample_interval = None
        self._transmission_interval = None
        self._transmit_immediately = None
        self._upper_limit = None
        self.discriminator = None
        self.comment = comment
        self.display_name = display_name
        self.false_alarm_filter = false_alarm_filter
        self.lower_limit = lower_limit
        if notification_actions is not None:
            self.notification_actions = notification_actions
        if output_actions is not None:
            self.output_actions = output_actions
        if sample_actions is not None:
            self.sample_actions = sample_actions
        self.sample_interval = sample_interval
        self.transmission_interval = transmission_interval
        self.transmit_immediately = transmit_immediately
        self.upper_limit = upper_limit

    @property
    def comment(self):
        """Gets the comment of this ThresholdLevel.  # noqa: E501

        Comment for the threshold's level  # noqa: E501

        :return: The comment of this ThresholdLevel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ThresholdLevel.

        Comment for the threshold's level  # noqa: E501

        :param comment: The comment of this ThresholdLevel.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def display_name(self):
        """Gets the display_name of this ThresholdLevel.  # noqa: E501

        Name of the threshold's level  # noqa: E501

        :return: The display_name of this ThresholdLevel.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ThresholdLevel.

        Name of the threshold's level  # noqa: E501

        :param display_name: The display_name of this ThresholdLevel.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def false_alarm_filter(self):
        """Gets the false_alarm_filter of this ThresholdLevel.  # noqa: E501

        Threshold triggered interval in seconds  # noqa: E501

        :return: The false_alarm_filter of this ThresholdLevel.  # noqa: E501
        :rtype: int
        """
        return self._false_alarm_filter

    @false_alarm_filter.setter
    def false_alarm_filter(self, false_alarm_filter):
        """Sets the false_alarm_filter of this ThresholdLevel.

        Threshold triggered interval in seconds  # noqa: E501

        :param false_alarm_filter: The false_alarm_filter of this ThresholdLevel.  # noqa: E501
        :type: int
        """
        if false_alarm_filter is None:
            raise ValueError("Invalid value for `false_alarm_filter`, must not be `None`")  # noqa: E501

        self._false_alarm_filter = false_alarm_filter

    @property
    def lower_limit(self):
        """Gets the lower_limit of this ThresholdLevel.  # noqa: E501

        Lower limit of the threshold range  # noqa: E501

        :return: The lower_limit of this ThresholdLevel.  # noqa: E501
        :rtype: float
        """
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, lower_limit):
        """Sets the lower_limit of this ThresholdLevel.

        Lower limit of the threshold range  # noqa: E501

        :param lower_limit: The lower_limit of this ThresholdLevel.  # noqa: E501
        :type: float
        """
        if lower_limit is None:
            raise ValueError("Invalid value for `lower_limit`, must not be `None`")  # noqa: E501

        self._lower_limit = lower_limit

    @property
    def notification_actions(self):
        """Gets the notification_actions of this ThresholdLevel.  # noqa: E501


        :return: The notification_actions of this ThresholdLevel.  # noqa: E501
        :rtype: list[ThresholdActionNotification]
        """
        return self._notification_actions

    @notification_actions.setter
    def notification_actions(self, notification_actions):
        """Sets the notification_actions of this ThresholdLevel.


        :param notification_actions: The notification_actions of this ThresholdLevel.  # noqa: E501
        :type: list[ThresholdActionNotification]
        """

        self._notification_actions = notification_actions

    @property
    def output_actions(self):
        """Gets the output_actions of this ThresholdLevel.  # noqa: E501


        :return: The output_actions of this ThresholdLevel.  # noqa: E501
        :rtype: list[ThresholdActionOutput]
        """
        return self._output_actions

    @output_actions.setter
    def output_actions(self, output_actions):
        """Sets the output_actions of this ThresholdLevel.


        :param output_actions: The output_actions of this ThresholdLevel.  # noqa: E501
        :type: list[ThresholdActionOutput]
        """

        self._output_actions = output_actions

    @property
    def sample_actions(self):
        """Gets the sample_actions of this ThresholdLevel.  # noqa: E501


        :return: The sample_actions of this ThresholdLevel.  # noqa: E501
        :rtype: list[ThresholdActionSample]
        """
        return self._sample_actions

    @sample_actions.setter
    def sample_actions(self, sample_actions):
        """Sets the sample_actions of this ThresholdLevel.


        :param sample_actions: The sample_actions of this ThresholdLevel.  # noqa: E501
        :type: list[ThresholdActionSample]
        """

        self._sample_actions = sample_actions

    @property
    def sample_interval(self):
        """Gets the sample_interval of this ThresholdLevel.  # noqa: E501

        Sample interval in seconds how often the device streams  # noqa: E501

        :return: The sample_interval of this ThresholdLevel.  # noqa: E501
        :rtype: int
        """
        return self._sample_interval

    @sample_interval.setter
    def sample_interval(self, sample_interval):
        """Sets the sample_interval of this ThresholdLevel.

        Sample interval in seconds how often the device streams  # noqa: E501

        :param sample_interval: The sample_interval of this ThresholdLevel.  # noqa: E501
        :type: int
        """
        if sample_interval is None:
            raise ValueError("Invalid value for `sample_interval`, must not be `None`")  # noqa: E501

        self._sample_interval = sample_interval

    @property
    def transmission_interval(self):
        """Gets the transmission_interval of this ThresholdLevel.  # noqa: E501

        Transmission device report interval  # noqa: E501

        :return: The transmission_interval of this ThresholdLevel.  # noqa: E501
        :rtype: str
        """
        return self._transmission_interval

    @transmission_interval.setter
    def transmission_interval(self, transmission_interval):
        """Sets the transmission_interval of this ThresholdLevel.

        Transmission device report interval  # noqa: E501

        :param transmission_interval: The transmission_interval of this ThresholdLevel.  # noqa: E501
        :type: str
        """
        if transmission_interval is None:
            raise ValueError("Invalid value for `transmission_interval`, must not be `None`")  # noqa: E501
        allowed_values = ["normal", "event", "emergency"]  # noqa: E501
        if transmission_interval not in allowed_values:
            raise ValueError(
                "Invalid value for `transmission_interval` ({0}), must be one of {1}"  # noqa: E501
                .format(transmission_interval, allowed_values)
            )

        self._transmission_interval = transmission_interval

    @property
    def transmit_immediately(self):
        """Gets the transmit_immediately of this ThresholdLevel.  # noqa: E501

        When a device reached threshold zone does he need to transmit immediately  # noqa: E501

        :return: The transmit_immediately of this ThresholdLevel.  # noqa: E501
        :rtype: bool
        """
        return self._transmit_immediately

    @transmit_immediately.setter
    def transmit_immediately(self, transmit_immediately):
        """Sets the transmit_immediately of this ThresholdLevel.

        When a device reached threshold zone does he need to transmit immediately  # noqa: E501

        :param transmit_immediately: The transmit_immediately of this ThresholdLevel.  # noqa: E501
        :type: bool
        """
        if transmit_immediately is None:
            raise ValueError("Invalid value for `transmit_immediately`, must not be `None`")  # noqa: E501

        self._transmit_immediately = transmit_immediately

    @property
    def upper_limit(self):
        """Gets the upper_limit of this ThresholdLevel.  # noqa: E501

        Upper limit of the threshold range  # noqa: E501

        :return: The upper_limit of this ThresholdLevel.  # noqa: E501
        :rtype: float
        """
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, upper_limit):
        """Sets the upper_limit of this ThresholdLevel.

        Upper limit of the threshold range  # noqa: E501

        :param upper_limit: The upper_limit of this ThresholdLevel.  # noqa: E501
        :type: float
        """
        if upper_limit is None:
            raise ValueError("Invalid value for `upper_limit`, must not be `None`")  # noqa: E501

        self._upper_limit = upper_limit

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
        if issubclass(ThresholdLevel, dict):
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
        if not isinstance(other, ThresholdLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

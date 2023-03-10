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

class AkapiStoredDevice(object):
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
        'akid': 'str',
        'display_name': 'str',
        'firmware_version': 'str',
        'iccid': 'str',
        'iccid2': 'str',
        'id': 'int',
        'meid': 'str',
        'model_number': 'str',
        'serial_number': 'str',
        'site_display_name': 'str',
        'site_id': 'int'
    }

    attribute_map = {
        'akid': 'akid',
        'display_name': 'display_name',
        'firmware_version': 'firmware_version',
        'iccid': 'iccid',
        'iccid2': 'iccid2',
        'id': 'id',
        'meid': 'meid',
        'model_number': 'model_number',
        'serial_number': 'serial_number',
        'site_display_name': 'site_display_name',
        'site_id': 'site_id'
    }

    def __init__(self, akid=None, display_name=None, firmware_version=None, iccid=None, iccid2=None, id=None, meid=None, model_number=None, serial_number=None, site_display_name=None, site_id=None):  # noqa: E501
        """AkapiStoredDevice - a model defined in Swagger"""  # noqa: E501
        self._akid = None
        self._display_name = None
        self._firmware_version = None
        self._iccid = None
        self._iccid2 = None
        self._id = None
        self._meid = None
        self._model_number = None
        self._serial_number = None
        self._site_display_name = None
        self._site_id = None
        self.discriminator = None
        self.akid = akid
        self.display_name = display_name
        self.firmware_version = firmware_version
        self.iccid = iccid
        self.iccid2 = iccid2
        self.id = id
        self.meid = meid
        self.model_number = model_number
        self.serial_number = serial_number
        self.site_display_name = site_display_name
        self.site_id = site_id

    @property
    def akid(self):
        """Gets the akid of this AkapiStoredDevice.  # noqa: E501

        Device HW ID  # noqa: E501

        :return: The akid of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._akid

    @akid.setter
    def akid(self, akid):
        """Sets the akid of this AkapiStoredDevice.

        Device HW ID  # noqa: E501

        :param akid: The akid of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if akid is None:
            raise ValueError("Invalid value for `akid`, must not be `None`")  # noqa: E501

        self._akid = akid

    @property
    def display_name(self):
        """Gets the display_name of this AkapiStoredDevice.  # noqa: E501

        Device name  # noqa: E501

        :return: The display_name of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AkapiStoredDevice.

        Device name  # noqa: E501

        :param display_name: The display_name of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def firmware_version(self):
        """Gets the firmware_version of this AkapiStoredDevice.  # noqa: E501

        Firmware version  # noqa: E501

        :return: The firmware_version of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this AkapiStoredDevice.

        Firmware version  # noqa: E501

        :param firmware_version: The firmware_version of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if firmware_version is None:
            raise ValueError("Invalid value for `firmware_version`, must not be `None`")  # noqa: E501

        self._firmware_version = firmware_version

    @property
    def iccid(self):
        """Gets the iccid of this AkapiStoredDevice.  # noqa: E501

        Cellular ICCID  # noqa: E501

        :return: The iccid of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this AkapiStoredDevice.

        Cellular ICCID  # noqa: E501

        :param iccid: The iccid of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if iccid is None:
            raise ValueError("Invalid value for `iccid`, must not be `None`")  # noqa: E501

        self._iccid = iccid

    @property
    def iccid2(self):
        """Gets the iccid2 of this AkapiStoredDevice.  # noqa: E501

        Cellular ICCID  # noqa: E501

        :return: The iccid2 of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._iccid2

    @iccid2.setter
    def iccid2(self, iccid2):
        """Sets the iccid2 of this AkapiStoredDevice.

        Cellular ICCID  # noqa: E501

        :param iccid2: The iccid2 of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if iccid2 is None:
            raise ValueError("Invalid value for `iccid2`, must not be `None`")  # noqa: E501

        self._iccid2 = iccid2

    @property
    def id(self):
        """Gets the id of this AkapiStoredDevice.  # noqa: E501

        ID is the unique id of the device.  # noqa: E501

        :return: The id of this AkapiStoredDevice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AkapiStoredDevice.

        ID is the unique id of the device.  # noqa: E501

        :param id: The id of this AkapiStoredDevice.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def meid(self):
        """Gets the meid of this AkapiStoredDevice.  # noqa: E501

        Cellular ICCID  # noqa: E501

        :return: The meid of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._meid

    @meid.setter
    def meid(self, meid):
        """Sets the meid of this AkapiStoredDevice.

        Cellular ICCID  # noqa: E501

        :param meid: The meid of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if meid is None:
            raise ValueError("Invalid value for `meid`, must not be `None`")  # noqa: E501

        self._meid = meid

    @property
    def model_number(self):
        """Gets the model_number of this AkapiStoredDevice.  # noqa: E501

        Model number  # noqa: E501

        :return: The model_number of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this AkapiStoredDevice.

        Model number  # noqa: E501

        :param model_number: The model_number of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if model_number is None:
            raise ValueError("Invalid value for `model_number`, must not be `None`")  # noqa: E501

        self._model_number = model_number

    @property
    def serial_number(self):
        """Gets the serial_number of this AkapiStoredDevice.  # noqa: E501

        Serial number  # noqa: E501

        :return: The serial_number of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this AkapiStoredDevice.

        Serial number  # noqa: E501

        :param serial_number: The serial_number of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def site_display_name(self):
        """Gets the site_display_name of this AkapiStoredDevice.  # noqa: E501

        Site name  # noqa: E501

        :return: The site_display_name of this AkapiStoredDevice.  # noqa: E501
        :rtype: str
        """
        return self._site_display_name

    @site_display_name.setter
    def site_display_name(self, site_display_name):
        """Sets the site_display_name of this AkapiStoredDevice.

        Site name  # noqa: E501

        :param site_display_name: The site_display_name of this AkapiStoredDevice.  # noqa: E501
        :type: str
        """
        if site_display_name is None:
            raise ValueError("Invalid value for `site_display_name`, must not be `None`")  # noqa: E501

        self._site_display_name = site_display_name

    @property
    def site_id(self):
        """Gets the site_id of this AkapiStoredDevice.  # noqa: E501

        Site ID of device  # noqa: E501

        :return: The site_id of this AkapiStoredDevice.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this AkapiStoredDevice.

        Site ID of device  # noqa: E501

        :param site_id: The site_id of this AkapiStoredDevice.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

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
        if issubclass(AkapiStoredDevice, dict):
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
        if not isinstance(other, AkapiStoredDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

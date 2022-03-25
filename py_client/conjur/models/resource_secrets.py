# coding: utf-8

"""
    Conjur

    This is an API definition for CyberArk Conjur Open Source. You can find out more at [Conjur.org](https://www.conjur.org/).  # noqa: E501

    The version of the OpenAPI document: 5.3.0
    Contact: conj_maintainers@cyberark.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from conjur.configuration import Configuration


class ResourceSecrets(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'expires_at': 'str',
        'version': 'float'
    }

    attribute_map = {
        'expires_at': 'expires_at',
        'version': 'version'
    }

    def __init__(self, expires_at=None, version=None, local_vars_configuration=None):  # noqa: E501
        """ResourceSecrets - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expires_at = None
        self._version = None
        self.discriminator = None

        if expires_at is not None:
            self.expires_at = expires_at
        if version is not None:
            self.version = version

    @property
    def expires_at(self):
        """Gets the expires_at of this ResourceSecrets.  # noqa: E501


        :return: The expires_at of this ResourceSecrets.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this ResourceSecrets.


        :param expires_at: The expires_at of this ResourceSecrets.  # noqa: E501
        :type: str
        """

        self._expires_at = expires_at

    @property
    def version(self):
        """Gets the version of this ResourceSecrets.  # noqa: E501


        :return: The version of this ResourceSecrets.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ResourceSecrets.


        :param version: The version of this ResourceSecrets.  # noqa: E501
        :type: float
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceSecrets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceSecrets):
            return True

        return self.to_dict() != other.to_dict()
# coding: utf-8

"""
    DCV Session Manager

    DCV Session Manager API  # noqa: E501

    OpenAPI spec version: 2020.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeleteSessionRequestData(object):
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
        'session_id': 'str',
        'owner': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'session_id': 'SessionId',
        'owner': 'Owner',
        'force': 'Force'
    }

    def __init__(self, session_id=None, owner=None, force=False):  # noqa: E501
        """DeleteSessionRequestData - a model defined in Swagger"""  # noqa: E501
        self._session_id = None
        self._owner = None
        self._force = None
        self.discriminator = None
        if session_id is not None:
            self.session_id = session_id
        if owner is not None:
            self.owner = owner
        if force is not None:
            self.force = force

    @property
    def session_id(self):
        """Gets the session_id of this DeleteSessionRequestData.  # noqa: E501

        The session id  # noqa: E501

        :return: The session_id of this DeleteSessionRequestData.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this DeleteSessionRequestData.

        The session id  # noqa: E501

        :param session_id: The session_id of this DeleteSessionRequestData.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def owner(self):
        """Gets the owner of this DeleteSessionRequestData.  # noqa: E501

        The owner  # noqa: E501

        :return: The owner of this DeleteSessionRequestData.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DeleteSessionRequestData.

        The owner  # noqa: E501

        :param owner: The owner of this DeleteSessionRequestData.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def force(self):
        """Gets the force of this DeleteSessionRequestData.  # noqa: E501

        The parameter to force a deletion  # noqa: E501

        :return: The force of this DeleteSessionRequestData.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this DeleteSessionRequestData.

        The parameter to force a deletion  # noqa: E501

        :param force: The force of this DeleteSessionRequestData.  # noqa: E501
        :type: bool
        """

        self._force = force

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
        if issubclass(DeleteSessionRequestData, dict):
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
        if not isinstance(other, DeleteSessionRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

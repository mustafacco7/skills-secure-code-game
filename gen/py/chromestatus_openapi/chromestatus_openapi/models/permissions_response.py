from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.user_permissions import UserPermissions
from chromestatus_openapi import util

from chromestatus_openapi.models.user_permissions import UserPermissions  # noqa: E501

class PermissionsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user=None):  # noqa: E501
        """PermissionsResponse - a model defined in OpenAPI

        :param user: The user of this PermissionsResponse.  # noqa: E501
        :type user: UserPermissions
        """
        self.openapi_types = {
            'user': UserPermissions
        }

        self.attribute_map = {
            'user': 'user'
        }

        self._user = user

    @classmethod
    def from_dict(cls, dikt) -> 'PermissionsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PermissionsResponse of this PermissionsResponse.  # noqa: E501
        :rtype: PermissionsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user(self) -> UserPermissions:
        """Gets the user of this PermissionsResponse.


        :return: The user of this PermissionsResponse.
        :rtype: UserPermissions
        """
        return self._user

    @user.setter
    def user(self, user: UserPermissions):
        """Sets the user of this PermissionsResponse.


        :param user: The user of this PermissionsResponse.
        :type user: UserPermissions
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.feature_link import FeatureLink
from chromestatus_openapi import util

from chromestatus_openapi.models.feature_link import FeatureLink  # noqa: E501

class SpecMentor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email=None, mentored_features=None):  # noqa: E501
        """SpecMentor - a model defined in OpenAPI

        :param email: The email of this SpecMentor.  # noqa: E501
        :type email: str
        :param mentored_features: The mentored_features of this SpecMentor.  # noqa: E501
        :type mentored_features: List[FeatureLink]
        """
        self.openapi_types = {
            'email': str,
            'mentored_features': List[FeatureLink]
        }

        self.attribute_map = {
            'email': 'email',
            'mentored_features': 'mentored_features'
        }

        self._email = email
        self._mentored_features = mentored_features

    @classmethod
    def from_dict(cls, dikt) -> 'SpecMentor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpecMentor of this SpecMentor.  # noqa: E501
        :rtype: SpecMentor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this SpecMentor.


        :return: The email of this SpecMentor.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this SpecMentor.


        :param email: The email of this SpecMentor.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def mentored_features(self) -> List[FeatureLink]:
        """Gets the mentored_features of this SpecMentor.


        :return: The mentored_features of this SpecMentor.
        :rtype: List[FeatureLink]
        """
        return self._mentored_features

    @mentored_features.setter
    def mentored_features(self, mentored_features: List[FeatureLink]):
        """Sets the mentored_features of this SpecMentor.


        :param mentored_features: The mentored_features of this SpecMentor.
        :type mentored_features: List[FeatureLink]
        """
        if mentored_features is None:
            raise ValueError("Invalid value for `mentored_features`, must not be `None`")  # noqa: E501

        self._mentored_features = mentored_features

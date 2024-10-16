from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.feature_link import FeatureLink
from chromestatus_openapi.models.gate_latency import GateLatency
from chromestatus_openapi import util

from chromestatus_openapi.models.feature_link import FeatureLink  # noqa: E501
from chromestatus_openapi.models.gate_latency import GateLatency  # noqa: E501

class ReviewLatency(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, feature=None, gate_reviews=None):  # noqa: E501
        """ReviewLatency - a model defined in OpenAPI

        :param feature: The feature of this ReviewLatency.  # noqa: E501
        :type feature: FeatureLink
        :param gate_reviews: The gate_reviews of this ReviewLatency.  # noqa: E501
        :type gate_reviews: List[GateLatency]
        """
        self.openapi_types = {
            'feature': FeatureLink,
            'gate_reviews': List[GateLatency]
        }

        self.attribute_map = {
            'feature': 'feature',
            'gate_reviews': 'gate_reviews'
        }

        self._feature = feature
        self._gate_reviews = gate_reviews

    @classmethod
    def from_dict(cls, dikt) -> 'ReviewLatency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReviewLatency of this ReviewLatency.  # noqa: E501
        :rtype: ReviewLatency
        """
        return util.deserialize_model(dikt, cls)

    @property
    def feature(self) -> FeatureLink:
        """Gets the feature of this ReviewLatency.


        :return: The feature of this ReviewLatency.
        :rtype: FeatureLink
        """
        return self._feature

    @feature.setter
    def feature(self, feature: FeatureLink):
        """Sets the feature of this ReviewLatency.


        :param feature: The feature of this ReviewLatency.
        :type feature: FeatureLink
        """
        if feature is None:
            raise ValueError("Invalid value for `feature`, must not be `None`")  # noqa: E501

        self._feature = feature

    @property
    def gate_reviews(self) -> List[GateLatency]:
        """Gets the gate_reviews of this ReviewLatency.


        :return: The gate_reviews of this ReviewLatency.
        :rtype: List[GateLatency]
        """
        return self._gate_reviews

    @gate_reviews.setter
    def gate_reviews(self, gate_reviews: List[GateLatency]):
        """Sets the gate_reviews of this ReviewLatency.


        :param gate_reviews: The gate_reviews of this ReviewLatency.
        :type gate_reviews: List[GateLatency]
        """
        if gate_reviews is None:
            raise ValueError("Invalid value for `gate_reviews`, must not be `None`")  # noqa: E501

        self._gate_reviews = gate_reviews
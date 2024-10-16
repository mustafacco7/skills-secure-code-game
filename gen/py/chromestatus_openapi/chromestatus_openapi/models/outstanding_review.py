from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.feature_link import FeatureLink
from chromestatus_openapi import util

from chromestatus_openapi.models.feature_link import FeatureLink  # noqa: E501

class OutstandingReview(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, review_link=None, feature=None, current_stage=None, estimated_start_milestone=None, estimated_end_milestone=None):  # noqa: E501
        """OutstandingReview - a model defined in OpenAPI

        :param review_link: The review_link of this OutstandingReview.  # noqa: E501
        :type review_link: str
        :param feature: The feature of this OutstandingReview.  # noqa: E501
        :type feature: FeatureLink
        :param current_stage: The current_stage of this OutstandingReview.  # noqa: E501
        :type current_stage: str
        :param estimated_start_milestone: The estimated_start_milestone of this OutstandingReview.  # noqa: E501
        :type estimated_start_milestone: int
        :param estimated_end_milestone: The estimated_end_milestone of this OutstandingReview.  # noqa: E501
        :type estimated_end_milestone: int
        """
        self.openapi_types = {
            'review_link': str,
            'feature': FeatureLink,
            'current_stage': str,
            'estimated_start_milestone': int,
            'estimated_end_milestone': int
        }

        self.attribute_map = {
            'review_link': 'review_link',
            'feature': 'feature',
            'current_stage': 'current_stage',
            'estimated_start_milestone': 'estimated_start_milestone',
            'estimated_end_milestone': 'estimated_end_milestone'
        }

        self._review_link = review_link
        self._feature = feature
        self._current_stage = current_stage
        self._estimated_start_milestone = estimated_start_milestone
        self._estimated_end_milestone = estimated_end_milestone

    @classmethod
    def from_dict(cls, dikt) -> 'OutstandingReview':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OutstandingReview of this OutstandingReview.  # noqa: E501
        :rtype: OutstandingReview
        """
        return util.deserialize_model(dikt, cls)

    @property
    def review_link(self) -> str:
        """Gets the review_link of this OutstandingReview.


        :return: The review_link of this OutstandingReview.
        :rtype: str
        """
        return self._review_link

    @review_link.setter
    def review_link(self, review_link: str):
        """Sets the review_link of this OutstandingReview.


        :param review_link: The review_link of this OutstandingReview.
        :type review_link: str
        """
        if review_link is None:
            raise ValueError("Invalid value for `review_link`, must not be `None`")  # noqa: E501

        self._review_link = review_link

    @property
    def feature(self) -> FeatureLink:
        """Gets the feature of this OutstandingReview.


        :return: The feature of this OutstandingReview.
        :rtype: FeatureLink
        """
        return self._feature

    @feature.setter
    def feature(self, feature: FeatureLink):
        """Sets the feature of this OutstandingReview.


        :param feature: The feature of this OutstandingReview.
        :type feature: FeatureLink
        """
        if feature is None:
            raise ValueError("Invalid value for `feature`, must not be `None`")  # noqa: E501

        self._feature = feature

    @property
    def current_stage(self) -> str:
        """Gets the current_stage of this OutstandingReview.

        The development stage that the feature has reached:   - [`incubating`](https://www.chromium.org/blink/launching-features/#start-incubating)   - [`prototyping`](https://www.chromium.org/blink/launching-features/#prototyping)   - [`dev-trial`](https://www.chromium.org/blink/launching-features/#dev-trials)   - [`wide-review`](https://www.chromium.org/blink/launching-features/#widen-review)   - [`origin-trial`](https://www.chromium.org/blink/launching-features/#origin-trials)   - [`shipping`](https://www.chromium.org/blink/launching-features/#new-feature-prepare-to-ship)   - `shipped` - The feature is enabled by default in Chromium.   # noqa: E501

        :return: The current_stage of this OutstandingReview.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage: str):
        """Sets the current_stage of this OutstandingReview.

        The development stage that the feature has reached:   - [`incubating`](https://www.chromium.org/blink/launching-features/#start-incubating)   - [`prototyping`](https://www.chromium.org/blink/launching-features/#prototyping)   - [`dev-trial`](https://www.chromium.org/blink/launching-features/#dev-trials)   - [`wide-review`](https://www.chromium.org/blink/launching-features/#widen-review)   - [`origin-trial`](https://www.chromium.org/blink/launching-features/#origin-trials)   - [`shipping`](https://www.chromium.org/blink/launching-features/#new-feature-prepare-to-ship)   - `shipped` - The feature is enabled by default in Chromium.   # noqa: E501

        :param current_stage: The current_stage of this OutstandingReview.
        :type current_stage: str
        """
        allowed_values = ["incubating", "prototyping", "dev-trial", "wide-review", "origin-trial", "shipping", "shipped"]  # noqa: E501
        if current_stage not in allowed_values:
            raise ValueError(
                "Invalid value for `current_stage` ({0}), must be one of {1}"
                .format(current_stage, allowed_values)
            )

        self._current_stage = current_stage

    @property
    def estimated_start_milestone(self) -> int:
        """Gets the estimated_start_milestone of this OutstandingReview.


        :return: The estimated_start_milestone of this OutstandingReview.
        :rtype: int
        """
        return self._estimated_start_milestone

    @estimated_start_milestone.setter
    def estimated_start_milestone(self, estimated_start_milestone: int):
        """Sets the estimated_start_milestone of this OutstandingReview.


        :param estimated_start_milestone: The estimated_start_milestone of this OutstandingReview.
        :type estimated_start_milestone: int
        """

        self._estimated_start_milestone = estimated_start_milestone

    @property
    def estimated_end_milestone(self) -> int:
        """Gets the estimated_end_milestone of this OutstandingReview.


        :return: The estimated_end_milestone of this OutstandingReview.
        :rtype: int
        """
        return self._estimated_end_milestone

    @estimated_end_milestone.setter
    def estimated_end_milestone(self, estimated_end_milestone: int):
        """Sets the estimated_end_milestone of this OutstandingReview.


        :param estimated_end_milestone: The estimated_end_milestone of this OutstandingReview.
        :type estimated_end_milestone: int
        """

        self._estimated_end_milestone = estimated_end_milestone

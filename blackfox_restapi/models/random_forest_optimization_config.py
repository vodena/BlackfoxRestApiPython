# coding: utf-8

"""
    BlackFox

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from blackfox_restapi.configuration import Configuration
from blackfox_restapi.models.optimization_engine_config import OptimizationEngineConfig
from blackfox_restapi.models.problem_type import ProblemType
from blackfox_restapi.models.binary_metric import BinaryMetric
from blackfox_restapi.models.regression_metric import RegressionMetric
from blackfox_restapi.models.range_int import RangeInt

class RandomForestOptimizationConfig(object):
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
        'dataset_id': 'str',
        'validation_set_id': 'str',
        'inputs': 'list[InputConfig]',
        'output_ranges': 'list[Range]',
        'problem_type': 'ProblemType',
        'binary_optimization_metric': 'BinaryMetric',
        'regression_optimization_metric': 'RegressionMetric',
        'validation_split': 'float',
        'random_seed': 'int',
        'engine_config': 'OptimizationEngineConfig',
        'number_of_estimators': 'RangeInt',
        'max_depth': 'RangeInt',
        'max_features': 'Range'
    }

    attribute_map = {
        'dataset_id': 'datasetId',
        'validation_set_id': 'validationSetId',
        'inputs': 'inputs',
        'output_ranges': 'outputRanges',
        'problem_type': 'problemType',
        'binary_optimization_metric': 'binaryOptimizationMetric',
        'regression_optimization_metric': 'regressionOptimizationMetric',
        'validation_split': 'validationSplit',
        'random_seed': 'randomSeed',
        'engine_config': 'engineConfig',
        'number_of_estimators': 'numberOfEstimators',
        'max_depth': 'maxDepth',
        'max_features': 'maxFeatures'
    }

    def __init__(self, dataset_id=None, validation_set_id=None, inputs=None, output_ranges=None, problem_type=ProblemType.REGRESSION, binary_optimization_metric=BinaryMetric.ROC_AUC, regression_optimization_metric=RegressionMetric.MAE, validation_split=0.2, random_seed=300, engine_config=OptimizationEngineConfig(), number_of_estimators=None, max_depth=None, max_features=None, local_vars_configuration=None):  # noqa: E501
        """RandomForestOptimizationConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dataset_id = None
        self._validation_set_id = None
        self._inputs = None
        self._output_ranges = None
        self._problem_type = None
        self._binary_optimization_metric = None
        self._regression_optimization_metric = None
        self._validation_split = None
        self._random_seed = None
        self._engine_config = None
        self._number_of_estimators = None
        self._max_depth = None
        self._max_features = None
        self.discriminator = None

        self.dataset_id = dataset_id
        self.validation_set_id = validation_set_id
        self.inputs = inputs
        self.output_ranges = output_ranges
        if problem_type is not None:
            self.problem_type = problem_type
        if binary_optimization_metric is not None:
            self.binary_optimization_metric = binary_optimization_metric
        if regression_optimization_metric is not None:
            self.regression_optimization_metric = regression_optimization_metric
        self.validation_split = validation_split
        self.random_seed = random_seed
        self.engine_config = engine_config
        if number_of_estimators is not None:
        	self.number_of_estimators = number_of_estimators
        if max_depth is not None:
            self.max_depth = max_depth
        if max_features is not None:
            self.max_features = max_features

    @property
    def dataset_id(self):
        """Gets the dataset_id of this RandomForestOptimizationConfig.  # noqa: E501

        Data set id on which to train model  # noqa: E501

        :return: The dataset_id of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this RandomForestOptimizationConfig.

        Data set id on which to train model  # noqa: E501

        :param dataset_id: The dataset_id of this RandomForestOptimizationConfig.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def validation_set_id(self):
        """Gets the validation_set_id of this RandomForestOptimizationConfig.  # noqa: E501

        Data set id on which to validate model  # noqa: E501

        :return: The validation_set_id of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._validation_set_id

    @validation_set_id.setter
    def validation_set_id(self, validation_set_id):
        """Sets the validation_set_id of this RandomForestOptimizationConfig.

        Data set id on which to validate model  # noqa: E501

        :param validation_set_id: The validation_set_id of this RandomForestOptimizationConfig.  # noqa: E501
        :type: str
        """

        self._validation_set_id = validation_set_id

    @property
    def inputs(self):
        """Gets the inputs of this RandomForestOptimizationConfig.  # noqa: E501

        Define min and max value for each output column(feature), and is input optional  # noqa: E501

        :return: The inputs of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: list[InputConfig]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this RandomForestOptimizationConfig.

        Define min and max value for each output column(feature), and is input optional  # noqa: E501

        :param inputs: The inputs of this RandomForestOptimizationConfig.  # noqa: E501
        :type: list[InputConfig]
        """

        self._inputs = inputs

    @property
    def output_ranges(self):
        """Gets the output_ranges of this RandomForestOptimizationConfig.  # noqa: E501

        Define min and max value for each output column(feature)  # noqa: E501

        :return: The output_ranges of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: list[Range]
        """
        return self._output_ranges

    @output_ranges.setter
    def output_ranges(self, output_ranges):
        """Sets the output_ranges of this RandomForestOptimizationConfig.

        Define min and max value for each output column(feature)  # noqa: E501

        :param output_ranges: The output_ranges of this RandomForestOptimizationConfig.  # noqa: E501
        :type: list[Range]
        """

        self._output_ranges = output_ranges

    @property
    def problem_type(self):
        """Gets the problem_type of this RandomForestOptimizationConfig.  # noqa: E501

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :return: The problem_type of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: ProblemType
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """Sets the problem_type of this RandomForestOptimizationConfig.

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :param problem_type: The problem_type of this RandomForestOptimizationConfig.  # noqa: E501
        :type: ProblemType
        """

        self._problem_type = problem_type

    @property
    def binary_optimization_metric(self):
        """Gets the binary_optimization_metric of this RandomForestOptimizationConfig.  # noqa: E501

        USED ONLY IN BINARY CLASSIFICATION.  Default metric: ROC_AUC (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :return: The binary_optimization_metric of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: BinaryMetric
        """
        return self._binary_optimization_metric

    @binary_optimization_metric.setter
    def binary_optimization_metric(self, binary_optimization_metric):
        """Sets the binary_optimization_metric of this RandomForestOptimizationConfig.

        USED ONLY IN BINARY CLASSIFICATION.  Default metric: ROC_AUC (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :param binary_optimization_metric: The binary_optimization_metric of this RandomForestOptimizationConfig.  # noqa: E501
        :type: BinaryMetric
        """

        self._binary_optimization_metric = binary_optimization_metric

    @property
    def regression_optimization_metric(self):
        """Gets the regression_optimization_metric of this RandomForestOptimizationConfig.  # noqa: E501

        USED ONLY IN REGRESSION.  Default metric: MAE (MEAN ABSOLUTE ERROR).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :return: The regression_optimization_metric of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: RegressionMetric
        """
        return self._regression_optimization_metric

    @regression_optimization_metric.setter
    def regression_optimization_metric(self, regression_optimization_metric):
        """Sets the regression_optimization_metric of this RandomForestOptimizationConfig.

        USED ONLY IN REGRESSION.  Default metric: MAE (MEAN ABSOLUTE ERROR).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :param regression_optimization_metric: The regression_optimization_metric of this RandomForestOptimizationConfig.  # noqa: E501
        :type: RegressionMetric
        """

        self._regression_optimization_metric = regression_optimization_metric

    @property
    def validation_split(self):
        """Gets the validation_split of this RandomForestOptimizationConfig.  # noqa: E501

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :return: The validation_split of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: float
        """
        return self._validation_split

    @validation_split.setter
    def validation_split(self, validation_split):
        """Sets the validation_split of this RandomForestOptimizationConfig.

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :param validation_split: The validation_split of this RandomForestOptimizationConfig.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and validation_split is None:  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                validation_split is not None and validation_split > 1):  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                validation_split is not None and validation_split < 0):  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must be a value greater than or equal to `0`")  # noqa: E501

        self._validation_split = validation_split

    @property
    def random_seed(self):
        """Gets the random_seed of this RandomForestOptimizationConfig.  # noqa: E501

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :return: The random_seed of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this RandomForestOptimizationConfig.

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :param random_seed: The random_seed of this RandomForestOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._random_seed = random_seed

    @property
    def engine_config(self):
        """Gets the engine_config of this RandomForestOptimizationConfig.  # noqa: E501

        Optimization engine config  # noqa: E501

        :return: The engine_config of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: OptimizationEngineConfig
        """
        return self._engine_config

    @engine_config.setter
    def engine_config(self, engine_config):
        """Sets the engine_config of this RandomForestOptimizationConfig.

        Optimization engine config  # noqa: E501

        :param engine_config: The engine_config of this RandomForestOptimizationConfig.  # noqa: E501
        :type: OptimizationEngineConfig
        """

        self._engine_config = engine_config

    @property
    def number_of_estimators(self):
        """Gets the number_of_estimators of this RandomForestOptimizationConfig.  # noqa: E501

        Number of estimators  # noqa: E501

        :return: The number_of_estimators of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._number_of_estimators

    @number_of_estimators.setter
    def number_of_estimators(self, number_of_estimators):
        """Sets the number_of_estimators of this RandomForestOptimizationConfig.

        Number of estimators  # noqa: E501

        :param number_of_estimators: The number_of_estimators of this RandomForestOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """
        if self.local_vars_configuration.client_side_validation and number_of_estimators is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_estimators`, must not be `None`")  # noqa: E501

        self._number_of_estimators = number_of_estimators

    @property
    def max_depth(self):
        """Gets the max_depth of this RandomForestOptimizationConfig.  # noqa: E501

        Max depth of tree  # noqa: E501

        :return: The max_depth of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        """Sets the max_depth of this RandomForestOptimizationConfig.

        Max depth of tree  # noqa: E501

        :param max_depth: The max_depth of this RandomForestOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """
        if self.local_vars_configuration.client_side_validation and max_depth is None:  # noqa: E501
            raise ValueError("Invalid value for `max_depth`, must not be `None`")  # noqa: E501

        self._max_depth = max_depth

    @property
    def max_features(self):
        """Gets the max_features of this RandomForestOptimizationConfig.  # noqa: E501

        Max features  # noqa: E501

        :return: The max_features of this RandomForestOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._max_features

    @max_features.setter
    def max_features(self, max_features):
        """Sets the max_features of this RandomForestOptimizationConfig.

        Max features  # noqa: E501

        :param max_features: The max_features of this RandomForestOptimizationConfig.  # noqa: E501
        :type: Range
        """
        if self.local_vars_configuration.client_side_validation and max_features is None:  # noqa: E501
            raise ValueError("Invalid value for `max_features`, must not be `None`")  # noqa: E501

        self._max_features = max_features

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
        if not isinstance(other, RandomForestOptimizationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RandomForestOptimizationConfig):
            return True

        return self.to_dict() != other.to_dict()

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
from blackfox_restapi.models.ann_optimization_engine_config import AnnOptimizationEngineConfig
from blackfox_restapi.models.problem_type import ProblemType
from blackfox_restapi.models.binary_metric import BinaryMetric

class AnnOptimizationConfig(object):
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
        'dropout': 'Range',
        'batch_size': 'int',
        'dataset_id': 'str',
        'inputs': 'list[InputConfig]',
        'output_ranges': 'list[Range]',
        'problem_type': 'ProblemType',
        'binary_optimization_metric': 'BinaryMetric',
        'hidden_layer_count_range': 'RangeInt',
        'neurons_per_layer': 'RangeInt',
        'training_algorithms': 'list[NeuralNetworkTrainingAlgorithm]',
        'activation_functions': 'list[NeuralNetworkActivationFunction]',
        'max_epoch': 'int',
        'cross_validation': 'bool',
        'validation_split': 'float',
        'random_seed': 'int',
        'engine_config': 'AnnOptimizationEngineConfig'
    }

    attribute_map = {
        'dropout': 'dropout',
        'batch_size': 'batchSize',
        'dataset_id': 'datasetId',
        'inputs': 'inputs',
        'output_ranges': 'outputRanges',
        'problem_type': 'problemType',
        'binary_optimization_metric': 'binaryOptimizationMetric',
        'hidden_layer_count_range': 'hiddenLayerCountRange',
        'neurons_per_layer': 'neuronsPerLayer',
        'training_algorithms': 'trainingAlgorithms',
        'activation_functions': 'activationFunctions',
        'max_epoch': 'maxEpoch',
        'cross_validation': 'crossValidation',
        'validation_split': 'validationSplit',
        'random_seed': 'randomSeed',
        'engine_config': 'engineConfig'
    }

    def __init__(self, dropout=None, batch_size=512, dataset_id=None, inputs=None, output_ranges=None, problem_type=ProblemType.REGRESSION, binary_optimization_metric=BinaryMetric.AUC, hidden_layer_count_range=None, neurons_per_layer=None, training_algorithms=["Adadelta","Adagrad","Adam","Adamax","Nadam","RMSprop","SGD"], activation_functions=["Elu","HardSigmoid","Linear","ReLu","Selu","Sigmoid","SoftMax","SoftPlus","SoftSign","TanH"], max_epoch=3000, cross_validation=False, validation_split=0.2, random_seed=300, engine_config=AnnOptimizationEngineConfig(), local_vars_configuration=None):  # noqa: E501
        """AnnOptimizationConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dropout = None
        self._batch_size = None
        self._dataset_id = None
        self._inputs = None
        self._output_ranges = None
        self._problem_type = None
        self._binary_optimization_metric = None
        self._hidden_layer_count_range = None
        self._neurons_per_layer = None
        self._training_algorithms = None
        self._activation_functions = None
        self._max_epoch = None
        self._cross_validation = None
        self._validation_split = None
        self._random_seed = None
        self._engine_config = None
        self.discriminator = None

        self.dropout = dropout
        if batch_size is not None:
            self.batch_size = batch_size
        self.dataset_id = dataset_id
        self.inputs = inputs
        self.output_ranges = output_ranges
        if problem_type is not None:
            self.problem_type = problem_type
        if binary_optimization_metric is not None:
            self.binary_optimization_metric = binary_optimization_metric
        self.hidden_layer_count_range = hidden_layer_count_range
        self.neurons_per_layer = neurons_per_layer
        self.training_algorithms = training_algorithms
        self.activation_functions = activation_functions
        self.max_epoch = max_epoch
        if cross_validation is not None:
            self.cross_validation = cross_validation
        self.validation_split = validation_split
        self.random_seed = random_seed
        self.engine_config = engine_config

    @property
    def dropout(self):
        """Gets the dropout of this AnnOptimizationConfig.  # noqa: E501


        :return: The dropout of this AnnOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._dropout

    @dropout.setter
    def dropout(self, dropout):
        """Sets the dropout of this AnnOptimizationConfig.


        :param dropout: The dropout of this AnnOptimizationConfig.  # noqa: E501
        :type: Range
        """

        self._dropout = dropout

    @property
    def batch_size(self):
        """Gets the batch_size of this AnnOptimizationConfig.  # noqa: E501


        :return: The batch_size of this AnnOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this AnnOptimizationConfig.


        :param batch_size: The batch_size of this AnnOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

    @property
    def dataset_id(self):
        """Gets the dataset_id of this AnnOptimizationConfig.  # noqa: E501

        Data set id on which to train network  # noqa: E501

        :return: The dataset_id of this AnnOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this AnnOptimizationConfig.

        Data set id on which to train network  # noqa: E501

        :param dataset_id: The dataset_id of this AnnOptimizationConfig.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def inputs(self):
        """Gets the inputs of this AnnOptimizationConfig.  # noqa: E501

        Define min and max value for each output column(feature), and is input optional  # noqa: E501

        :return: The inputs of this AnnOptimizationConfig.  # noqa: E501
        :rtype: list[InputConfig]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this AnnOptimizationConfig.

        Define min and max value for each output column(feature), and is input optional  # noqa: E501

        :param inputs: The inputs of this AnnOptimizationConfig.  # noqa: E501
        :type: list[InputConfig]
        """

        self._inputs = inputs

    @property
    def output_ranges(self):
        """Gets the output_ranges of this AnnOptimizationConfig.  # noqa: E501

        Define min and max value for each output column(feature)  # noqa: E501

        :return: The output_ranges of this AnnOptimizationConfig.  # noqa: E501
        :rtype: list[Range]
        """
        return self._output_ranges

    @output_ranges.setter
    def output_ranges(self, output_ranges):
        """Sets the output_ranges of this AnnOptimizationConfig.

        Define min and max value for each output column(feature)  # noqa: E501

        :param output_ranges: The output_ranges of this AnnOptimizationConfig.  # noqa: E501
        :type: list[Range]
        """

        self._output_ranges = output_ranges

    @property
    def problem_type(self):
        """Gets the problem_type of this AnnOptimizationConfig.  # noqa: E501

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :return: The problem_type of this AnnOptimizationConfig.  # noqa: E501
        :rtype: ProblemType
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """Sets the problem_type of this AnnOptimizationConfig.

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :param problem_type: The problem_type of this AnnOptimizationConfig.  # noqa: E501
        :type: ProblemType
        """

        self._problem_type = problem_type

    @property
    def binary_optimization_metric(self):
        """Gets the binary_optimization_metric of this AnnOptimizationConfig.  # noqa: E501

        USED ONLY IN BINARY CLASSIFICATION.  Default metric: Auc (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :return: The binary_optimization_metric of this AnnOptimizationConfig.  # noqa: E501
        :rtype: BinaryMetric
        """
        return self._binary_optimization_metric

    @binary_optimization_metric.setter
    def binary_optimization_metric(self, binary_optimization_metric):
        """Sets the binary_optimization_metric of this AnnOptimizationConfig.

        USED ONLY IN BINARY CLASSIFICATION.  Default metric: Auc (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :param binary_optimization_metric: The binary_optimization_metric of this AnnOptimizationConfig.  # noqa: E501
        :type: BinaryMetric
        """

        self._binary_optimization_metric = binary_optimization_metric

    @property
    def hidden_layer_count_range(self):
        """Gets the hidden_layer_count_range of this AnnOptimizationConfig.  # noqa: E501

        Range in which to search number of hidden layers  # noqa: E501

        :return: The hidden_layer_count_range of this AnnOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._hidden_layer_count_range

    @hidden_layer_count_range.setter
    def hidden_layer_count_range(self, hidden_layer_count_range):
        """Sets the hidden_layer_count_range of this AnnOptimizationConfig.

        Range in which to search number of hidden layers  # noqa: E501

        :param hidden_layer_count_range: The hidden_layer_count_range of this AnnOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """

        self._hidden_layer_count_range = hidden_layer_count_range

    @property
    def neurons_per_layer(self):
        """Gets the neurons_per_layer of this AnnOptimizationConfig.  # noqa: E501

        Range in which to search number of neurons per layer  # noqa: E501

        :return: The neurons_per_layer of this AnnOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._neurons_per_layer

    @neurons_per_layer.setter
    def neurons_per_layer(self, neurons_per_layer):
        """Sets the neurons_per_layer of this AnnOptimizationConfig.

        Range in which to search number of neurons per layer  # noqa: E501

        :param neurons_per_layer: The neurons_per_layer of this AnnOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """

        self._neurons_per_layer = neurons_per_layer

    @property
    def training_algorithms(self):
        """Gets the training_algorithms of this AnnOptimizationConfig.  # noqa: E501

        List of training algorithms to use  # noqa: E501

        :return: The training_algorithms of this AnnOptimizationConfig.  # noqa: E501
        :rtype: list[NeuralNetworkTrainingAlgorithm]
        """
        return self._training_algorithms

    @training_algorithms.setter
    def training_algorithms(self, training_algorithms):
        """Sets the training_algorithms of this AnnOptimizationConfig.

        List of training algorithms to use  # noqa: E501

        :param training_algorithms: The training_algorithms of this AnnOptimizationConfig.  # noqa: E501
        :type: list[NeuralNetworkTrainingAlgorithm]
        """

        self._training_algorithms = training_algorithms

    @property
    def activation_functions(self):
        """Gets the activation_functions of this AnnOptimizationConfig.  # noqa: E501

        List of activation functions to use  # noqa: E501

        :return: The activation_functions of this AnnOptimizationConfig.  # noqa: E501
        :rtype: list[NeuralNetworkActivationFunction]
        """
        return self._activation_functions

    @activation_functions.setter
    def activation_functions(self, activation_functions):
        """Sets the activation_functions of this AnnOptimizationConfig.

        List of activation functions to use  # noqa: E501

        :param activation_functions: The activation_functions of this AnnOptimizationConfig.  # noqa: E501
        :type: list[NeuralNetworkActivationFunction]
        """

        self._activation_functions = activation_functions

    @property
    def max_epoch(self):
        """Gets the max_epoch of this AnnOptimizationConfig.  # noqa: E501

        Maximum number of epoch  # noqa: E501

        :return: The max_epoch of this AnnOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_epoch

    @max_epoch.setter
    def max_epoch(self, max_epoch):
        """Sets the max_epoch of this AnnOptimizationConfig.

        Maximum number of epoch  # noqa: E501

        :param max_epoch: The max_epoch of this AnnOptimizationConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_epoch is None:  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_epoch is not None and max_epoch > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_epoch is not None and max_epoch < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_epoch = max_epoch

    @property
    def cross_validation(self):
        """Gets the cross_validation of this AnnOptimizationConfig.  # noqa: E501

        Use cross validation  # noqa: E501

        :return: The cross_validation of this AnnOptimizationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._cross_validation

    @cross_validation.setter
    def cross_validation(self, cross_validation):
        """Sets the cross_validation of this AnnOptimizationConfig.

        Use cross validation  # noqa: E501

        :param cross_validation: The cross_validation of this AnnOptimizationConfig.  # noqa: E501
        :type: bool
        """

        self._cross_validation = cross_validation

    @property
    def validation_split(self):
        """Gets the validation_split of this AnnOptimizationConfig.  # noqa: E501

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :return: The validation_split of this AnnOptimizationConfig.  # noqa: E501
        :rtype: float
        """
        return self._validation_split

    @validation_split.setter
    def validation_split(self, validation_split):
        """Sets the validation_split of this AnnOptimizationConfig.

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :param validation_split: The validation_split of this AnnOptimizationConfig.  # noqa: E501
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
        """Gets the random_seed of this AnnOptimizationConfig.  # noqa: E501

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :return: The random_seed of this AnnOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this AnnOptimizationConfig.

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :param random_seed: The random_seed of this AnnOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._random_seed = random_seed

    @property
    def engine_config(self):
        """Gets the engine_config of this AnnOptimizationConfig.  # noqa: E501

        Optimization engine config  # noqa: E501

        :return: The engine_config of this AnnOptimizationConfig.  # noqa: E501
        :rtype: AnnOptimizationEngineConfig
        """
        return self._engine_config

    @engine_config.setter
    def engine_config(self, engine_config):
        """Sets the engine_config of this AnnOptimizationConfig.

        Optimization engine config  # noqa: E501

        :param engine_config: The engine_config of this AnnOptimizationConfig.  # noqa: E501
        :type: AnnOptimizationEngineConfig
        """

        self._engine_config = engine_config

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
        if not isinstance(other, AnnOptimizationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnOptimizationConfig):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    BlackFox

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import blackfox_restapi
from blackfox_restapi.models.xg_boost_optimization_status import XGBoostOptimizationStatus  # noqa: E501
from blackfox_restapi.rest import ApiException

class TestXGBoostOptimizationStatus(unittest.TestCase):
    """XGBoostOptimizationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XGBoostOptimizationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = blackfox_restapi.models.xg_boost_optimization_status.XGBoostOptimizationStatus()  # noqa: E501
        if include_optional :
            return XGBoostOptimizationStatus(
                guid = '0', 
                state = None, 
                generation = 56, 
                total_generations = 56, 
                validation_set_error = 1.337, 
                training_set_error = 1.337, 
                best_model = None
            )
        else :
            return XGBoostOptimizationStatus(
        )

    def testXGBoostOptimizationStatus(self):
        """Test XGBoostOptimizationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

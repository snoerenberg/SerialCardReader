# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.card import Card  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCardreaderController(BaseTestCase):
    """CardreaderController integration test stubs"""

    def test_cardreader_get_card_number_get(self):
        """Test case for cardreader_get_card_number_get

        Get cardnumber from serial reader
        """
        response = self.client.open(
            '/v1/cardreader/getCardNumber',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

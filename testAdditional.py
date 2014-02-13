"""                                                                                                             
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.\
RestTestCase                                                                                                    
"""

import unittest
import os
import testLib

class TestAddWithEmptyPassword(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """                                                                                                     
        Check that the response data dictionary matches the expected values                                     
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAddWithEmptyPW(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : ''} )
        self.assertResponse(respData, count = 1)

    def testAddWithMaxLengthUserName(self):
        s = ''
        for i in range(128):
            s += 'a'
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : s, 'password' : ''} )
        self.assertResponse(respData, count = 1)

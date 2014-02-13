"""                                                                                                             
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.\
RestTestCase                                                                                                    
"""

import unittest
import os
import testLib

class TestAdditional(testLib.RestTestCase):
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
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : ''} )
        self.assertResponse(respData, count = 1)

    def testAddWithMaxLengthUserName(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        s = ''
        for i in range(128):
            s += 'a'
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : s, 'password' : ''} )
        self.assertResponse(respData, count = 1)

    def testAddWithMaxPasswordLength(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        s = ''
        for i in range(128):
            s += 'a'
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'Bob', 'password' : s} )
        self.assertResponse(respData, count = 1)

    def testAddWithOverlyLongUserName(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        s = ''
        for i in range(129):
            s += 'a'
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : s, 'password' : 'blah'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

    def testMultipleLogin(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'blah'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'b', 'password' : 'blah'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'a', 'password' : 'blah'} )
        self.assertResponse(respData, count = 2)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'b', 'password' : 'blah'} )
        self.assertResponse(respData, count = 2)

    def testUsersRemovedProperly(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'blah'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'b', 'password' : 'blah'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = { } )
        self.assertResponse(respData, count = None)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'a', 'password' : 'blah'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'b', 'password' : 'blah'} )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

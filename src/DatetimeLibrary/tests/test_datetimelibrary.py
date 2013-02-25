#-------------------------------------------------------------------------------
# Copyright 2013 Maldivica, Inc (www.maldivica.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------
'''
Created on Oct 21, 2012

@author: Trey Duskin <trey@maldivica.com>
'''
import unittest

class TestDatetimeLibrary(unittest.TestCase):
    '''
    tests functions of DatetimeLibrary
    '''
    
    def test_timestamps_should_be_equal(self):
        from DatetimeLibrary.keywords import Keywords
        keywords = Keywords()
        timestamp1 = 'Wed, 24 Oct 2012 16:40:47'
        timeformat1 = '%a, %d %b %Y %H:%M:%S'
        timestamp2 = '2012-10-24T16:40:47.000000'
        timeformat2 = '%Y-%m-%dT%H:%M:%S.%f'
        timestamp3 = 'Mon, 15 Oct 1980 06:25:44 GMT'
        timeformat3 = '%a, %d %b %Y %H:%M:%S %Z'
        timestampTZ = '10/24/12 EDT 15:54:42.000000'
        timeformatTZ = '%m/%d/%y %Z %H:%M:%S.%f'
        
        '''test dateutil parser'''
        self.assertTrue(keywords.timestamps_should_be_equal(timestamp1,
                                                            timestamp2))
        '''test datetime strptime'''
        self.assertTrue(keywords.timestamps_should_be_equal(timestamp1,
                                                            timestamp2,
                                                            timeformat1,
                                                            timeformat2))
        '''test mix of both'''
        self.assertTrue(keywords.timestamps_should_be_equal(timestamp1, 
                                                            timestamp2, 
                                                            timeformat1))
        
        '''tz tests srtptime'''
        self.assertTrue(keywords.timestamps_should_be_equal(timestampTZ, 
                                                            timestampTZ, 
                                                            timeformatTZ, 
                                                            timeformatTZ))
        '''tz tests srtptime vs parser'''
        '''TODO: this fails, figure out how to make it work
        self.assertTrue(keywords.timestamps_should_be_equal(timestampTZ, 
                                                            timestampTZ, 
                                                            format1=timeformatTZ))'''
        
        '''failure tests'''
        self.assertRaises(AssertionError,keywords.timestamps_should_be_equal,
                          timestamp1,timestamp3,timeformat1,timeformat3)
        self.assertRaises(AssertionError,keywords.timestamps_should_be_equal,
                          timestamp2,timestamp3,timeformat2,timeformat3)
        self.assertRaises(ValueError,keywords.timestamps_should_be_equal,
                          timestamp1,timestamp3,timeformat2,timeformat1)    
    
    def test_timestamps_should_be_close(self):
        from DatetimeLibrary.keywords import Keywords
        keywords = Keywords()
        timestamp1 = 'Mon, 15 Oct 2012 06:25:44 GMT'
        timeformat1 = '%a, %d %b %Y %H:%M:%S %Z'
        timestamp2 = '2012-10-15T06:25:47.5'
        timeformat2 = '%Y-%m-%dT%H:%M:%S.%f'
        timestamp3 = 'Mon, 15 Oct 2012 07:25:44 GMT'
        timeformat3 = '%a, %d %b %Y %H:%M:%S %Z'
        
        self.assertTrue(keywords.timestamps_should_be_close(timestamp1,
                                                            timestamp2,
                                                            '4.0',
                                                            timeformat1,
                                                            timeformat2))
        
        self.assertTrue(keywords.timestamps_should_be_close(timestamp1,
                                                            timestamp2,
                                                            3.5,
                                                            timeformat1,
                                                            timeformat2))
        
        self.assertTrue(keywords.timestamps_should_be_close(timestamp1,
                                                            timestamp3,
                                                            3600.0,
                                                            timeformat1,
                                                            timeformat3))
        
        self.assertRaises(AssertionError,keywords.timestamps_should_be_close,
                          timestamp1,timestamp2,'3.0',timeformat1,timeformat2)
        

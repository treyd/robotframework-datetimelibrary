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
from datetime import datetime
import math
from dateutil import parser as dateparser

class Keywords(object):

    def _parse_timestamps(self, ts1, ts2, format1, format2):
        """parses timestamps and returns datetime objects
        
        if format1 or format2 is given, use strptime to parse ts1
        or ts2, respectively
        """
        if format1:
            timestamp1 = datetime.strptime(ts1, format1)
        else:
            timestamp1 = dateparser.parse(ts1)
        if format2:
            timestamp2 = datetime.strptime(ts2, format2)
        else:
            timestamp2 = dateparser.parse(ts2)
        return timestamp1, timestamp2

    def timestamps_should_be_equal(self, ts1, ts2, 
                                   format1=None, format2=None):
        """
        Checks if timestamps ts1 and ts2 are equal.
        
        Timestamps can be given in any form which will be parsed by 
        dateutil.parser
        
        You can optionally provide a format string for either timestamp.  
        Format strings should follow _strftime_ format codes.
        """
        timestamp1, timestamp2 = self._parse_timestamps(ts1, 
                                                        ts2, 
                                                        format1, 
                                                        format2)
        
        if timestamp1 != timestamp2:
            raise AssertionError("Given timestamps %s and %s are not equal." 
                                 % (ts1,ts2))
        
        return True

    
    def timestamps_should_be_close(self, ts1, ts2, limit, 
                                   format1=None, format2=None):
        """
        Checks if timestamps _ts1_ and _ts2_ are within _limit_ seconds 
        of each other.
        
        Timestamps can be given in any form which will be parsed by 
        dateutil.parser
        
        You can optionally provide a format string for either timestamp.
        Format strings should follow _strftime_ format codes.
        """
        timestamp1, timestamp2 = self._parse_timestamps(ts1, 
                                                        ts2, 
                                                        format1, 
                                                        format2)
        
        flimit = float(limit)
        
        delta = timestamp2 - timestamp1
        fdelta = math.fabs(float(delta.total_seconds()))
        
        if fdelta > flimit:
            raise AssertionError("Timestamps %s and %s are %f seconds apart, "
                                 "greater than the limit of %f seconds" %
                                 (ts1,ts2,fdelta,flimit))
            
        return True

    
    
    
    




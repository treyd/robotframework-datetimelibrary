from datetime import datetime
import math
from dateutil.parser import *
class Keywords:
    
    

    def _parse_timestamps(self, ts1, ts2, format1, format2):
        if format1 == None:
            timestamp1 = parse(ts1)
        else:
            timestamp1 = datetime.strptime(ts1, format1)
        if format2 == None:
            timestamp2 = parse(ts2)
        else:
            timestamp2 = datetime.strptime(ts2, format2)
        return timestamp1, timestamp2

    def timestamps_should_be_equal(self, ts1, ts2, format1=None, format2=None):
        """
        Checks if timestamps ts1 and ts2 are equal.
        
        Timestamps can be given in any form which will be parsed by dateutil.parser
        
        You can optionally provide a format string for either timestamp.  Format strings
        should follow _strftime_ format codes.
        """
        timestamp1, timestamp2 = self._parse_timestamps(ts1, ts2, format1, format2)
        
        if timestamp1 != timestamp2:
            raise AssertionError("Given timestamps %s and %s are not equal." % (ts1,ts2))
        
        return True

    
    def timestamps_should_be_close(self, ts1, ts2, limit, format1=None, format2=None):
        """
        Checks if timestamps ts1 and ts2 are within limit seconds of each other.
        
        Timestamps can be given in any form which will be parsed by dateutil.parser
        
        You can optionally provide a format string for either timestamp.  Format strings
        should follow _strftime_ format codes.
        """
        timestamp1, timestamp2 = self._parse_timestamps(ts1, ts2, format1, format2)

        
        flimit = float(limit)
        
        delta = timestamp2 - timestamp1
        fdelta = math.fabs(float(delta.total_seconds()))
        
        if fdelta > flimit:
            raise AssertionError("Timestamps %s and %s are %f seconds apart, greater than the limit of %f seconds" %
                                 (ts1,ts2,fdelta,flimit))
            
        return True

    
    
    
    




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
from keywords import Keywords

__version__ = '0.01'

class DatetimeLibrary(Keywords):
    """
    DatetimeLibrary provides keywords for comparing date strings within Robotframework.
    
    Requires:
    
    python-datetime
    python-dateutil
    
    References:
    
       * http://docs.python.org/2/library/datetime.html - Python Standard Library, Datetime Documentation
       * http://labix.org/python-dateutil - Dateutil Library
    """
    
    ROBOT_LIBRARY_VERSION = __version__
    

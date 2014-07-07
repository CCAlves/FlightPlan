from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *

from qgis.core import *
from qgis.gui import *
 
import sys
import os
 
qgis_prefix = "C:/OSGeo4W/apps/qgis"

from FlightPlan_gui import *

class FlightPlan:
    
 
      def __init__(self,values):

  
         self.gsd = values[3]

         print(self.gsd)

		

		
 
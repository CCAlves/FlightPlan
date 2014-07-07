from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PyQt4 import uic

from qgis.core import *
from qgis.gui import *

from FlightPlan import *

import sys
import os

from MainClass_gui import Ui_MainWindow

qgis_prefix = "C:/OSGeo4W/apps/qgis"

class MainClass(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
  
		self.path = os.path.dirname( os.path.abspath(__file__) )
 
		self.setupUi(self)
 
		self.setWindowTitle("FlightPlan")
 
		self.canvas = QgsMapCanvas()
		self.canvas.useImageToRender(False)
		self.canvas.show()
 
		self.layout = QVBoxLayout(self.frame)
		self.layout.addWidget(self.canvas)
		self.setCentralWidget(self.canvas)
 
		
	def callAddFlightPlan(self):

         self.uiNewProjectScreen = uic.loadUi( os.path.join( self.path, "FlightPlan_gui.ui" ) )
         self.uiNewProjectScreen.show()

         values = [0,1,2,3]
             
         flightPlan = FlightPlan(values)
         
	def triggerAddFlightPlan(self):

         self.uiNewProjectScreen = uic.loadUi( os.path.join( self.path, "FlightPlan_gui.ui" ) )
         self.uiNewProjectScreen.show()

         values = [0,1,2,3]
             
         flightPlan = FlightPlan(values)
	
	 
		
def main(argv):
 
    	app = QApplication(argv)
 
    	QgsApplication.setPrefixPath(qgis_prefix, True)
    	QgsApplication.initQgis()
 
    	flightPlanMainWindow = MainClass()

    	flightPlanMainWindow.move(100,100)
    	flightPlanMainWindow.show()
     
        addFlightPlanACT = QAction( 'Add FlightPlan', flightPlanMainWindow)
        addFlightPlanACT.setShortcut('Ctrl+A')
        addFlightPlanACT.setStatusTip('Add a new flight plan')
        addFlightPlanACT.triggered.connect(flightPlanMainWindow.callAddFlightPlan)
     
        flightPlanMenuBar = flightPlanMainWindow.menuBar()
        
        menuProject = flightPlanMenuBar.addMenu('Project')
        menuProject.addAction(addFlightPlanACT)
        

	
	#graphic = QGraphicsView()
	#mScene =  QGraphicsScene();
	#graphic.setScene( mScene );
	#brush = QBrush(QColor.fromRgb(255,192,192))
	#mScene.setBackgroundBrush (brush)
	#graphic.show()
	
	#canvas = QgsMapCanvas()
	#canvas.useImageToRender(False)
	#canvas.show()
	
	# run!
	retval = app.exec_()
	
	# exit
	QgsApplication.exitQgis()
	sys.exit(retval)
	

 
if __name__ == "__main__":
	main(sys.argv)
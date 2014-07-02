from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import sys
import os

from FlightPlan_gui import Ui_MainWindow

# Environment variable QGISHOME must be set to the install directory
# before running the application
# qgis_prefix = os.getenv("QGISHOME")

qgis_prefix = "C:/OSGeo4W/apps/qgis"

class FlightPlan(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		
		# Required by Qt4 to initialize the UI
		self.setupUi(self)
		
		# Set the title for the app
		self.setWindowTitle("FlightPlan")
		 
		# Create the map canvas
		self.canvas = QgsMapCanvas()
		self.canvas.useImageToRender(False)
		self.canvas.show()
		
		# Lay our widgets out in the main window using a
		# vertical box layout
		self.layout = QVBoxLayout(self.frame)
		self.layout.addWidget(self.canvas)
		self.setCentralWidget(self.canvas)
		
	def showMap(self):
		self.canvas.show()
		print("Showmap")
		
def main(argv):
	# create Qt application
	app = QApplication(argv)
	
	# Initialize qgis libraries
	QgsApplication.setPrefixPath(qgis_prefix, True)
	QgsApplication.initQgis()
	# create main window
	
	wnd = FlightPlan()
	# Move the app window to upper left
	wnd.move(100,100)
	wnd.show()
	wnd.showMap()
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
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindowUI import Ui_MainWindow
import sys
import os
from enum import Enum, unique

VIDEO_EXTEND = [".mp4", ".avi"]

@unique
class ThingLevel(Enum):
	S = 0;
	A = 1;
	B = 2;
	Undefined = 3;

@unique
class ThingType(Enum):
	Video = 0;
	Directory = 1;

class Thing(object):
	def __init__(self, type_):
		self.type_ = type_
		self.level = ThingLevel.Undefined;

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.storage = {}
		self.setupUi(self)
		self.loadData()
		self.scanFile()

	def loadData(self):
		pass

	def saveData(self):
		pass

	def scanFile(self):
		for thing in os.listdir("./Storage"):
			filename, ext = os.path.splitext(thing)
			if ext.lower() in VIDEO_EXTEND:
				self.storage[thing] = Thing(ThingType.Video)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	try:
		sys.exit(app.exec_())
	except SystemExit:
		os._exit(0)

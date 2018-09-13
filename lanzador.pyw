import sys
from editor import *

class miLanzador (QtGui.QFrame):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Aplication()
        self.ui.setup(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myApp = miLanzador()
    myApp.show()
    sys.exit(app.exec_())

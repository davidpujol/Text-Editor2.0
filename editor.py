from PyQt4 import QtCore, QtGui
import sys
import os

_fromUtf8 = QtCore.QString.fromUtf8


class Aplication(object):
    def setup (self, Frame):  # constructor
        Frame.resize(800, 600)
        Frame.setMaximumHeight(600)
        Frame.setMaximumWidth(800)
        self.name = QtCore.QString

        self.menu = QtGui.QMenuBar(Frame)
        self.files = self.menu.addMenu('&Files')
        self.edit = self.menu.addMenu('&Edit')
        self.mode = self.menu.addMenu('&Mode')
        self.help = self.menu.addMenu('&Help')


        #CREEM EL WIDGET AMB L'EDITOR I EL TAB
        self.counter = 1
        self.centralwidget = QtGui.QWidget(Frame)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 30, 500, 500))
        self.tab = QtGui.QWidget()  #creem un tab
        self.text = QtGui.QTextEdit(self.tab)
        self.text.setMinimumHeight(500)
        self.text.setMinimumWidth(500)
        self.tabWidget.addTab(self.tab, "Tab1")  #l'incloim al menu de tabs


        #CREEM EL WIDGET PER A FER LA BUSQUEDA DE DIRECTORIS
        self.leftwidget = QtGui.QTreeWidget(Frame)
        self.leftwidget.setGeometry(0,30,200,500)

        #CREEM EL WIDGET PER A FER LA BUSQUEDA DE DIRECTORIS
        self.leftwidget = QtGui.QTreeWidget(Frame)
        self.leftwidget.setGeometry(0,30,200,500)
        self.leftwidget.setHeaderLabel('Directories:')
        
        self.configure_files(Frame)
        self.configure_edit(Frame)
        self.configure_mode(Frame)
        self.configure_help(Frame)
        self.menu.raise_()

    def configure_files (self, Frame):
        self.new = QtGui.QAction("&New", Frame)
        self.new.setShortcut("Ctrl+N")
        self.new.triggered.connect(self.new_func)
        self.files.addAction(self.new)

        self.open = QtGui.QAction("&Open", Frame)
        self.open.setShortcut("Ctrl+O")
        self.open.triggered.connect (self.open_func)
        self.files.addAction(self.open)

        self.save = QtGui.QAction("&Save", Frame)
        self.save.setShortcut("Ctrl+S")
        self.save.triggered.connect(self.save_func)
        self.files.addAction(self.save)

        self.save_as = QtGui.QAction("&Save as", Frame)
        self.save_as.triggered.connect(self.save_as_func)
        self.files.addAction(self.save_as)

        self.configuration = QtGui.QAction("&Configuration", Frame)
        #self.configuration.triggered.connect(self.configuration_func)
        self.files.addAction(self.configuration)

        self.close_tab = QtGui.QAction("&Close tab", Frame)
        self.close_tab.setShortcut("Ctrl+W")
        self.close_tab.triggered.connect(self.close_tab_func)
        self.files.addAction(self.close_tab)

        self.close = QtGui.QAction("&Close", Frame)
        self.close.setShortcut("Ctrl+Q")
        self.close.triggered.connect(self.close_func)
        self.files.addAction(self.close)

    def configure_edit (self, Frame):
        self.copy = QtGui.QAction("&Copy", Frame)
        self.copy.setShortcut("Ctrl+C")
        self.copy.triggered.connect(self.copy_func)
        self.edit.addAction(self.copy)

        self.paste = QtGui.QAction("&Paste", Frame)
        self.paste.setShortcut("Ctrl+V")
        self.paste.triggered.connect(self.paste_func)
        self.edit.addAction(self.paste)
        
        self.undo = QtGui.QAction("&Undo", Frame)
        self.undo.triggered.connect(self.undo_func)
        self.edit.addAction(self.undo)

        self.redo = QtGui.QAction("&Redo", Frame)
        self.redo.triggered.connect(self.redo_func)
        self.edit.addAction(self.redo)
        
        self.find = QtGui.QAction("&Find", Frame)
        self.find.setShortcut("Ctrl+F")
        self.find.triggered.connect(self.find_func)
        self.edit.addAction(self.find)

        self.replace = QtGui.QAction("&Replace", Frame)
        self.replace.setShortcut("Ctrl+R")
        self.replace.triggered.connect(self.replace_func)
        self.edit.addAction(self.replace)

    def configure_mode (self, Frame):
        self.normal = QtGui.QAction("&Normal", Frame)
        #self.normal.triggered.connected(self.normal_func)
        self.mode.addAction(self.normal)

        self.gpp = QtGui.QAction("&C++", Frame)
        #self.gpp.triggered.connected(self.gpp_func)
        self.mode.addAction(self.gpp)

    def configure_help (self, Frame):
        self.faqs = QtGui.QAction("&FAQS", Frame)
        #self.faqs.triggered.connected(self.faqs_func)
        self.help.addAction(self.faqs)

        self.shortcuts = QtGui.QAction("&Shortcuts", Frame)
        #self.shortcuts.triggered.connected(self.shortcuts_func)
        self.help.addAction(self.shortcuts)

        self.info = QtGui.QAction("&Info", Frame)
        #self.info.triggered.connected(self.info_func)
        self.help.addAction(self.info)

        self.faqs = self.help.addAction('FAQS')
        #self.faqs = self.help.addAction('Shortcuts')
        self.help.addAction('General Info')

    def new_func(self):
        new_tab = QtGui.QWidget()
        self.text = QtGui.QTextEdit(new_tab)
        self.text.setMinimumHeight(500)
        self.text.setMinimumWidth(500)
        self.counter = self.counter +1
        self.tabWidget.addTab(new_tab, 'Tab' + str(self.counter))
        new_tab.raise_()

    def open_func(self):
        self.name = QtGui.QFileDialog.getOpenFileName(None, 'Open file')
        file = open(self.name, 'r')
        data = file.read()
        self.text.setText(data)
        file.close()
        self.clear_directories_structure(self.leftwidget)
        self.directoris_structure(os.getcwd(), self.leftwidget)
        
    def save_func(self):
        file = open(self.name, 'w')
        self.contingut = self.text.toPlainText()  # obtenim el text de la pantalla
        file.write(self.contingut)
        self.clear_directories_structure(self.leftwidget)
        self.directoris_structure(os.getcwd(), self.leftwidget)
        
    def save_as_func(self):
        self.name = QtGui.QFileDialog.getSaveFileName(None, 'Save file')
        file = open(self.name, 'w')
        self.contingut = self.text.toPlainText()    #obtenim el text de la pantalla
        file.write(self.contingut)
        self.clear_directories_structure(self.leftwidget)
        self.directoris_structure(os.getcwd(), self.leftwidget)
    
   # def configuration_func(self):

    def close_tab_func(self):
         ind = self.tabWidget.currentIndex()
         self.tabWidget.removeTab(ind)
         self.counter = self.counter -1

    def close_func(self):
         exit(0)

    def copy_func(self):
        self.text.copy()

    def paste_func(self):
        self.text.paste()
    
    def undo_func (self):
        self.text.undo()
        
    def redo_func(self):
        self.text.redo()
        
    def find_func(self):
        self.buscar = QtGui.QFrame()
        self.buscar.setGeometry(0,0, 500,150)
        self.buscar.setWindowTitle("Finder")
        self.buscar.autoFillBackground()
        self.paraula = QtGui.QTextEdit(self.buscar)
        self.paraula.setGeometry(280,42, 140, 32)
        self.instruccions = QtGui.QLabel("Escriu el que vols buscar:", self.buscar)
        self.instruccions.setGeometry(75, 40, 250, 40)
        self.buto = QtGui.QPushButton("Find", self.buscar)
        self.buto.setGeometry(150, 120, 75, 20)
        self.buto.clicked.connect(self.clicar_boto_find)
        self.buto_next =  QtGui.QPushButton("Next", self.buscar)
        self.buto_next.setGeometry(260, 120, 75, 20)
        self.buto_next.clicked.connect(self.seguent)
        self.buscar.show()
    
    def seguent(self):
        if self.text.find(self.word)==False:
            self.buscar.hide()
        
    def clicar_boto_find (self):
        self.word = QtCore.QString
        self.word = self.paraula.toPlainText()
        self.cursor = QtGui.QTextCursor()
        self.text.setTextCursor(self.cursor) #creem un cursor i l'assignem al editor
        self.cursor.beginEditBlock()

        self.text.find(self.word)

    def replace_func(self):
        self.rep = QtGui.QFrame()
        self.rep.setGeometry(0, 0, 500, 175)
        self.rep.setWindowTitle("Replacer")
        self.rep.autoFillBackground()
        self.paraula1 = QtGui.QTextEdit(self.rep)
        self.paraula1.setGeometry(280, 40, 140, 35)
        self.instruccions1 = QtGui.QLabel("Escriu el que vols canviar:", self.rep)
        self.instruccions1.setGeometry(75, 40, 250, 35)

        self.instruccions2 = QtGui.QLabel("Escriu pel que ho vols substituir:", self.rep)
        self.instruccions2.setGeometry(75, 90, 250, 35)
        self.paraula2 = QtGui.QTextEdit(self.rep)
        self.paraula2.setGeometry(280, 90, 140, 35)

        self.buto = QtGui.QPushButton("Replace", self.rep)
        self.buto.setGeometry(210, 145, 75, 20)
        self.buto.clicked.connect(self.clicar_boto_replace)
        self.rep.show()

    def clicar_boto_replace (self):
        text2 = self.text.toPlainText()
        newText = text2.replace(self.paraula1.toPlainText(),self.paraula2.toPlainText())
        self.text.clear()
        self.text.append(newText)
        self.rep.close()

    def directoris_structure (self, startpath, tree):
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = QtGui.QTreeWidgetItem(tree, [os.path.basename(element)])
        
            if os.path.isdir(path_info):
                self.directoris_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QtGui.QIcon('/home/alumne/Documents/Editor/folder.gif'))
            else:
                parent_itm.setIcon(0, QtGui.QIcon('/home/alumne/Documents/Editor/file.jpeg'))

    def clear_directories_structure(self, tree):
            tree.clear()

    #def normal_func(self):

    #def cpp_func(self):

    #def faqs_func(self):

    #def shortcuts_func(self):

    #def info_func(self):

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myApp = ()
    myApp.show()
    sys.exit(app.exec_())

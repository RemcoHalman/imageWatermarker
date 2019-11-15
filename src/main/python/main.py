from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys, os
from imageProces import FolderSelectAndRun

selectInFolder = False
selectOutFolder = False
watermarkSet = False
smallCheck = [selectInFolder, selectOutFolder, watermarkSet]

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui = appctxt.get_resource('gui.ui')
        uic.loadUi(ui, self)
        self.setWindowTitle(appctxt.build_settings['app_name'])
        self.statusBar().showMessage(f"{appctxt.build_settings['app_name']} | version: {appctxt.build_settings['version']} | Author: {appctxt.build_settings['author']}")
        width = self.width()
        height = self.height()
        self.setFixedSize(self.size())

        ## Defining items
        self.startButton = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.quitButton = self.findChild(QtWidgets.QPushButton, 'quitButton')
        self.resetButton = self.findChild(QtWidgets.QPushButton, 'resetButton')
        self.selectFolder = self.findChild(QtWidgets.QPushButton, 'selectFolder')
        self.selectOutputFolder = self.findChild(QtWidgets.QPushButton, 'selectOutputFolder')
        self.selectWatermark = self.findChild(QtWidgets.QPushButton, 'selectWatermark')
        self.watermarkPreview = self.findChild(QtWidgets.QLabel ,'watermarkPreview')
        self.watermarkPreview.setStyleSheet("border: 1px inset grey;")
        self.watermarkPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.selectFolderLabel = self.findChild(QtWidgets.QLabel ,'selectFolderLabel')
        self.selectOutputFolderLabel = self.findChild(QtWidgets.QLabel ,'selectOutputFolderLabel')
        self.watermarkPath = self.findChild(QtWidgets.QLabel, 'watermarkPath')

        ## Button Functions
        self.selectWatermark.clicked.connect(self.openWatermarkDialog)
        self.selectFolder.clicked.connect(self.inputFolder)
        self.selectOutputFolder.clicked.connect(self.outputFolder)
        self.startButton.clicked.connect(self.startImages)
        self.resetButton.clicked.connect(self.reset)
        self.quitButton.clicked.connect(self.quit)
    
        ## Set defined text
        self.selectFolderLabel.setText("Selecteer uw map")
        self.selectOutputFolderLabel.setText("Selecteer uw bestemmings map")

        self.show()


    def reset(self):
        self.selectFolderLabel.setText("Selecteer uw map")
        self.selectOutputFolderLabel.setText("Selecteer uw bestemmings map")
        self.watermarkPreview.clear()
        self.watermarkPath.clear()
        self.selectFolderLabel.setStyleSheet('color: black')
        self.selectOutputFolderLabel.setStyleSheet('color: black')

    def quit(self):
        app.quit()

    def startImages(self):
        # print("____________________________________________________________________")
        # print("Path inputmap: " + self.selectFolderLabel.text())
        # print("Path outputmap: " + self.selectOutputFolderLabel.text())
        # print("Path watermark: " + self.watermarkPreview.text())
        # print("____________________________________________________________________")
 
        if self.selectFolderLabel.text() == "Selecteer uw map":
            self.selectFolderLabel.setStyleSheet('color: red')
       
        if self.selectOutputFolderLabel.text() == "Selecteer uw bestemmings map":
           self.selectOutputFolderLabel.setStyleSheet('color: red')

        FolderSelectAndRun.batch(
            self.selectFolderLabel.text(), 
            self.selectOutputFolderLabel.text(),
            self.watermarkPath.text()
            )
        self.reset()

    def inputFolder(self):
        dialog = QtWidgets.QFileDialog(self, 'Image Files', os.getcwd())
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.selectFolderLabel.setText(dialog.selectedFiles()[0])
    
    def outputFolder(self):
        dialog = QtWidgets.QFileDialog(self, 'Destination Files', os.getcwd())
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.selectOutputFolderLabel.setText(dialog.selectedFiles()[0])

    def openWatermarkDialog(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QtWidgets.QFileDialog.getOpenFileName()", "","Images (*.png *.jpg)", options=options)
        print(fileName)
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            watermark = pixmap
            smaller_pixmap = pixmap.scaled(161, 81, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.watermarkPreview.setPixmap(smaller_pixmap)
            self.watermarkPath.setText(fileName)
           

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
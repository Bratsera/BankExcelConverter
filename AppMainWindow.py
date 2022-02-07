import sys
from pandas import ExcelWriter
from qtpy import QtWidgets
from TableConverter import TableConverter
from ui.mainwindow import Ui_MainWindow
from PdTableConverter import TableModel
from FileBrowser import FileBrowser


# Contains the UI-Elements of the application and the main functions,
# that are called by them
class MainWindow(QtWidgets.QMainWindow):
    convertedFile = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.chooseFileBtn.clicked.connect(self.loadTable)
        # Export the converted table as Excel-file in the hard-drive
        self.ui.exportFileBtn.clicked.connect(self.exportTable)
        self.setWindowTitle('MacGiro/DTE Excel Konverter')
        self.fb = FileBrowser()

    # Loads an Excel-file, converts it and displays the result-table in the application
    def loadTable(self):

        # TODO add check if the file is of type .xlsx
        # TODO add check if file was succesfully opened and add errorhandling for cases if file is used by another programm or has password
        # TODO implement saveFile-Method
        # TODO add Tabview in UI to display all Tables
        # open Excel-table
        file = FileBrowser.chooseFile()
        print(file.__str__())

        if file[0] != '':
            # convert table
            tableConverter = TableConverter(file[0])
            tableConverter.convertFile()
            self.convertedFile = tableConverter.table

            # Variant, using a QTableWidget as UI-Element
            # model = TableWidget(tableConverter.table)
            # view = self.ui.gridLayout
            # try:
            #     view.addWidget(model)
            # except Exception as e:
            #     print(e)

            # Variant, using a QTableView as UI-Element
            # load table into application
            model = TableModel(self.convertedFile)
            tableUI = self.ui.succesTable
            tableUI.setModel(model)

    def exportTable(self):
        FileBrowser.exportFile(self.convertedFile)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

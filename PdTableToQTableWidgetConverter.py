import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
    QPushButton, QItemDelegate, QVBoxLayout
from PyQt6.QtGui import QDoubleValidator


class FloatDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor


# Converts pandas-dataframe file into a QTableWidget,
# so it can be added to the Qt-application
class TableWidget(QTableWidget):
    def __init__(self, df: pd.DataFrame, table: QTableWidget):
        super().__init__()
        self.df = df
        self.table = table
        self.loadTable()

    def updateDF(self, row, column):
        text = self.table.item(row, column).text()
        self.df.iloc[row, column] = text

    def loadTable(self):
        self.clearTable()
        self.table.setStyleSheet('font-size: 16px;')
        # set table dimension
        nRows, nColumns = self.df.shape
        self.table.setColumnCount(nColumns)
        self.table.setRowCount(nRows)

        self.table.setHorizontalHeaderLabels(self.df.head(0))

        self.table.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        self.table.cellChanged[int, int].connect(self.updateDF)

    def clearTable(self):
        for i in range( self.table.rowCount()):
            self.table.removeRow(0)
        for i in range( self.table.columnCount()):
            self.table.removeColumn(0)
        self.table.setRowCount(0)






























#Demo-class
class DFEditor(QWidget):
    data = {
        'Col X': list('ABCD'),
        'col Y': [10, 20, 30, 40]
    }

    df = pd.DataFrame(data)

    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        mainLayout = QVBoxLayout()

        self.table = TableWidget(DFEditor.df)
        mainLayout.addWidget(self.table)

        button_print = QPushButton('Display DF')
        button_print.setStyleSheet('font-size: 30px')
        button_print.clicked.connect(self.print_DF_Values)
        mainLayout.addWidget(button_print)

        button_export = QPushButton('Export to CSV file')
        button_export.setStyleSheet('font-size: 30px')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)

        self.setLayout(mainLayout)

    def print_DF_Values(self):
        print(self.table.df)

    def export_to_csv(self):
        self.table.df.to_csv('Data export.csv', index=False)
        print('CSV file exported.')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DFEditor()
    demo.show()

    sys.exit(app.exec())
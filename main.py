import sys
from qtpy import QtWidgets
from AppMainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())

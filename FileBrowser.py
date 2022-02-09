import os
from datetime import datetime

from pandas import ExcelWriter
from qtpy import QtWidgets
from PyQt6.QtCore import QDir
from PyQt6.QtWidgets import QFileDialog


class FileBrowser:

    @staticmethod
    def chooseFile():
        fileBrowser = QFileDialog()
        fileBrowser.setFileMode(QFileDialog.ExistingFile)
        try:
            selectedFile = fileBrowser.getOpenFileName(fileBrowser, "Choose file", os.path.dirname(__file__), "Excel-file (*.xlsx *.xls)")

            return selectedFile
        except Exception as e:
            print(e)


    def saveFile(self, type):
        #Todo Abbruch des Exports abfangen
        fileBrowser = QFileDialog()

        match type:
            case 'success':
                filename = "Bankdatenkonvertierung_erfolgreich"
            case 'check':
                filename = "Bankdatenkonvertierung_zu_prüfen"
            case 'ignore':
                filename = "Bankdatenkonvertierung_fehlgeschlagen"

        rootPath = os.path.join(os.path.dirname(__file__), "Export", datetime.now().strftime(
            "%d-%m-%Y_%H.%M") + filename)
        a = fileBrowser.getSaveFileName(fileBrowser, 'Save file as', rootPath, "Excel-file (*.xlsx *.xls)")
        print(a)
        if a[0] == '':
            return None
        else:
            # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
            # On Windows, toNativeSeparators("c:/winnt/system32") returns
            # "c:\winnt\system32".

            a = QDir.toNativeSeparators(a[0])
            return a

    @staticmethod
    def exportFile(file, type):
        # Error-alert-box
        error = QtWidgets.QMessageBox()

        if file is None:
            error.information(file, "Keine Tabelle eingelesen",
                              "Es wurde noch keine Tabelle eingelesen. Um eine Tabelle einzulesen, "
                              "klicken Sie auf den Button 'Choose file' und wählen Sie eine Excel Datei aus.",
                              error.Ok)
        else:
            fileToSave = FileBrowser.saveFile(FileBrowser, type)
            if fileToSave is not None:
                try:
                    with ExcelWriter(fileToSave, date_format='dd.mm.yyyy', datetime_format='dd.mm.yyyy hh:mm:ss') as writer:
                        file.to_excel(writer)
                except PermissionError:
                    error.critical(error, "Fehler beim Speichern der Datei",
                                   "Die Datei kann nicht überschrieben werden. "
                                   "Sie ist möglicherweise schreibgeschützt oder aktuell geöffnet "
                                   "oder Sie verfügen nicht über die erforderliche Berechtigung.", error.Ok)
                    FileBrowser.exportFile(file)


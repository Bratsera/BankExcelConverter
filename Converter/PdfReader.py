import pandas
import tabula
from TableData import Stats, ConvertedTables
import pandas as pd
import re
import GlobalConstants

pd.options.mode.chained_assignment = None  # default='warn'


def convertFile(pdfFile):
    try:
        # Convert Desktop-Enterprise pdf-Export into an array of pandas Dataframe
        file = tabula.read_pdf(pdfFile, pages='all', pandas_options={'header': None,
                                                                     'dtype': str,
                                                                     })
        # Reformat each Dataframe in the array, drop empty columns (converting issues) and reset column headers to
        # the new amount of columns
        for index, page in enumerate(file):
            page.dropna(axis=1, inplace=True)
            page.columns = range(page.columns.size)

        # Concat all Dataframes in the array to one Dataframe and set the column headers
        table = pandas.concat(file, ignore_index=True)
        table.columns = ["Name",
                         "Vorgang",
                         "Lieferschein-Nr",
                         "Datum",
                         "Kundennummer",
                         "Betrag",
                         "Rechnungs-Nr"
                         ]
    except Exception as e:
        print(e)

    # Convert the Dataframe to the desired format
    mergedResult = __filterByInvoiceId(table[["Name",
                                  "Vorgang",
                                  "Lieferschein-Nr",
                                  "Kundennummer",
                                  "Betrag",
                                  "Rechnungs-Nr"]],
                           "Rechnungs-Nr")

    # Save Table and rowCount in TableData
    ConvertedTables.dtePdfTable = mergedResult
    Stats.dteTotalCount = len(mergedResult.index)


# Returns a table which contains only rows with an invoice-Id in a specified column
def __filterByInvoiceId(table, invoiceColumnString):

    newTable = []
    # The column to check for an invoice-Id
    invoiceColumn = table[invoiceColumnString]

    try:
        for index, line in enumerate(invoiceColumn):
            # A check if line is not a number NaN
            if line != line:
                continue

            if line is not None:

                try:
                    result = re.search(GlobalConstants.REGEX_INVOICE_ID, line)
                    # If there´s a match with an invoice-Id, add row to the table
                    if result is not None:
                        invoiceColumn.at[index] = result.group()
                        newTable.append(table.loc[index])
                except Exception as e:
                    print(e + str(table.loc[index]))

        # Convert array to Dataframe
        newTable = pandas.DataFrame(newTable)

        return newTable

    except Exception as e:
        invoiceColumn.at[index]
        print(e)

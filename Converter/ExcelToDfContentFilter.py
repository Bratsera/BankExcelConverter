import pandas as pd
import re
import GlobalConstants
from TableData import Stats,ConvertedTables

pd.options.mode.chained_assignment = None  # default='warn'

# Reads the Bank-transaction-excel-export and converts it to a pandas Dataframe.
# Checks the transaction reference column for any invoice references, and  stores the result in 3 different tables:
# one for matching invoice ref, one for no match and one where more than one invoice ref was found or an customer-Id or
# delivery-Id was found
def convertFile(excelFile):
    table = pd.read_excel(excelFile)

    Stats.totalCount = len(table.index)
    # Array containing exact one invoice-Id
    successTable = []
    # Array containing more than one invoice-Id, no invoice-Id BUT at least a customer-Id or Delivery-Id
    toCheckTable = []
    # Array containing no Id or no content
    ignoreTable = []
    # ----------------------------------------- Matching for id´s ------------------------------------------------------
    # The column of the table with the bank transfer reference where to search or any invoice, delivery- or customer-Id
    transferDesc = table['Verwendungszweck']

    try:
        # check each item in the column
        for index, line in enumerate(transferDesc):
            # A check if line is not a number NaN
            if line != line:
                ignoreTable.append(table.loc[index])
                continue

            # Check item for any invoice-Id
            result = re.findall(GlobalConstants.REGEX_INVOICE_ID, line)

            match result:
                # Match for one Invoice-id in reference-column
                case result if len(result) == 1:

                    transferDesc.at[index] = result[0]
                    successTable.append(table.loc[index])

                # Match for more than one Invoice-id´s in reference-column
                case result if len(result) > 1:
                    # Check item also for a customer-Id
                    customer = re.search(GlobalConstants.REGEX_CUSTOMER_ID, line)
                    matches = ', '.join(result)
                    newDesc = 'Re-Nr: ' + matches
                    transferDesc.at[index] = newDesc + '; Kd-Nr: ' + customer.group()[0:5] if customer else newDesc
                    toCheckTable.append(table.loc[index])

                # If no Invoice-id in reference-column, match for one delivery-id in reference-column
                case result if len(result) == 0:
                    try:

                        deliveryId = re.findall(GlobalConstants.REGEX_DELIVERY_ID, line)
                        customer = re.search(GlobalConstants.REGEX_CUSTOMER_ID, line)

                        match deliveryId:
                            # No match on delivery- or customer-Id
                            case deliveryId if len(deliveryId) == 0 and customer is None:
                                ignoreTable.append(table.loc[index])
                            # Match on customer-id
                            case deliveryId if len(deliveryId) == 0 and customer:
                                transferDesc.at[index] = customer.group()[0:5]
                                toCheckTable.append(table.loc[index])
                            # Match on delivery-Id
                            case _:

                                matches = ', '.join(deliveryId)
                                transferDesc.at[index] = matches
                                toCheckTable.append(table.loc[index])

                    except Exception as e:
                        print(transferDesc.at[index])
                        print(e)

    except Exception as e:
        print(e)
    # ----------------------------------------- Matching for id´s END---------------------------------------------------

    # Convert arrays to dataframes
    successTable = pd.DataFrame(successTable)
    toCheckTable = pd.DataFrame(toCheckTable)
    ignoreTable = pd.DataFrame(ignoreTable)

    # Store tables and Table length in TableData
    Stats.successCount = len(successTable.index)
    Stats.checkCount = len(toCheckTable.index)
    Stats.ignoreCount = len(ignoreTable.index)

    ConvertedTables.successTable = successTable
    ConvertedTables.toCheckTable = toCheckTable
    ConvertedTables.ignoreTable = ignoreTable

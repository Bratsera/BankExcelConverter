# BankExcelConverter
This tool was built for using with the ERP-Software "Desktop-Enterprise" (DTE). It converts Bank-data Excel-exports, so that the payments can be matched by DTE with its open item accounting automatically.
Therefor it matches every transfer reference wheater it contains one invoice number. It there is a match, the transfer reference gets overwritten so it only contains this number
as DTE doesn't recognize any transfer with additional information in the reference (at least if you don´t pay for an additional Converter-Tool ;-))
The UI was made with the QT-Community-Edition 

# What it does
1. This tool has an UI, where you can select the Excel-file you want to convert.
2. After selecting the file the program looks for the column "Verwendungszweck" in the file (in further updates you´ll be able to choose the column) and checks it with the following rules:
  a. if there is ONE match, a serial of 6 digits starting with 10#### (invoice nr), (the regex expressions can be changed in the code,see "How to run". In further updates you will be able to change the regesx in the UI)
     overwrite the cell with the serial 
  b. if there are more than one matches, overwrite the cell and concat the serials and look for another Serial of 5 digits starting with 1#### (customer-nr) and also concat
     DTE won´t be able to match these, but it will be easier to read, and match manually afterwards
  c. If there no match with the invoice nr serial, check if the cell contains a serial of 6 digits starting with 50#### (delivery nr) and concat them all + the customer-nr as in b
  d. If no matches were found, don´t make any changes in the cell
 3. The modified table will be displayed in the UI.
 4. With the export-button you can export the table as a new Excel-file in the desired destination
 

# How to run

You have to execute the main.py with your python program.
In the program you can click on "Choose file" and select a export file (you can find a demo file in the directory "TestExample"
You can change the regex-expression in the TableConverter.py:
    __REGEX_CUSTOMER_ID 
    __REGEX_INVOICE_ID 
    __REGEX_DELIVERY_ID
In the current version the export-Table must have the header-name "Verwendungszweck" in the reference-column 

This is the Alpha-Version of this tool and was made for a specific client, so the functionalities were tailored to the client needs and will need adjustments to fit to your needs.  

If you have any questions or feedback, feel free to write me

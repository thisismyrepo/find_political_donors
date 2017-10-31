# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import statistics
import re
import pandas as pd
import numpy as np

HowManyTransactions=0                # Counts the number of transactions

input_file = "/input/itcont.txt"
fileHandle = open('input_file', 'r')       # Opening input file "itcont.txt"

#fileHandle = """
#C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783
#C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312017|384||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337
#C00384818|N|M2|P|201702039042412112|15|IND|ABBOTT, JOSEPH|WOONSOCKET|RI|028956146|CVS HEALTH|VP, RETAIL PHARMACY OPS|01122017|250||2017020211435-887|1147467|||4020820171370030285
#C00177436|N|M2|P|201702039042410893|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|307502818|UNUM|SVP, CORPORATE COMMUNICATIONS|01312017|230||PR1890575345050|1147350||P/R DEDUCTION ($115.00 BI-WEEKLY)|4020820171370029335
#C00177436|N|M2|P|201702039042410895|15|IND|JEROME, CHRISTOPHER|FALMOUTH|ME|041051896|UNUM|EVP, GLOBAL SERVICES|01312017|384||PR2283905245050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029342
#C00384818|N|M2|P|201702039042412112|15|IND|BAKER, SCOTT|WOONSOCKET|RI|028956146|CVS HEALTH|EVP, HEAD OF RETAIL OPERATIONS|01122017|333||2017020211435-910|1147467|||4020820171370030287
#C00177436|N|M2|P|201702039042410894|15|IND|FOLEY, JOSEPH|FALMOUTH|ME|041051935|UNUM|SVP, CORP MKTG & PUBLIC RELAT.|01312017|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339
#"""
#for line in fileHandle:
#    fields = line.split('|')

input_data = re.sub(r'(C0)', r'|\1', fileHandle)   
fields = input_data.split('|')                       # Splits data into separate indices
del fields[0]
counter = 0
#while fields/21 :
#    # CMTE_ID = fields[1]                # Recipient of the contribution (indices: 1, 22, 43, ... )
#    CMTE_ID = fields[counter + 1]                                      # increment counter by 21 for each loop iteration
#    # ZIP_CODE = fields[11]               # Zip code of contributor (we only want the first 5 digits)
#    ZIP_CODE = fields[counter + 11]                                        # (indices: 11, 32, 53, ...  )
#    # TRANSACTION_DT = fields[14] 
#    TRANSACTION_DT = fields[counter + 14]         # Transaction date (indices: 14, 35, 56, ... )
#    TRANSACTION_AMT = fields[counter + 15]        # Transaction amount (indices: 15, 36, 57, ... )
#    OTHER_ID = fields[counter + 16]               # whether contribution came from a person or an entity
#    counter = counter + 21                                       # (indices: 16, 37, 58, ... )




NumberOfRows = round(len(fields)/21)
NumberOfCols = 5


df = pd.DataFrame(fields)
data = pd.DataFrame(df.values.reshape(-1,21), index = range(NumberOfRows), columns = ['CMTE_ID', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'ZIP_CODE', 12, 13, 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 17, 18, 19, 20, 21])


for i in range(NumberOfRows):
     
        # check if OTHER_ID is empty. If not, skip the record
    
    #if data.iloc[i]['OTHER_ID'] :
    #    i=i+1
    
    # Calculations for medianvals_by_zip.txt
    
    
    MedianOfContributions = data.iloc[range(i+1)]['TRANSACTION_AMT'].median(axis=0)
    #MedianOfContributions = data.groupby('CMTE_ID')['TRANSACTION_AMT'].median()
    ##MedianOfContributions = round(statistics.median(ContributionsList),0)
    #    # Rounded to nearest whole dollar
    value = data.iloc[range(i+1)]
    HowManyTransactions = HowManyTransactions + 1
    #HowManyTransactions = data.groupby("CMTE_ID")['TRANSACTION_AMT'].count
    ##TotalAmount = data[['TRANSACTION_AMT']].iloc[range(i)].sum(axis=0)
    TotalAmount = data.iloc[range(i+1)]['TRANSACTION_AMT'].sum(axis=0)   # sum the column
    #TotalAmount = data.groupby('CMTE_ID')['TRANSACTION_AMT'].sum(axis=0)
    

    
    # write to output file "medianvals_by_zip.txt"
    # output_line=[CMTE_ID, ZIP_CODE, MedianOfContributions, HowManyTransactions, TotalAmount]
    
    #output_line=[data['CMTE_ID'].iloc[i], '|', data['ZIP_CODE'].iloc[i], '|', MedianOfContributions,'|', HowManyTransactions,'|', TotalAmount]  
    #output_line = [data.iloc[i]['CMTE_ID'], |, data.iloc[i]['ZIP_CODE'], |, MedianOfContributions,|, HowManyTransactions,|, TotalAmount]             
    
    CMTE_ID = data.iloc[i]['CMTE_ID']
    ZIP_CODE = data.iloc[i]['ZIP_CODE']
    
    print(CMTE_ID, '|', ZIP_CODE, '|', MedianOfContributions, '|', HowManyTransactions, '|', TotalAmount)
    
    outputfile = open('/output/medianvals_by_zip.txt','w') 
 
    outputfile.write(CMTE_ID, '|', ZIP_CODE, '|', MedianOfContributions, '|', HowManyTransactions, '|', TotalAmount)
    
    TotalAmount=0
    
TotalAmountByDate = data.groupby(['TRANSACTION_DT', 'CMTE_ID'])['TRANSACTION_AMT'].sum(axis=0)

print(TotalAmountByDate)

outputfile2 = open('/output/medianvals_by_date.txt','w') 
 
outputfile2.write(TotalAmountByDate) 

#StatsByDate= data.groupby(['TRANSACTION_DT', 'CMTE_ID', as_index=False]).agg('TRANSACTION_AMT': [count(axis=0), sum(axis=0), median(axis=0)])
#print(StatsByDate)


# donations.groupby("CMTE_ID").sum().sort("contb_receipt_amt")

#if [!CMTE_ID | !TRANSACTION_AMT] # if these are empty, skip the record    
    # go back to line 15






# Calculations for medianvals_by_date.txt
# Output: TRANSACTION_DT|CMTE_ID|HowManyTransactions|TotalAmount|MedianOfContributions



# fileHandle.close()

   # print(fields[0]) # prints the first fields value
   # print(fields[1]) # prints the second fields value


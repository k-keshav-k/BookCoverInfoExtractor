import xlrd
from xlutils.copy import copy

# class to add rows to an excel sheet
class Excel_Utils:

    # function to add rows to an excel sheet
    def saveWorkSpace(fields):
        
        # open the workbook
        rb = xlrd.open_workbook('tester1.xls',formatting_info=True)

        # get the sheet
        r_sheet = rb.sheet_by_index(0) 

        # get the rows
        r = r_sheet.nrows

        # restore previous values
        wb = copy(rb) 

        # write the new row
        sheet = wb.get_sheet(0) 
        sheet.write(r,0,fields['name'])
        sheet.write(r,1,fields['title'])
        sheet.write(r,2,fields['author'])
        sheet.write(r,3,fields['ISBN'])
        sheet.write(r,4,fields['Publisher'])

        # save the chnages
        wb.save('tester1.xls')

        # show the status
        print ('Wrote tester1.xls')
import csv
import string
import xlrd
import glob
from bs4 import BeautifulSoup

# function that checks to see if the file passed in is of type .xls/.xlsx
def is_xls_xlsx(file):
    good_file = ["xls", "xlsx"]
    head, sep, tail = file.partition('.')
     # if the file extension is something other than xls/xlsx, return false
    if tail not in good_file:
        return False
    # otherwise, return true! file is xls/xlsx
    return True

# function that checks to see if the file passed in is of type .html
def is_html(file):
    head, sep, tail = file.partition('.')
     # if the file extension is something other than html, return false
    if tail != "html":
        return False
    # otherwise, return true! file is html
    return True

# get an array of all xls and xlsx files
def get_xls_xlsx_files(filepath):
    # Get an array of .xls and .xlsx files
    xls_xlsx_files = []
    # loop through files ending in .xls
    for xls_file in glob.glob("*.xls"):
        # add file name to array
        xls_xlsx_files.append(xls_file)
    # loop through files ending in .xls in quotes dir
    for xls_file in glob.glob(filepath + "/*.xls"):
        # add file name to array
        xls_xlsx_files.append(xls_file)
    # loop through files ending in .xlsx
    for xlsx_file in glob.glob("*.xlsx"):
        # add file name to array
        xls_xlsx_files.append(xlsx_file)
    # loop through files ending in .xlsx in quotes dir
    for xlsx_file in glob.glob(filepath + "/*.xlsx"):
        # add file name to array
        xls_xlsx_files.append(xlsx_file)
    return xls_xlsx_files

# accepts xls and xlsx files and their paths and converts to csv file
def convert_xls_xlsx_to_csv(filename, filepath):
    # list of good sheet names to return
    good_sheets = []
    # list of sheets that we don't want to convert
    bad_sheets = ['T&C', 'XDO_METADATA'];
    # open file
    wb = xlrd.open_workbook(filepath)
    # get all possible sheet names (could be more than 1)
    sheets = wb.sheet_names()

    # for sheet in sheets: ************ ONLY WITH MULTIPLE SHEETS - DOESN'T WORK ON FRONTEND SO DON'T CONVERT ALL SHEETS
    # check if the sheet is a bad sheet
    # if sheets[0] in bad_sheets: *********** ONLY WITH MULTIPLE SHEETS
    #     # skip the sheet if it is
    #     break
    # get specific sheet as a Sheet object (needed for sh.nrows below)
    sh = wb.sheet_by_name(sheets[0])
    # head is raw file name without its file extension
    head, sep, tail = filename.partition('.')
    # append csv file extension to string
    # head += sheet + ".csv" ******** ONLY WITH MULTIPLE SHEETS
    head += ".csv"
    # create csv file with same name
    csv_file = open(head, 'w', newline='')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    # write to csv file
    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()
    # add this sheet file path to good sheet list
    good_sheets.append(csv_file.name)

    # return the array of sheets as csv file (with path) ******ONLY SEND FIRST SHEET SO IT WORKS ON FRONT END
    # return good_sheets[0]

# accepts html file and it's filepath and converts to csv
def convert_html_to_csv(filename, filepath):
    html = open(filepath).read()
    # use html.parser argument instead of lxml
    soup = BeautifulSoup(html, 'html.parser')
    # get all tables in html doc
    tables = soup.findAll("table")
    output_rows = []
    # loop thorugh all the tables and save the text in the tables to an output array to wrtie to csv
    for table in tables:
        for table_row in table.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_rows.append(output_row)
        # give the new csv file the same name (just change extension)
        head, sep, tail = filename.partition('.')
        head += ".csv"
    # write output array to new csv file
    csv_file = open(head, 'w', newline='')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    wr.writerows(output_rows)
    csv_file.close()

# Utilizes a CSV dictionary to gather fieldnames and reformats the headers on input file to case-desensitize.
def reformat_header(filename):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # print(csv_reader.fieldnames)
        count = 0

        # iterates through all fieldnames and makes case insensitive, removes punctuation and spaces except hashtags(#)
        for fieldname in csv_reader.fieldnames:
            fieldname = fieldname.lower()
            fieldname = fieldname.translate(str.maketrans('','',".,"))
            fieldname = fieldname.replace(" ","")
            csv_reader.fieldnames[count] = fieldname
            # print(csv_reader.fieldnames[count])
            count += 1
        print(csv_reader.fieldnames)

#

def csv_avt(filename,filepath,vendorname,manufacturername):
    # check to see if the file type is .xls, .xlsx
    if is_xls_xlsx(filename) == True:
        # if the file is .xls, .xlsx
        convert_xls_xlsx_to_csv(filename, filepath)
        head, sep, tail = filename.partition('.')
        filepath = head + ".csv"
        filename = filepath
    # check to see if the file type is .html
    if is_html(filename) == True:
        # if the file is .html
        convert_html_to_csv(filename, filepath)
        head, sep, tail = filename.partition('.')
        filepath = head + ".csv"
        filename = filepath

    # loop through csv sheet file array (only loops if there's multiple sheets) *****NOT WOKRING ON FRONT END SO LEAVE COMMENTED
    # for file in new_filepath:
    # update new filepath (from .xls, .xlsx to .csv)
    # filepath = new_filepath
    # head, sep, tail = new_filepath.partition('/')
    # filter out the directory name and just get file name
    # filename = tail

    # counter for total parts in the quote
    items = 0
    #variable for vendor quote number found in lines outside of table
    vendor_quote_found = None

    # opens input file
    with open(filepath, encoding='utf-8-sig', errors="ignore") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        #get fieldnames
        try:
            csv_reader.fieldnames
        except UnicodeDecodeError:
            print("Invalid header")
            return "Invalid header"

        #delete unnecessary rows (check if second fieldname is blank)
        while True:
            count = 0
            col_names = csv_reader.fieldnames
            if col_names[0] != "":
                temp_fieldnames = col_names
                # case-desensitizes and removes punctuation
                for fieldname in csv_reader.fieldnames:
                    fieldname = fieldname.lower()
                    fieldname = fieldname.translate(str.maketrans('','',".,"))
                    fieldname = fieldname.replace("\n","")
                    fieldname = fieldname.replace(" ","")
                    csv_reader.fieldnames[count] = fieldname
                    count += 1
                #check if valid header found
                if part_finder(csv_reader) is not None:
                    break
                #handle if vendor quote number found outside of table
                else:
                    for field in col_names:
                        if str_vendorquote_finder(field) != None:
                            vendor_quote_found = str_vendorquote_finder(field).upper()

            csv_reader = csv.DictReader(csv_file)

        # calls helper functions to find header variations and saves as variable to pass into as dictionary keys
        part_name = part_finder(csv_reader)
        description_name = description_finder(csv_reader)
        listprice_name = listprice_finder(csv_reader)
        wwtcost_name = wwtprice_finder(csv_reader)
        quantity_name = quantity_finder(csv_reader)
        manufacturer_name = manufacturer_finder(csv_reader)
        vendorquote_name = vendorquote_finder(csv_reader)
        add_description_name = add_description_finder(csv_reader)


        # writes into a new file
        with open('wwt_'  + filename,mode='w',newline='') as wwt_file:
            # headers for wwt quote template
            headers = ['Part #', 'Description', 'List Price', 'WWT Cost','Customer Price','Qty','Manufacturer','Vendor','Additional Description', 'Cust Product #', 'Lab Flag (Y/N)', 'Contract Start Date (MM/DD/YYYY)','Contract End Date (MM/DD/YYYY)', 'Serial #', 'Vendor Quote #','Duration','Lead Time', 'Cost Type']
            # invalid part numbers | stops iterating the loop
            part_blacklist = ['Products / Services Total', 'Sub-Total', 'Total']
            # list of text that needs to be filtered out but doesn't stop iterating the loop
            blacklist_continue_list = ['Hardware:', 'Services:', 'Software:']
            #creates CSV dictionary writer
            csv_writer=csv.DictWriter(wwt_file, fieldnames=headers)
            csv_writer.writeheader()

            # iterates through rows of csv_reader dictionary object
            for i, row in enumerate(csv_reader):
                # items is a counter for parts with a description field (doesn't work for every quote)
                #if row[description_name]:
                #   items += 1
                # if the iterator is greater than or equal to the items counter, stop iterating
                # if i >= (items):
                    # break

                # terminates when rows are not populated by part #, description and quantity
                if row[part_name] == '' and row[description_name] == '' and row[quantity_name] == '':
                    print("row doesn't have part #, description, or quantity")
                    break

                # terminates with incorrect part #
                if row[part_name] in part_blacklist:
                    print("found blacklisted item, stopping loop")
                    break

                # skips line with certain strings
                if row[part_name] in blacklist_continue_list:
                    print("filtered out blacklisted item")
                    continue

                #initializes empty dictionary to add keys-value pairs into
                output_dictionary = {}
                # Updates individual columns for each row into dictionary. If the column does not exist on original input file, leaves blank entry.
                # updates Part #
                if part_name is not None:
                    output_dictionary.update({'Part #':row[part_name]})
                else:
                    output_dictionary.update({'Part #':None})
                #updates Description
                if description_name is not None:
                    output_dictionary.update({'Description':row[description_name]})
                else:
                    output_dictionary.update({'Description':None})
                # updates List Price
                if listprice_name is not None:
                    output_dictionary.update({'List Price':row[listprice_name]})
                else:
                    output_dictionary.update({'List Price':None})
                # updates WWT Cost
                if wwtcost_name is not None:
                    output_dictionary.update({'WWT Cost':row[wwtcost_name]})
                else:
                    output_dictionary.update({'WWT Cost':None})
                # updates Qty
                if quantity_name is not None:
                    output_dictionary.update({'Qty':row[quantity_name]})
                else:
                    output_dictionary.update({'Description':None})
                # updates Manufacturer
                if manufacturer_name is not None:
                    output_dictionary.update({'Manufacturer':row[manufacturer_name]})
                else:
                    output_dictionary.update({'Manufacturer':manufacturername})
                # updates Vendor Quote #
                if vendor_quote_found != None:
                    output_dictionary.update({'Vendor Quote #':vendor_quote_found})
                elif vendorquote_name is not None:
                    output_dictionary.update({'Vendor Quote #':row[vendorquote_name]})
                else:
                    output_dictionary.update({'Vendor Quote #':None})

                #updates additional description and vendor fields
                if add_description_name is not None:
                    output_dictionary.update({'Additional Description':row[add_description_name], 'Vendor':vendorname})
                else:
                    output_dictionary.update({'Additional Description':None, 'Vendor':vendorname})

                csv_writer.writerow(output_dictionary)


# Looks for variations of 'Part #' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.

def part_finder(csv_dict):
    if 'partnumber' in csv_dict.fieldnames:
        part_name = 'partnumber'
    elif 'itemnumber' in csv_dict.fieldnames:
        part_name = 'itemnumber'
    elif 'item' in csv_dict.fieldnames:
        part_name =  'item'
    elif 'mfrpart#' in csv_dict.fieldnames:
        part_name = 'mfrpart#'
    elif 'part#' in csv_dict.fieldnames:
        part_name = 'part#'
    elif 'itemno' in csv_dict.fieldnames:
        part_name = 'itemno'
    elif 'partno' in csv_dict.fieldnames:
        part_name = 'partno'
    else:
        print('Part # fieldname not found.')
        return None
    return part_name

# Looks for variations of 'Description' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def description_finder(csv_dict):
    if 'product' in csv_dict.fieldnames:
        return 'product'
    elif 'description' in csv_dict.fieldnames:
        return 'description'
    elif 'productdescription' in csv_dict.fieldnames:
        return 'productdescription'
    elif 'descriptionandproductinfo' in csv_dict.fieldnames:
        return 'descriptionandproductinfo'
    else:
        print('Description fieldname not found.')
        return None

# Looks for variations of 'List Price' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def listprice_finder(csv_dict):
    if 'listprice' in csv_dict.fieldnames:
        return 'listprice'
    elif 'totallistpriceusd' in csv_dict.fieldnames:
        return 'total list price (usd)'
    elif 'unitlistprice' in csv_dict.fieldnames:
        return 'unitlistprice'
    elif 'msrp' in csv_dict.fieldnames:
        return 'msrp'
    else:
        print('Price fieldname not found.')
        return None

# Looks for variations of 'WWT Price' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def wwtprice_finder(csv_dict):
    if 'resellernetprice' in csv_dict.fieldnames:
        return 'resellernetprice'
    elif 'resellerprice' in csv_dict.fieldnames:
        return 'resellerprice'
    elif 'quoteprice' in csv_dict.fieldnames:
        return 'quoteprice'
    elif 'unitprice' in csv_dict.fieldnames:
        return 'unitprice'
    elif 'unitnetprice' in csv_dict.fieldnames:
        return 'unitnetprice'
    elif 'price' in csv_dict.fieldnames:
        return 'price'
    else:
        print('WWT Cost fieldname not found.')
        return None

# Looks for variations of 'Qty' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def quantity_finder(csv_dict):
    if 'qty' in csv_dict.fieldnames:
        return 'qty'
    elif 'quantity' in csv_dict.fieldnames:
        return 'quantity'
    elif 'qtyquoted' in csv_dict.fieldnames:
        return 'qtyquoted'
    elif 'extqty' in csv_dict.fieldnames:
        return 'extqty'
    else:
        print('Quantity fieldname not found.')
        return None

# Looks for variations of 'Manufacturer' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def manufacturer_finder(csv_dict):
    if 'manufacturer' in csv_dict.fieldnames:
        return 'manufacturer'
    elif 'supplier' in csv_dict.fieldnames:
        return 'supplier'
    else:
        print('Manufacturer fieldname not found.')
        return None

# Looks for variations of 'Vendor Quote #' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def vendorquote_finder(csv_dict):
    if 'quotename' in csv_dict.fieldnames:
        return 'quotename'
    elif 'supplierquote#' in csv_dict.fieldnames:
        return 'supplierquote#'
    elif 'quote#' in csv_dict.fieldnames:
        return 'quote#'
    elif 'quote' in csv_dict.fieldnames:
        return 'quote'
    elif 'quoteno' in csv_dict.fieldnames:
        return 'quoteno'
    elif 'pricequotation' in csv_dict.fieldnames:
        return 'pricequotation'
    elif 'quotenumber' in csv_dict.fieldnames:
        return 'quotenumber'
    else:
        print('Vendor Quote # fieldname not found.')
        return None

#Looks for variations of "Vendor Quote #' in lines before dictionary, returns the number as a string. None if no variation found
def str_vendorquote_finder(quote_str):
    if 'quote:' in quote_str:
        return quote_str.replace('quote:', "")
    elif 'arrowquote#:' in quote_str:
        return quote_str.replace('arrowquote#:', "")
    else:
        return None

# Looks for variations of 'Additional Description' fieldnames and returns value found in vendor csv quote. Returns None if no variation is found.
def add_description_finder(csv_dict):
    if 'additionaldescription' in csv_dict.fieldnames:
        return 'additionaldescription'
    if 'comments' in csv_dict.fieldnames:
        return 'comments'
    else:
        print('Additional Description fieldname not found.')
        return None

# reformat_header('5807.csv')
# ********** TEMP UNIT TESTS *****************
# csv_avt('GBQUOTE.csv', 'quotes/GBQUOTE.csv', "test", "test")
# csv_avt('NetApp_5807.csv', 'quotes/NetApp_5807.csv', "test", "test")
# csv_avt('061219-WWT-Hawaii Medical Service Association.xls', 'quotes/061219-WWT-Hawaii Medical Service Association.xls', "test", "test")
# csv_avt('061219-WWT-Hawaii Medical Service Association.xls', 'quotes/061219-WWT-Hawaii Medical Service Association.xls', "test", "test")
# csv_avt('06062019-WWT-Hawaii Medical Service Association[1].xls', 'quotes/06062019-WWT-Hawaii Medical Service Association[1].xls', "test", "test")
# csv_avt('PaloAlto_PAN_Hawaiian Airlines_0020706101.xls', 'quotes/PaloAlto_PAN_Hawaiian Airlines_0020706101.xls', "test", "test")
# csv_avt('PAN_Brigham Young University-Hawaii_0020724391.xls', 'quotes/PAN_Brigham Young University-Hawaii_0020724391.xls', "test", "test")
# csv_avt('QUO-1953529-L6W1V2-1.xlsx', 'quotes/QUO-1953529-L6W1V2-1.xlsx', "test", "test")
# csv_avt('QUO-2621751-L9R4M7-0.xlsx', 'quotes/QUO-2621751-L9R4M7-0.xlsx', "test", "test")
# csv_avt('QUO-2738183-V3M3C4-1.xlsx', 'quotes/QUO-2738183-V3M3C4-1.xlsx', "test", "test")
# csv_avt('Quote_748239329.html', 'quotes/Quote_748239329.html', "test", "test")

# print(convert_xls_xlsx_to_csv('quotes/PAN_Brigham Young University-Hawaii_0020724391.xls'))
# convert_html_to_csv('Quote_748239329.html', 'quotes/Quote_748239329.html')

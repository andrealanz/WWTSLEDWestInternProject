import csv
import string

# with open('5807.csv') as csv_file:
    # csv_reader = csv.DictReader(csv_file)
    # with open('5807_wwt.csv',mode='w',newline='') as wwt_file:
        # headers = ['Part #', 'Description', 'List Price', 'WWT Cost', 'Customer Price', 'Qty']
        # csv_writer=csv.DictWriter(wwt_file, fieldnames=headers)
        # csv_writer.writeheader()
        # for row in csv_reader:
            # count += 1
            # # print('Row ' + str(count))
            # csv_writer.writerow({'Part #':row['Part Number'],'Description':row['Part Number'], 'List Price': row['List Price'], 'WWT Cost':row['Reseller Net Price'], 'Customer Price':row['Reseller Net Price'], 'Qty':row['Qty']})
            # # print(row['Part Number'])
# def csv_avt(filename):
    # with open(filename) as csv_file:
        # csv_reader = csv.DictReader(csv_file)
        # part_name = part_finder(csv_reader)
        # descrition_name = description_finder(csv_reader)
        # listprice_name = listprice_finder(csv_reader)
        # wwtcost_name = wwtprice_finder(csv_reader)
        # quantity_name = quantity_finder(csv_reader)
        # manufacturer_name = manufacturer_finder(csv_reader)

        # with open('wwt_'  + filename,mode='w',newline='') as wwt_file:
            # headers = ['Part #', 'Description', 'List Price', 'WWT Cost', 'Customer Price', 'Qty']
            # csv_writer=csv.DictWriter(wwt_file, fieldnames=headers)
            # csv_writer.writeheader()
            # for row in csv_reader:
                # (csv_writer.writerow({'Part #':row['Part Number'],'Description':row['Part Number'], 'List Price': row['List Price'], 'WWT Cost':row['Reseller Net Price'],
                # 'Qty':row['Qty'],'Manufacturer':row[None],'Vendor':None}))
                # print(row)

def reformat_header(filename):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # print(csv_reader.fieldnames)
        count = 0

        #iterates through all fieldnames and makes case insensitive, removes punctuation and spaces except hashtags(#)

        for fieldname in csv_reader.fieldnames:
            fieldname = fieldname.lower()
            fieldname = fieldname.translate(str.maketrans('','',".,"))
            fieldname = fieldname.replace(" ","")
            csv_reader.fieldnames[count] = fieldname
            # print(csv_reader.fieldnames[count])
            count += 1
        print(csv_reader.fieldnames)

# def csv_avt(filename):
    # with open(filename) as csv_file:
        # csv_reader = csv.DictReader(csv_file)
        # count = 0
        # for fieldname in csv_reader.fieldnames:
            # fieldname = fieldname.lower()
            # fieldname = fieldname.translate(str.maketrans('','',".,"))
            # fieldname = fieldname.replace(" ","")
            # csv_reader.fieldnames[count] = fieldname
            # print(csv_reader.fieldnames[count])
            # count += 1
        # part_name = part_finder(csv_reader)
        # descrition_name = description_finder(csv_reader)
        # listprice_name = listprice_finder(csv_reader)
        # wwtcost_name = wwtprice_finder(csv_reader)
        # quantity_name = quantity_finder(csv_reader)
        # manufacturer_name = manufacturer_finder(csv_reader)
        # vendorquote_name = vendorquote_finder(csv_reader)
        # with open('wwt_'  + filename,mode='w',newline='') as wwt_file:
            # headers = ['Part #', 'Description', 'List Price', 'WWT Cost','Qty','Manufacturer','Vendor','Additional Description','Vendor Quote #']
            # csv_writer=csv.DictWriter(wwt_file, fieldnames=headers)
            # csv_writer.writeheader()
            # for row in csv_reader:
                # (csv_writer.writerow({'Part #':row[part_name],'Description':row[descrition_name], 'List Price': row[listprice_name], 'WWT Cost':row[wwtcost_name],
                # 'Qty':row[quantity_name],'Manufacturer':None,'Vendor':None,'Additional Description':None,'Vendor Quote #':None}))

def csv_avt(filename,filepath,vendorname):
    items = 0

    with open(filepath, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        for fieldname in csv_reader.fieldnames:
            fieldname = fieldname.lower()
            fieldname = fieldname.translate(str.maketrans('','',".,"))
            fieldname = fieldname.replace("\n","")
            fieldname = fieldname.replace(" ","")
            csv_reader.fieldnames[count] = fieldname
            # print(csv_reader.fieldnames[count])
            count += 1
        part_name = part_finder(csv_reader)
        description_name = description_finder(csv_reader)
        listprice_name = listprice_finder(csv_reader)
        wwtcost_name = wwtprice_finder(csv_reader)
        quantity_name = quantity_finder(csv_reader)
        manufacturer_name = manufacturer_finder(csv_reader)
        vendorquote_name = vendorquote_finder(csv_reader)

        with open('wwt_'  + filename,mode='w',newline='') as wwt_file:
            headers = ['Part #', 'Description', 'List Price', 'WWT Cost','Customer Price','Qty','Manufacturer','Vendor','Additional Description', 'Cust Product #', 'Lab Flag (Y/N)', 'Contract Start Date (MM/DD/YYYY)','Contract End Date (MM/DD/YYYY)', 'Serial #' 'Vendor Quote #','Duration','Lead Time', 'Cost Type']
            csv_writer=csv.DictWriter(wwt_file, fieldnames=headers)
            csv_writer.writeheader()


            for i, row in enumerate(csv_reader):
                # print("i:", i)
                # print(items)
                if row[description_name]:
                    items += 1
                # print(items)
                # if i >= (items):
                    # break
                if row[part_name] is None and row[description_name] is None and row[quantity_name] is None:
                    break

                output_dictionary = {}
                if part_name is not None:
                    output_dictionary.update({'Part #':row[part_name]})
                else:
                    output_dictionary.update({'Part #':None})
                if description_name is not None:
                    output_dictionary.update({'Description':row[description_name]})
                else:
                    output_dictionary.update({'Description':None})
                if listprice_name is not None:
                    output_dictionary.update({'List Price':row[listprice_name]})
                else:
                    output_dictionary.update({'List Price':None})
                if wwtcost_name is not None:
                    output_dictionary.update({'WWT Cost':row[wwtcost_name]})
                else:
                    output_dictionary.update({'WWT Cost':None})
                if quantity_name is not None:
                    output_dictionary.update({'Qty':row[quantity_name]})
                else:
                    output_dictionary.update({'Description':None})
                if manufacturer_name is not None:
                    output_dictionary.update({'Manufacturer':row[manufacturer_name]})
                else:
                    output_dictionary.update({'Manufacturer':None})
                if vendorquote_name is not None:
                    output_dictionary.update({'Vendor Quote #':row[vendorquote_name]})
                else:
                    output_dictionary.update({'Vendor Quote #':None})
                output_dictionary.update({'Additional Description':None, 'Vendor':vendorname})
                csv_writer.writerow(output_dictionary)
                # (csv_writer.writerow({'Part #':row[part_name],'Description':row[description_name], 'List Price': row[listprice_name], 'WWT Cost':row[wwtcost_name],
                # 'Qty':row[quantity_name],'Manufacturer':None,'Vendor':None,'Additional Description':None,'Vendor Quote #':None}))


# def part_finder(csv_dict):
    # if 'partnumber' in csv_dict.fieldnames:
        # return 'partnumber'
    # elif 'itemnumber' in csv_dict.fieldnames:
        # return 'itemnumber'
    # elif 'item' in csv_dict.fieldnames:
        # return 'item'
    # elif 'mfrpart#' in csv_dict.fieldnames:
        # return 'mfrpart#'
    # elif 'part#' in csv_dict.fieldnames:
        # return 'part#'
    # elif 'itemno' in csv_dict.fieldnames:
        # return 'itemno'
    # elif 'partno' in csv_dict.fieldnames:
        # return 'partno'
    # else:
        # print('Part # fieldname not found.')
        # return None


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

def description_finder(csv_dict):
    if 'product' in csv_dict.fieldnames:
        return 'product'
    elif 'description' in csv_dict.fieldnames:
        return 'description'
    elif 'productdescription' in csv_dict.fieldnames:
        return 'productdescription'
    else:
        print('Description fieldname not found.')
        return None

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

def quantity_finder(csv_dict):
    if 'qty' in csv_dict.fieldnames:
        return 'qty'
    elif 'quantity' in csv_dict.fieldnames:
        return 'quantity'
    elif 'qtyquoted' in csv_dict.fieldnames:
        return 'qty quoted'
    elif 'extqty' in csv_dict.fieldnames:
        return 'extqty'
    else:
        print('Quantity fieldname not found.')
        return None


def manufacturer_finder(csv_dict):
    if 'manufacturer' in csv_dict.fieldnames:
        return 'manufacturer'
    elif 'supplier' in csv_dict.fieldnames:
        return 'supplier'
    else:
        print('Manufacturer fieldname not found.')
        return None

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

# reformat_header('5807.csv')
# csv_avt('QUO-test.csv', 'QUO-test.csv', "test")
# csv_avt('5807.csv', "b")

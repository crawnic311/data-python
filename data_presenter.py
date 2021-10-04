cupcakes_invoices = open('CupcakeInvoices.csv')

#for line in cupcakes_invoices:
#    print(line)


for line in cupcakes_invoices:
    line_split = line.rstrip('\r\n').split(",") 
    print(line_split[2])  
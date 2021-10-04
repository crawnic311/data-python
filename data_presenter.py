cupcakes_invoices = open('CupcakeInvoices.csv')

#for line in cupcakes_invoices:
#    print(line)


#for line in cupcakes_invoices:
#    line_split = line.rstrip('\r\n').split(",") 
#    print(line_split[2])  
sum = 0

for line in cupcakes_invoices:
    line_split = line.rstrip('\r\n').split(",") 
    quant = float(line_split[3])
    price = float(line_split[4])
    total = quant * price
    print(total)
    sum += total 

print(sum)
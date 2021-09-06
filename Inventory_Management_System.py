import json
import datetime

fdr = open("manage.json",'r')
txt = fdr.read()
fdr.close()

# USER INPUTS 

product = json.loads(txt)
print("------ Respectd Product Keys ----- ")
for _ in product.keys():
        print(f"{_} to purchase {product[_]['Name']}")

print(" \n\nEnter Total Number of different product you want to purchase from list ")
total = int(input())

Purchase_Detail = {}            # Dictionary to store User Purchase Details

print(f"Enter {total} product keys and Quantity  ")

while total >0:
        k = input("Enter Product Key  ")
        if k in product.keys() and k not in Purchase_Detail.keys(): 
                q = input("Enter Quantity  ")
                if int(q) <= int(product[k]['Quant']): 
                      Purchase_Detail[k] = q
                else:
                        print("Sorry We Don't Have Enough Quantity of Entered Product")
                        tmp = input("Please Enter Smaller Quantity  ")
                        Purchase_Detail[k] = tmp

        elif k in Purchase_Detail.keys():                # IF KEY IS ALREADY PRESENT IN PURCHASE DETAIL
                q = input("Enter Quantity  ")
                if int(q) <= int(product[k]['Quant']): 
                      Purchase_Detail[k] = int(q) + int(Purchase_Detail[k])

        else :
                print("Please Enter Valid Key ")
                total+=1
        total-=1

# UPDATING  SYSTEM  FILE

for _ in Purchase_Detail.keys():
        product[_]['Quant'] = int(product[_]['Quant']) - int(Purchase_Detail[_])

js = json.dumps(product)
fd = open("manage.json",'w')
fd.write(js)
fd.close()


# BILL PREPRATION 

curr_t = datetime.datetime.now()
my_format = "{:<8}{:<15}{:<7}{:<7}{:<7}"
name = input("Enter Your Name  ")
phn = input("Enter Your Phone Number  ")
i = 1
GT = 0
print(f"\n\nHello  Mr./Mrs.  {name} ")
print("\nYour Shopping Bill    - >>> \n")
print(f"Date :-    {curr_t.day}/{curr_t.month}/{curr_t.year}")
ct = curr_t.strftime("%H:%M:%S")
print(f"Shopping time :-    {ct}\n")
print(my_format.format('S.No.', 'Product', 'Rate', 'QTY', 'Amount'))
for _ in Purchase_Detail.keys():
        print(my_format.format(i, product[_]['Name'], product[_]['Price'], Purchase_Detail[_], int(product[_]['Price'])*int(Purchase_Detail[_])))
        GT += int(product[_]['Price'])*int(Purchase_Detail[_])
        i+=1

print(f"\n Total Paying Amount ->  {GT}\n")
print("*****  THANK YOU for SHOPING  ******")
print(":) :)  HAVE A NICE DAY  :) :)")




#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


print("==================================================================")
print("   SMARTCAMPUS UTILITY & ACCESS PASS GENERATOR   ")
print("==================================================================")

user=input("Select User category(1:student, 2: Faculty/Staff):").strip()
if user=="1":
    sub_category=input("Enter Sub-Category (a: Undergraduate (UG), b: Postgraduate(PG)):").lower().strip()
    if sub_category=="a":
       base_fee=500
    elif sub_category=="b":
        base_fee=350
    else:
        print("[Error]:Invalid Sub-Categories")
        exit()
elif user=="2":
    sub_category=input("Enter Sub-Category (c: Resident Faculty, d: Visiting/ Guest Faculty):").lower().strip()
    if sub_category=="c":
        base_fee=800
    elif sub_category=="d":
        base_fee=1200 
    else:
        print("[Erroe]:Invalid Sub-Categories") 
        exit()

discount_rate=0
if user=="1":
    student_cgpa=float(input("Enter Your CGPA (0.0-10.0):"))
    if student_cgpa<0.0 or student_cgpa>10.0:
        print("[ERROR]:CGPA should be between 0.0 and 10.0")
        exit()
    if student_cgpa>=8.5:
         discount_rate=20
    elif student_cgpa>=7.5:
        discoun_rate=10

    elif user=="2":
        service_years=int(input("Enter total Years of Service:"))
        if service_year>10:
            discount_rate=15
    discount_amount=(base_fee*discount_rate)/100       


parking=input("Select Parking Permit(0:None,2:Two_Wheeler ,4:Four_Wheeler):")          
parking_fee=0
peak_surcharge=0
if parking=="2":
    parking_fee=200
elif parking=="4":
    parking_fee=600
    if user=="1":
        peak_surcharge=150
elif parking=="0":
    parking_fee=0
else:
    print("[ERROR]:Invalid Parking option")
    exit()

units=int(input("Enter Monthly Electricity Consumption(in kwh):"))
if units<0:
    print("[ERROR]:Electricity units cannot be negative")
    exit()
if units<=100:
    bill=units*3
    fixed_charge=50
elif units<=300:
    bill=(100*3)+((units-100)*5)
    fixed_charge=100
elif units<=500:
    bill=(100*3)+(200*5)+((units-300)*7.5)
    fixed_charge=150
else:
    bill=(100*3)+(200*5)+(200*7.5)+((units-500)*10)
    fixed_charge=250
electricity_bill=bill+fixed_charge
net_pass_parking=base_fee-discount_amount+parking_fee+peak_surcharge
total_monthly_payable=net_pass_parking+electricity_bill




print("\n-----------------------------------------")
print("CALCULATED INVOICE DETAILS")
print("-----------------------------------------")

print(f"Base Access Pass Fee:    ₹{base_fee:.2f}")
print(f"Discount Applied({discount_rate}%): -₹{discount_amount:.2f}")
print(f"Parking Fee:  ₹{parking_fee:.2f}")
print(f"Peak Surcharge(Student):  ₹{peak_surcharge:.2f}")
print(f"Net Pass & Parking Total:  ₹{net_pass_parking:.2f}")

print("----------------------------------------------------------------------")
print(f"Electricity Bill({units}kwh):  ₹{electricity_bill:.2f}(Fixed charge:  ₹{fixed_charge})")

print("-----------------------------------------------------------------------")
print(f"TOTAL AMOUNT TO PAY : ₹ {total_monthly_payable:.2f}")
print("=======================================================================")





# In[ ]:





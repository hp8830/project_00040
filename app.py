import datetime
import os
from bills import Bill, Flatmate
from bills_report import PdfReport




amount_entry = float(input("Hey User, enter the bill amount: "))
date_entry = input('Enter a date in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
bill_date = str(datetime.date(year, month, day))


month_bill = Bill(amount=amount_entry, period=bill_date)

mate1 = input('Input Flatmate 1 Name: ')
mate2 = input('Input Flatmate 2 Name: ')
mate3 = input('Input Flatmate 3 Name: ')
mate1_days = int(input('Input Flatmate 1 days: '))
mate2_days = int(input('Input Flatmate 2 days: '))
mate3_days = int(input('Input Flatmate 3 days: '))

roommate_01 = Flatmate(name=mate1, days_in_house=mate1_days)
roommate_02 = Flatmate(name=mate2, days_in_house=mate2_days)
roommate_03 = Flatmate(name=mate3, days_in_house=mate3_days)

print(roommate_01.pays(bill=month_bill, flatmate2=roommate_02,flatmate3=roommate_03))
print(roommate_02.pays(bill=month_bill, flatmate2=roommate_01,flatmate3=roommate_03))
print(roommate_03.pays(bill=month_bill, flatmate2=roommate_01,flatmate3=roommate_02))

os.chdir("C:/portfolio_2022/python/project_00039/files")
pdf_report = PdfReport(filename=f"{month_bill.period}_report.pdf")
pdf_report.generate(flatmate1=roommate_01, flatmate2=roommate_02, flatmate3=roommate_03, bill=month_bill)
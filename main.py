Worker_current_age= int(input("Enter current age in year:"))
Worker_current_years_of_service=int(input("Enter current years of service:"))
#Input for worker's details
Largest_expected_annual_income= float(input("Enter the largest expected annual:"))
second_largest_expected_annual_income=float(input("Enter the second-largest expected annual income:"))
Third_largest_expected_annual_income= float(input("Enter the third-largest expected annual income:"))
rate= 1.4 #set by the pension provider
#Calculate the average of the three Largers Incomes 
average_of_best_3_annual_incomes= (Largest_expected_annual_income + second_largest_expected_annual_income + Third_largest_expected_annual_income)/ 3
#The exact number of the years of service 
years_of_service= Worker_current_age - 30
#The provided formula 
pension_income = (average_of_best_3_annual_incomes * rate/100) * years_of_service
retirement_ages=[55, 60, 65] #the ages I want to calculate for 
#Calculate for 55 years old 
pension_income_55= (average_of_best_3_annual_incomes * rate/100)* 25
#Calculate for 60 years old 
pension_income_60= (average_of_best_3_annual_incomes * rate/100)* 30
#Calculate for 65 years old 
pension_income_65= (average_of_best_3_annual_incomes * rate/100)* 35
#formating the table
table=f"""
{"retirement age"}\t{"retirement incom"}
{"55"}\t\t ${pension_income_55:.2f}
{"60"}\t\t ${pension_income_60:.2f}
{"65"}\t\t ${pension_income_65:.2f}
"""
print(table) 
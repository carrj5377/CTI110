# CTI-110
# P3HW2 - Salary
# Julian Carr
# 10/3/2023
# Calculate an employees over time pay, total pay without overtime, and gross pay 
#and print differnet results depending on if employee had overtime

# Ask for stating information like emplyee name,hours they worked, and pay rate
name = input("Enter employee's name: ")

hours_worked = float(input("Enter number of hours worked: "))

pay_rate = float(input("Enter employee's pay rate: "))
print('-'*50)

print('employe name: ', name)
print()

#if the emplyee worked more than 40 hours the excess is considered overtime
# Ex. 45 the 5 would be the overtime
if hours_worked > 40.0:
  overtime = float(input("Overtime: "))
  reg_pay = pay_rate * 40
  
# Use the overtime the pay rate and 1.5 to lean the overtime pay
  
  OT_pay = overtime * pay_rate * 1.5
  
  # Add the regular pay and the overtime pay together to get gross pay
  gross_pay = reg_pay + OT_pay

  # Print results
  print("Hours Worked","Pay Rate", "Over Time " ,"Over Time Pay ", "RegHour Pay " , 
        "Gross Pay", sep='\t\t')
  
  
  print("-"*100)
  
  print(hours_worked, pay_rate, overtime , OT_pay , reg_pay, gross_pay, sep = '\t\t\t\t')

# if the hours are not more the 40 just do not print overtime, overtime pay
# ,or gross pay
else:
  reg_pay2 = hours_worked * pay_rate
  print("Hours Worked", "Pay Rate", "RegHour Pay", sep='\t\t')
  print("-"*100)
  print(hours_worked, pay_rate, f'{reg_pay2:.2f}', sep = '\t\t\t\t')
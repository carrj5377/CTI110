# CTI-110
# P3HW2 - Salary
# Julian Carr
# 10/3/2023
# Calculate an employees over time pay, total pay without overtime, and gross pay 
# and print differnet results depending on if employee had overtime
# Ask for stating information like emplyee name,hours they worked, and pay rate
# Use sentinel value to continue loop until user inputs "Done"

employee_count = 0
name = 0
OT_hours = 0
OT_pay = 0
gross_pay = 0
total_reg_pay = 0
total_grospay = 0
total_OT = 0
reg_pay = 0
while name != "Done":
  
  name = input("Enter employee name or 'Done' to quit: ")
  if name == "Done":
    print("-"*100)
    print("Total Employees: ", employee_count)
    print("Total regular pay: ", total_reg_pay)
    print("Total Overtime Pay: ", total_OT)
    print("Total Gross Pay: ", total_grospay)
    print("-"*100)
    print("Thank you for using this program")
    break
  employee_count += 1
  OT_hours = 0 # start at zero for each employee
  hours_worked = float(input("Enter number of hours worked: "))

  pay_rate = float(input("Enter employee's pay rate: "))
  print('-'*50)

  print('employe name: ', name)
  print()
 
#if the emplyee worked more than 40 hours the excess is considered overtime
# Ex. 45 the 5 would be the overtime

  if hours_worked >= 0 and hours_worked <= 40:
    
    reg_pay = pay_rate * hours_worked
    total_reg_pay += reg_pay
    OT_pay = 0
  elif hours_worked > 40:
    reg_pay = pay_rate * 40
    total_reg_pay += reg_pay
# Use the overtime the pay rate and 1.5 to learn the overtime pay
  if hours_worked > 40:
      OT_hours = hours_worked - 40
      OT_pay = OT_hours * pay_rate * 1.5
   
  total_OT += OT_pay
  # Add the regular pay and the overtime pay together to get gross pay
  gross_pay = reg_pay + OT_pay
  total_grospay += gross_pay
  # Print results
  print("Hours Worked","Pay Rate", "Over Time " ,"Over Time Pay ", "RegHour Pay " , 
        "Gross Pay", sep='\t\t')
  
  
  print("-"*100)
  
  print(hours_worked, pay_rate, OT_hours , OT_pay , reg_pay, gross_pay, sep = '\t\t\t\t')
    # if the hours are not more the 40 just do not print overtime, overtime pay
    # ,or gross pay
  
  
    


    
     
      
    


  
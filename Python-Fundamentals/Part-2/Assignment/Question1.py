# 1. Write a program that takes as input. Using conditional statements, calculate the final tax rate based on these rules: 
# • If salary < 30,000 → 5% 
# • If salary is 30,000–70,000 → 15% 
# • If salary > 70,000 → 25% 

names = ["Aman", "Naman", "Riya"]
salaries = [25000, 45000, 80000]

for i in range(len(names)):
    salary = salaries[i]

    if salary < 30000:
        tax = salary*0.5
    elif salary <= 70000:
        tax = salary*0.15
    else:
        tax = salary*0.25

    print("Name : " , names[i])
    print("Salary : " , salaries[i])
    print("Tax : " , tax)
    print("Final Salary : " , salary-tax)
    print("-------------")
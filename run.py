
salary = float(input('Yearly salary before deductions: '))
pension_percent = float(input('Percentage of income paid to pension (%) :'))/100
pension_personal = salary * pension_percent

print(f'salary = £{"{:.2f}".format(salary)} \npension_percent = {pension_percent * 100}% \npension_personal = £{pension_personal}')
taxable_salary = salary - pension_personal

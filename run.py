# Modules
import utils.tools as tools

def main():
    tax_table_df = tools.get_tax_table()
    tax_table_df = tools.clean_tax_table(tax_table_df)

    print(tax_table_df)

    salary = float(input('Yearly salary before deductions: '))
    pension_percent = float(input('Percentage of income paid to pension (%) :'))/100
    pension_personal = salary * pension_percent

    print(f'salary = £{"{:.2f}".format(salary)} \npension_percent = {pension_percent * 100}% \npension_personal = £{pension_personal}')
    taxable_salary = salary - pension_personal
    

if __name__ == "__main__":
    main()
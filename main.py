from datetime import date
from application import people as p
from application import salary

current_date = date.today()



if __name__ == '__main__':
    p.get_employees('Анатолий')
    salary.calculate_salary(3000,40000)
    print(f'Текущая дата {current_date}')



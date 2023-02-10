Employee Payout Program
Introduction
This program is developed to calculate the overtime and commission of employees. The program is developed by Tamires Lucas on 06/27/2022.

Classes
The program consists of four classes:

Employee
CommissionPaid
HourlyPaid
SalaryPaid
Employee
This is the base class for all the employee classes. It has the following methods and variables:

name
department
get_name()
set_name()
get_department()
set_department()
pay()
CommissionPaid
This class is inherited from the Employee class. It calculates the commission based on the sales made by an employee. It has the following methods and variables:

base_rate
sales
get_base_rate()
set_base_rate()
get_sales()
set_sales()
HourlyPaid
This class is inherited from the Employee class. It calculates the payment for an hourly employee based on the hours worked. It has the following methods and variables:

hourly_rate
hours
get_hourly_rate()
set_hourly_rate()
get_hours()
set_hours()
SalaryPaid
This class is inherited from the Employee class. It calculates the payment for a salaried employee. It has the following methods and variables:

salary
get_salary()
set_salary()
Conclusion
This program provides a solution to calculate the payouts of employees. It is a great starting point for calculating the payouts for different types of employees, such as hourly employees, salaried employees, and employees who receive commission based on sales.

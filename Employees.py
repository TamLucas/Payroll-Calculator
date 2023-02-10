#Description: This program was developed to calculate overtime and comission
#Author: Tamires Lucas
#Date: 06/27/2022

#base class Employee
class Employee(object):
    #constructor
    def __init__(self, name="", department=""):
        self.name = name
        self.department = department
     #getter name variable
    def get_name(self):
        return self.name
    #setter name variable
    def set_name(self, department):
        self.name = name
    #getter department variable
    def get_department(self):
        return self.department
    #setter department variable
    def set_department(self, department):
        self.department = department
    #pay function
    def pay(self):
        return 0.0

    def __str__(self):
        return self.name + " " + self.department

#class Commission
class CommissionPaid(Employee):
    #constructor
    def __init__(self, name, department, base_rate, sales):
        self.base_rate = base_rate
        self.sales = sales
        Employee.__init__(self, name, department)
    
    def get_base_rate(self):
        return self.base_rate
    def setBaseRate(self, base_rate):
        self.base_rate = base_rate

    def get_sales(self):
        return self.sales
    def set_sales(self, sales):
        self.sales = sales
    
    #pay function
    def pay(self):
        payout = 0.0
        if self.sales > 30000:
            payout = self.base_rate + (self.sales * 0.03)
        elif self.sales > 5000 and self.sales < 30000:
            payout = self.base_rate + (self.sales * 0.01)
        else:
            payout = self.base_rate
        return payout
    
    def __str__(self):
        return "{:<25}{:<20}{:<15}{:<15}".format("Commission Paid", self.name, self.department, "$" + str(self.pay()))

#class Hourly Payment
class HourlyPaid(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours
        Employee.__init__(self, name, department)
            
    def get_hourly_rate(self):
        return self.hourly_rate
    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate
        
    def get_hours(self):
        return self.hours
    def set_hours(self, hours):
        self.hours = hours
    
    #pay function 
    def pay(self):
        payout = 0.0
        overtime = 0.0
        if self.hours > 40:
            overtime = self.hourly_rate * (self.hours - 40) * 1.5
            payout = self.hourly_rate * 40 + overtime
        else:
            payout = self.hourly_rate * self.hours
        return payout

    def __str__(self):
        return "{:<25}{:<20}{:<15}{:<15}".format("Hourly Paid", self. name, self. department, "$" + str(self.pay()))
        
    #class Salary
class SalaryPaid(Employee):
    def __init__(self, name, department, salary):
        self.salary = salary
        Employee.__init__(self, name, department)

    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary
        
    def pay(self):
        return self.salary
        
    def __str__(self):
        return "{:<25}{:<20}{:<15}{:<15}".format("Salary Paid", self.name, self.department, "$" + str(self.pay()))



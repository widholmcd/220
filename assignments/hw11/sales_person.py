"""
Name: Calvin Widholm
sales_person.py

Problem: Creating a sales person object and various methods to access data about sales people

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""
class SalesPerson:
    """
    sales person constructor
    """
    def __init__(self, employee_id:int, name:str):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        total = sum(self.sales)
        return float(total)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = sum(self.sales)
        if total >= quota:
            return True
        return False

    def compare_to(self, other):
        total = self.total_sales()
        other_total = other.total_sales()
        if total > other_total:
            return 1
        if total < other_total:
            return -1
        return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())

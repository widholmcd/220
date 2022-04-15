"""
Name: Calvin Widholm
sales_force.py

Problem: Using sales people and investigating their ids, contributions to sales force and sales statistics

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I talked with Brett Widholm.- I Certify- CW
"""
from sales_person import SalesPerson

class SalesForce:
    """
    sales force constructor
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        opened = open(file_name, "r")
        for line in opened:
            split = line.split(',')
            employee_id = eval(split[0])
            name = split[1].lstrip()
            person = SalesPerson(employee_id, name)
            sales = split[2].lstrip()
            sales_split = sales.split(' ')
            for i in range(len(sales_split)):
                person.enter_sale(sales_split[i])
            self.sales_people.append(person)
        print(self.sales_people)

    def quota_report(self, quota):
        employees_list = []
        for i in range(len(self.sales_people)):
            employee_details_list = []
            person = self.sales_people[i]
            employee_id = person.get_id()
            name = person.get_name()
            total = person.total_sales()
            employee_details_list.append(employee_id)
            employee_details_list.append(name)
            employee_details_list.append(total)
            if total >= quota:
                employee_details_list.append(True)
            else:
                employee_details_list.append(False)
            employees_list.append(employee_details_list)
        return employees_list

    def top_seller(self):
        sales_people_list = []
        total_list = []
        top_seller_list = []
        returned_list = []
        for i in range(len(self.sales_people)):
            person = self.sales_people[i]
            total = person.total_sales()
            total_list.append(total)
            sales_people_list.append(person)
        total_list_2 = total_list.copy()
        total_list_2.sort(reverse=True)
        top_seller_list.append(total_list_2[0])
        count = 1
        while total_list_2[0] == total_list_2[count]:
            top_seller_list.append(total_list_2[count])
            count += 1
        counter = 0
        while counter < len(total_list):
            if top_seller_list[0] == total_list[counter]:
                returned_list.append(sales_people_list[counter])
            counter += 1
        return returned_list

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            person = self.sales_people[i]
            identify = person.get_id()
            if identify == employee_id:
                return person
        return None

    def get_sale_frequencies(self):
        sale_frequency = {}
        for i in range(len(self.sales_people)):
            person = self.sales_people[i]
            sales = person.get_sales()
            for j in range(len(sales)):
                sale = sales[j]
                sale_frequency[sale] = sale_frequency.get(sale, 0) + 1
        return sale_frequency

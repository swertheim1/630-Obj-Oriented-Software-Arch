from person import Person as p
from datetime import date


class Employee(p):
    """
    Attributes:
        emp_num, ssn, start_date, job_title, date_of_birth, hourly_rate, emp_type, p_id, first_name, last_name, phone_no
        email, st_address, city, state, zip_code
    """

    def __init__(self, p_id, first_name, last_name, phone_no, email, st_address, city,
                 state, zip_code, emp_num, ssn, start_date, job_title, date_of_birth, hourly_rate, emp_type,
                 active_emp):
        super().__init__(p_id, first_name, last_name, phone_no, email, st_address, city, state, zip_code)
        self.emp_num = emp_num
        self.ssn = ssn
        self.start_date = start_date
        self.job_title = job_title
        self.date_of_birth = date_of_birth
        self.hourly_rate = hourly_rate
        self.emp_type = emp_type
        self.active_emp = active_emp

    def update_job_title(self, job_title):
        self.job_title = job_title

    def update_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def update_emp_type(self, emp_type):
        self.emp_type = emp_type

    def hire_employee(self):
        self.is_employee = 1

    def terminate_employee(self):
        self.is_employee = 0

    def __repr__(self):
        return f"emp_num: {self.emp_num} Name: {self.first_name} {self.last_name}, Email: {self.email}, " \
               f"Phone_no: {self.phone_no} Address: {self.st_address}, {self.city}, {self.state} {self.zip_code}" \
               f" Job Title: {self.job_title}  Emp Status: {self.is_employee}"


def test():
    # p_id, first_name, last_name, phone_no, email, st_address, city, state, zip_code, is_customer,  is_employee,
    # emp_num, ssn, start_date, job_title, date_of_birth, hourly_rate, emp_type, is_employee):
    employee_list = []
    employee1 = Employee('PER-1013', 'Mary', 'Simons', '555-123-4567', 'm.simons@email.com', '1234 Main St,',
                         'Cleveland', 'OH', '11521', 'EMP_2001', '543-21-2215', date(2023, 2, 2), 'Front Desk Clerk',
                         date(1991, 1, 1), 15.75, 'non-exempt', 1)
    employee2 = Employee('PER-1014', 'Mark', 'Fink', '436-215-1234', 'm.fink@eamil.com', '1234 First St,',
                         'White Salmon', 'WA', '91253', 'EMP_2002', '123-45-6789', date(2015, 2, 2), 'Front Desk Clerk',
                         date(2000, 1, 1), 85.75, 'non-exempt', 1)
    employee3 = Employee('PER-1015', 'Mark', 'Ford', '555-346-2587', 'MarkF@ford.com', '435 E 79th St.',
                         'New York', 'NY', '02145', 'EMP_2003', '123-45-6789', date(2022, 1, 1), 'Front Desk Clerk',
                         date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee4 = Employee('PER-1016', 'Bill', 'Worth', '555-951-3578', 'bworth@worths.com', '75 14th St.',
                         'Plano', 'TX', '72145', 'EMP_2004', '123-45-6789', date(2022, 1, 1), 'Front Desk Clerk',
                         date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee5 = Employee('PER-1017', 'Beth', 'Apple', '555-456-4826', 'Beth.Stull@stull_family.com', '134 Bryan Road.',
                         'Lakeside', 'TX', '73226', 'EMP_2005', '123-45-6789', date(2022, 1, 1), 'House Keeping',
                         date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee6 = Employee('PER-1018', 'Jerry', 'Springer', '555-156-9872', 'jerry@email.com', '8912 Park Ave',
                         'New York', 'NY', '02115', 'EMP_2006', '123-45-6789', date(2022, 1, 1), 'House Keeping',
                         date(1962, 8, 15), 25.75, 'non-exempt', 0)
    employee7 = Employee('PER-1019', 'Chris', 'Peek', '555-871-8963', 'cpeek@peek.com', '2272 First St.', 'Stafford',
                         'TX', '72231', 'EMP_2007', '123-45-6789', date(2022, 1, 1), 'House Keeping',
                         date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee8 = Employee('PER-1020', 'Marjorie', 'Slacker', '555-123-4567', 'mslacker@slackers.com', '2216 Alberts Dr.',
                         'Cleveland', 'OH', '42114', 'EMP_2008', '123-45-6789', date(2022, 1, 1), 'House Keeping',
                         date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee9 = Employee('PER-1021', 'Lola', 'Sawyer', '555-267-3311', 'lola@sawyer.com', '1212 E 7th St.', 'St. Pete',
                         'FL', '33622', 'EMP_2009', '123-45-6789', date(2022, 1, 1), 'House Keeping',
                         date(1962, 8, 15), 25.75, 'non-exempt', 0)
    employee10 = Employee('PER-1022', 'Bella', 'Thomas', '555-987-6543', 'bt6543@thomas.com', '2242 Claiborne St.',
                          'Clearwater', 'FL', '33516', 'EMP_2010', '123-45-6789', date(2022, 1, 1), 'House Keeping',
                          date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee11 = Employee('PER-1023', 'James', 'Feldman', '555-987-6543', 'bt6543@thomas.com', '191 Main Cir.',
                          'Lake Saint Louis', 'MO', '63367', 'EMP_2011', '123-45-6789', date(2022, 1, 1),
                          'House Keeping', date(1962, 8, 15), 25.75, 'non-exempt', 1)
    employee12 = Employee('PER-1024', 'Martha', 'Peterson', '555-582-5820', 'marthapetersonk@peterson.com',
                          '1515 North Point Rd.', 'Owlet', 'TX', '73511', 'EMP_2012', '123-45-6789', date(2022, 1, 1),
                          'House Keeping', date(1962, 8, 15), 25.75, 'non-exempt', 0)

    employee_list.append(employee1)
    employee_list.append(employee2)
    employee_list.append(employee3)
    employee_list.append(employee4)
    employee_list.append(employee5)
    employee_list.append(employee6)
    employee_list.append(employee7)
    employee_list.append(employee8)
    employee_list.append(employee9)
    employee_list.append(employee10)
    employee_list.append(employee11)
    employee_list.append(employee12)
    print('<<<<<<<< ALL EMPLOYEES >>>>>>>>')
    print(employee_list)
    print(p.print_list_of_people(employee_list))

    active_employee = []
    inactive_employee = []

    for employee in employee_list:
        if employee.active_emp == 1:
            active_employee.append(employee)
        else:
            inactive_employee.append(employee)

    print('<<<<<<<<< Active Employees >>>>>>>>>')
    print(p.print_list_of_people(active_employee))
    print('<<<<<<<<< Inactive Employees >>>>>>>>>')
    print(p.print_list_of_people(inactive_employee))


if __name__ == '__main__':
    test()

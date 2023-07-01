from sqlalchemy import select
from db_models import PersonTable, EmployeeTable
from person import Person as p
from main import session
from datetime import date


class Employee:
    @staticmethod
    def create_employee(person_id, is_current, ssn, start_date, job_title, dob, hourly_rate, end_date=''):
        customer = EmployeeTable(start_date=start_date, job_title=job_title, date_of_birth=dob,
                                 hourly_rate=hourly_rate, person_id=person_id, is_current=is_current, ssn=ssn,
                                 end_date=end_date)
        session.add_all([customer])
        session.commit()

    @staticmethod
    def update_job_title_by_emp_id(emp_id, job_title):
        employee_to_update = session.query(Employee).filter(EmployeeTable.emp_id == emp_id).first()
        employee_to_update.job_title = job_title
        session.commit()

    @staticmethod
    def create_list_of_non_current_employees():
        statement = select(Employee).join(PersonTable, EmployeeTable.person_id == PersonTable.person_id) \
            .filter(EmployeeTable.is_current_employee == 0)
        results = session.scalars(statement)
        return results

    @staticmethod
    def update_hourly_rate_by_emp_id(emp_id, hourly_rate):
        employee_to_update = session.query(Employee).filter(EmployeeTable.emp_id == emp_id).first()
        employee_to_update.hourly_rate = hourly_rate
        session.commit()

    @staticmethod
    def create_list_of_current_employees():
        statement = select(Employee).join(PersonTable, EmployeeTable.person_id == PersonTable.person_id) \
            .filter(EmployeeTable.is_current_employee == 1)
        results = session.scalars(statement)
        return results

    @staticmethod
    def update_pay_type_by_emp_id(emp_id, pay_type):
        employee_to_update = session.query(EmployeeTable).filter(EmployeeTable.emp_id == emp_id).first()
        employee_to_update.pay_type = pay_type
        session.commit()

    @staticmethod
    def delete_customer_by_id(emp_id):
        statement = select(Employee).join(PersonTable, EmployeeTable.person_id == PersonTable.person_id) \
            .filter(EmployeeTable.emp_id == emp_id)

        results = session.scalars(statement)
        for employee in results:
            if not employee.is_guest:
                session.delete(employee)
                session.commit()
                p.delete_person_by_id(employee.person.person_id)
            else:
                print(f'<<<< Cannot delete Person ID: {employee.person.person_id}  '
                      f'Name: {employee.person.first_name, employee.person.last_name} they are currently a guest. >>>>')


def test():
    Employee.create_employee(person_id=6, is_current=1, ssn='234-23-2345', start_date=date(2022, 12, 10),
                             dob=date(2001, 3, 4), hourly_rate=22.5, job_title='Front Desk Clerk')
    Employee.create_employee(person_id=7, is_current=1, ssn='345-34-3456', start_date=date(2022, 12, 10),
                             dob=date(2001, 3, 4), hourly_rate=22.5, job_title='Front Desk Clerk')
    Employee.create_employee(person_id=8, is_current=0, ssn='234-23-2345', start_date=date(2022, 12, 10),
                             dob=date(2001, 3, 4), hourly_rate=22.5, job_title='Front Desk Clerk')

    # Customer.update_is_guest_by_id(2, 1)

    results = Employee.create_list_of_non_current_employees()
    print("<<<< Customer that are not Guests >>>>>")
    for employee in results:
        print(employee.customer_id, employee.person)

    results = Employee.create_list_of_current_employees()
    print("<<<< Customer that are Guests >>>>>")
    for customer in results:
        print(customer.customer_id, customer.person)

    # Customer.delete_customer_by_id(2)
    # Employee.delete_employee_by_id(7)
    # Employee.delete_employee_by_id(1)


if __name__ == '__main__':
    test()

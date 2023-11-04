import sqlalchemy
from sqlalchemy import text, create_engine
import allure

class CompanyTable:
    
    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string)
    
    @allure.step("DB. Get employees list from company {max_id}")
    def get_list_of_employees(self, max_id: int) -> dict:
        """DB. Get list of employees"""
        query = text("select * from employee where id =:company_id")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.begin() as conn:
            bd_result = conn.execute(statement=query, parameters=dict(company_id = max_id)).fetchall()
        return bd_result

    @allure.step("DB. Add to {max_id} new employee {name} {surname} {phone}")
    def add_new_employee(self, max_id: int, name: str, surname: str, phone: int) -> None:
        """DB. Add new employee to database """
        query = text("insert into employee(company_id, first_name, last_name, phone) values(:company_id, :first_name, :surname, :phone)")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.connect() as conn:
            result = conn.execute(statement=query, parameters=dict(company_id=max_id, first_name=name, surname=surname, phone=phone))
            conn.commit()
        return result

    @allure.step("DB. Get employee bi id {id}")
    def get_employee_by_id(self, id: int) -> int:
        """DB. Get employee id by company id"""
        query = text("select id from employee where company_id =:company_id")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.begin() as conn:
            bd_result = conn.execute(statement=query, parameters=dict(company_id=id)).fetchall()[0][0]
        return bd_result
    
    @allure.step("DB. Update employee {id}: new name: {new_name}")
    def update_employee_info(self, new_name: str, id: int) -> None:
        """DB. Update user info """
        query = text("update employee set first_name = :new_name where id = :employee_id")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(new_name=new_name, employee_id=id))
            conn.commit()
    
    @allure.step("DB. Create new company {new_name}")
    def create(self, new_name: str) -> None:
        """
        DB. Add new company to database
        """
        query = text("insert into company(name) values(:new_name)")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(new_name = new_name))
            conn.commit()
    
    @allure.step("DB. Get max id")
    def get_max_id(self) -> int:
        """
        DB. Get the most recent id from database
        """
        query = text("select max(id) from company")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.connect() as conn:
            result = conn.execute(statement=query).fetchall()[0][0]
        return result
    
    @allure.step("DB. Delete company with id {new_id}")
    def delete(self, new_id: int) -> None:
        """
        DB. Delete company from database by company id
        """
        query = text("delete from company where id=:company_id")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(company_id=new_id))
            conn.commit()
    
    @allure.step("DB. Delete employee with id {id}")
    def delete_employee(self, id: int) -> None:
        """
        DB. Delete employee from database by employee id
        """
        query = text("delete from employee where id=:employee_id")
        allure.attach(str(query), 'SQL', allure.attachment_type.TEXT)
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(employee_id=id))
            conn.commit()
import sqlalchemy
from sqlalchemy import text, create_engine

class CompanyTable:
    
    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string)
    
    def get_list_of_employees(self, max_id: int) -> list:
        query = text("select * from employee where id =:company_id")
        with self.__db.engine.begin() as conn:
            bd_result = conn.execute(statement=query, parameters=dict(company_id = max_id)).fetchall()
        return bd_result

    def add_new_employee(self, max_id: int, name: str, surname: str, phone: int) -> None:
        """ add new employee to database """
        query = text("insert into employee(company_id, first_name, last_name, phone) values(:company_id, :first_name, :surname, :phone)")
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(company_id=max_id, first_name=name, surname=surname, phone=phone))
            conn.commit()

    def create(self, new_name: str) -> None:
        """
        add new company to database
        """
        query = text("insert into company(name) values(:new_name)")
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(new_name = new_name))
            conn.commit()
            
    def get_max_id(self) -> int:
        """
        Get the most recent id from database
        """
        query = text("select max(id) from company")
        with self.__db.engine.connect() as conn:
            result = conn.execute(statement=query).fetchall()[0][0]
        return result
    
    def delete(self, new_id: int) -> None:
        """
        Delete company from database by company id
        """
        query = text("delete from company where id=:company_id")
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(company_id=new_id))
            conn.commit()
            
    def delete_employee(self, id: int) -> None:
        """
        Delete employee from database by employee id
        """
        query = text("delete from employee where id=:employee_id")
        with self.__db.engine.connect() as conn:
            conn.execute(statement=query, parameters=dict(employee_id=id))
            conn.commit()
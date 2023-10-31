from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g")

def test_get_list_of_employees():
    db.create("Testing employee")
    max_id = db.get_max_id()
    db_employee_list = db.get_list_of_employees(max_id)
    api_employee_list = api.get_list_employee(max_id)
    assert len(api_employee_list) == len(db_employee_list)
    db.delete(max_id)

def test_add_new_employee():
    db.create("Company for adding new employee")
    max_id = db.get_max_id()
    new_employee = db.add_new_employee(max_id, "Oleg", "Fursov", 9098087766)
   
    resp = api.get_list_employee(max_id)
    employee_id = resp[0]["id"]
    
    assert resp[0]["companyId"] == max_id
    assert resp[0]["firstName"] == "Oleg"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "Fursov"
    db.delete_employee(employee_id)
    db.delete(max_id)

def test_get_employee_by_id():
    db.create("Company for adding new employee")
    max_id = db.get_max_id()
    new_employee = db.add_new_employee(max_id, "Oleg", "Fursov", 9098087766)
    employee_id = db.get_employee_by_id(max_id)
    
    get_info = api.get_employee_by_id(employee_id)
    assert get_info["firstName"] == "Oleg"
    assert get_info["lastName"] == "Fursov"
    db.delete_employee(employee_id)
    db.delete(max_id)

def test_update_user_info():
    db.create("Company for update employees info")
    max_id = db.get_max_id()
    new_employee = db.add_new_employee(max_id, "Oleg", "Fursov", 9098087766)
    employee_id = db.get_employee_by_id(max_id)
    db.update_employee_info("Ivan", employee_id)
    
    get_info = api.get_employee_by_id(employee_id)
    assert get_info["firstName"] == "Ivan"
    assert get_info["lastName"] == "Fursov"
    assert get_info["isActive"] == True
    db.delete_employee(employee_id)
    db.delete(max_id)
 
    
    

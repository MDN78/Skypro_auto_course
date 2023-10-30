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
    db.create("Add new employee")
    max_id = db.get_max_id()
    new_employee = db.add_new_employee(max_id, "Pavel", "Durov", 9098087766)
    db_employee_list = db.get_list_of_employees(max_id)
    # name = "Company for new employee"
    # descr = "SkyPro testing"
    # company = api.create_company(name, descr)
    # new_id = company["id"]
    # new_employee = api.add_new_employee(new_id, "Pavel", "Durov")
    # assert new_employee["id"] > 0
    
    resp = api.get_list_employee(max_id)
    assert len(resp) == len(db_employee_list)
    assert resp[0]["companyId"] == max_id
    assert resp[0]["firstName"] == "Pavel"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "Durov"

def test_get_employee_by_id():
    name = "Company for testing id employee"
    descr = "SkyPro testing"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Alex", "Fursov")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Alex"
    assert get_info["lastName"] == "Fursov"

def test_update_user_info():
    name = "Company for update user info"
    descr = "SkyPro testing"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Alex", "Fursov2")
    id_employee = new_employee["id"]
    
    update = api.update_employee_info(id_employee, "Fursov2", "test@ya.ru")
    assert update["id"] == id_employee
    assert update["email"] == "test@ya.ru"
    assert update["isActive"] == True
    
    

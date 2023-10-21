from CompanyApi import CompanyApi

api = CompanyApi("https://x-clients-be.onrender.com")

def test_get_list_of_employees():
    name = "New Orlean"
    descr = "SkyPro testing"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0

def test_add_new_employee():
    name = "Company for new employee"
    descr = "SkyPro testing"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Pavel", "Durov")
    assert new_employee["id"] > 0
    
    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
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
    
    

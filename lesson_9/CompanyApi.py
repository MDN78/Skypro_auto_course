import requests

class CompanyApi:
    
    def __init__(self, url):
        self.url = url
    
    def get_token(self, user = 'bloom', password = 'fire-fairy') -> str:
        """Get x-client token"""
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        return resp.json()["userToken"]
    
    def create_company(self, name: str, description='') -> dict:
        """Create company via API request"""
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/company", json=company, headers=my_headers)
        return resp.json()
    
    def get_list_employee(self, id: int) -> dict:
        """Get list of employees by id"""
        my_params = {
            "company": id
        }
        resp = requests.get(f"{self.url}/employee", params=my_params)
        return resp.json()
    
    def add_new_employee(self, new_id: int, name: str, last_name: str) -> dict:
        """Add new employee via API request"""
        employee = {
            "id": 111,
            "firstName": name,
            "lastName": last_name,
            "middleName": "-",
            "companyId": new_id,
            "email": "email@ya.com",
            "url": "string",
            "phone": "88009004546",
            "birthdate": "2023-10-21T11:06:26.567Z",
            "isActive": 'true'
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/employee", headers=my_headers, json=employee)
        return resp.json()
    
    def get_employee_by_id(self, id_employee: int) -> dict:
        resp = requests.get(f"{self.url}/employee/{id_employee}")
        return resp.json()
    
    def update_employee_info(self, id_employee: int, last_name: str, email: str) -> dict:
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": True
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=my_headers, json=user_info)
        return resp.json()
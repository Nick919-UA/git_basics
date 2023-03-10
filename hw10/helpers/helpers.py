from .system_helpers import save_to_file, get_file_data, save_list_to_file
from .decorators_helpers import is_email_valid, is_phone_valid

@is_email_valid
@is_phone_valid
def save(
        email, first_name, last_name,
        phone, work_id, type
):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "work_id": work_id,
        "type": type,
    }
    save_to_file(new_employee, "git_basics\hw9\database\employees.json")

def update_user_info(id):
    fields = {
        1: "email",
        2: "first_name",
        3: "last_name",
        4: "phone",
        5: "work_id",
        6: "type"
    }
    print("Choose what you want to update:")
    for key, value in fields.items():
        print(f"{key}. {value.capitalize()}")
    number = int(input("Choose: "))

    try:
        employers = get_file_data("git_basics\hw9\database\employees.json")
        for employee in employers:
            if id == employee["id"]:
                employee[fields[number]] = input(f"New {fields[number].capitalize()}: ")
        save_list_to_file(employers, "git_basics\hw9\database\employees.json")
    except Exception as ex:
        print(f"{ex}")

def get_all_employers():
    employees = get_file_data("git_basics\hw9\database\employees.json")
    for employee in employees:
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])
        print(employee["work_id"])
        print(employee["type"])


def get_employee_by_email(email):
    employees = get_file_data("git_basics\hw9\database\employees.json")
    for employee in employees:
        if employee["email"] == email:
            print(f'{employee["email"]}\n{employee["first_name"]}\n'
                  f'{employee["last_name"]}\n{employee["phone"]}\n'
                  f'{employee["work_id"]}\n{employee["type"]}\n')
            return employee

def save_plant(name, address):
    if name is not None and address.strip() != '':
        new_plant = {"name": name, "address": address}
        save_to_file(new_plant, "git_basics\hw9\database\plants.json")
    else:
        raise ValueError("Both name and address of plant must be provided and address cannot be empty.")


def get_all_plants():
    plants = get_file_data("git_basics\hw9\database\plants.json")
    for plant in plants:
        print(plant["name"])
        print(plant["address"])


def get_plant_by_id(id):
    plants = get_file_data("git_basics\hw9\database\plants.json")
    found = False
    for plant in plants:
        if plant["id"] == id:
            found = True
            print(plant["name"])
            print(plant["address"])
            found = True
    if not found:
        raise ValueError(f"No plant with id {id} was found.")


def save_salon(name, address):
    if name is not None and address.strip() != '':
        new_salon = {"name": name, "address": address}
        save_to_file(new_salon, "git_basics\hw9\database\salons.json")
    else:
        raise ValueError("Both name and address of salon must be provided and address cannot be empty.")

def get_salon_by_id(id):
    salons = get_file_data("git_basics\hw9\database\salons.json")
    found = False
    for salon in salons:
        if salon["id"] == id:
            found = True
            print(salon["name"])
            print(salon["address"])
            found = True
    if not found:
        raise ValueError(f"No salon with id {id} was found.")


def delete_employee(id):
    employees = get_file_data("git_basics\hw9\database\employees.json")
    found = False
    for i in range(len(employees)):
        if id == employees[i]["id"]:
            found = True
            del employees[i]
            save_list_to_file(employees, "git_basics\hw9\database\employees.json")
    if not found:
        raise ValueError(f"No emploee with id {id} was found.")
    
def save_sales_dep(name, address):
    if name is not None and address.strip() != '':
        new_plant = {"name": name, "address": address}
        save_to_file(new_plant, "git_basics\hw9\database\sales_dep.json")
    else:
        raise ValueError("Both name and address of plant must be provided and address cannot be empty.")

def get_sales_dep_by_id(id):
    sales_deps = get_file_data("git_basics\hw9\database\sales_dep.json")
    found = False
    for dep in sales_deps:
        if dep["id"] == id:
            found = True
            print(dep["name"])
            print(dep["address"])
            found = True
    if not found:
        raise ValueError(f"No salon with id {id} was found.")
from helpers import save, get_all_employers, get_employee_by_email,\
    update, save_plant, get_all_plants,\
    get_plant_by_id, save_salon, get_salon_by_id, delete_employee, \
    update_emploee


while True:
    print("1.Add new Employee\n2.Get all Employees\n3.Get employee by email\n4. Update Employee\n5. Add plant\n6.Get all plants\n7.Get plant by id\n8.Add salon\n9.Del Employee\n10.Update Employee")
    flag = int(input("Choose menu item: "))
    if flag == 1:
        email = input("Employee email: ")
        first_name = input("Employee first name: ")
        last_name = input("Employee last name: ")
        phone_number = input("Employee phone number: ")
        work_id = int(input("Employee work id: "))
        type = input("Employee work type: ")
        save(email, first_name, last_name, phone_number, work_id, type)
    elif flag == 2:
        get_all_employers()
    elif flag == 3:
        email_to_find = input("Type email of employee which you want to find: ")
        employee = get_employee_by_email(email_to_find)

        print("1.Display info about place of work.\n0.Exit")
        flag_inner = int(input("Your choose: "))
        if flag_inner == 1:
            if employee["type"] == "plant":
                get_plant_by_id(int(employee["work_id"]))
            elif employee["type"] == "salon":
                get_salon_by_id(int(employee["work_id"]))
        else:
            continue
    elif flag == 4:
        id = int(input("Type a id of user which you want to update: "))
        update(id)
    elif flag == 5:
        name = input("Type a name of Plant: ")
        address = input("Type an address of Plant: ")
        save_plant(name, address)
    elif flag == 6:
        get_all_plants()
    elif flag == 7:
        id = int(input("Id of plant: "))
        get_plant_by_id(id)

    elif flag == 8:
        name = input("Type a name of Salon: ")
        address = input("Type an address of Salon: ")
        save_salon(name, address)
    elif flag == 9:
        id = int(input("Id of element which you want to delete: "))
        delete_employee(id)
    elif flag == 10:
        id = int(input("Id of element which you want to delete: "))
        update_emploee(id)



    print("===============================================================================")

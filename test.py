positions = {}
while True:
    print("Menu:")
    print("1. Add a position")
    print("2. Edit a position")
    print("3. Add an employee")
    print("4. Remove an employee")
    print("5. Total number of employees")
    print("6. Total salary for a position")
    print("7. Positions with the most vacancies")
    print("8. Exit")
    choice = input("Enter your choice(1-8): ")

    if choice == "1":
        position_name = input("Enter position name: ")
        if position_name in positions:
            print("This position already exists.")
            continue
        max_employees = input("Enter maximum number of employees: ")
        salary = input("Enter salary: ")
        bonus_percentage = input("Enter bonus percentage: ")

        positions[position_name] = {
            "max_employees": int(max_employees),
            "current_employee": 0,
            "salary": int(salary),
            "bonus_percentage": int(bonus_percentage),
            "employees": set()
        }
        print(f"Position: {position_name} added." )
    elif choice == "2":
        position_name = input("Enter position name to edit: ")
        if position_name not in positions:
            print("Position not found.")
            continue
        print("Editing position...")
        max_employees = int(input(f"Enter new max number of employees for {position_name}: "))
        salary = float(input(f"Enter new salary for {position_name}: "))
        bonus_percentage = float(input(f"Enter bonus percentage for {position_name}: "))

        positions[position_name]["max_employees"] = int(max_employees)
        positions[position_name]["salary"] = int(salary)
        positions[position_name]["bonus_percentage"] = int(bonus_percentage)
        print(f"Position: {position_name} updated." )

    elif choice == "3":
        position_name = input("Enter position name: ")
        if position_name not in positions:
            print("Position not found.")
            continue
        if positions[position_name]["current_employee"] >= positions[position_name]["max_employees"]:
            print(f"{position_name} position is full.")
            continue
        employee_name = input("Enter employee name: ")
        if employee_name in positions[position_name]["employees"]:
            print(f"Employee {employee_name} is already in position {position_name}")
            continue
        positions[position_name]["employees"].add(employee_name)
        positions[position_name]["current_employee"] += 1
        print(f"Employee {employee_name} added to position {position_name}.")

    elif choice == "4":
        position_name = input("Enter position name: ")
        if position_name not in positions:
            print("Position not found.")
            continue
        employee_name = input("Enter employee name to remove: ")
        if employee_name not in positions[position_name]["employees"]:
            print(f"Employee {employee_name} is not in position {position_name}")
            continue
        positions[position_name]["employees"].remove(employee_name)
        positions[position_name]["current_employee"] -= 1
        print(f"Employee {employee_name} removed from position {position_name}.")

    elif choice == "5":
        total = sum(position["current_employee"] for position in positions.values())
        print(f"Total employees: {total}")

    elif choice == "6":
        position_name = input("Enter position name: ")
        if position_name not in positions:
            print("Position not found.")
            continue
        position = positions[position_name]
        total_salary = position["current_employee"] * position["salary"]
        total_bonus = total_salary * (position["bonus_percentage"] / 100)
        total_salary_with_bonus = total_salary + total_bonus
        print(f"Total salary for position: {total_salary} with bonus: {total_salary_with_bonus}")

    elif choice == "7":
        max_vacancies = 0
        position_with_max_vacancies = []
        for position_name, position in positions.items():
            vacancies = position["max_employees"] - position["current_employee"]
            if vacancies > max_vacancies:
                max_vacancies = vacancies
                position_with_max_vacancies = [position_name]
            elif vacancies == max_vacancies:
                position_with_max_vacancies.append(position_name)


        position_with_max_vacancies.sort()
        print(f"Positions with maximum vacancies: {", ".join(position_with_max_vacancies)}")

    elif choice == "8":
        print("Exiting...")
        break


    else:
        print("Invalid choice. Please try again.")


import json
from datetime import datetime

# store attendance data
DATA_FILE = "attendance.json"

# Load attendance
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            data = json.loads(content)
            
            # Convert lists back to sets 
            attendance_data = {}
            for employee, dates in data.items():
                attendance_data[employee] = set(dates)
            return attendance_data
            
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Data file corrupted or empty")
        return {}

# Save attendance to file
def save_data(attendance):
    # Convert sets to lists 
    data_to_save = {}
    for employee, dates in attendance.items():
        data_to_save[employee] = list(dates)  

    with open(DATA_FILE, "w") as f:
        json.dump(data_to_save, f, indent=4)

# Add new employee
def add_employee(attendance):
    name = input("Enter employee name: ").strip()
    if name in attendance:
        print(f"{name} already exists.")
    else:
        attendance[name] = set()
        print(f"Employee {name} added successfully.")

# Mark attendance
def mark_attendance(attendance):
    name = input("Enter employee name: ").strip()
    if name not in attendance:
        print("Employee not found. Please add them first.")
        return
    
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_input = datetime.today().strftime("%Y-%m-%d")
    
    if date_input in attendance[name]:
        print(f"Attendance for {date_input} is already marked for {name}.")
    else:
        attendance[name].add(date_input)
        print(f"Attendance marked for {name} on {date_input}.")

# Show summary
def show_summary(attendance):
    if not attendance:
        print("No employee records found.")
        return
    
    print("\n Employee Attendance Summary:")
    for name, dates in attendance.items():
        dates_list = sorted(dates)
        print(f"{name}: {len(dates_list)} days attended -> {dates_list}")

# Show employees with perfect attendance
def perfect_attendance(attendance):
    if not attendance:
        print("No employee records found.")
        return
    
    all_dates = set()
    for dates in attendance.values():
        all_dates.update(dates)
    
    perfect_employees = [name for name, dates in attendance.items() if dates == all_dates]
    
    if perfect_employees:
        print("Employees with perfect attendance:")
        for name in perfect_employees:
            print(f"- {name}")
    else:
        print("No employees with perfect attendance yet.")

# Main program
def main():
    attendance = load_data()
    print("Welcome to Employee Attendance Tracker")

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. Show Attendance Summary")
        print("4. Show Employees with Perfect Attendance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_employee(attendance)
        elif choice == "2":
            mark_attendance(attendance)
        elif choice == "3":
            show_summary(attendance)
        elif choice == "4":
            perfect_attendance(attendance)
        elif choice == "5":
            save_data(attendance)
            print("Data saved. Exit")
            break
        else:
            print("Invalid choice. Please try again.")


main()



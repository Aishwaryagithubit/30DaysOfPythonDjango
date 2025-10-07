# Grade Management System
import json
# store student data
DATA_FILE = "students.json"

# Load student data 
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:   # if file is empty
                return {}
            return json.loads(content)
    except FileNotFoundError:
        return {}  
    except json.JSONDecodeError:
        print("Data file corrupted or empty")
        return {}

# Save student data 
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Calculate stats
def calculate_stats(students):
    if not students:
        print("No student records available.")
        return
    grades = list(students.values())
    avg = sum(grades) / len(grades)
    print(f"Average Grade: {avg:.2f}")
    print(f"Highest Grade: {max(grades)}")
    print(f"Lowest Grade: {min(grades)}")

def main():
    students = load_data()  
    print("Welcome to Student Grades Manager")

    while True:
        print("\nGrade Management System")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Remove Student")
        print("4. Show All Students")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter grade: "))
                students[name] = grade
                print(f"{name} added with grade {grade}")
            except ValueError:
                print("Grade must be a number.")

        elif choice == "2":
            name = input("Enter student name to update: ").strip()
            if name in students:
                try:
                    grade = int(input("Enter new grade: "))
                    students[name] = grade
                    print(f"{name}'s grade updated to {grade}")
                except ValueError:
                    print("Grade must be a number.")
            else:
                print("Student not found")

        elif choice == "3":
            name = input("Enter student name to remove: ").strip()
            if name in students:
                del students[name]
                print(f"{name} removed")
            else:
                print("Student not found")

        elif choice == "4":
            if students:
                print("\nStudent Records:")
                for name, grade in students.items():
                    print(f"{name}: {grade}")
            else:
                print("No students found.")

        elif choice == "5":
            calculate_stats(students)

        elif choice == "6":
            save_data(students) 
            print("Data saved. Exit")
            break
        else:
            print("Invalid choice. Try again.")


main()

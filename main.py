DATA_FILE = "data.txt"
GOAL_FILE = "goal.txt"
def load_data():
    total = 0
    logs = []
    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                hours = float(line.strip())
                logs.append(hours)
                total += hours
    except FileNotFoundError:
        pass
    return total, logs
def save_data(hours):
    with open(DATA_FILE, "a") as f:
        f.write(str(hours) + "\n")
def set_goal():
    try:
        goal = float(input("Enter weekly goal (hours): "))
        with open(GOAL_FILE, "w") as f:
            f.write(str(goal))
        print("Goal set successfully!")
    except:
        print("Invalid input!")
def view_progress(total):
    try:
        with open(GOAL_FILE, "r") as f:
            goal = float(f.read())
        print(f"Goal: {goal} hours")
        print(f"Completed: {total} hours")
        if total >= goal:
            print("Goal achieved!")
        else:
            print(f"{goal - total:.2f} hours remaining")
    except FileNotFoundError:
        print("No goal set yet.")
    except:
        print("Error reading goal data")
def add_hours():
    try:
        hours = float(input("Enter study hours: "))
        if hours <= 0:
            raise ValueError
        save_data(hours)
        print("Hours added")
    except:
        print("Invalid input")
def view_total():
    total, _ = load_data()
    print(f"Total Study Hours: {total}")
def view_history():
    _, logs = load_data()
    if logs:
        print("\nStudy History:")
        for i, h in enumerate(logs, 1):
            print(f"{i}. {h} hours")
    else:
        print("No data yet.")
def reset_data():
    confirm = input("Are you sure you want to delete all data?")
    if confirm.lower() == "yes":
        open(DATA_FILE, "w").close()
        open(GOAL_FILE, "w").close()
        print("Data reset successfully!")
    else:
        print("Reset cancelled.")
def menu():
    while True:
        print("\n====== Productivity Tracker ======")
        print("1. Add Study Hours")
        print("2. View Total Hours")
        print("3. View History")
        print("4. Set Weekly Goal")
        print("5. View Progress")
        print("6. Reset Data")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_hours()
        elif choice == "2":
            view_total()
        elif choice == "3":
            view_history()
        elif choice == "4":
            set_goal()
        elif choice == "5":
            total, _ = load_data()
            view_progress(total)
        elif choice == "6":
            reset_data()
        elif choice == "7":
            print("Exited")
            break
        else:
            print("Invalid choice!")
menu()